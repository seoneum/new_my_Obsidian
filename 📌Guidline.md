# 📌 CMDS Vault 완전 가이드

> 이 문서를 읽고 따라하면 **처음 쓰는 사람도 똑같이 사용**할 수 있습니다.
> 복잡해 보여도 핵심은 간단합니다: **캡처 → 이해 → 정리 → 산출**

---

## 목차
1. [5분 퀵스타트](#1-5분-퀵스타트)
2. [폴더 구조 (무엇을 어디에)](#2-폴더-구조-무엇을-어디에)
3. [노트 타입별 사용법](#3-노트-타입별-사용법)
4. [일일 루틴 가이드](#4-일일-루틴-가이드)
5. [플래시카드 시스템](#5-플래시카드-시스템)
6. [태그 & 속성 규칙](#6-태그--속성-규칙)
7. [템플릿 사용법](#7-템플릿-사용법)
8. [플러그인 가이드](#8-플러그인-가이드)
9. [FAQ](#9-faq)
10. [트러블슈팅](#10-트러블슈팅)

---

# 1. 5분 퀵스타트

## 1.1 필수 플러그인 설치

Community Plugins에서 아래를 설치하세요:

| 플러그인 | 필수 여부 | 역할 |
|---------|----------|------|
| **Templater** | ⭐ 필수 | 모든 템플릿 작동의 핵심 |
| **Dataview** | ⭐ 필수 | 통계/자동 조회 기능 |
| **Calendar** | 권장 | 달력에서 Daily 노트 클릭 생성 |
| **Spaced Repetition** | 권장 | 플래시카드 복습 |

## 1.2 Templater 설정 (중요!)

1. Settings → Templater
2. **Template folder location**: `CMDS/500. setting/501. Template`
3. **Trigger Templater on new file creation**: OFF (수동 실행 권장)

## 1.3 첫 노트 만들기

1. 아무 곳에서나 새 노트 생성 (Ctrl+N)
2. **Ctrl+T** (또는 Alt+N) → `Master Template` 선택
3. 원하는 노트 타입 선택
4. 끝! 자동으로 올바른 폴더로 이동됩니다

> [!tip] 단축키 설정
> Settings → Hotkeys에서 "Templater: Create new note from template"에 `Alt+N` 지정 권장

---

# 2. 폴더 구조 (무엇을 어디에)

```
CMDS/
├── 100. Inbox/          → 빠른 캡처 (분류 나중에)
├── 200. CMDS/           → 내 지식 시스템
│   ├── 201. Connect/    → 강의 필기
│   ├── 220. Merge/      → 내 지식 (파인만)
│   │   ├── 221. Journaling/
│   │   ├── 222. FlashCard/
│   │   └── 223. Feynman/
│   ├── 240. Develop/    → 이론 정리/치트시트
│   ├── 260. Share/      → 외부 공유 산출물
│   └── 280. Project/    → 프로젝트 본진
├── 300. Thinking/       → 미해결 질문/아이디어
├── 400. Reference/      → 자료 창고
│   ├── 401~430/         → 분야별 자료
│   └── 490. People/     → 인물 노트
└── 500. setting/        → 템플릿/설정
```

## 2.1 핵심 규칙: "역할"로 분류한다

**주제(EE/Phil/로봇)** 가 아니라 **노트의 역할**로 분류합니다.

| 역할 | 폴더 | 언제 사용 |
|-----|------|----------|
| 빠른 메모 | 100. Inbox | 3초 안에 판단 안 될 때 |
| 강의 필기 | 201. Connect | 받아쓰기, 남의 말 기록 |
| 내 지식 | 220. Merge | 내 말로 설명할 수 있는 것 |
| 치트시트 | 240. Develop | 공식/정의/절차 정리 |
| 산출물 | 260. Share | 블로그/발표/보고서 |
| 프로젝트 | 280. Project | 로봇/대회/제작 |
| 미해결 질문 | 300. Thinking | 답 못 찾은 질문, 아이디어 |
| 자료 보관 | 400. Reference | 논문/책/웹페이지 |

---

# 3. 노트 타입별 사용법

## 3.1 INBOX — 빠른 캡처

**언제**: 어디에 둘지 모르겠을 때, 일단 적고 싶을 때

```
📥 INBOX 선택 → 분야 선택 → 제목 입력 → 끝
```

- 자동으로 `tagging/needed` 태그가 붙음
- 나중에 정리 세션에서 처리

## 3.2 DAILY — 일일 노트

**언제**: 매일 아침 (하루 시작할 때)

```
📅 DAILY 선택 → 하루 타입 선택 → 자동 생성
```

### 하루 타입

| 타입 | 설명 | 자동 생성 섹션 |
|-----|------|---------------|
| 📚 공부 Day | 학교/도서관 | Study Log |
| 🔧 프로젝트 Day | 로봇/개발 | Project Log |
| 📚🔧 혼합 Day | 둘 다 | Study + Project |
| 🌴 쉬는 Day | 휴식 | Rest Day |

## 3.3 CONNECT — 강의 필기

**언제**: 수업/유튜브/세미나 들을 때

```
📚 CONNECT 선택 → 분야 선택 → 과목/회차 입력 → 강의 URL(선택)
```

**규칙**: 여기에는 "남의 말"만 적습니다. 내 생각은 Merge에서!

## 3.4 MERGE — 내 지식 (파인만 노트)

**언제**: 배운 것을 내 말로 정리할 때

```
🧠 MERGE 선택 → 제목 입력 → 파인만 4단계로 작성
```

### 파인만 4단계

1. **Explain**: 12살에게 설명하듯 쓰기
2. **Gaps**: 설명 중 막히는 부분 찾기
3. **Repair**: 다시 공부해서 빈틈 채우기
4. **Teach-back**: 3문장 → 1문장으로 압축

## 3.5 THINKING — 미해결 질문/아이디어

**언제**: 답을 못 찾은 질문, 떠오른 아이디어, 고민

```
💭 THINKING 선택 → 유형 선택 → 분야 선택 → 제목 입력
```

### 사유 유형

| 유형 | 언제 |
|-----|------|
| ❓ 미해결 질문 | 답을 모르는 질문 |
| 💡 아이디어 | 검증 안 된 가설/아이디어 |
| 🤔 고민/딜레마 | 선택지가 있는 결정 |
| 🔗 연결점 | 두 개념 사이의 연결 발견 |

## 3.6 WEEKLY — 주간 복습

**언제**: 일요일 저녁

```
📊 WEEKLY 선택 → 자동으로 이번 주 노트 조회
```

- Dataview로 이번 주 노트 자동 표시
- 주간 핵심 플래시카드 정리
- 다음 주 목표 설정

## 3.7 PROJECT — 프로젝트

**언제**: 로봇/대회/개발 프로젝트 시작할 때

```
🔧 PROJECT 선택 → 분야 선택 → 목표/마감일 입력
```

프로젝트 노트는 **컨트롤타워**입니다:
- 개념이 필요하면 → Merge 만들고 링크
- 자료가 필요하면 → Reference에 저장하고 링크

---

# 4. 일일 루틴 가이드

## 4.1 풀 루틴 (권장)

```
┌─────────────────────────────────────────────────────────────┐
│  ☀️ 아침 (기상 ~ 출발)                                       │
│  ├─ 1. 기상                                                  │
│  ├─ 2. 📖 아침 독서 (40분) - 책 읽기                          │
│  ├─ 3. 씻기 + 아침                                           │
│  └─ 4. 📝 FC (아침) - 전날 노트 복습                          │
├─────────────────────────────────────────────────────────────┤
│  🏫 낮 (학교/도서관)                                         │
│  ├─ Daily 노트에 Top 3 체크                                  │
│  ├─ 공부/프로젝트 진행                                        │
│  └─ 새로 배운 것 → Connect/Inbox에 기록                       │
├─────────────────────────────────────────────────────────────┤
│  🌙 저녁 (집 가기 1시간 전)                                   │
│  ├─ 1. 🪞 Evening Reflection (사유 중심 저널링)               │
│  │     ├─ 🔧 오늘의 공학                                     │
│  │     ├─ 🏛️ 오늘의 철학                                     │
│  │     └─ 💭 자유 사유 (공학+철학 교차점)                      │
│  ├─ 2. 🧠 Feynman 노트 (오늘 배운 것 설명)                    │
│  ├─ 3. 📝 FC (저녁) - 오늘 배운 것 플래시카드                  │
│  └─ 4. 📋 내일 Top 3 미리 작성                               │
└─────────────────────────────────────────────────────────────┘
```

## 4.2 사유 중심 저널링

이 볼트의 저널링은 **"감사일기"가 아닙니다**.
**오늘 사유한 것**을 기록합니다.

### 🔧 오늘의 공학 (Engineering)
```markdown
- 오늘 배운/작업한 기술:
- 막혔던 문제:
- 해결했거나 시도한 방법:
- 내일 이어서 할 것:
```

### 🏛️ 오늘의 철학 (Philosophy)
```markdown
- 오늘 읽은/생각한 텍스트:
- 핵심 논증/개념:
- 내 해석/의문:
- 더 생각해볼 질문:
```

### 💭 자유 사유 (Free Thinking)
```markdown
- 오늘 머릿속을 맴돈 생각:
- 공학과 철학이 만난 지점 (있다면):
- 아직 답 못 찾은 질문 → [[300. Thinking]] 으로
```

## 4.3 주간 루틴

| 요일 | 추가 작업 |
|-----|----------|
| 월~토 | 일일 루틴 |
| **일요일 저녁** | 📊 Weekly Review 작성 |

---

# 5. 플래시카드 시스템

## 5.1 스케줄

| 시간 | 이름 | 복습 대상 |
|-----|------|----------|
| 아침 (출발 전) | FC Morning | 전날 노트 |
| 저녁 (집 가기 전) | FC Evening | 오늘 노트 |
| 일요일 저녁 | FC Weekly | 이번 주 전체 |

## 5.2 플래시카드 작성법

Spaced Repetition 플러그인 문법:

```markdown
질문:: 답변
```

또는 양방향:

```markdown
개념::: 정의
```

### 분야별 태그

```markdown
#flashcards/philosophy
#flashcards/engineering  
#flashcards/math
#flashcards/coding
#flashcards/weekly
```

### 예시

```markdown
## 🔧 공학
#flashcards/engineering

PID 제어기의 P항 역할:: 현재 오차에 비례하여 제어 출력을 생성

## 🏛️ 철학
#flashcards/philosophy

칸트의 정언명령 첫 번째 정식화::: "네 의지의 준칙이 항상 동시에 보편적 법칙 수립의 원리로서 타당할 수 있도록 행위하라"

## 🔢 수학
#flashcards/math

라그랑주 승수법:: $\nabla f = \lambda \nabla g$ 를 풀어 제약조건 하 극값 찾기
```

## 5.3 복습 방법

1. 왼쪽 사이드바 → 📚 아이콘 (Review)
2. 또는 `Ctrl+P` → "Spaced Repetition: Review flashcards"
3. 카드 보면서 난이도 선택 (Easy/Good/Hard)

---

# 6. 태그 & 속성 규칙

## 6.1 핵심 태그 (이것만 기억)

| 태그 | 의미 |
|-----|------|
| `tagging/needed` | 나중에 정리 필요 |
| `to-merge` | Merge 노트로 발전시킬 것 |
| `flashcards/*` | 플래시카드 분야별 분류 |

## 6.2 자동 생성 태그

템플릿이 자동으로 붙이는 태그:

- `daily`, `day/study`, `day/project` 등
- `thinking/question`, `thinking/idea` 등
- `lecture`, `reference`, `merge` 등

## 6.3 속성(Properties) 규칙

### authors 규칙 (중요!)

```yaml
# 내가 쓴 글
authors:
  - "[[김선음]]"

# 남의 말 기록 (강의/논문)
authors: []
```

이 규칙 덕분에 "내 지식만" 필터링 가능합니다.

### type 규칙

한 노트 = 한 타입

```yaml
type: daily      # 또는 lecture, reference, merge, develop, project, thinking 등
```

### group 규칙

분야/도메인 1개만 선택

```yaml
group: EE        # 또는 Phil, SE, Math, Robotics, General
```

---

# 7. 템플릿 사용법

## 7.1 템플릿 목록

| 템플릿 | 단축 접근 | 용도 |
|-------|----------|------|
| Master Template | 메인 진입점 | 모든 노트 타입 선택 |
| Daily_Template | DAILY 메뉴 | 일일 노트 |
| Thinking_Template | THINKING 메뉴 | 미해결 질문/아이디어 |
| Weekly_Review_Template | WEEKLY 메뉴 | 주간 복습 |
| FC_Morning_Template | FC MORNING 메뉴 | 아침 플래시카드 |
| FC_Evening_Template | FC EVENING 메뉴 | 저녁 플래시카드 |
| Feynman Template | MERGE 후 수동 | 파인만 노트 |
| People 템플릿 (4종) | PEOPLE 메뉴 | 인물 노트 |

## 7.2 파일명 규칙 (Prefix)

템플릿이 자동으로 붙입니다:

| Prefix | 역할 |
|--------|------|
| `D -` | Daily |
| `N -` | Inbox 메모 |
| `L -` | Lecture (Connect) |
| `W -` | Web clip (임시) |
| `R -` | Reference |
| `M -` | Merge |
| `DEV -` | Develop |
| `SHARE -` | Share |
| `PRJ -` | Project |
| `PPL -` | People |
| `THK -` | Thinking |
| `FC -` | FlashCard |
| `FYN -` | Feynman |

---

# 8. 플러그인 가이드

## 8.1 Kanban — 프로젝트 관리

### 설치 & 기본 사용

1. Community Plugins → Kanban 설치
2. `Ctrl+P` → "Kanban: Create new board"
3. 보드 이름 입력 → 생성

### 실전 사용법

**프로젝트별 Kanban 보드 만들기:**

```
┌──────────┬──────────┬──────────┬──────────┐
│ Backlog  │ This Week│ In Progress│ Done   │
├──────────┼──────────┼──────────┼──────────┤
│ - 기능A  │ - 기능B  │ - 기능C  │ - 기능D  │
│ - 기능E  │          │          │          │
└──────────┴──────────┴──────────┴──────────┘
```

**추천 활용:**
- 로봇 프로젝트 → `PRJ - 로봇대회` 노트에서 Kanban 링크
- 학기별 과제 → 과목별 Kanban 보드

### 카드 추가

- 각 열 하단 `+ Add a card` 클릭
- 또는 기존 노트를 드래그해서 넣기 (`[[노트명]]` 형태)

### 설정 팁

보드 왼쪽 위 ⚙️ → Settings:
- `Lane width`: 300px 권장
- `Show card checkbox`: ON (완료 체크)

## 8.2 Zotero — 논문 관리

### 워크플로우 개요

```
Zotero (논문 수집)
    ↓ 
Obsidian Reference 폴더 (노트 생성)
    ↓
Merge 노트 (내 이해)
```

### 설치

1. [Zotero](https://www.zotero.org/) 설치
2. Zotero Better BibTeX 플러그인 설치
3. Obsidian: "Zotero Integration" 플러그인 설치

### 설정

1. Zotero → Edit → Preferences → Better BibTeX
   - Citation key format: `[auth:lower][year]`
2. Obsidian → Zotero Integration 설정
   - Database: Zotero 라이브러리 경로 선택
   - Note folder: `CMDS/400. Reference/420. Engineering_Reference` (또는 원하는 폴더)

### 논문 가져오기

1. Zotero에서 논문 추가 (PDF 드래그 또는 브라우저 플러그인)
2. Obsidian에서 `Ctrl+P` → "Zotero: Insert citation"
3. 논문 검색 → 선택 → 노트 자동 생성

### 추천 템플릿 (Zotero Integration 설정)

```markdown
---
type: reference
title: "{{title}}"
authors: {{authors}}
year: {{date | format("YYYY")}}
tags:
  - reference
  - paper
---

# {{title}}

## Metadata
- Authors: {{authors}}
- Year: {{date | format("YYYY")}}
- DOI: {{DOI}}

## Abstract
{{abstractNote}}

## Notes
- 

## Key Points
- 

## Next
- [ ] Merge로 발전시키기
```

## 8.3 Remotely-Save — 아이패드 동기화

### 개요

Obsidian Sync 없이 **Google Drive/Dropbox/OneDrive**로 무료 동기화

### 설치

1. Community Plugins → "Remotely Save" 설치
2. 모바일 기기에도 동일하게 설치

### Google Drive 설정 (권장)

**PC에서:**

1. Settings → Remotely Save
2. Remote Service: `Google Drive (GDrive)`
3. `Auth` 버튼 클릭 → Google 로그인
4. 동기화 폴더: 기본값 사용 (`/Apps/remotely-save-obsidian/`)

**아이패드에서:**

1. Obsidian 설치
2. 같은 vault 이름으로 빈 vault 생성
3. Remotely Save 설치 → 같은 Google 계정 연결
4. `Sync` 버튼 → 파일 동기화

### 동기화 설정 권장값

| 설정 | 권장값 |
|-----|--------|
| Sync on Save | ON |
| Auto Sync Interval | 5분 |
| Skip Large Files | ON (>50MB) |

### 주의사항

- **양쪽에서 동시 편집 금지** (충돌 발생 가능)
- 편집 전 반드시 `Sync` 실행
- 충돌 시 백업 폴더 확인 (`remotely-save-backup/`)

### 트러블슈팅

| 문제 | 해결 |
|-----|------|
| 동기화 안 됨 | Auth 다시 진행 |
| 충돌 발생 | 백업 폴더에서 원본 확인 후 수동 병합 |
| 느린 동기화 | Skip Large Files 활성화 |

## 8.4 기타 유용한 플러그인

| 플러그인 | 용도 | 핵심 단축키/기능 |
|---------|------|-----------------|
| Outliner | 글머리 기호 편집 | Ctrl+A (위계별 선택) |
| Tag Wrangler | 태그 이름 일괄 변경 | 태그 우클릭 → Rename |
| Omnisearch | 전체 검색 | Ctrl+Shift+O |
| Calendar | 달력에서 Daily 노트 | 날짜 클릭 |

---

# 9. FAQ

## Q1. "이거 어디에 저장해야 하지?"

**3초 안에 결정 안 되면 → Inbox**

나중에 `tagging/needed`로 정리하면 됩니다.

## Q2. 웹클립이 애매해요

- 임시로 저장 → Web Clip (임시) → Inbox
- 확실히 보관할 것 → Web Clip (Reference) → Reference 폴더

## Q3. 강의 필기에 내 생각이 섞였어요

- 강의 노트는 그대로 둡니다
- 내 생각은 **새 Merge 노트**에 작성
- 서로 링크로 연결

## Q4. 300. Thinking은 언제 쓰나요?

Daily 저널링 중 **"아직 답 못 찾은 질문"**이 생기면:
1. `💭 THINKING` 으로 새 노트 생성
2. 질문/아이디어/딜레마/연결점 중 선택
3. 나중에 답을 찾으면 Resolution 섹션 작성

## Q5. 플래시카드가 너무 많아요

- 아침/저녁 FC는 **당일 것만**
- 주간 FC에서 **중요한 것만** 선별
- 태그별로 복습 (Settings에서 태그 필터)

## Q6. Dataview가 안 보여요

1. Dataview 플러그인 설치 확인
2. Settings → Dataview → Enable JavaScript Queries: ON
3. Settings → Dataview → Enable Inline JavaScript: ON

---

# 10. 트러블슈팅

## 템플릿이 작동 안 해요

1. **Templater 설정 확인**
   - Template folder: `CMDS/500. setting/501. Template`
2. **문법 오류 확인**
   - `<%` 와 `%>` 짝이 맞는지
3. **콘솔 확인**
   - `Ctrl+Shift+I` → Console 탭에서 에러 확인

## 자동 이동이 안 돼요

- 대상 폴더가 존재하는지 확인
- 예: `CMDS/200. CMDS/220. Merge/222. FlashCard/` 폴더 있는지

## 동기화 충돌 발생

1. 양쪽 기기 모두 Obsidian 종료
2. 클라우드 서비스에서 최신 버전 확인
3. 한쪽에서만 편집 후 동기화
4. 다른 쪽에서 Pull

## Dataview 쿼리 에러

- `dv.pages()` → 모든 노트
- `dv.pages('"폴더명"')` → 특정 폴더 (따옴표 2개 필요)
- 날짜 비교 시 `dv.date("YYYY-MM-DD")` 사용

---

# 부록: 빠른 참조 카드

## 일일 체크리스트

```
☀️ 아침
- [ ] 기상 + 독서 (40분)
- [ ] FC Morning (전날 복습)

🌙 저녁
- [ ] Evening Reflection (공학/철학/자유사유)
- [ ] Feynman 노트
- [ ] FC Evening (오늘 복습)
- [ ] 내일 Top 3

📅 일요일
- [ ] Weekly Review
```

## 노트 생성 흐름

```
Alt+N → Master Template → 타입 선택 → 정보 입력 → 완료!
```

## 핵심 단축키

| 동작 | 단축키 |
|-----|--------|
| 새 노트 from 템플릿 | Alt+N |
| 템플릿 삽입 | Ctrl+T |
| 명령어 팔레트 | Ctrl+P |
| 전체 검색 | Ctrl+Shift+O |
| Daily 노트 | 캘린더에서 날짜 클릭 |

---

> 💡 **기억하세요**: 완벽하게 분류하려고 멈추지 마세요. 
> 모르면 Inbox, 나중에 정리. 흐름을 유지하는 게 핵심입니다.
