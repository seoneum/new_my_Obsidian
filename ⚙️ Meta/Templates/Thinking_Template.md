---
migrated_from: CMDS/500. setting/501. Template/Thinking_Template.md
updated: 2026-01-18T16:42:53
domain:
  - phil
cmds: connect
---
<%*
const ME = '[[김선음]]';
const NOW_DATE = tp.date.now("YYYY-MM-DD");
const NOW_DT = tp.date.now("YYYY-MM-DDTHH:mm:ss");

const thinkingType = await tp.system.suggester(
  ["❓ 미해결 질문 (Question)", "💡 아이디어/가설 (Idea)", "🤔 고민/딜레마 (Dilemma)", "🔗 연결점 (Connection)"],
  ["question", "idea", "dilemma", "connection"]
);
if (!thinkingType) {
  new Notice("❌ Thinking 노트 생성이 취소되었습니다.");
  return;
}

const domain = await tp.system.suggester(
  ["🔧 Engineering", "🏛️ Philosophy", "🔧+🏛️ 교차점", "📐 Math", "💻 Software", "🤖 Robotics", "🌐 General"],
  ["EE", "Phil", "Cross", "Math", "SE", "Robotics", "General"]
);
if (!domain) {
  new Notice("❌ Thinking 노트 생성이 취소되었습니다.");
  return;
}

const title = (await tp.system.prompt("질문/아이디어 제목:", tp.file.title))?.trim() || tp.file.title;

const taggingMode = await tp.system.suggester(["기본 태그만", "지금 태그 추가"], ["later", "now"]);
let extraTags = [];
if (taggingMode === "now") {
  const raw = await tp.system.prompt("추가 tags(쉼표):", "");
  extraTags = (raw ?? "").split(",").map(s => s.trim().replace(/^#/, "")).filter(Boolean);
}

let tags = ["thinking", `thinking/${thinkingType}`, ...extraTags];
if (taggingMode === "later") tags.push("tagging/needed");

// 타입 라벨
let typeLabel = "";
if (thinkingType === "question") {
  typeLabel = "❓ 미해결 질문";
} else if (thinkingType === "idea") {
  typeLabel = "💡 아이디어/가설";
} else if (thinkingType === "dilemma") {
  typeLabel = "🤔 고민/딜레마";
} else {
  typeLabel = "🔗 연결점";
}

// 세부 섹션 결정
let detailSection = "";
if (thinkingType === "question") {
  detailSection = `---

## ❓ Question Details

### 질문이 생긴 맥락
- 어디서/언제 이 질문이 떠올랐나:
- 관련 노트: [[ ]]

### 왜 이게 중요한가?
- 

### 현재 내 가설/추측
- 

### 찾아봐야 할 것들
- [ ] 
- [ ] 

### 관련 개념/키워드
- `;
} else if (thinkingType === "idea") {
  detailSection = `---

## 💡 Idea Details

### 아이디어 요약
- 

### 이게 해결하는 문제
- 

### 예상되는 장점
- 

### 예상되는 한계/리스크
- 

### 검증 방법
- [ ] 
- [ ] 

### 관련 프로젝트/연구
- [[ ]]`;
} else if (thinkingType === "dilemma") {
  detailSection = `---

## 🤔 Dilemma Details

### 상황 설명
- 

### Option A
- 설명:
- 장점:
- 단점:

### Option B
- 설명:
- 장점:
- 단점:

### 핵심 고려사항
- 

### 현재 기울어지는 쪽
- 

### 결정을 위해 더 필요한 정보
- [ ] 
- [ ] `;
} else {
  detailSection = `---

## 🔗 Connection Details

### 연결되는 두 개념/분야
- A: 
- B: 

### 발견한 연결점
- 

### 이 연결이 의미하는 것
- 

### 더 탐구할 방향
- 

### 관련 노트
- [[ ]]
- [[ ]]`;
}

const fileName = `Q - ${title}`;
await tp.file.rename(fileName);
await tp.file.move(`💡 Notes/${fileName}`);
-%>
---
type: thinking
title: "<% title %>"
created: <% NOW_DATE %>
updated: <% NOW_DT %>
author:
  - "<% ME %>"
group: <% domain %>
status:
  - "[[🌱Seed]]"
thinking_type: <% thinkingType %>
tags:
<% tags.map(t => `  - ${t}`).join("\n") %>
aliases: []
resolved: false
---

# <% title %>

> [!abstract] 사유 유형
> **<% typeLabel %>** | 분야: **<% domain %>**

---

## 📝 핵심 질문/아이디어

> 한 문장으로 정리

<% detailSection %>

---

## 📚 참고 자료
- 

---

## 🔄 진행 상황

### <% NOW_DATE %>
- 최초 기록

### (날짜)
- 

---

## ✅ Resolution (해결되면 작성)

> 해결 여부: ⬜ 미해결 / ⬜ 해결됨 / ⬜ 보류

### 결론/답변
- 

### 이 과정에서 배운 것
- 

### 연결된 Merge 노트
- [[ ]]
