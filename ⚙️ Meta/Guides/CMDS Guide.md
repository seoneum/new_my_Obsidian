---
tags:
  - Syntax
  - Obsidian
  - Guideline
  - CMDS
  - setting
created: <% tp.file.creation_date() %>
author:
  - "[[김선음]]"
  - "[[구요한]]"
migrated_from: CMDS/500. setting/502. CMDS setting/CMDS Guide.md
updated: 2026-01-18T16:42:53
cmds: connect
---
### CMDS Guide v3 - 김선음 맞춤형

- **CMDS Guide v3**
    
    - **Status**: 운영 중
        
    - **Created by**: 커맨드스페이스
        
    - **Updated by**: 김선음 (2026-01)
        
    - **Links::** [[🏛 CMDS Head Quarter]] | [[🏛 CMDS Guide]]
        
- **🏛 CMDS Guide v3**
    
    - 📌 Version 3.0 - 대학생 맞춤형 개선
        
    - Last Updated: 2026-01-18
        

---

## 📌 김선음 맞춤형 Prefix 체계

| Prefix | 용도 | 예시 |
|--------|------|------|
| `D -` | Daily | `D - 2026-01-18` |
| `N -` | 메모 | `N - 아이디어` |
| `L -` | 강의/수업 | `L - 공업수학1 3주차` |
| `C -` | 개념 정리 | `C - 포인터와 참조` |
| `P -` | 문제 풀이 | `P - 백준 1234` |
| `R -` | Reference | `R - PID 논문` |
| `W -` | Web clip | `W - C++ 튜토리얼` |
| `DEV -` | 치트시트 | `DEV - STL 정리` |
| `PRJ -` | 프로젝트 | `PRJ - Hexapod` |
| `MTG -` | 회의록 | `MTG - 2026-01-18 회장단 3회` |
| `Q -` | 미해결 질문 | `Q - 왜 에러가?` |
| `PPL -` | 인물 | `PPL - 칸트` |
| `FC -` | 플래시카드 | `FC - 2026-01-18 (Evening)` |

---

## 📁 폴더 구조 (김선음)

```
CMDS/
├── 100. Inbox/
│   ├── 101. Daily/          # 일일노트
│   └── 102. Zettle/         # 빠른 메모
│
├── 200. CMDS/
│   ├── 201. Connect/        # 배우는 것들
│   │   └── 26-1/            # 26-1학기 수업 노트
│   │       ├── 26-1-Phil-언어철학/
│   │       ├── 26-1-Phil-존재론과형이상학/
│   │       ├── 26-1-Phil-서양현대철학사/
│   │       ├── 26-1-Math-공업수학1/
│   │       ├── 26-1-Math-일반수학2/
│   │       └── 26-1-EE-전자기학1/
│   │
│   ├── 220. Merge/          # 내 주제와 연결
│   │   ├── 223. Concept/    # 개념 정리
│   │   │   ├── Math/
│   │   │   ├── CS/
│   │   │   ├── EE/
│   │   │   ├── Phil/
│   │   │   └── Robotics/
│   │   └── 224. Problem/    # 문제 풀이
│   │       ├── Math/
│   │       └── Coding/
│   │
│   ├── 230. Develop/        # 치트시트, 정리본
│   └── 240. Share/          # 완성된 산출물
│
├── 300. Thinking/           # 미해결 질문, 아이디어
│
├── 400. Reference/
│   ├── 410. Web/            # 웹 클리핑
│   ├── 420. Papers/         # 논문
│   ├── 430. Books/          # 도서
│   ├── 440. Project/        # 프로젝트
│   └── 450. Meeting/        # 회의록
│       └── 26-1/
│           ├── 회장단/
│           ├── Hexapod/
│           └── Bipedal/
│
└── 500. setting/
    ├── 501. Template/
    └── 502. CMDS setting/
```

---

## 📋 템플릿 목록

### 일상
| 템플릿 | 용도 | Prefix |
|--------|------|--------|
| Daily_Template | 하루 계획/마무리 | `D -` |
| Master Template | 새 노트 생성 메뉴 | - |

### 학습
| 템플릿 | 용도 | Prefix |
|--------|------|--------|
| Lecture_Template | 수업 노트 | `L -` |
| Concept_Template | 개념 정리 | `C -` |
| Problem_Template | 문제 풀이 | `P -` |

