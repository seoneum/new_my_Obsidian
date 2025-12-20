<%* // 1. 도메인 설정 const domains =; const domainVals =; const domain = await tp.system.suggester(domains, domainVals, true, "1. 분야를 선택하세요");

// 2. 출처 설정 const sources =; const sourceVals = ["school", "mooc"]; const source = await tp.system.suggester(sources, sourceVals, true, "2. 출처를 선택하세요");

// 3. 상태 설정 const statuses = ["🚜 수강 중 (Processing)", "🌲 정리 완료 (Permanent)"]; const statusVals = ["🚜", "🌲"]; const status = await tp.system.suggester(statuses, statusVals, true, "3. 현재 상태는?");

// 4. 인덱스 입력 const index = await tp.system.prompt("4. 과목명 또는 강의명을 입력하세요 (Index)");

## // 5. 태그 자동 생성 로직 let myTags =; if (source === "school") myTags.push("exam_prep"); if (source === "mooc") myTags.push("skill_up"); if (status === "🚜") myTags.push("processing"); %>

## type: lecture domain: <% domain %> source_type: <% source %> status: <% status %> index: "[[<% index %>]]" tags: <%* myTags.forEach(t => { %> - <% t %> <%* }) %> date created: <% tp.file.creation_date("YYYY-MM-DD") %>

# <% domain === "SE"? "💻" : "🦉" %> [<% tp.file.cursor(1) %>] <% tp.file.title %>

## 📌 메타데이터

- **챕터/주차:**
    
- **선수 지식:** [[ ]]
    

## 🔑 핵심 키워드

1. 2.

<%* if (domain == "SE") { %>

## 📝 이론 (Theory)

> 해결하려는 문제(Why)와 핵심 원리(How)는 무엇인가?

## 💻 코드 및 구현 (Implementation)python

# Code snippet here

```
```

## ⚠️ 트러블슈팅

| 에러 메시지 | 원인 | 해결 |
|:---|:---|:---|
| | | |
<%* } else { %>
## 📜 텍스트 분석 (Context)
> 텍스트의 배경과 핵심 질문은 무엇인가?

## 🗺️ 논증 지도 (Argument Map)
1. **P1 (전제):** 
2. **P2 (전제):** 
3. **C (결론):** 

## ⚔️ 비판 (Critique)
- **반론:**
- **나의 생각:**
<%* } %>

## 🔗 연결
- **관련 노트:** [[ ]]