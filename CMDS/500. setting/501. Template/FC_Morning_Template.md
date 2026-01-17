<%*
// FC Morning Template - 전날 노트 기반 플래시카드 (8AM)
const d = tp.date.now("YYYY-MM-DD");
const yday = tp.date.now("YYYY-MM-DD", -1);
const dt = tp.date.now("YYYY-MM-DDTHH:mm:ss");
const ME = '[[김선음]]';

const fileName = `FC - ${d} (Morning)`;
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
  - morning-review
aliases: []
review_date: <% yday %>
---

# <% fileName %>

> [!tip] 전날(<% yday %>) 공부한 내용 복습
> 아래는 전날 생성된 노트에서 플래시카드를 작성하기 위한 템플릿입니다.

## 전날 생성된 노트

```dataviewjs
const yday = "<% yday %>";
const toYMD = (v) => {
  if (!v) return null;
  if (typeof v === 'string') return v.slice(0,10);
  if (v && typeof v.toFormat === 'function') return v.toFormat('yyyy-MM-dd');
  return null;
};
const notes = dv.pages()
  .where(p => toYMD(p.created) === yday)
  .where(p => !p.file.path.includes("FlashCard"))
  .sort(p => p.group, 'asc');

if (notes.length === 0) {
  dv.paragraph("ℹ️ 전날 생성된 노트가 없습니다.");
} else {
  dv.paragraph(`📚 **${notes.length}개** 노트 발견`);
  dv.table(["노트", "분야", "타입"], 
    notes.map(p => [p.file.link, p.group || "General", p.type || "-"])
  );
}
```

---

## 📖 철학 (개념 정의)

#flashcards/philosophy

개념?
?
정의

논증?
?
구조와 결론

---

## 🔢 수학 (공식/알고리즘)

#flashcards/math

공식명?
?
$수식$
<!--SR:!2026-01-22,4,270-->

증명 단계?
?
1. → 2. → 3.

---

## 💻 코딩 (알고리즘/개념)

#flashcards/coding

알고리즘?
?
시간복잡도 O(?)

함수/메서드?
?
역할과 반환값

---

## 🔧 공학 (원리/설계)

#flashcards/engineering

원리?
?
설명

설계 패턴?
?
언제/왜 사용?

---

## 📝 일반

#flashcards/general

Q?
?
A

