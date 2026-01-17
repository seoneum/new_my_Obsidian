---
tags:
  - plugin
  - setting
  - Obsidian
link: "[[📌Guidline]]"
updated: 2025-01-17
---

# Obsidian 플러그인 가이드

> 이 문서는 CMDS Vault에서 사용하는 플러그인을 정리합니다.
> 각 플러그인의 설치법, 설정, 실전 사용법을 포함합니다.

---

## 📌 필수 플러그인 (반드시 설치)

### 1. Templater ⭐⭐⭐

**역할**: 모든 템플릿의 핵심 엔진

**설치**: Community Plugins → Templater

**필수 설정**:
| 설정 | 값 |
|-----|---|
| Template folder location | `CMDS/500. setting/501. Template` |
| Trigger on new file creation | OFF |

**단축키**:
- `Alt+N`: Create new note from template
- `Ctrl+T`: Open insert template modal
- `Ctrl+Alt+T`: Replace templates in active file

**문법 예시**:
```javascript
<% tp.date.now("YYYY-MM-DD") %>      // 오늘 날짜
<% tp.file.title %>                   // 파일 이름
<%* await tp.file.rename("새이름") %> // 파일 이름 변경
<%* await tp.file.move("폴더/파일") %> // 파일 이동
```

---

### 2. Dataview ⭐⭐⭐

**역할**: 노트를 데이터베이스처럼 조회/정렬/필터

**설치**: Community Plugins → Dataview

**필수 설정**:
| 설정 | 값 |
|-----|---|
| Enable JavaScript Queries | ON |
| Enable Inline JavaScript | ON |

**기본 문법**:
```dataview
TABLE file.ctime as "생성일", type, group
FROM "CMDS/200. CMDS"
WHERE type = "merge"
SORT file.ctime DESC
LIMIT 10
```

**JavaScript 문법** (더 유연):
```dataviewjs
const pages = dv.pages('"CMDS/200. CMDS"')
  .where(p => p.type === "merge")
  .sort(p => p.file.ctime, 'desc')
  .limit(10);

dv.table(["노트", "분야", "타입"], 
  pages.map(p => [p.file.link, p.group, p.type])
);
```

---

### 3. Calendar

**역할**: 달력에서 Daily 노트 클릭 생성

**설치**: Community Plugins → Calendar

**설정**:
- Weekly note format: `YYYY-[W]WW`
- Show week number: ON

**사용법**: 오른쪽 사이드바 달력에서 날짜 클릭 → Daily 노트 자동 생성

---

### 4. Spaced Repetition

**역할**: 플래시카드 복습 시스템

**설치**: Community Plugins → Spaced Repetition

**플래시카드 문법**:
```markdown
질문:: 답변
개념::: 정의  <!-- 양방향 -->
```

**태그로 분류**:
```markdown
#flashcards/philosophy
#flashcards/engineering
#flashcards/math
```

**복습**: 
- 사이드바 📚 아이콘 클릭
- 또는 `Ctrl+P` → "Review flashcards"

---

## 🔧 프로젝트 관리 플러그인

### 5. Kanban

**역할**: 칸반 보드로 프로젝트/할일 관리

**설치**: Community Plugins → Kanban

#### 기본 사용법

1. **새 보드 만들기**: `Ctrl+P` → "Kanban: Create new board"
2. **열(Lane) 추가**: 보드 우측 "+" 버튼
3. **카드 추가**: 열 하단 "Add a card"

#### 실전 활용: 프로젝트 관리

```
┌────────────┬────────────┬────────────┬────────────┐
│  Backlog   │ This Week  │In Progress │   Done     │
├────────────┼────────────┼────────────┼────────────┤
│ - 모터 선정 │ - 센서 테스트│ - 제어기 튜닝│ - 기구 설계 │
│ - 통신 구현 │            │            │ - BOM 작성  │
└────────────┴────────────┴────────────┴────────────┘
```

#### 권장 보드 구조

**프로젝트용**:
- Backlog → This Week → In Progress → Review → Done

**학기용**:
- To Do → In Progress → Waiting → Done

#### 설정 팁

보드 왼쪽 위 ⚙️ → Settings:
| 설정 | 권장값 |
|-----|-------|
| Lane width | 300px |
| Show card checkbox | ON |
| New cards to | Bottom |

#### 노트 연결

카드에 `[[노트명]]` 입력하면 해당 노트로 링크됩니다.

---

## 📚 논문/자료 관리 플러그인

### 6. Zotero Integration

**역할**: Zotero 논문 관리자와 Obsidian 연동

**설치**: 
1. [Zotero](https://www.zotero.org/) 설치 (데스크탑 앱)
2. Zotero → Tools → Add-ons → Better BibTeX 설치
3. Obsidian → Community Plugins → Zotero Integration

#### Zotero 설정

1. Edit → Preferences → Better BibTeX
2. Citation key format: `[auth:lower][year]`
3. Export → Quick Copy: Better BibTeX Citation Key

#### Obsidian 설정

Settings → Zotero Integration:
| 설정 | 값 |
|-----|---|
| Database | Zotero 라이브러리 경로 |
| Note folder | `CMDS/400. Reference/420. Engineering_Reference` |
| Bibliography style | APA 7th (또는 선호 스타일) |

#### 논문 가져오기 워크플로우

```
1. Zotero에서 논문 추가 (브라우저 플러그인 or PDF 드래그)
      ↓
2. Obsidian: Ctrl+P → "Zotero: Insert citation"
      ↓
3. 논문 검색 → 선택
      ↓
4. Reference 폴더에 노트 자동 생성
      ↓
5. 읽고 이해한 내용 → Merge 노트로 발전
```

#### 추천 템플릿

Zotero Integration 설정 → Note Template:

```markdown
---
type: reference
title: "{{title}}"
authors:
{{#each creators}}
  - "{{lastName}}, {{firstName}}"
{{/each}}
year: {{date | format("YYYY")}}
tags:
  - reference
  - paper
  - tagging/needed
citekey: {{citekey}}
---

# {{title}}

## Metadata
- Authors: {{authors}}
- Year: {{date | format("YYYY")}}
- DOI: {{DOI}}
- Citekey: {{citekey}}

## Abstract
{{abstractNote}}

## Key Points
- 

## My Notes
- 

## Questions
- 

## Next
- [ ] Merge로 발전시키기
```

---

## ☁️ 동기화 플러그인

### 7. Remotely Save

**역할**: Google Drive/Dropbox/OneDrive로 무료 동기화 (아이패드 포함)

**설치**: Community Plugins → Remotely Save

#### Google Drive 설정 (권장)

**PC에서**:
1. Settings → Remotely Save
2. Remote Service: `Google Drive (GDrive)`
3. `Auth` 버튼 → Google 계정 로그인
4. 인증 완료 후 `Check` 버튼으로 연결 확인

**아이패드에서**:
1. Obsidian 앱 설치
2. 같은 이름의 vault 생성 (빈 vault)
3. Remotely Save 설치 → 같은 Google 계정 연결
4. `Sync` 버튼 클릭 → 전체 동기화

#### 권장 설정

| 설정 | 값 | 설명 |
|-----|---|-----|
| Sync on Save | ON | 저장할 때마다 동기화 |
| Auto Sync Interval | 5분 | 자동 동기화 주기 |
| Skip Large Files | ON (50MB) | 큰 파일 제외 |
| Conflict Resolution | Keep Both | 충돌 시 둘 다 보관 |

#### 동기화 순서 (중요!)

```
1. 편집하기 전에 반드시 Sync 버튼 클릭
2. 편집 완료
3. Sync 버튼 클릭 (또는 자동 동기화 대기)
4. 다른 기기로 이동
5. 그 기기에서 Sync 버튼 클릭 후 편집
```

#### 트러블슈팅

| 문제 | 해결 |
|-----|-----|
| 동기화 안 됨 | Settings → Remotely Save → Re-authenticate |
| 충돌 발생 | `remotely-save-backup/` 폴더에서 원본 확인 |
| 느림 | Skip Large Files 활성화, 첨부파일 정리 |
| 특정 파일 누락 | `.obsidian/` 폴더 제외 여부 확인 |

#### 주의사항

⚠️ **양쪽에서 동시 편집 금지** - 충돌 발생
⚠️ **플러그인 설정**은 동기화 안 됨 - 각 기기에서 별도 설정

---

## 🛠️ 편의성 플러그인

### 8. Outliner

**역할**: 글머리 기호 편집 향상

**핵심 기능**:
- `Ctrl+A`: 위계에 따라 선택 (문장 → 문단 → 전체)
- `Tab/Shift+Tab`: 들여쓰기/내어쓰기
- `Ctrl+↑/↓`: 항목 위/아래 이동

---

### 9. Tag Wrangler

**역할**: 태그 관리 (이름 변경, 병합)

**사용법**:
1. 오른쪽 사이드바 → Tags 패널
2. 태그 우클릭 → Rename tag
3. 전체 노트에서 일괄 변경됨

---

### 10. Omnisearch

**역할**: 강력한 전체 검색

**단축키**: `Ctrl+Shift+O`

**특징**: 키워드가 들어간 모든 파일 검색 (파일명 + 내용)

---

### 11. Highlightr

**역할**: 다양한 색상 하이라이트

**사용법**: 
1. 텍스트 드래그
2. `Ctrl+P` → "Highlightr"
3. 색상 선택

---

### 12. Paste URL into Selection

**역할**: URL을 마크다운 링크로 쉽게 변환

**사용법**:
1. 링크 텍스트가 될 문장 드래그
2. URL 복사한 상태에서 `Ctrl+V`
3. 자동으로 `[선택한 텍스트](URL)` 형식으로 변환

---

### 13. Excalidraw

**역할**: 다이어그램/스케치 도구

**사용법**: `Ctrl+P` → "Create new drawing"

**팁**:
- `Shift` 누르고 그리면 각도/비율 고정
- 노트에서 `![[drawing.excalidraw]]`로 임베드

---

## 📖 독서/학습 플러그인

### 14. Korean Book Info

**역할**: 국내 도서 정보 자동 입력

**사용법**:
1. `[[책제목]]` 형식으로 노트 생성
2. `Ctrl+P` → "Korean Book Info"
3. 도서 정보 자동 채움

---

### 15. Book Search

**역할**: 해외 도서 정보 검색

**단축키**: `Ctrl+Shift+B`

---

## 🎨 테마/스타일 플러그인

### 16. Minimal Theme

**설치**: 
1. Settings → Appearance → Themes → Minimal
2. Community Plugins → Minimal Theme Settings

**추천 설정**:
- Style: Default
- Accent color: 선호 색상
- Image grids: ON

---

### 17. Style Settings

**역할**: 테마 세부 커스터마이징

Settings → Style Settings에서 폰트, 색상, 여백 등 조절

---

## ⚡ 고급 플러그인

### 18. Graph Analysis

**역할**: 노트 간 연결 분석

**설정**: Adamic, Jaccard 알고리즘만 ON 권장

---

### 19. Strange New World

**역할**: 노트 참조 횟수 표시

파일명 옆에 참조 횟수가 표시됩니다.

---

### 20. Smart Composer

**역할**: AI 기반 노트 작성 도우미

API 키 필요 (OpenAI, Claude 등)

---

## 📋 플러그인 설치 우선순위

### 1순위 (필수)
- [ ] Templater
- [ ] Dataview
- [ ] Calendar
- [ ] Spaced Repetition

### 2순위 (강력 권장)
- [ ] Kanban
- [ ] Remotely Save (아이패드 사용시)
- [ ] Outliner
- [ ] Tag Wrangler

### 3순위 (편의)
- [ ] Omnisearch
- [ ] Highlightr
- [ ] Paste URL into Selection
- [ ] Excalidraw

### 4순위 (논문 관리시)
- [ ] Zotero Integration

---

## 🔗 관련 문서

- [[📌Guidline]] - 전체 사용 가이드
- [[Template Syntax]] - 템플릿 문법
- [[Dataview Test]] - Dataview 예제

