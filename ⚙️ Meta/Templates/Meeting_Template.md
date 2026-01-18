---
migrated_from: CMDS/500. setting/501. Template/Meeting_Template.md
updated: 2026-01-18T16:42:53
cmds: connect
---
<%*
const ME = '[[김선음]]';
const d = tp.date.now("YYYY-MM-DD");
const dt = tp.date.now("YYYY-MM-DDTHH:mm:ss");
const time = tp.date.now("HH:mm");

// 회의 종류
const meetingType = await tp.system.suggester(
  ["🏛️ 회장단", "🦿 Hexapod", "🚶 Bipedal", "📚 기타"],
  ["회장단", "Hexapod", "Bipedal", "other"]
);
if (!meetingType) {
  new Notice("❌ Meeting 노트 생성이 취소되었습니다.");
  return;
}

// 회차
const num = await tp.system.prompt("회차:", "1");

// 참석자
const attendees = await tp.system.prompt("참석자 (쉼표):", "");

// 태그
let tags = ["meeting", `meeting/${meetingType}`];

// 파일명 및 이동
const fileName = `MTG - ${d} ${meetingType} ${num}회`;
await tp.file.rename(fileName);

const folder = "🗃️ Archive/Meetings";
await tp.file.move(`${folder}/${fileName}`);
-%>
---
type: meeting
title: "<% meetingType %> <% num %>회"
created: <% d %>
updated: <% dt %>
author:
  - "<% ME %>"
meeting_type: <% meetingType %>
meeting_num: <% num %>
attendees: [<% attendees.split(",").map(a => `"${a.trim()}"`).join(", ") %>]
status:
  - "[[🍂Archive]]"
tags:
<% tags.map(t => `  - ${t}`).join("\n") %>
---

# <% meetingType %> <% num %>회 회의록

> 📅 **<% d %> <% time %>** | 참석: <% attendees %>

---

## 📋 안건

1. [ ] 
2. [ ] 
3. [ ] 

---

## 📝 내용

### 1. 
- 

### 2. 
- 

---

## ✅ Action Items

| 담당 | 할 일 | 마감 |
|-----|------|-----|
| | | |
| | | |

---

## 📅 다음 회의

- 일시: 
- 안건: 

---

## 🔗 관련

- 이전: [[ ]]
- 프로젝트: [[ ]]

