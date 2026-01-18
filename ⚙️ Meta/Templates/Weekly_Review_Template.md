---
migrated_from: CMDS/500. setting/501. Template/Weekly_Review_Template.md
updated: 2026-01-18T16:42:53
domain:
  - phil
cmds: connect
---
<%*
const ME = '[[김선음]]';
const d = tp.date.now("YYYY-MM-DD");
const dt = tp.date.now("YYYY-MM-DDTHH:mm:ss");
const weekNum = tp.date.now("WW");
const year = tp.date.now("YYYY");

// 이번 주 시작일(월요일)과 종료일(일요일)
const weekStart = tp.date.now("YYYY-MM-DD", -6); // 대략적인 시작
const weekEnd = d;

const fileName = `FC - ${year}-W${weekNum} (Weekly)`;
await tp.file.rename(fileName);
await tp.file.move(`💡 Notes/Flashcards/${fileName}`);
-%>
---
type: weekly-review
title: "<% fileName %>"
created: <% d %>
updated: <% dt %>
author:
  - "<% ME %>"
group: General
status:
  - "[[🚜In Progress]]"
tags:
  - weekly
  - review
  - flashcards
aliases: []
week: W<% weekNum %>
year: <% year %>
---

# 📅 <% year %>-W<% weekNum %> 주간 복습

> [!tip] 일요일 저녁 루틴
> 이번 주에 생성된 모든 노트를 복습하고 핵심 플래시카드를 정리합니다.

---

## 📊 이번 주 통계

```dataviewjs
const weekNum = "<% weekNum %>";
const year = "<% year %>";

// 이번 주 노트 찾기 (week 속성 또는 created 날짜 기준)
const weekNotes = dv.pages()
  .where(p => p.week === `W${weekNum}` || 
    (p.created && p.created.toString().slice(0,4) === year))
  .where(p => !p.file.path.includes("Template"))
  .where(p => !p.file.path.includes("FlashCard"));

const byType = {};
weekNotes.forEach(p => {
  const t = p.type || "unknown";
  byType[t] = (byType[t] || 0) + 1;
});

dv.paragraph(`📝 이번 주 총 노트: **${weekNotes.length}개**`);
dv.paragraph(`📚 타입별: ${Object.entries(byType).map(([k,v]) => `${k}(${v})`).join(", ")}`);
```

---

## 📚 이번 주 생성된 노트

```dataviewjs
const today = dv.date("<% d %>");
const weekAgo = dv.date("<% weekStart %>");

const notes = dv.pages()
  .where(p => p.created >= weekAgo && p.created <= today)
  .where(p => !p.file.path.includes("Template"))
  .where(p => !p.file.path.includes("setting"))
  .sort(p => p.created, 'desc');

if (notes.length === 0) {
  dv.paragraph("ℹ️ 이번 주 생성된 노트가 없습니다.");
} else {
  dv.table(["날짜", "노트", "분야", "타입"], 
    notes.map(p => [
      p.created ? p.created.toString().slice(0,10) : "-",
      p.file.link, 
      p.group || "General", 
      p.type || "-"
    ])
  );
}
```

---

## 🎯 주간 핵심 요약

### 🔧 공학 (Engineering) - 이번 주 배운 것
1. 
2. 
3. 

### 🏛️ 철학 (Philosophy) - 이번 주 읽고 생각한 것
1. 
2. 
3. 

### 🔧 프로젝트 진행 상황
- 프로젝트명:
- 이번 주 진행:
- 다음 주 목표:

---

## 📝 주간 통합 플래시카드

> 이번 주 Daily FC에서 중요한 것들을 여기에 모읍니다.

#flashcards/weekly

### 🔧 공학
Q:: A

### 🏛️ 철학
개념:: 정의

### 🔢 수학
공식:: $수식$

### 💻 코딩
함수/개념:: 설명

---

## 🔍 이번 주 미해결 질문

> [[300. Thinking]]으로 옮길 것들

- [ ] 
- [ ] 
- [ ] 

---

## 📊 주간 자기 평가

### 목표 달성도
- 공부: ⬜⬜⬜⬜⬜ (1-5)
- 프로젝트: ⬜⬜⬜⬜⬜ (1-5)
- 루틴 준수: ⬜⬜⬜⬜⬜ (1-5)

### 이번 주 가장 큰 성과
- 

### 이번 주 아쉬운 점
- 

### 다음 주 집중할 것
1. 
2. 
3. 

---

## 🔗 관련 노트
- 이번 주 Daily 노트들
- 이번 주 Feynman 노트들
- 이번 주 FC (Morning/Evening) 노트들
