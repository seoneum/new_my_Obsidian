<%*
/**
 * Daily Template - 일일 노트 + 저널링/Feynman 자동 링크
 */
const ME = '[[김선음]]';
const d = tp.date.now("YYYY-MM-DD");
const dt = tp.date.now("YYYY-MM-DDTHH:mm:ss");
const weekday = tp.date.now("ddd");
const weekNum = tp.date.now("WW");

// 하루 타입
const dayKind = await tp.system.suggester(
  ["📚 공부", "🔧 프로젝트", "📚🔧 혼합", "🌴 휴식"],
  ["study", "project", "mixed", "off"]
);

if (!dayKind) {
  new Notice("❌ Daily 노트 생성이 취소되었습니다.");
  return;
}

// 저널링 노트 자동 생성 여부
const createJournal = await tp.system.suggester(
  ["✅ 저널링 노트도 생성", "❌ Daily만 생성"],
  [true, false]
) ?? false;

// 오늘 Feynman 학습 주제
const createFeynman = await tp.system.suggester(
  ["✅ 오늘 Feynman 노트 생성", "❌ 나중에"],
  [true, false]
) ?? false;

let feynmanLink = "";
let journalLink = "";
let feynmanTopic = "";

// 저널링 노트 링크 - 📅 Daily/Journal 폴더에 생성
if (createJournal) {
  const journalFile = `JRN - ${d}`;
  journalLink = `[[${journalFile}]]`;
}

// Feynman 노트 링크 - 💡 Notes/Feynman 폴더에 생성
if (createFeynman) {
  feynmanTopic = await tp.system.prompt("오늘 Feynman 주제:", "");
  if (feynmanTopic) {
    const feynmanFile = `FYN - ${d} ${feynmanTopic}`;
    feynmanLink = `[[${feynmanFile}]]`;
  }
}

const fileName = `D - ${d}`;
await tp.file.rename(fileName);
await tp.file.move(`📅 Daily/${fileName}`);
-%>
---
type: daily
title: "<% d %>"
created: <% d %>
updated: <% dt %>
author: "<% ME %>"
day_kind: <% dayKind %>
week: W<% weekNum %>
journal: "<% journalLink %>"
feynman: "<% feynmanLink %>"
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
<%* if (journalLink || feynmanLink) { -%>

## 🔗 오늘의 연결 노트

<%* if (journalLink) { -%>
- 📝 **저널링**: <% journalLink %> → *하루를 마무리하며 생각 정리*
  - 경로: `📅 Daily/Journal/JRN - <% d %>.md`
<%* } -%>
<%* if (feynmanLink) { -%>
- 🧠 **Feynman**: <% feynmanLink %> → *오늘 배운 개념을 내 말로 설명*
  - 경로: `💡 Notes/Feynman/FYN - <% d %> <% feynmanTopic %>.md`
<%* } -%>

---
<%* } -%>
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

