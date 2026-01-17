<%*
// FC Evening Template - 당일 공부 내용 플래시카드 (10PM)
const d = tp.date.now("YYYY-MM-DD");
const dt = tp.date.now("YYYY-MM-DDTHH:mm:ss");
const ME = '[[김선음]]';

const fileName = `FC - ${d} (Evening)`;
await tp.file.rename(fileName);
await tp.file.move(`CMDS/200. CMDS/220. Merge/222. FlashCard/${fileName}`);
-%>
---
type: flashcards
title: <% fileName %>
created: <% d %>
updated: <% dt %>
author: <% ME %>
group: General
status: "[[🚜In Progress]]"
tags:
  - flashcards
  - daily
  - evening-review
aliases: []
review_date: <% d %>
---

# <% fileName %>

> [!tip] 오늘(<% d %>) 공부한 내용 꼼꼼히 정리
> 하루를 마무리하며 오늘 배운 것을 플래시카드로 정리합니다.

## 오늘 생성/수정된 노트

```dataviewjs
const today = "<% d %>";
const toYMD = (v) => {
  if (!v) return null;
  if (typeof v === 'string') return v.slice(0,10);
  if (v && typeof v.toFormat === 'function') return v.toFormat('yyyy-MM-dd');
  return null;
};
const notes = dv.pages()
  .where(p => toYMD(p.created) === today || toYMD(p.updated)?.slice(0,10) === today)
  .where(p => !p.file.path.includes("FlashCard"))
  .sort(p => p.group, 'asc');

if (notes.length === 0) {
  dv.paragraph("ℹ️ 오늘 생성/수정된 노트가 없습니다.");
} else {
  dv.paragraph(`📚 **${notes.length}개** 노트 발견`);
  dv.table(["노트", "분야", "타입"], 
    notes.map(p => [p.file.link, p.group || "General", p.type || "-"])
  );
}
```

---

## 🎯 오늘의 핵심 개념 (3-5개)

#flashcards/daily

핵심개념1?
?
한 줄 정의

핵심개념2?
?
한 줄 정의

핵심개념3?
?
한 줄 정의

---

## 📖 철학 - 개념과 논증

#flashcards/philosophy

### 개념 정의

용어?
?
정의 (누가 말했는지 포함)

### 논증 구조

논증명?
?
전제1 + 전제2 → 결론

### 반론/한계

이론의 한계?
?
비판점

---

## 🔢 수학 - 공식과 증명

#flashcards/math

### 정리/공식

정리명?
?
$LaTeX 수식$
<!--SR:!2026-01-22,4,270-->

### 증명 단계

증명?
?
Step 1 → Step 2 → Step 3

### 적용 예시

언제 사용?
?
조건과 상황

---

## 💻 코딩 - 알고리즘과 패턴

#flashcards/coding

### 알고리즘

알고리즘명?
?
시간 O(?), 공간 O(?)

### 핵심 로직

함수명()?
?
입력 → 처리 → 출력

### 트릭/팁

최적화 포인트?
?
왜 이렇게?

---

## 🔧 공학/로보틱스

#flashcards/engineering

### 원리

물리원리?
?
수식과 설명

### 제어/설계

제어기법?
?
언제/왜 사용?

---

## ❓ 아직 모르는 것 (내일 복습)

- [ ] 
- [ ] 

---

## 📊 오늘 학습 통계

- 새 노트 수:
- 플래시카드 수:
- 가장 어려웠던 것:
- 내일 우선순위:

