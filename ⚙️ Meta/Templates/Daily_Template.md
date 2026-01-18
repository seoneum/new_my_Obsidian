---
migrated_from: CMDS/500. setting/501. Template/Daily_Template.md
updated: 2026-01-18T16:42:53
cmds: connect
---
<%*
const ME = '[[김선음]]';
const d = tp.date.now("YYYY-MM-DD");
const dt = tp.date.now("YYYY-MM-DDTHH:mm:ss");
const weekday = tp.date.now("ddd");
const weekNum = tp.date.now("WW");

// 하루 타입
const dayKind = await tp.system.suggester(
  ["📚 공부", "🔧 프로젝트", "📚🔧 혼합", "🌴 휴식"],
  ["study", "project", "mixed", "off"]
) || "study";

const fileName = `D - ${d}`;
await tp.file.rename(fileName);
await tp.file.move(`CMDS/100. Inbox/102. 📝Daily_Note/${fileName}`);
-%>
---
type: daily
title: "<% d %>"
created: <% d %>
updated: <% dt %>
author: "<% ME %>"
day_kind: <% dayKind %>
week: W<% weekNum %>
tags:
  - daily
  - day/<% dayKind %>
---

# <% d %> (<% weekday %>)

## 🎯 Top 3
1. [ ] 
2. [ ] 
3. [ ] 

---
<%* if (dayKind === "study" || dayKind === "mixed") { -%>

## 📚 공부

| 시간 | 과목 | 내용 |
|-----|-----|-----|
| 오전 | | |
| 오후 | | |

### 오늘 배운 것
- 

### 모르는 것
- 
<%* } -%>
<%* if (dayKind === "project" || dayKind === "mixed") { -%>

## 🔧 프로젝트

### 작업
- [ ] 

### 진행
- 

### 막힌 것 → 내일
- 
<%* } -%>
<%* if (dayKind === "off") { -%>

## 🌴 휴식

- [ ] 하고 싶은 것:
- 한 것:
<%* } -%>

---

## 🌙 마무리

### 오늘 핵심 3줄
1. 
2. 
3. 

### 내일 우선
1. 
2. 

---

## 📎 메모


