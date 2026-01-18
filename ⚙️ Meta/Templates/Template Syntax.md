---
tag: Syntax
source_url: https://silentvoid13.github.io/Templater/introduction.html
migrated_from: CMDS/500. setting/502. CMDS setting/Template Syntax.md
updated: 2026-01-18T16:42:53
domain:
  - robotics
cmds: connect
---

<< [[<% tp.date.now("YYYY-MM-DD", -1) %>]] | [[<% tp.date.now("YYYY-MM-DD", 1) %>]] >>

# <% tp.file.title %>

<% tp.web.daily_quote() %>


## tp.file
#### tp.file.title
- 파일 제목 추출
	- <% tp.file.title %>
	- <% tp. file.title.slice(5) %>
	- <% tp. file.title.slice(0,5) %>
	- <% tp. file.title.slice(2,5) %>
- 공백 제거
	- <%* let name = tp.file.title; let nametag = name.replace(/ /g,""); -%> <% nametag %>
- 파일이름 변경
	- <% await tp.file.rename("MyNewName") %>
	- <% await tp.file.rename(tp.file.title + "2") %>
- 파일이동+파일이름 변경
	- <% await tp.file.move("/50. Inbox/" + tp.file.title) %>
- 문자추출
	- <%* const title = tp.file.title; const matches = title.match(/[a-zA-Z가-힣]+/g); const text = matches ? matches.join('') : ''; -%> <% text %> 
- 숫자추출
	- <%* const title = tp.file.title; const matches = title.match(/\d+/g); const number = matches ? matches.join('') : ''; -%> <% number %>
#### tp.file.tags
- 파일 태그(컴마로 연결)
	- <% tp.file.tags %>
#### tp.file.creation_date
- <% tp.file.creation_date() %> 
- <% tp.file.creation_date("YYYY-MM-DD HH:mm") %> 
- <% tp.file.creation_date("YYYY년 MM월 DD일 HH시 mm분") %> 
- <% tp.file.creation_date("YYYY년 MM월 DD일 H시 m분") %> 
- <% tp.file.creation_date("dddd Do MMMM YYYY HH:mm") %>
- [참고할 날짜 포멧](https://momentjs.com/docs/#/displaying/format/)
#### tp.file.folder
<% tp.file.folder() %>

#### tp.file.path
<% tp.file.path() %>

## tp.date
- 오늘 날짜 삽입
	- <% tp.date.now("YYYY-MM-DD") %>
- 주간 일일 링크 생성
	- 월요일 [[<% tp.date.weekday("YYYY-MM-DD", 0) %>]] 
	- 월요일 [[<% tp.date.weekday("YYYY-MM-DD", 1) %>]] 
	- 화요일 [[<% tp.date.weekday("YYYY-MM-DD", 2) %>]] 

## tp.system
- 드롭다운 메뉴 생성
	- <% tp.system.suggester(["옵션1선택", "옵션2선택", "옵션3선택"], ["옵션1결과", "옵션2결과", "옵션3결과"]) %>
	- //Philosophy, Engineering, Computer Science
- Tag 선택
	- <% tp.system.suggester(item => item, Object.keys(app.metadataCache.getTags()).map(x => x.replace("#", "")), true, "태그 선택") %>
## tp.web
- 랜덤 이미지
	- <% tp.web.random_picture("200x200", "landscape,water") %>
	- <% tp.web.random_picture("400", tp.file.title, "landscape") %>