# 🤖 AI Vault 생성 프롬프트

아래 프롬프트를 AI(ChatGPT, Claude, opencode 등)에게 복사해서 사용하세요.

---

## 전체 Vault 생성 프롬프트

```
나는 대학생이고, Obsidian을 사용해서 학습 관리 시스템을 만들고 싶어.
CMDS(Connect-Merge-Develop-Share) 시스템 기반으로 vault를 구성해줘.

## 내 정보
- 전공: [전공1], [전공2] (있다면)
- 주로 사용하는 프로그래밍 언어: [언어들]
- 현재 학기: [예: 24-1]

## 요청 사항

### 1. 폴더 구조 생성
```
Vault/
├── 100. Inbox/
│   ├── 101. Anything/
│   ├── 102. Daily_Note/
│   └── 103. Excalidraw/
├── 200. CMDS/
│   ├── 201. Connect/
│   │   └── [현재학기]/
│   ├── 220. Merge/
│   │   ├── 221. Journaling/
│   │   ├── 222. FlashCard/
│   │   ├── 223. Concept/
│   │   │   ├── CS/
│   │   │   ├── Math/
│   │   │   └── [내 전공들]/
│   │   ├── 224. Problem/
│   │   │   ├── Math/
│   │   │   └── Coding/
│   │   └── 225. Feynman/
│   └── 280. Project/
├── 300. Thinking/
├── 400. Reference/
│   ├── 401. Anything/
│   ├── 410. Software/
│   ├── 420. Engineering/
│   ├── 450. Meeting/
│   │   └── [현재학기]/
│   └── 490. People/
└── 500. Setting/
    ├── 501. Template/
    ├── 502. Guide/
    └── 503. Properties/
```

### 2. 템플릿 파일 생성 (500. Setting/501. Template/에)
다음 템플릿들을 만들어줘:
- Daily_Template.md
- Weekly_Review_Template.md
- Lecture_Template.md
- Concept_Template.md
- Problem_Template.md
- Meeting_Template.md
- FlashCard_Template.md
- Feynman_Template.md
- Project_Template.md

### 3. Prefix 체계
파일명에 사용할 Prefix:
- D - : Daily Note
- N - : 일반 메모
- L - : 강의 노트
- C - : 개념 정리
- P - : 문제 풀이
- MTG - : 회의록
- Q - : 미해결 질문
- FC - : 플래시카드
- FYN - : 파인만 노트
- JRN - : 저널
- PRJ - : 프로젝트
- R - : 참고자료

### 4. 플래시카드 형식
Spaced Repetition 플러그인 호환:
```
질문
?
답변
```

### 5. 가이드 문서
500. Setting/502. Guide/에 CMDS 사용 가이드 문서 작성

각 템플릿에는 적절한 frontmatter(tags, created 등)와 섹션을 포함해줘.
```

---

## 템플릿만 생성하는 프롬프트

```
Obsidian용 학습 템플릿들을 만들어줘.

필요한 템플릿:
1. Daily_Template - 일일 기록 (할 일, 오늘의 학습, 메모)
2. Lecture_Template - 강의 노트 (과목, 주차, 핵심 내용, 질문)
3. Concept_Template - 개념 정리 (정의, 예시, 연관 개념)
4. Problem_Template - 문제 풀이 (문제, 접근법, 풀이, 회고)
5. FlashCard_Template - 암기 카드 (Spaced Repetition 호환, ? 구분자 사용)
6. Meeting_Template - 회의록 (일시, 참석자, 안건, 결정사항)
7. Weekly_Review_Template - 주간 회고 (이번 주 성과, 배운 것, 다음 주 계획)
8. Feynman_Template - 파인만 노트 (개념을 쉽게 설명하기)
9. Project_Template - 프로젝트 관리 (목표, 마일스톤, 진행상황)

Templater 플러그인 문법 사용:
- 날짜: <% tp.date.now("YYYY-MM-DD") %>
- 파일명: <% tp.file.title %>

각 템플릿에 적절한 frontmatter(tags, created, status 등) 포함해줘.
```

---

## 폴더 구조만 생성하는 프롬프트

```
Obsidian vault에 CMDS 폴더 구조를 만들어줘.

내 정보:
- 전공: [전공명]
- 현재 학기: [학기]

폴더 구조:
- 100. Inbox/ (임시 저장)
  - 101. Anything/, 102. Daily_Note/, 103. Excalidraw/
- 200. CMDS/ (학습 핵심)
  - 201. Connect/[학기]/ (과목별 강의노트)
  - 220. Merge/ (통합 지식)
    - 221. Journaling/, 222. FlashCard/, 223. Concept/, 224. Problem/, 225. Feynman/
  - 280. Project/
- 300. Thinking/ (미해결 질문)
- 400. Reference/ (참고자료)
  - 401. Anything/, 410. Software/, 420. Engineering/, 450. Meeting/, 490. People/
- 500. Setting/ (설정)
  - 501. Template/, 502. Guide/, 503. Properties/

223. Concept/ 하위에 내 전공 관련 폴더도 만들어줘.
```

---

## 특정 과목 설정 프롬프트

```
[과목명] 과목을 위한 Obsidian 설정을 해줘.

필요한 것:
1. 201. Connect/[학기]/[과목명]/ 폴더
2. 해당 과목용 플래시카드 파일: FC - [과목명] 기초.md
3. 개념 정리 시작 파일: C - [과목명] 개요.md

플래시카드 형식:
```
개념 질문
?
답변
```

처음 시작할 수 있도록 기본 틀만 만들어줘.
```

---

## 플러그인 설정 요청 프롬프트

```
Obsidian CMDS 시스템에 필요한 플러그인 설정을 알려줘.

필수 플러그인:
1. Templater - 템플릿 폴더를 500. Setting/501. Template/로 설정
2. Calendar - Daily Note 폴더를 100. Inbox/102. Daily_Note/로 설정
3. Spaced Repetition - 플래시카드 구분자를 ?로 설정
4. Dataview - 기본 설정

각 플러그인의:
- 핵심 설정 옵션
- 권장 설정값
- CMDS 시스템과 연동하는 방법

을 알려줘.
```

---

## 마이그레이션 프롬프트 (기존 vault가 있을 때)

```
기존 Obsidian vault를 CMDS 시스템으로 마이그레이션하고 싶어.

현재 내 vault 상황:
- [현재 폴더 구조 설명]
- [현재 사용 중인 템플릿/태그 설명]

CMDS 구조로 변환해줘:
1. 기존 파일들을 어디로 옮겨야 하는지
2. 파일명에 Prefix를 어떻게 붙일지
3. 새로 만들어야 할 폴더는 무엇인지
4. 기존 태그를 어떻게 정리할지

점진적으로 마이그레이션할 수 있도록 단계별로 알려줘.
```
