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
---
### CMDS Guide v2 - Slashpage

- **CMDS Guide v2**
    
    - **Status**: 설계 단계
        
    - **Created by**: 커맨드스페이스
        
    - **Created at**: Jul 15, 2024 5:05 PM
        
    - **Links::** [[🏛 CMDS Head Quarter]] | [[🏛 CMDS Guide]]
        
- **🏛 CMDS Guide v2**
    
    - 📌 Version 2.0 - Properties 표준화 및 체계 개선판
        
    - Last Updated: 2025-09-15
        

#### 📊 Properties 표준화 규칙

- **필수 Properties (Required)**
    
    - 모든 노트는 다음 5개의 필수 properties를 포함해야 합니다:
        
        - `type`: # 노트 유형 (아래 표준 type 참조)
            
        - `aliases`: [ ] # 별칭 (배열 형식)
            
        - `author`: "[[구요한]]" # 작성자 (wikilink 형식)
            
        - `date created`: # 생성일 (YYYY-MM-DD)
            
        - `tags`: [ ] # 태그 (배열 형식)
            
- **표준 Properties 정의**
    
    - **📅 날짜 관련**
        
        - `date created` - 생성일 (YYYY-MM-DD)
            
        - `date modified` - 수정일 (YYYY-MM-DD)
            
        - `date` - 이벤트/미팅 날짜 (YYYY-MM-DD)
            
        - `publish_date` - 발행일 (YYYY-MM-DD)
            
        - `year` - 연도 (YYYY)
            
        - ⚠️ 통일 규칙: 모든 날짜는 ISO 8601 형식 (YYYY-MM-DD) 사용
            
    - **👤 작성자 및 관계**
        
        - `author`: [[구요한]] - 항상 wikilink 형식 사용
            
        - `attendees`: [ ] - 참석자 목록 (wikilink 배열)
            
        - `organization`: [[조직명]] - 조직 (wikilink)
            
    - **📌 분류 및 상태**
        
        - `type` - 노트 유형 (아래 표준 type 목록 참조)
            
        - `CMDS` - CMDS 카테고리 연결 (예: [[📚 620 Generative AI]])
            
        - `index` - 인덱스 참조 (예: [[🏷 Meeting Notes]])
            
        - `status` - 상태값
            
            - ✅ 표준값: `unread` | `reading` | `inProgress` | `completed` | `archived`
                
    - **📊 평가 및 측정**
        
        - `myRate` - 평점 (1-5 scale, 숫자)
            
        - `totalPage` - 총 페이지 수 (camelCase)
            
        - `views` - 조회수
            
    - **🔗 연결 및 참조**
        
        - `aliases`: [ ] - 별칭 (배열 형식으로 통일)
            
        - `tags`: [ ] - 태그 (배열 형식으로 통일)
            
        - `links` - 관련 링크
            
        - `source` - 출처
            
        - `source_url` - 출처 URL
            
        - `bookends` - 북엔드 (기존 유지)
            
        - `MOC` - Map of Content 참조
            

#### 표준 Type 목록

- **주요 노트 타입**
    
    - `note` - 일반 노트
        
    - `terminology` - 용어 정의
        
    - `meeting` - 회의록
        
    - `people` - 인물 정보
        
    - `curriculum` - 강의 커리큘럼
        
    - `memo` - 메모
        
    - `class` - 수업 관련
        
    - `manuscript` - 원고/초안
        
    - `daily-note` - 일일 노트
        
    - `article` - 글/기사
        
    - `sermon` - 설교
        
    - `review` - 리뷰/연구평론
        
    - `project` - 프로젝트
        
    - `zettel` - 제텔카스텐 노트
        
- **구조/조직 타입**
    
    - `moc` - Map of Content
        
    - `CMDS` - 커맨드스페이스 인덱스
        
    - `organization` - 조직/기관
        
    - `portal` - 포털 페이지
        
    - `documentation` - 문서화/가이드
        
    - `index` - 색인
        
- **콘텐츠 타입**
    
    - `books` - 도서
        
    - `research-review` - 연구 리뷰
        
    - `idea` - 아이디어
        
    - `resource` - 리소스
        
    - `product` - 제품/서비스
        

#### Collections

- **CMDS**
    
    - `[[🏛 CMDS Head Quarter]]`
        
- **Index**
    
    - `#index #NoteClass #maps`
        
    - `[[🏷 Guideline]]`
        
    - `[[🏷 Daily Notes]]`
        
    - `[[🏷 Research Notes]]`
        
    - `[[🏷 Project Notes]]`
        
    - `[[🏷 Lecture Notes]]`
        
    - `[[🏷 Review Notes]]`
        
    - `[[🏷 Draft Article]]`
        
    - `[[🏷 Web Clips]]`
        
    - `[[🏷 Waypoint]]`
        
    - `[[🏷 Meeting Notes]]`
        
    - `[[🏷 People]]`
        
    - `[[🏷 Organization]]`
        
    - `[[🏷 Prompts]] #GenAI #ChatGPT #SystemPrompt`
        
    - `[[🏷 Syntax and Codes]] #R #Python #SPSS #Mplus`
        
    - `[[🏷 Recordings]]`
        

#### Tags

- 태그는 자유롭게 `#태그는자유로워야지`
    
- Nested tags 예시:
    
    - `#Author/Koo`
        
    - `#가이드/태그작성법`
        
    - `#가이드/목차작성법`
        

#### Backlinks

- 백링크는 내 인지범위가 허락하는 선까지 `[[]]`
    
- 한 번에 다 할 필요는 없음
    
