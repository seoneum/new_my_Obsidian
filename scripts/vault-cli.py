#!/usr/bin/env python3
"""
vault-cli: Obsidian Vault 자동화 도구
CPZ (CMDS + PARA + Zettelkasten) 통합 시스템

사용법:
    vault note "제목"        # 빠른 노트 생성
    vault today              # 오늘 Daily 노트 생성
    vault process            # Inbox 노트 자동 처리
    vault review week        # 주간 리뷰
    vault stats              # 통계 보기
    vault link <파일>        # 관련 노트 링크 제안
    vault tag <파일>         # 태그 추천
    vault move               # 폴더 이동 제안
"""

import os
import re
import sys
import json
import argparse
from pathlib import Path
from datetime import datetime, timedelta
from collections import Counter
from typing import Dict, List, Tuple, Any

try:
    import yaml

    HAS_YAML = True
except ImportError:
    HAS_YAML = False


def simple_yaml_parse(text: str) -> dict:
    result = {}
    current_key = None
    current_dict = None

    for line in text.split("\n"):
        if not line.strip() or line.strip().startswith("#"):
            continue

        indent = len(line) - len(line.lstrip())
        stripped = line.strip()

        if indent == 0 and ":" in stripped:
            key, _, value = stripped.partition(":")
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            if value:
                result[key] = value
            else:
                result[key] = {}
                current_key = key
                current_dict = result[key]
        elif indent > 0 and current_key and ":" in stripped:
            key, _, value = stripped.partition(":")
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            if isinstance(result[current_key], dict):
                result[current_key][key] = value
        elif indent > 0 and stripped.startswith("- "):
            if current_key and not isinstance(result[current_key], list):
                result[current_key] = []
            if current_key:
                result[current_key].append(stripped[2:].strip())

    return result


class Config:
    def __init__(self, vault_path: str = None):
        self.vault_path = Path(vault_path or os.environ.get("VAULT_PATH", os.getcwd()))
        self.config_file = self.vault_path / "scripts" / "config.yaml"
        self._load_config()

    def _load_config(self):
        defaults = {
            "author": "[[김선음]]",
            "folders": {
                "inbox": "📥 Inbox",
                "quick": "📥 Inbox/_quick",
                "webclip": "📥 Inbox/_webclip",
                "projects": "🎯 Projects",
                "areas": "🔄 Areas",
                "resources": "📚 Resources",
                "archive": "🗃️ Archive",
                "zettel": "💎 Zettel",
                "meta": "⚙️ Meta",
                "templates": "⚙️ Meta/Templates",
                "daily": "🔄 Areas/Daily",
            },
            "cmds_stages": ["inbox", "connect", "merge", "develop", "share"],
            "status_levels": ["seed", "sapling", "evergreen", "archive"],
            "domains": ["cs", "ee", "phil", "math", "robotics", "general"],
            "prefixes": {
                "daily": "D",
                "lecture": "L",
                "concept": "C",
                "problem": "P",
                "reference": "R",
                "meeting": "MTG",
                "project": "PRJ",
                "zettel": "Z",
                "question": "Q",
            },
        }

        if self.config_file.exists():
            with open(self.config_file, "r", encoding="utf-8") as f:
                content = f.read()
                if HAS_YAML:
                    user_config = yaml.safe_load(content) or {}
                else:
                    user_config = simple_yaml_parse(content)
                self._merge_config(defaults, user_config)

        self.author = defaults["author"]
        self.folders = defaults["folders"]
        self.cmds_stages = defaults["cmds_stages"]
        self.status_levels = defaults["status_levels"]
        self.domains = defaults["domains"]
        self.prefixes = defaults["prefixes"]

    def _merge_config(self, base: dict, override: dict):
        for key, value in override.items():
            if key in base and isinstance(base[key], dict) and isinstance(value, dict):
                self._merge_config(base[key], value)
            else:
                base[key] = value


