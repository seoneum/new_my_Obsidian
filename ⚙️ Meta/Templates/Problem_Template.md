---
migrated_from: CMDS/500. setting/501. Template/Problem_Template.md
updated: 2026-01-18T16:42:53
domain:
  - cs
cmds: connect
---
<%*
const ME = '[[김선음]]';
const d = tp.date.now("YYYY-MM-DD");
const dt = tp.date.now("YYYY-MM-DDTHH:mm:ss");

// 문제 타입 선택
const problemType = await tp.system.suggester(
  ["🔢 수학 문제", "💻 코딩 문제", "⚡ 공학 문제", "🏛️ 철학 문제"],
  ["math", "coding", "engineering", "philosophy"]
) || "math";

// 출처/플랫폼
let source = "";
let problemId = "";

if (problemType === "coding") {
  source = await tp.system.suggester(
    ["백준", "LeetCode", "프로그래머스", "기타"],
    ["baekjoon", "leetcode", "programmers", "other"]
  ) || "baekjoon";
  problemId = await tp.system.prompt("문제 번호:", "");
} else if (problemType === "math") {
  source = await tp.system.suggester(
    ["공업수학1", "일반수학2", "기출문제", "기타"],
    ["공업수학1", "일반수학2", "exam", "other"]
  ) || "other";
  problemId = await tp.system.prompt("챕터/문제번호:", "");
} else if (problemType === "engineering") {
  source = await tp.system.suggester(
    ["전자기학1", "기타"],
    ["전자기학1", "other"]
  ) || "other";
  problemId = await tp.system.prompt("문제 번호:", "");
} else {
  source = await tp.system.prompt("출처:", "");
  problemId = await tp.system.prompt("문제:", "");
}

// 난이도
const difficulty = await tp.system.suggester(
  ["🟢 Easy", "🟡 Medium", "🔴 Hard"],
  ["easy", "medium", "hard"]
) || "medium";

// 제목
const title = await tp.system.prompt("문제 제목:", problemId);

// 코딩 언어 (코딩 문제인 경우)
let codeLang = "";
if (problemType === "coding") {
  codeLang = await tp.system.suggester(
    ["C++", "Python", "둘 다"],
    ["cpp", "python", "both"]
  ) || "cpp";
}

// 태그
let tags = ["problem", `problem/${problemType}`, `difficulty/${difficulty}`];
if (source && source !== "other") tags.push(`source/${source}`);

// language 라인
let languageLine = codeLang ? `language: ${codeLang}` : "";

// 문제 섹션 결정
let problemSection = "";
if (problemType === "coding") {
  problemSection = `### 입력
\`\`\`

\`\`\`

### 출력
\`\`\`

\`\`\`

### 제한
- 시간: 
- 메모리: `;
} else if (problemType === "math" || problemType === "engineering") {
  problemSection = `### Given (주어진 것)
- 

### Find (구할 것)
- `;
} else {
  problemSection = `### 문제/논제
- `;
}

// 풀이 섹션 결정
let solutionSection = "";

if (problemType === "coding") {
  if (codeLang === "cpp" || codeLang === "both") {
    solutionSection += `### C++
\`\`\`cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    
    return 0;
}
\`\`\`
`;
  }
  if (codeLang === "python" || codeLang === "both") {
    solutionSection += `
### Python
\`\`\`python

\`\`\`
`;
  }
  solutionSection += `
### 복잡도
- 시간: O()
- 공간: O()`;
} else if (problemType === "math" || problemType === "engineering") {
  solutionSection = `### Step 1
$$

$$

### Step 2
$$

$$

### 답
$$
\\boxed{}
$$`;
} else {
  solutionSection = `### 논증
1. 
2. 
3. 

### 결론
- `;
}

// 파일명 및 이동
const fileName = `P - ${title}`;
await tp.file.rename(fileName);

const folder = problemType === "coding" 
  ? "CMDS/200. CMDS/220. Merge/224. Problem/Coding"
  : "CMDS/200. CMDS/220. Merge/224. Problem/Math";
await tp.file.move(`${folder}/${fileName}`);
-%>
---
type: problem
title: "<% title %>"
created: <% d %>
updated: <% dt %>
author:
  - "<% ME %>"
problem_type: <% problemType %>
source: <% source %>
difficulty: <% difficulty %>
<% languageLine %>
status:
  - "[[🚜In Progress]]"
tags:
<% tags.map(t => `  - ${t}`).join("\n") %>
solved: false
time_spent: 0
---

# <% title %>

> **<% problemType %>** | 난이도: **<% difficulty %>** | 출처: <% source %> <% problemId %>

---

## 📋 문제

<% problemSection %>

---

## 🧠 접근

### 첫 생각
- 

### 핵심 아이디어
- 

### 필요 개념
- [[ ]]

---

## ✏️ 풀이

<% solutionSection %>

---

## 🔍 복기

### 맞았으면
- 핵심:
- 더 좋은 방법:

### 틀렸으면
- 실수:
- 정답:

---

## 📝 FC

#flashcards/<% problemType %>

<% title %> 핵심:: 