- ChatGPT에게 자동 연결 시킬 수 있음
    

#### CMDS Levels (계층 구조)

- `🏛` - Home, Guide (최상위)
    
- `📖` - 1st level CMDS (100-900 시리즈)
    
    - Space Collection
        
    - 1 digit (100-900)
        
- `📚` - 2nd level CMDS (N01-N99)
    
    - Spaces
        
    - 2 digit (N01-N99)
        
- `(No Icon)` - 3rd level CMDS
    
    - 상세 주제는 3rd level CMDS로 분류
        
- **CMDS Level Example**
    
    - `📚 840 Lectures`
        
        - `├── 840.01 University Courses`
            
            - `│ ├── 840.01-A 차의과학대학교`
                
                - `│ │ ├── 840.01-A1 2024-1`
                    
                    - `│ │ │ └── [[생성형 AI 기초와 활용]]`
                        
                - `│ │ └── 840.01-A2 2024-2`
                    
                    - `│ │ └── AI 융합 연구방법론`
                        
            - `│ └── 840.01-B 한양대학교`
                

#### Filename Conventions

- **접두사(Prefix)**
    
    - Wis' Rule
        
        - `u.` - usecase `#example`
            
        - `f.` - feature `#operation`
            
        - `p.` - product `#service`
            
    - Input
        
        - `📎` - Web Clips (W@)
            
        - `🌿` - Readwise (WW@)
            
        - `📘` - Books, Reference `#📚Book`
            
    - Process
        
        - `🏷` - Index (E@)
            
        - `📦` - Review (EE@)
            
        - `📐` - Variables (EEEE@)
            
    - Output
        
        - `🔖` - Output from YHN's Idea (R@)
            
        - `📜` - Output from Other's Idea (RR@)
            
        - `📈` - Code and Syntax (RRR@)
            
        - `🎹` - Music (RRRR@)
            
        - `🏙` - Canvas (F@)
            
    - References
        
        - `📕` - Bible (EEE@)
            
- **접미사(Suffix)**
    
    - Service에 따라
        
        - `.obsidian`
            
        - `.python`
            
        - `.chatgpt`
            
        - `.claude`
            
        - `.midjourney`
            
    - Purpose에 따라
        
        - `.meeting`
            
        - `.portal`
            

#### Folder Structure

- `00. Inbox/`
    
    - `├── 01. Daily Notes/`
        
    - `├── 02. Weekly Notes/`
        
    - `├── 03. Claude Code/ # 코드 작업 전용`
        
    - `├── 04. Excalidraw/`
        
    - `├── 05. Canvas/`
        
    - `├── 06. GenAI Chats/`
        
    - `└── 07. Clippings/`
        
- `10. CMDS Process/`
    
    - `├── 11. Connect # 배우고있는것들 #capture`
        
    - `├── 12. Merge # 내주제와연결 #Areas #organize`
        
    - `├── 13. Develop # #distill`
        
    - `└── 14. Share # 완성된산출물 #express`
        
- `20. Literature Notes/`
    
- `30. Permanent Notes/`
    
- `50. Assets/`
    
- `60. Preferences/`
    
- `70. Collections/ # Resources`
    
    - `├── 71. People/`
        
    - `├── 74. Meetings/`
        
    - `├── 75. Spirituality/`
        
    - `├── 76. Curriculum/`
        
    - `└── 78. Bases/`
        
- `80. References/`
    
    - `├── 81. Attachment/`
        
    - `├── 82. Academic Sources/`
        
    - `├── 83. Web Articles/`
        
    - `└── 84. Omnivore/`
        
- `90. Settings/`
    
    - `├── 91. Templates/`
        
    - `└── 94. System Prompts/`
        

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

- **v2.0 (2025-01-09): Properties 표준화 및 체계 개선**
    
    - 날짜 형식 ISO 8601 통일
        
    - `author` 필드 wikilink 형식 통일
        
    - `status` 표준값 정의
        
    - `myRate`로 평점 통일
        
    - `totalPage`로 camelCase 통일
        
    - `tags`/`aliases` 배열 형식 통일
        
    - `bookends` 유지
        
- **v1.0 (2024-02-25): 초기 버전**
    
- **주요 개선사항 (v2.0)**
    
    - ✅ 표준화 완료
        
        1. 날짜 형식: 모든 날짜 필드 ISO 8601 (`YYYY-MM-DD`) 형식 통일
            
        2. 작성자 표기: `author` 필드에 항상 `[[구요한]]` wikilink 형식 사용
            
        3. 상태값: `status`는 5개 표준값만 사용 (`unread`/`reading`/`inProgress`/`completed`/`archived`)
            
        4. 평점: `myRate`로 통일 (1-5 scale)
            
        5. 페이지: `totalPage`로 camelCase 통일
            
        6. 태그/별칭: `tags`와 `aliases` 배열 형식 통일
            
        7. 북엔드: `bookends` 기존 유지
            
    - 🚫 제거/통합
        
        - Nested properties 사용 안 함 (단순 구조 유지)
            
        - 중복 필드 제거 (`tag`→`tags`, `my_rate`→`myRate`, `total_page`→`totalPage`)
            
    - 📋 필수 Properties
        
        - 모든 노트는 최소한 다음 5개 필드 포함:
            
            - `type`
                
            - `aliases`
                
            - `author`
                
            - `date created`
                
            - `tags`
                
- 이 가이드는 CMDSPACE 볼트의 표준 Properties 체계를 정의합니다.
    
- 모든 새로운 노트는 이 규칙을 따라 작성되어야 합니다.
    
- Made with Slashpage