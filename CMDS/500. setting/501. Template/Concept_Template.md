<%*
const ME = '[[김선음]]';
const d = tp.date.now("YYYY-MM-DD");
const dt = tp.date.now("YYYY-MM-DDTHH:mm:ss");

// 분야
const domain = await tp.system.suggester(
  ["💻 CS (C++/Python)", "🔢 Math", "⚡ EE", "🏛️ Phil", "🤖 Robotics"],
  ["CS", "Math", "EE", "Phil", "Robotics"]
) || "CS";

// CS 세부
let subDomain = "";
if (domain === "CS") {
  subDomain = await tp.system.suggester(
    ["C++", "Python", "알고리즘", "자료구조", "기타"],
    ["cpp", "python", "algorithm", "ds", "other"]
  ) || "cpp";
}

// 수학 세부
if (domain === "Math") {
  subDomain = await tp.system.suggester(
    ["공업수학1", "일반수학2", "선형대수", "미적분", "기타"],
    ["공업수학", "일반수학", "linear", "calculus", "other"]
  ) || "other";
}

// 철학 세부
if (domain === "Phil") {
  subDomain = await tp.system.suggester(
    ["언어철학", "존재론과형이상학", "서양현대철학사", "기타"],
    ["언어철학", "존재론", "현대철학", "other"]
  ) || "other";
}

// EE 세부
if (domain === "EE") {
  subDomain = await tp.system.suggester(
    ["전자기학1", "회로", "기타"],
    ["전자기학", "circuit", "other"]
  ) || "other";
}

// 제목
const title = await tp.system.prompt("개념 이름:", tp.file.title);

// 난이도
const level = await tp.system.suggester(
  ["🟢 기초", "🟡 중급", "🔴 심화"],
  ["basic", "mid", "adv"]
) || "mid";

// 태그
let tags = ["concept", `concept/${domain.toLowerCase()}`];
if (subDomain && subDomain !== "other") tags.push(`topic/${subDomain}`);
tags.push(`level/${level}`);

// 파일명 및 이동
const fileName = `C - ${title}`;
await tp.file.rename(fileName);
await tp.file.move(`CMDS/200. CMDS/220. Merge/223. Concept/${domain}/${fileName}`);
-%>
---
type: concept
title: "<%= title %>"
created: <% d %>
updated: <% dt %>
author:
  - "<% ME %>"
domain: <% domain %>
<% if (subDomain && subDomain !== "other") { -%>
topic: <% subDomain %>
<% } -%>
level: <% level %>
CMDS: Merge
status:
  - "[[🌿Sapling]]"
tags:
<% tags.map(t => `  - ${t}`).join("\n") %>
confidence: 0
---

# <% title %>

> **한 줄 요약**: 

---

## 📖 정의

<% if (domain === "CS") { -%>
```cpp
// 기본 형태

```
<% } else if (domain === "Math" || domain === "EE") { -%>
$$

$$
<% } else { -%>
> 
<% } -%>

---

## 💡 직관적 이해

- 이건 마치 _______ 같다
- 왜냐하면 _______

---

## 📐 핵심

<% if (domain === "CS") { -%>
### 문법
```cpp

```

### 예시
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    
    return 0;
}
```

### 주의
- 
<% } else if (domain === "Math") { -%>
### 공식
$$

$$

### 증명 (간략)
1. 
2. 

### 언제 사용?
- 
<% } else if (domain === "EE") { -%>
### 원리
- 

### 수식
$$

$$

### 적용
- 
<% } else if (domain === "Phil") { -%>
### 핵심 논증
1. 전제: 
2. 전제: 
3. 결론: 

### 주요 철학자
- 

### 비판
- 
<% } else { -%>
### 핵심 포인트
1. 
2. 
3. 
<% } -%>

---

## 📝 예시

### 예시 1
- 

### 예시 2
- 

---

## ⚠️ 흔한 실수

- ❌ 
- ✅ 

---

## 🔗 연결

- 선행: [[ ]]
- 후행: [[ ]]
- 관련: [[ ]]

---

## 📚 출처

- 강의: [[ ]]
- 교재: 

---

## 📝 FC

#flashcards/<% domain.toLowerCase() %>

<% title %> 정의:: 

<% title %> 예시:: 

<% title %> 주의점:: 