class Note:
    """마크다운 노트 파싱 및 조작"""

    def __init__(self, path: Path):
        self.path = path
        self.frontmatter: Dict[str, Any] = {}
        self.content: str = ""
        self.links: List[str] = []
        self.tags: List[str] = []
        self.headings: List[Tuple[int, str]] = []
        self._load()

    def _load(self):
        """파일 로드 및 파싱"""
        if not self.path.exists():
            return

        with open(self.path, "r", encoding="utf-8") as f:
            text = f.read()

        fm_match = re.match(r"^---\n(.*?)\n---\n?(.*)", text, re.DOTALL)
        if fm_match:
            try:
                if HAS_YAML:
                    self.frontmatter = yaml.safe_load(fm_match.group(1)) or {}
                else:
                    self.frontmatter = simple_yaml_parse(fm_match.group(1))
            except Exception:
                self.frontmatter = {}
            self.content = fm_match.group(2)
        else:
            self.content = text

        self.links = re.findall(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]", self.content)

        fm_tags = self.frontmatter.get("tags", [])
        if isinstance(fm_tags, str):
            fm_tags = [fm_tags]
        elif isinstance(fm_tags, dict):
            fm_tags = list(fm_tags.keys()) if fm_tags else []
        elif not isinstance(fm_tags, list):
            fm_tags = []
        inline_tags = re.findall(
            r"(?<!\w)#([a-zA-Z가-힣][a-zA-Z0-9가-힣/_-]*)", self.content
        )
        self.tags = list(set(fm_tags + inline_tags))

        # 헤딩 추출
        self.headings = [
            (len(m.group(1)), m.group(2))
            for m in re.finditer(r"^(#{1,6})\s+(.+)$", self.content, re.MULTILINE)
        ]

    def save(self):
        if HAS_YAML:
            fm_str = yaml.dump(
                self.frontmatter,
                allow_unicode=True,
                default_flow_style=False,
                sort_keys=False,
            )
        else:
            lines = []
            for k, v in self.frontmatter.items():
                if isinstance(v, list):
                    if v:
                        lines.append(f"{k}:")
                        for item in v:
                            lines.append(f"  - {item}")
                    else:
                        lines.append(f"{k}: []")
                elif v is None or v == "":
                    lines.append(f"{k}:")
                else:
                    lines.append(f"{k}: {v}")
            fm_str = "\n".join(lines) + "\n"

        with open(self.path, "w", encoding="utf-8") as f:
            f.write(f"---\n{fm_str}---\n{self.content}")

    @property
    def title(self) -> str:
        return self.frontmatter.get("title", self.path.stem)

    @property
    def cmds_stage(self) -> str:
        return self.frontmatter.get("cmds", "inbox")

    @property
    def status(self) -> str:
        return self.frontmatter.get("status", "seed")

    @property
    def domains(self) -> List[str]:
        d = self.frontmatter.get("domain", [])
        return d if isinstance(d, list) else [d] if d else []

    @property
    def note_type(self) -> str:
        t = self.frontmatter.get("type", "note")
        return t[0] if isinstance(t, list) else t

    def get_words(self) -> List[str]:
        """내용에서 단어 추출 (분석용)"""
        # 마크다운 문법 제거
        text = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", self.content)  # 링크
        text = re.sub(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]", r"\1", text)  # 위키링크
        text = re.sub(r"`[^`]+`", "", text)  # 코드
        text = re.sub(r"[#*_~`>\-|]", " ", text)  # 마크다운 기호

        # 한글 + 영어 단어
        words = re.findall(r"[가-힣]+|[a-zA-Z]{2,}", text.lower())
        return words


# ==================== 자동 분류 엔진 ====================


