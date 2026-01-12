---
tags:
  - plugin
  - "#hotkey"
  - setting
  - Obsidian
link: "[[Plugins]]"
share_link: https://share.note.sx/x3szvyiu#f8ZgAjVYnlhpc5aKciE9IHh6hE2Hla99abDwFThNiKg
share_updated: 2025-12-17T18:10:58+09:00
---

1. Outliner :
     - 글머리 기호 편집을 자유롭게 함.
     - ctrl + A : 원래 전체 페이지지만 outliner적용하면 위계에 따라 선택. E.G.) 문장->문단->전체
2. various Complements
	- 사용한 용어 자동완성 기능 있음
3. Editing toolbar
	- markdown 익숙하지 않은 사람 도와주는거.
	- 지우개 모양은 양식 다 지워줌. 
4. Highlightr 
	- <mark style="background: #F2BED1;">하이라이터</mark> <mark style="background: #FDCEDF;">기능</mark>. <mark style="background: #71C9CE;">색깔은</mark> <mark style="background: #A6E3E9;">지정 가능함</mark>. <mark style="background: #BE9FE1;">드래그 후</mark> <mark style="background: #E1CCEC;">ctrl + p로 색 지정</mark>.
5. Translate
	- 는 api필요하니까 그냥 대충 다른 ai써서 번역 해오자~
6. Tag wrangler
	- tag들을 /로 파일처럼 쓰고 볼 수 있음. E.G.) \#어쩌구/저쩌구
	- tag이름 전체를 변경하고 싶을 때 오른쪽 바에 있는 tag에서 rename으로 바꾸면 전체가 한번에 바뀜
	- new search for~~ 하면 그 태그에 관련된 file/project찾아줌
	- 검색하고 ...에서 bookmark 설정해 놓으면 왼쪽 바 위에 북마크에 그 tag가 되어있는 것 나옴. 태그는 자유롭게 사용하자~~
7. Note Refactor
	- 노트를 분리하는 것.
	- 노트 안에서 분리할 글을 드래그 후 ctrl+p -> refactor:contents only 
	- refactor:first line as file name
	- refactor:split note by headings -> heading마다 노트 분리시킴
	- 하나의 노트에 한 주제만을 작성하고 연결하는 것이 좋음
8. Templater
	- create new note from template : Alt+n
	- open insert template : ctrl+t
	- replace template in the active file : ctrl+alt+t
	- < % 로 시작해서 %>로 끝남. 안에 \[tp.]해서 기능 명령어 집어넣음.
	- [[Template Syntax]]
9. Calendar, Periodic Note
	- 어떤 날, 어떤 노트를? 
	- 오른쪽 위의 바에 달력 클릭하고 그 날짜를 클릭하면 해당 날의 [[🏷 Daily Notes]] 생성됨. 
	- Periodic Note의 설정에서 생성 시 들어가는 파일, 기본 template 설정해주고 캘린더에서 [[🏷 Daily Notes]]생성 시 template적용됨.
10. Paste URL into selection
	- 원래 URL syntax : \[title](url) -> ctrl+k 
	- 이걸 쉽게 해줌. url을 복사 후 title로 쓸 문장을 드래그 후 그 위에 ctrl+v.  E.G.) [obsidian_tip_link](https://slashpage.com/cmds-class) 
11. Korean Book Info
	- 국내 도서 정리
	- \[\[Book title]]로 노트 만들어주고 그 노트에서 ctrl+p -> korea하면 됨
	- [[알고리즘으로 철학하기 코드 너머의 사유 기술과 존재를 잇다]]]
	- \[책커버|400] : 쓰고 url 붙여 넣으면 커버 사진 나옴. 크기는 뒤 숫자로
12. Book Search
	- 똑같음 위에 것이랑. 설정 template에 book search하고 ctrl+shift+b 후 검색하면 됨.
	- u
13. Obsidian Web Clipper
	1) 확장프로그램 -> Obsidian Web Clipper 다운
	2) general -> Vault만 내 볼트로 선택
	3) 인터프리터 활성화 -> 사용할 api추가
	4) 설정할 template -> import template -> properties세팅
	5) Note content : "\~~"안에 들어가는거 프롬프트임. 영어로 쓰는게 좋을듯? example보고 ㄱ
	   중괄호 두 개로 프롬프트 구분. heading같은 것 적용 가능
	   Interpreter context : 기본 프롬프트. api비용 높으니 무료일 경우만 사용. (gemini)
14. Data view
	- js못 써도 일단 켜놓기~
	- properties나 태그한 모든 것을 데이터 베이스화.
	- [[Dataview Test]] 테스트 노트고 밑에 문법 링크 첨부함.
	- sort도 됨.
15. Canvas
	- 파일 생성 경로만 option에서 선택해주는 것이 편함.
	- 그냥 열고 하고 싶은 대로 하면 됨.
	- 마크다운 적용 됨.
	- 노트를 드래그해서 넣는 것이 됨. 그룹 만들어서 안에 노트나 다른 것 넣으면 그룹화 돼서 같이 움직임.
	- 이미지 넣는 것도 됨.
	- 약간 내 노트들에서 dataview로 정리하고 그거 기반으로 에세이나 플젝할 때 정리하기 좋을듯?
	- [[Canvas_Test.canvas|Canvas_Test]]``
