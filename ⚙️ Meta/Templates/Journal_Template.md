<%*
/**
 * Journal Template - 저널링/일기
 * 저장 경로: 📅 Daily/Journal/
 */
const ME = '[[김선음]]';
const d = tp.date.now("YYYY-MM-DD");
const dt = tp.date.now("YYYY-MM-DDTHH:mm:ss");
const weekday = tp.date.now("ddd");

const fileName = `JRN - ${d}`;
await tp.file.rename(fileName);
await tp.file.move(`📅 Daily/Journal/${fileName}`);
-%>
---
type: journal
title: "<% d %> 저널"
created: <% d %>
updated: <% dt %>
author: "<% ME %>"
mood: 
energy: 
tags:
  - journal
  - daily
---

# <% d %> (<% weekday %>) 저널

> [!tip] 오늘 하루를 되돌아보며 생각을 정리합니다.

---

## 🌅 오늘 하루 한 줄
> 

---

## 💭 오늘의 생각

### 좋았던 것
- 

### 아쉬웠던 것
- 

### 깨달은 것
- 

---

## 📚 오늘 배운 것

### 공부
- 

### 삶
- 

---

## ❓ 질문/고민

- 

---

## 🎯 내일 다짐

- 

---

## 📎 메모