class Classifier:
    """노트 자동 분류 엔진"""

    # 도메인별 키워드
    DOMAIN_KEYWORDS = {
        "cs": [
            "python",
            "c++",
            "cpp",
            "algorithm",
            "알고리즘",
            "자료구조",
            "class",
            "function",
            "code",
            "코드",
            "git",
            "linux",
            "array",
            "list",
            "tree",
            "graph",
            "stack",
            "queue",
            "hash",
            "sort",
        ],
        "ee": [
            "전자",
            "전기",
            "회로",
            "circuit",
            "전압",
            "전류",
            "저항",
            "capacitor",
            "inductor",
            "전자기",
            "electromagnetic",
            "맥스웰",
            "ampere",
            "voltage",
            "current",
            "ohm",
        ],
        "phil": [
            "철학",
            "philosophy",
            "존재",
            "인식",
            "윤리",
            "논리",
            "형이상학",
            "metaphysics",
            "epistemology",
            "칸트",
            "헤겔",
            "plato",
            "aristotle",
            "논증",
            "argument",
            "명제",
            "판단",
        ],
        "math": [
            "수학",
            "미적분",
            "calculus",
            "선형대수",
            "linear algebra",
            "미분",
            "적분",
            "행렬",
            "matrix",
            "벡터",
            "vector",
            "방정식",
            "equation",
            "함수",
            "function",
            "theorem",
            "증명",
        ],
        "robotics": [
            "로봇",
            "robot",
            "제어",
            "control",
            "pid",
            "센서",
            "actuator",
            "slam",
            "경로",
            "path",
            "kinematics",
            "동역학",
            "dynamics",
            "servo",
            "motor",
        ],
    }

    # 타입별 키워드
    TYPE_KEYWORDS = {
        "lecture": ["강의", "수업", "교수", "lecture", "주차", "week"],
        "concept": ["정의", "개념", "definition", "concept", "이란", "무엇"],
        "problem": ["문제", "풀이", "problem", "solution", "백준", "leetcode"],
        "reference": ["논문", "paper", "참고", "reference", "출처", "source"],
        "meeting": ["회의", "meeting", "참석", "안건", "agenda"],
        "project": ["프로젝트", "project", "목표", "goal", "마감", "deadline"],
        "daily": ["오늘", "today", "top 3", "아침", "저녁"],
    }

    def __init__(self, config: Config):
        self.config = config

    def suggest_domain(self, note: Note) -> List[Tuple[str, float]]:
        """도메인 추천 (확률 포함)"""
        words = note.get_words()
        word_set = set(words)
        word_counter = Counter(words)

        scores = {}
        for domain, keywords in self.DOMAIN_KEYWORDS.items():
            matches = word_set.intersection(keywords)
            score = sum(word_counter[w] for w in matches)
            if score > 0:
                scores[domain] = score

        if not scores:
            return [("general", 1.0)]

        total = sum(scores.values())
        return sorted([(d, s / total) for d, s in scores.items()], key=lambda x: -x[1])

    def suggest_type(self, note: Note) -> str:
        """노트 타입 추천"""
        words = note.get_words()
        word_set = set(words)

        # 제목에서 prefix 확인
        title = note.path.stem.lower()
        for prefix, note_type in [
            ("d -", "daily"),
            ("l -", "lecture"),
            ("c -", "concept"),
            ("p -", "problem"),
            ("r -", "reference"),
            ("mtg -", "meeting"),
            ("prj -", "project"),
            ("z -", "zettel"),
            ("q -", "question"),
        ]:
            if title.startswith(prefix):
                return note_type.split("-")[0]

        # 키워드 기반 추론
        best_type = "note"
        best_score = 0

        for note_type, keywords in self.TYPE_KEYWORDS.items():
            matches = word_set.intersection(keywords)
            if len(matches) > best_score:
                best_score = len(matches)
                best_type = note_type

        return best_type

    def suggest_cmds_stage(self, note: Note) -> str:
        """CMDS 단계 추천"""
        # 현재 위치 기반
        path_str = str(note.path).lower()

        if "inbox" in path_str or "_quick" in path_str:
            return "inbox"
        elif "project" in path_str:
            return "develop"
        elif "resource" in path_str or "reference" in path_str:
            return "connect"
        elif "zettel" in path_str or "merge" in path_str:
            return "merge"
        elif "share" in path_str:
            return "share"

        # 내용 기반 휴리스틱
        if note.frontmatter.get("authors") and "김선음" in str(
            note.frontmatter.get("authors", "")
        ):
            return "merge"  # 내가 쓴 것

        return "connect"  # 기본값

    def suggest_tags(self, note: Note) -> List[str]:
        """태그 추천"""
        suggestions = []

        # 도메인 태그
        domains = self.suggest_domain(note)
        if domains[0][0] != "general":
            suggestions.append(f"domain/{domains[0][0]}")

        # 타입 태그
        note_type = self.suggest_type(note)
        suggestions.append(f"type/{note_type}")

        # CMDS 태그
        cmds = self.suggest_cmds_stage(note)
        suggestions.append(f"cmds/{cmds}")

        # 기존 태그 유지
        for tag in note.tags:
            if tag not in suggestions and not tag.startswith("tagging/"):
                suggestions.append(tag)

        return suggestions