16. Excalidraw
	- 뭔가 그리는 것임
	- shift누르면 각도같은 것들이 고정된 상태로 사이즈, 방향 조절 가능.
	- api 연결하면 ai기능 쓸 수 있음.
	- [[Drawing 2025-12-17 15.29.34.excalidraw|Excalidraw_Test]]
17. Project
	- Bases로 재출시 예정
18. Kanban
	- ctrl+p -> kanban해서 새로 보드 만들기
	- 보드 만들고 기준에 따라 분류해서 바로바로 체크 가능. 어따 써야할지는 재미나이한테 물어봄. -> to do list만들고 체크박스 해서 과정이나 플젝 진행도 같은거 정리 가능.
	- 왼쪽 위에 각 kanban노트에 설정 가능.
	- [[Kanban_Test]]
19. Share Note
	- option에서 connect plug를 외부 인터넷 프로그램에서 열기.
	- ctrl+p을 눌러 기능 사용하기~
	- 링크도 같이 공유 되기 때문에 웹에서도 링크 누르면 타고 가짐.
20. omniserch
	- ctrl+shift+o : vault search
	- 키워드 검색하면 file, folder차원이 아닌 그냥 그 단어가 들어간 파일 몽땅 검색
	- 구글 검색과 동시에 그것에 관한 내 옵시디언 노트 검색 : option에서 enable http server ON하기 -> [onmisearch 홈페이지](https://publish.obsidian.md/omnisearch/How+to+use+Omnisearch)에서 Inject Omnisearch results into your search engine 파트의 tamoermonkey확장 프로그램 다운로드 -> 다시 ![[Pasted image 20251217193033.png|400]]에서 google선택 후 설치 -> 그럼 어디로 빨려들어가는데 들어가서 install누르면 댐. 그러면 구글에서 내 옵시디언 노트가 검색페이지 옆에 나옴.
21. Graph view
	- Filter에서 properties 등등을 이용해서 걸러서 볼 수 있음.
	- 그룹이라는 것을 만들 수 있는데 여러가지 정해서 그룹으로 묶고 색 나누면 됨.
	- ctrl+p로 현재 파일의 local graph만 볼 수 있음. depth로 몇다리 걸쳐서 볼 수 있는지 설정 가능. 
22. Graph Analisys
	- 설정 알고리즘에 따라 노드 들간의 가중치 정해짐. 
	- Adamic이랑 jaccard만 켜놓자
23. Strange New World
	- 노트가 몇번 참조되었는지 옆에 뜸.
	- [[CMDS Guide]]
24. Minimal Theme
	- Appearance -> theme -> minimal theme
	- community plugins -> minimal theme setting
25. Style Setting
	- 그냥 알아서 쓰셈. 영상 봐야 앎. 난 귀찮아서 걍 안 함.
	- 백업하고 다른 사람 스타일 가져 오는 것도 있는데 귀찮음. 나중에 ㄱㄱ
	- Part 2 chapter 7-2,3임 영상 ㄱㄱ
26. Supercharged Links
	- 정한 기준의 노트를 나열해줌. E.G) Tag, Note path등등
	- 정한 기준에 따라 색도 바꿀 수 있음. 
	- 이런 저런 색 변경 가능하니까 취향에 맞춰서 커스텀 하도록.
27. file tree alternative  -> 그냥 Make.md로 노션처럼 쓰는게 제일 라이트할듯.
	- 굳이 어렵게 이거저거 설정하지 말고 Make.md 플러그인 다운 받으면 노션처럼 쓰기 가능.
28. Workspace Plus
	- 현재 하는 작업의 디스플레이를 설정해 놓고 ctrl+u -> workspace저장.
	- 껐다가 키고 그 워크스페이스를 다시 선택하면 그 작업 디스플레이로 바뀜.
	- workspace 설정된 것을 불러오는 것을 따로 단축키 설정 가능함.
29. Spaced Repetition
	- 전공 공부를 위한 암기노트임.
	- [[Spaced repetition Test]] 예시. 
	- 내가 생각하는 사용법은 [notebookLM](https://notebooklm.google.com/)에서 교수님이 설명하신 것을 gemini에 넣고 그거 기반으로 spaced repetition문법으로 변형 시켜서 하는 것이 베스트라고 생각함.
	- 질문::답 형식이지만 답:::질문 형식으로 반대로 하는 것도 가능함.
	- \#flashcards/@@@로 태그로 문제 유형 나누기 가능띠
	- NotebookLM보다 성능이 뛰어날지는 모르겠음. => 선택사항인 plugin이라는거~
30. Smart Connection
	- 이거 어차피 유료밖에 안댐. 걍 보면 가중치에 따라 어떤 노트랑 가장 연결이 잘 되어있나 확인용임.
31. Smart Composer
	- AI와 함께하는 노트 작성~~ 얘가 도와줄거임
	- [[setting에서 smart composer의 Chat 시스템프롬프트]] 기본 제공 프롬프트.
32. Importer
	- 다른 노트 앱에서 노트를 가져오는 방법~ 그냥 다른 노트 앱 선택하고 경로 설정해서 가져오면 댐.
33. remotely save
	- 어려움. 아이패드랑 동기화 하고싶은 사람은 하시길. 나는 안 해도 될듯.
34. Make.md이거 좋은듯요?