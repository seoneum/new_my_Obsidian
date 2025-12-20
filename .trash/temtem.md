<%*// 1. 도메인 선택 (Software vs Philosophy)const domains =;const domainSetup = {"💻 Software Engineering": { code: "SE", icon: "💻", tags: "tech" },"🦉 Philosophy": { code: "Phil", icon: "🦉", tags: "humanities" }};const selectedDomain = await tp.system.suggester(domains, domains, true, "1. 공부할 분야를 선택하세요.");const domainConfig = domainSetup;// 2. 출처 선택 (School vs Online)const sources =;const sourceValues = ["school", "mooc"];const selectedSource = await tp.system.suggester(sources, sourceValues, true, "2. 강의 출처는 어디인가요?");// 3. 인덱스(과목명) 입력const courseName = await tp.system.prompt("3. 과목명이나 강의 시리즈 제목을 입력하세요 (Index용)");// 4. 상태 선택
const statuses = ["🚜 수업 듣는 중 (Processing)", "🌲 복습 완료 (Permanent)"];
const statusMap = { "🚜 수업 듣는 중 (Processing)": "🚜", "🌲 복습 완료 (Permanent)": "🌲" };
const selectedStatus = await tp.system.suggester(statuses, Object.values(statusMap), true, "4. 현재 상태는?");
%>type: lecturedomain: <% domainConfig.code %>source_type: <% selectedSource %>status: <% selectedStatus %>index: "[[<% courseName %>]]"tags:#<% selectedSource %>#processingdate created: <% tp.file.creation_date("YYYY-MM-DD") %><% domainConfig.icon %> [<% tp.file.cursor(1) %>] <% tp.file.title %>📌 메타데이터강의/챕터:선수 지식: [[ ]]🔑 핵심 키워드 (Keywords)<%* if (domainConfig.code == "SE") { %>📝 이론 및 개념 (Theory)이 기술이 해결하려는 문제는 무엇인가?💻 구현 및 코드 (Implementation)핵심 로직이나 명령어를 기록하세요.python여기에 코드를 입력하세요
## ⚠️ 트러블슈팅 & 에러 로그

| 에러 메시지 | 원인 | 해결 방법 |
|:---|:---|:---|
| | | |
<%* } else { %>
## 📜 텍스트 분석 (Text Analysis)
> 텍스트의 핵심 주장은 무엇인가?

## 🗺️ 논증 재구성 (Argument Map)
1. **전제 1 (P1):** 
2. **전제 2 (P2):** 
3. **결론 (C):** 

## ⚔️ 비판 및 반론 (Critique)
- **예상되는 반박:**
- **나의 재반박:**
<%* } %>

## 🔗 연결 (Connect)
- **관련 노트:** [[ ]]
- **CMDS 연결:** [[ ]]
<%*// 1. 자료 유형 선택const types =;const typeVals = ["book", "paper"];const subType = await tp.system.suggester(types, typeVals, true, "자료의 유형을 선택하세요.");// 2. 상태 선택const statusOptions = subType == "book"?:;const statusTags = subType == "book"? ["#buying_list", "#reading", "#archived"]: ["#to_summarize", "#analyzing", "#reference"];const selectedStatusIdx = await tp.system.suggester(statusOptions, , true, "현재 진행 상태는?");
const currentStatusTag = statusTags;
%>type: referencesubtype: <% subType %>index: "]"status: <% subType == "book"? "📚" : "📄" %>tags:<% currentStatusTag %>date created: <% tp.file.creation_date("YYYY-MM-DD") %>author:<% subType == "book"? "📖" : "📄" %> <% tp.file.title %><%* if (subType == "book") { %>📊 독서 개요읽는 목적:3줄 요약:1.2.3.📑 챕터별 메모 (Notes)Chapter 1.(인용문)💭 내 생각:<%* } else { %>📌 초록 (Abstract)논문의 핵심 내용을 요약합니다.🔬 연구 문제 & 방법론 (Methodology)Problem:Solution:💡 결과 및 기여 (Contribution)<%* } %>💎 CMDS 발전 (To Develop)이 자료에서 건져낸, 내 지식으로 발전시킬 아이디어.[[ ]]2.3 🚀 스마트 CMDS 노트 (Connect/Merge/Develop)기능: 지식 발전 단계(CMD)를 선택하여 그에 맞는 사고 도구를 불러옵니다. Index를 강제로 입력받아 고립된 노트가 되는 것을 방지합니다.<%*// 1. CMDS 단계 선택const steps =;const stepVals = ["connect", "merge", "develop"];const selectedStep = await tp.system.suggester(steps, stepVals, true, "CMDS 단계를 선택하세요.");// 2. 연결될 주제(Index) 선택 - 기존 폴더나 MOC를 염두에 둠
const topic = await tp.system.prompt("이 노트가 속할 상위 주제(Index/MOC)는 무엇인가요?");
%>type: <% selectedStep %>index: "[[<% topic %>]]"status: <% selectedStep == "develop"? "🌲" : "🌿" %>tags:#<% selectedStep %>date created: <% tp.file.creation_date("YYYY-MM-DD") %><% selectedStep == "connect"? "🔗" : (selectedStep == "merge"? "🗺️" : "🌲") %> <% tp.file.cursor(1) %><%* if (selectedStep == "connect") { %>🌉 연결의 맥락 (Context)**[[A]]**와 **]**는 어떤 관계인가요? (유사성, 인과관계, 대조)Link A: [[ ]]Link B: [[ ]]Insight:<%* } else if (selectedStep == "merge") { %>🎯 주제 정의 (Definition)이 MOC(Map of Content)가 다루는 영역을 정의합니다.🗂️ 지식의 구조 (Structure)1. 기초 개념[[ ]]2. 주요 논의[[ ]]<%* } else { %>🗣️ 핵심 주장 (Thesis)완전한 문장으로 나의 주장을 서술하세요.🛡️ 논거 및 증명 (Arguments)주장을 뒷받침하는 근거, 코드, 예시를 나열하세요.🚀 활용 (Action)[ ] 블로그 포스팅: [[ ]]<%* } %>2.4 📅 스마트 데일리 노트 (Daily Note)기능: 하루의 Index(집중 영역)를 설정하고, Tag(할 일 상태)를 필터링하여 보여줍니다.<%*
// 오늘의 기분이나 에너지 체크 (선택사항)
const energy = ["⚡️ High", "🙂 Normal", "🔋 Low"];
const curEnergy = await tp.system.suggester(energy, energy, false, "오늘의 에너지 레벨은?");
%>type: daily
tags: [#log/daily]
status: 🌿
energy: <% curEnergy %>
week: <% tp.date.now("gggg-ww") %>
date created: <% tp.file.creation_date("YYYY-MM-DD") %>📅 <% tp.date.now("YYYY-MM-DD (ddd)") %>🎯 오늘의 Index (Focus Area)오늘 가장 집중할 '공간'은 어디입니까?[ ] SE Focus: [[ ]][ ] Phil Focus: [[ ]]📥 태그 기반 할 일 (Action by Tags)#todo 태그가 달린 노트 중 처리가 필요한 것들dataviewTASKFROM #todoWHERE!completed AND file.day <= this.file.day
## 📝 퀵 로그 (Interstitials)
- <% tp.file.cursor(1) %>

## 🔄 회고 (Review)
- **Keep:**
- **Try:**
3. 요약: 템플릿 사용 가이드이 시스템은 사용자가 고민할 시간을 획기적으로 줄여줍니다.단축키 설정: Templater: Insert template 명령어를 단축키(예: Alt+N)로 지정하세요.선택의 순간: 템플릿을 실행하면 **"이 지식은 어디(Index)에 사는가?"**와 **"이 지식은 어떤 상태(Tag)인가?"**를 묻는 팝업이 뜹니다.결과: 사용자의 선택에 따라, 소프트웨어 공학 노트는 코드를 품고, 철학 노트는 논리를 품은 맞춤형 문서가 즉시 생성됩니다.