# ==================== 링크 분석 ====================


class LinkAnalyzer:
    """노트 간 연결 분석"""

    def __init__(self, config: Config):
        self.config = config
        self.vault_path = config.vault_path
        self.notes: Dict[str, Note] = {}
        self._index_vault()

    def _index_vault(self):
        """Vault 전체 인덱싱"""
        for md_file in self.vault_path.rglob("*.md"):
            # 시스템 폴더 제외
            if any(
                p in str(md_file)
                for p in [".obsidian", ".trash", ".git", "node_modules"]
            ):
                continue

            note = Note(md_file)
            key = md_file.stem
            self.notes[key] = note

    def find_related(self, note: Note, top_k: int = 5) -> List[Tuple[str, float]]:
        """관련 노트 찾기"""
        target_words = set(note.get_words())
        if not target_words:
            return []

        scores = []
        for name, other in self.notes.items():
            if other.path == note.path:
                continue

            other_words = set(other.get_words())
            if not other_words:
                continue

            # Jaccard 유사도
            intersection = len(target_words & other_words)
            union = len(target_words | other_words)
            score = intersection / union if union > 0 else 0

            # 도메인 보너스
            if set(note.domains) & set(other.domains):
                score *= 1.5

            if score > 0.05:  # 임계값
                scores.append((name, score))

        return sorted(scores, key=lambda x: -x[1])[:top_k]

    def find_orphans(self) -> List[Note]:
        """고아 노트 찾기 (링크 없는 노트)"""
        # 모든 링크 대상 수집
        linked = set()
        for note in self.notes.values():
            linked.update(note.links)

        orphans = []
        for name, note in self.notes.items():
            if name not in linked and len(note.links) == 0:
                orphans.append(note)

        return orphans

    def suggest_backlinks(self, note: Note) -> List[str]:
        """백링크 추가 제안"""
        note_name = note.path.stem
        suggestions = []

        for name, other in self.notes.items():
            if note_name in other.links and name not in note.links:
                suggestions.append(name)

        return suggestions


# ==================== 명령 처리 ====================


class VaultCLI:
    """메인 CLI 클래스"""

    def __init__(self, vault_path: str = None):
        self.config = Config(vault_path)
        self.classifier = Classifier(self.config)

    def cmd_note(self, title: str, note_type: str = "note"):
        """빠른 노트 생성"""
        now = datetime.now()
        note_id = now.strftime("%Y%m%d%H%M")

        # 폴더 결정
        folder = self.config.vault_path / self.config.folders["quick"]
        folder.mkdir(parents=True, exist_ok=True)

        # 파일명
        filename = f"N - {title}.md"
        filepath = folder / filename

        # Frontmatter
        fm = {
            "id": note_id,
            "title": title,
            "created": now.strftime("%Y-%m-%d"),
            "updated": now.isoformat(timespec="seconds"),
            "type": [note_type],
            "cmds": "inbox",
            "status": "seed",
            "domain": [],
            "tags": ["tagging/needed"],
        }

        content = f"\n# {title}\n\n## Notes\n\n\n## Next\n- [ ] \n"

        note = Note(filepath)
        note.frontmatter = fm
        note.content = content
        note.save()

        print(f"✅ Created: {filepath}")
        return filepath

    def cmd_today(self):
        """오늘 Daily 노트 생성"""
        now = datetime.now()
        date_str = now.strftime("%Y-%m-%d")
        weekday = ["월", "화", "수", "목", "금", "토", "일"][now.weekday()]

        folder = self.config.vault_path / self.config.folders["daily"]
        folder.mkdir(parents=True, exist_ok=True)

        filename = f"D - {date_str}.md"
        filepath = folder / filename

        if filepath.exists():
            print(f"📅 Already exists: {filepath}")
            return filepath

        fm = {
            "type": "daily",
            "title": date_str,
            "created": date_str,
            "updated": now.isoformat(timespec="seconds"),
            "author": self.config.author,
            "cmds": "merge",
            "status": "sapling",
            "tags": ["daily", f"week/{now.strftime('%W')}"],
        }

        content = f"""
# {date_str} ({weekday})

## 🎯 Top 3
1. [ ] 
2. [ ] 
3. [ ] 

---

## 📚 Today

### 오전


### 오후


---

## 🌙 Evening

### 오늘 핵심 3줄
1. 
2. 
3. 

### 내일 우선
1. 
2. 

---

## 📎 메모


"""

        note = Note(filepath)
        note.frontmatter = fm
        note.content = content
        note.save()

        print(f"✅ Created: {filepath}")
        return filepath

    def cmd_process(self, dry_run: bool = True):
        """Inbox 노트 자동 처리"""
        inbox_path = self.config.vault_path / self.config.folders["quick"]

        if not inbox_path.exists():
            print("📭 Inbox is empty")
            return

        processed = 0
        for md_file in inbox_path.glob("*.md"):
            note = Note(md_file)

            print(f"\n📄 Processing: {md_file.name}")

            # 분류 제안
            domains = self.classifier.suggest_domain(note)
            note_type = self.classifier.suggest_type(note)
            cmds_stage = self.classifier.suggest_cmds_stage(note)
            tags = self.classifier.suggest_tags(note)

            print(f"   📌 Type: {note_type}")
            print(f"   🏷️  Domain: {domains[0][0]} ({domains[0][1]:.0%})")
            print(f"   📊 CMDS: {cmds_stage}")
            print(f"   🔖 Tags: {', '.join(tags[:5])}")

            if not dry_run:
                # Frontmatter 업데이트
                note.frontmatter["type"] = [note_type]
                note.frontmatter["cmds"] = cmds_stage
                note.frontmatter["domain"] = [domains[0][0]]
                note.frontmatter["tags"] = tags
                note.frontmatter["updated"] = datetime.now().isoformat(
                    timespec="seconds"
                )

                # tagging/needed 제거
                if "tagging/needed" in note.frontmatter["tags"]:
                    note.frontmatter["tags"].remove("tagging/needed")

                note.save()
                print(f"   ✅ Updated!")
            else:
                print(f"   🔍 (dry-run, use --apply to save)")

            processed += 1

        print(f"\n📊 Processed: {processed} notes")

    def cmd_link(self, filepath: str):
        """관련 노트 링크 제안"""
        path = Path(filepath)
        if not path.exists():
            path = self.config.vault_path / filepath

        if not path.exists():
            print(f"❌ File not found: {filepath}")
            return

        note = Note(path)
        analyzer = LinkAnalyzer(self.config)

        print(f"\n🔗 Related notes for: {path.name}\n")

        related = analyzer.find_related(note)
        if related:
            for name, score in related:
                print(f"   • [[{name}]] ({score:.0%})")
        else:
            print("   No related notes found")

        # 백링크 제안
        backlinks = analyzer.suggest_backlinks(note)
        if backlinks:
            print(f"\n🔙 Suggested backlinks:")
            for name in backlinks[:5]:
                print(f"   • [[{name}]]")

    def cmd_stats(self):
        """Vault 통계"""
        analyzer = LinkAnalyzer(self.config)

        print("\n📊 Vault Statistics\n")
        print(f"   Total notes: {len(analyzer.notes)}")

        # 타입별 카운트
        type_counts = Counter()
        cmds_counts = Counter()
        domain_counts = Counter()

        for note in analyzer.notes.values():
            type_counts[note.note_type] += 1
            cmds_counts[note.cmds_stage] += 1
            for d in note.domains:
                domain_counts[d] += 1

        print("\n   📌 By Type:")
        for t, c in type_counts.most_common(10):
            print(f"      {t}: {c}")

        print("\n   📊 By CMDS Stage:")
        for s, c in cmds_counts.most_common():
            print(f"      {s}: {c}")

        print("\n   🏷️  By Domain:")
        for d, c in domain_counts.most_common():
            print(f"      {d}: {c}")

        # 고아 노트
        orphans = analyzer.find_orphans()
        if orphans:
            print(f"\n   ⚠️  Orphan notes: {len(orphans)}")

    def cmd_migrate(self, dry_run: bool = True):
        old_base = self.config.vault_path / "CMDS"

        if not old_base.exists():
            print("📭 No CMDS folder found - nothing to migrate")
            return

        migration_rules = {
            "102. 📝Daily_Note": self.config.folders["daily"],
            "221. Journaling": self.config.folders["daily"],
            "201. Connect": self.config.folders["resources"],
            "300. Thinking": self.config.folders["zettel"],
            "400. Reference": self.config.folders["resources"],
            "500. setting": self.config.folders["meta"],
        }

        files_to_migrate = []
        for md_file in old_base.rglob("*.md"):
            if ".obsidian" in str(md_file) or ".trash" in str(md_file):
                continue
            files_to_migrate.append(md_file)

        print(f"\n🔄 Migration Plan: {len(files_to_migrate)} files\n")

        moved_count = 0
        skipped_count = 0
        move_map = {}

        for md_file in files_to_migrate:
            rel_path = str(md_file.relative_to(old_base))
            filename = md_file.name.lower()

            target_folder = None

            if filename.startswith("d -") or filename.startswith("jrn -"):
                target_folder = self.config.folders["daily"]
            elif filename.startswith("l -"):
                target_folder = self.config.folders["resources"]
            elif filename.startswith(("c -", "z -", "q -")):
                target_folder = self.config.folders["zettel"]
            elif filename.startswith("prj -"):
                target_folder = self.config.folders["projects"]
            else:
                for pattern, new_folder in migration_rules.items():
                    if pattern in rel_path:
                        target_folder = new_folder
                        break

            if not target_folder:
                note = Note(md_file)
                note_type = self.classifier.suggest_type(note)

                if note_type == "daily":
                    target_folder = self.config.folders["daily"]
                elif note_type in ["lecture", "reference"]:
                    target_folder = self.config.folders["resources"]
                elif note_type in ["concept", "zettel", "question"]:
                    target_folder = self.config.folders["zettel"]
                elif note_type == "project":
                    target_folder = self.config.folders["projects"]
                else:
                    target_folder = self.config.folders["inbox"]

            target_dir = self.config.vault_path / target_folder

            if "Resources" in target_folder or "📚" in target_folder:
                parts = rel_path.split("/")
                for part in parts:
                    if not part.startswith(
                        (
                            "100.",
                            "102.",
                            "200.",
                            "201.",
                            "220.",
                            "221.",
                            "300.",
                            "400.",
                            "500.",
                        )
                    ):
                        if part != md_file.name and not part.startswith("."):
                            target_dir = target_dir / part
                            break

            target_path = target_dir / md_file.name

            if target_path.exists():
                print(f"   ⏭️  Skip (exists): {md_file.name}")
                skipped_count += 1
                continue

            print(f"   📄 {md_file.name}")
            print(f"      → {target_path.relative_to(self.config.vault_path)}")

            move_map[md_file.stem] = target_path

            if not dry_run:
                target_dir.mkdir(parents=True, exist_ok=True)

                import shutil

                shutil.move(str(md_file), str(target_path))

                note = Note(target_path)
                note.frontmatter["migrated_from"] = str(
                    md_file.relative_to(self.config.vault_path)
                )
                note.frontmatter["updated"] = datetime.now().isoformat(
                    timespec="seconds"
                )

                domains = self.classifier.suggest_domain(note)
                if domains[0][0] != "general":
                    note.frontmatter["domain"] = [domains[0][0]]

                note.frontmatter["cmds"] = self.classifier.suggest_cmds_stage(note)
                note.save()

            moved_count += 1

        print(f"\n📊 Summary:")
        print(f"   ✅ {'Would move' if dry_run else 'Moved'}: {moved_count}")
        print(f"   ⏭️  Skipped: {skipped_count}")

        if dry_run:
            print(f"\n💡 Run 'vault migrate --apply' to execute migration")
        else:
            print(f"\n✅ Migration complete!")
            print(f"💡 Run 'vault stats' to verify, then delete CMDS folder manually")

    def cmd_review(self, period: str = "week"):
        """리뷰 생성"""
        analyzer = LinkAnalyzer(self.config)

        now = datetime.now()
        if period == "week":
            start = now - timedelta(days=7)
            title = f"Week {now.strftime('%W')} Review"
        elif period == "month":
            start = now - timedelta(days=30)
            title = f"{now.strftime('%Y-%m')} Review"
        else:
            start = now - timedelta(days=1)
            title = "Yesterday Review"

        print(f"\n📋 {title}\n")

        # 기간 내 수정된 노트
        recent = []
        for note in analyzer.notes.values():
            updated = note.frontmatter.get("updated", "")
            if updated:
                try:
                    note_date = datetime.fromisoformat(updated.replace("Z", "+00:00"))
                    if note_date.replace(tzinfo=None) >= start:
                        recent.append(note)
                except:
                    pass

        print(f"   📝 Notes modified: {len(recent)}")

        # CMDS 단계별
        inbox_notes = [n for n in recent if n.cmds_stage == "inbox"]
        if inbox_notes:
            print(f"\n   📥 Inbox (unprocessed): {len(inbox_notes)}")
            for n in inbox_notes[:5]:
                print(f"      • {n.path.name}")

        # 고아 노트
        orphans = analyzer.find_orphans()
        print(f"\n   🔗 Orphan notes: {len(orphans)}")