### 정리
| 템플릿 | 용도 | Prefix |
|--------|------|--------|
| Reference_Template | 논문/책 참고 | `R -` |
| WebClip_Template | 웹 저장 | `W -` |
| Develop_Template | 치트시트 | `DEV -` |

### 협업
| 템플릿 | 용도 | Prefix |
|--------|------|--------|
| Project_Template | 프로젝트 | `PRJ -` |
| Meeting_Template | 회의록 | `MTG -` |

### 기타
| 템플릿 | 용도 | Prefix |
|--------|------|--------|
| Thinking_Template | 미해결 질문 | `Q -` |
| People_Template | 인물 노트 | `PPL -` |

### 복습
| 템플릿 | 용도 | Prefix |
|--------|------|--------|
| FC_Morning_Template | 아침 복습 | `FC -` |
| FC_Evening_Template | 저녁 복습 | `FC -` |
| Weekly_Review_Template | 주간 복습 | - |

---

## 📚 26-1학기 과목 정보

| 분야 | 과목명 | 폴더 |
|------|--------|------|
| Philosophy | 언어철학 | `26-1-Phil-언어철학/` |
| Philosophy | 존재론과형이상학 | `26-1-Phil-존재론과형이상학/` |
| Philosophy | 서양현대철학사 | `26-1-Phil-서양현대철학사/` |
| Math | 공업수학1 | `26-1-Math-공업수학1/` |
| Math | 일반수학2 | `26-1-Math-일반수학2/` |
| EE | 전자기학1 | `26-1-EE-전자기학1/` |

---

## 🔧 프로젝트 & 회의

### 진행 중 프로젝트
- **Hexapod**: 6족보행로봇
- **Bipedal**: 2족보행로봇

### 회의 종류
- **회장단**: 회장단 정기 회의
- **Hexapod**: 프로젝트 회의
- **Bipedal**: 프로젝트 회의

---

## 💻 코딩 언어

- **C++**: 주요 프로젝트, 시스템 프로그래밍
- **Python**: 데이터 처리, 스크립트, AI/ML

문제 풀이 시 `Problem_Template`에서 언어 선택 가능.

---

## 📊 개념 분류 체계

### Concept 분야
| 분야 | 세부 주제 |
|------|----------|
| **Math** | 미적분, 선형대수, 미분방정식, 복소해석 |
| **CS** | 자료구조, 알고리즘, OS, 네트워크 |
| **EE** | 회로이론, 전자기학, 신호처리 |
| **Phil** | 언어철학, 형이상학, 현대철학, 논리학 |
| **Robotics** | 제어이론, 기구학, 동역학, SLAM |

### Problem 분야
| 유형 | 설명 |
|------|------|
| **Math** | 수학 문제 (공업수학, 일반수학 등) |
| **Coding** | 코딩 문제 (백준, LeetCode 등) |

---
            

---

## 📊 Properties 표준화 규칙 (기존 유지)

#### 필수 Properties (Required)
모든 노트는 다음 5개의 필수 properties를 포함:
- `type`: 노트 유형
- `aliases`: [ ] 별칭 (배열)
- `author`: "[[김선음]]" 작성자 (wikilink)
- `date created`: 생성일 (YYYY-MM-DD)
- `tags`: [ ] 태그 (배열)

#### 날짜 형식
- 모든 날짜: ISO 8601 형식 (`YYYY-MM-DD`)
- `created`, `updated` 필드 사용

#### 상태값 (status)
- `unread` | `reading` | `inProgress` | `completed` | `archived`

---

## 📌 표준 Type 목록

### 김선음 추가 Type
| Type | 용도 |
|------|------|
| `daily-note` | 일일 노트 |
| `lecture` | 수업 노트 |
| `concept` | 개념 정리 |
| `problem` | 문제 풀이 |
| `meeting` | 회의록 |
| `project` | 프로젝트 |
| `thinking` | 미해결 질문 |
| `flashcard` | 플래시카드 |
| `webclip` | 웹 클리핑 |
| `reference` | 참고 자료 |
| `develop` | 치트시트/정리본 |

