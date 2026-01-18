# 📌 Vault 가이드

> **3초 룰**: 어디에 둘지 모르겠으면 → 📥 Inbox
> 복잡하게 생각하지 마세요. 일단 적고, 나중에 정리.

---

# 1. 폴더 구조

```
📥 Inbox/        → 일단 던지는 곳 (나중에 정리)
📅 Daily/        → 오늘 할 일 + 저널링
📚 Lectures/     → 강의 필기 (과목별)
📖 Books/        → 책/논문 읽은 것
💡 Notes/        → 내 생각, 개념 정리
📝 Problems/     → 문제 풀이 (수학, 코딩)
🧠 Flashcards/   → 플래시카드 모음
📓 Feynman/      → 페인만 학습 노트
🎯 Projects/     → 진행 중 프로젝트
🗃️ Archive/      → 끝난 것들
⚙️ Meta/         → 설정/시스템
    ├── Templates/  → 템플릿
    ├── Prompts/    → AI 프롬프트
    └── Guides/     → 시스템 가이드
```

## 어디에 둘까? (결정 트리)

```
새 노트 작성
    │
    ├─ 3초 안에 판단 안 됨 ──────→ 📥 Inbox
    │
    ├─ 오늘 할 일/일기 ──────────→ 📅 Daily
    │
    ├─ 강의/수업 들으면서 ───────→ 📚 Lectures/{과목명}
    │
    ├─ 책/논문 읽으면서 ─────────→ 📖 Books
    │
    ├─ 내 말로 정리/설명 ────────→ 💡 Notes
    │
    ├─ 문제 풀이 ────────────────→ 📝 Problems
    │
    ├─ 플래시카드 ───────────────→ 🧠 Flashcards
    │
    ├─ 페인만 학습 ──────────────→ 📓 Feynman
    │
    └─ 프로젝트 관련 ────────────→ 🎯 Projects
```

---

# 2. 파일명 규칙 (Prefix)

| Prefix | 용도 | 예시 |
|--------|------|------|
| `D -` | Daily | `D - 2026-01-18.md` |
| `L -` | 강의 | `L - MIT_18.01_1.md` |
| `N -` | 일반 메모 | `N - 아이디어.md` |
| `C -` | 개념 정리 | `C - Modern C++.md` |
| `P -` | 문제 풀이 | `P - 백준 1234.md` |
| `FC -` | 플래시카드 | `FC - C++ 기초.md` |
| `FYN -` | 페인만 노트 | `FYN - 2026-01-18.md` |
| `R -` | 레퍼런스 | `R - CMake Syntax.md` |
| `PRJ -` | 프로젝트 | `PRJ - Hexapod.md` |

---

# 3. 일일 워크플로우

## 아침 (5분)
1. 📅 Daily 노트 열기 (또는 생성)
2. 오늘 Top 3 작성
3. (선택) 전날 플래시카드 복습

## 낮 (공부/작업 중)
- 강의 → `📚 Lectures/{과목}`에 바로 작성
- 갑자기 떠오른 생각 → `📥 Inbox`에 던지기
- 모르는 개념 → 일단 적고 나중에 `💡 Notes`로

## 저녁 (10분)
1. 📅 Daily에 오늘 한 일 정리
2. (선택) 오늘 배운 것 플래시카드 작성
3. 내일 Top 3 미리 작성

---

# 4. 플래시카드

## 문법
```markdown
질문:: 답변
개념::: 정의 (양방향)
```

## 태그
```markdown
#flashcards/math
#flashcards/cs
#flashcards/philosophy
```

## 복습
`Ctrl+P` → "Spaced Repetition: Review"

---

# 5. 설정

## Templater
- Template folder: `⚙️ Meta/Templates`

## 필수 플러그인
| 플러그인 | 용도 |
|---------|------|
| Templater | 템플릿 |
| Dataview | 자동 조회 |
| Calendar | Daily 노트 |
| Spaced Repetition | 플래시카드 |

---

# 6. FAQ

**Q: 어디에 저장할지 모르겠어요**
→ 📥 Inbox. 나중에 정리하면 됨.

**Q: 강의 필기에 내 생각이 섞였어요**
→ 그냥 둬요. 나중에 `💡 Notes`에 따로 정리.

**Q: 폴더가 너무 많아요**
→ 자주 쓰는 건 4개뿐: Inbox, Daily, Lectures, Notes

---

# 7. 핵심 단축키

| 동작 | 단축키 |
|-----|--------|
| 새 노트 | Ctrl+N |
| 템플릿 삽입 | Ctrl+T |
| 명령어 팔레트 | Ctrl+P |
| 검색 | Ctrl+Shift+F |

---

> 💡 **기억하세요**: 완벽하게 분류하려고 멈추지 마세요.
> 모르면 Inbox, 나중에 정리. 흐름을 유지하는 게 핵심입니다.