# ==================== 메인 ====================


def main():
    parser = argparse.ArgumentParser(
        description="vault-cli: Obsidian Vault 자동화 도구",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  vault note "아이디어 제목"     빠른 노트 생성
  vault today                   오늘 Daily 노트 생성
  vault process                 Inbox 자동 처리 (dry-run)
  vault process --apply         Inbox 자동 처리 (적용)
  vault link note.md            관련 노트 제안
  vault stats                   통계 보기
  vault review week             주간 리뷰
        """,
    )

    parser.add_argument("--vault", "-v", help="Vault 경로")

    subparsers = parser.add_subparsers(dest="command", help="Commands")

    # note
    note_parser = subparsers.add_parser("note", help="빠른 노트 생성")
    note_parser.add_argument("title", help="노트 제목")
    note_parser.add_argument("--type", "-t", default="note", help="노트 타입")

    # today
    subparsers.add_parser("today", help="오늘 Daily 노트 생성")

    # process
    process_parser = subparsers.add_parser("process", help="Inbox 자동 처리")
    process_parser.add_argument("--apply", action="store_true", help="변경사항 적용")

    # link
    link_parser = subparsers.add_parser("link", help="관련 노트 제안")
    link_parser.add_argument("file", help="노트 파일")

    # stats
    subparsers.add_parser("stats", help="통계 보기")

    # review
    review_parser = subparsers.add_parser("review", help="리뷰")
    review_parser.add_argument(
        "period", nargs="?", default="week", choices=["day", "week", "month"]
    )

    # migrate
    migrate_parser = subparsers.add_parser("migrate", help="CMDS → PARA 마이그레이션")
    migrate_parser.add_argument("--apply", action="store_true", help="변경사항 적용")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    cli = VaultCLI(args.vault)

    if args.command == "note":
        cli.cmd_note(args.title, args.type)
    elif args.command == "today":
        cli.cmd_today()
    elif args.command == "process":
        cli.cmd_process(dry_run=not args.apply)
    elif args.command == "link":
        cli.cmd_link(args.file)
    elif args.command == "stats":
        cli.cmd_stats()
    elif args.command == "review":
        cli.cmd_review(args.period)
    elif args.command == "migrate":
        cli.cmd_migrate(dry_run=not args.apply)


if __name__ == "__main__":
    main()