### 기존 Type (유지)
- `note` - 일반 노트
- `terminology` - 용어 정의
- `people` - 인물 정보
- `memo` - 메모
- `article` - 글/기사
- `review` - 리뷰
- `zettel` - 제텔카스텐

---

#### Properties Template Examples

- **기본 노트 템플릿**
    
    - `type: note`
        
    - `aliases: []`
        
    - `author: - "[[구요한]]"`
        
    - `date created: 2025-01-09`
        
    - `date modified: 2025-01-09`
        
    - `tags: []`
        
    - `CMDS:`
        
    - `index:`
        
    - `status:`
        
- **회의록 템플릿**
    
    - `type: meeting`
        
    - `aliases: []`
        
    - `author: - "[[구요한]]"`
        
    - `date created: 2025-01-09`
        
    - `date: 2025-01-09`
        
    - `attendees: - "[[참석자1]]" - "[[참석자2]]"`
        
    - `organization: "[[조직명]]"`
        
    - `CMDS: "[[📚 831 Consulting]]"`
        
    - `index: "[[🏷 Meeting Notes]]"`
        
    - `status: inProgress`
        
    - `tags: [meeting]`
        
- **연구 노트 템플릿**
    
    - `type: research-review`
        
    - `aliases: []`
        
    - `author: - "[[구요한]]"`
        
    - `date created: 2025-01-09`
        
    - `title:`
        
    - `source:`
        
    - `source_url:`
        
    - `doi:`
        
    - `keywords: []`
        
    - `CMDS: "[[📚 820 Research]]"`
        
    - `index: "[[🏷 Research Notes]]"`
        
    - `status: reading`
        
    - `tags: [research]`
        
- **도서 노트 템플릿**
    
    - `type: books`
        
    - `aliases: []`
        
    - `author: - "[[구요한]]"`
        
    - `date created: 2025-01-09`
        
    - `title:`
        
    - `subtitle:`
        
    - `isbn:`
        
    - `publisher:`
        
    - `publish_date:`
        
    - `totalPage:`
        
    - `myRate:`
        
    - `status: unread`
        
    - `CMDS: "[[📚 240 Books]]"`
        
    - `index: "[[🏷 Books]]"`
        
    - `tags: [📚Book]`
        
- **인물 노트 템플릿**
    
    - `type: people`
        
    - `aliases: []`
        
    - `author: - "[[구요한]]"`
        
    - `date created: 2025-01-09`
        
    - `email:`
        
    - `mobile:`
        
    - `organization: "[[조직명]]"`
        
    - `group:`
        
    - `CMDS:`
        
    - `index: "[[🏷 People]]"`
        
    - `status:`
        
    - `tags: [people]`
        

#### Note-taking Guidelines

- **Citation Style**
    
    - 책 인용: `[!TIP] Knowledge Management for the Future`
        
    - 책의 내용 원본`^[Koo, Y. (2021). Knowledge Management for the Future. New York: Oxford University Press. p.25.]`
        
    - 논문 인용: `[!ABSTRACT] Knowledge Management in Organizations`
        
    - 조직 내 지식 관리의 중요성`^[Kim, S., & Lee, H. (2023). The impact of knowledge management. Journal of Knowledge Management, 27(4), 1012-1035.]`
        
    - 명언: `[!QUOTE]`
        
    - "2주 뒤에 뵙겠습니다." — 구요한(Yohan Koo)
        

#### Sync Settings

- **Obsidian Sync**
    
    - `.obsidian` - macOS, Windows, Android
        
    - `.obsidian_mobile` - iOS, iPadOS
        

#### Version History

- **v3.0 (2026-01-18): 김선음 맞춤형 개선**
    
    - 대학생 맞춤 Prefix 체계 추가
        
    - 26-1학기 폴더 구조 추가
        
    - 새 템플릿 추가 (Problem, Meeting, Concept)
        
    - Daily_Template 간소화
        
    - Master Template 새 메뉴 구조
        

- **v2.0 (2025-01-09): Properties 표준화 및 체계 개선**
    
    - 날짜 형식 ISO 8601 통일
        
    - `author` 필드 wikilink 형식 통일
        
    - `status` 표준값 정의
        

- **v1.0 (2024-02-25): 초기 버전**

---

Made with CMDS & Claude