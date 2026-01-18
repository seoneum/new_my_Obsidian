<%*
const ME = '[[김선음]]';
const NOW_DATE = tp.date.now("YYYY-MM-DD");
const NOW_DT = tp.date.now("YYYY-MM-DDTHH:mm:ss");

const group = await tp.system.suggester(
  ["EE (전기전자)", "Phil (철학)", "SE (소프트웨어)", "Math (수학)", "Robotics (로보틱스)", "SLAM", "AI", "General"],
  ["EE", "Phil", "SE", "Math", "Robotics", "SLAM", "AI", "General"]
) || "General";

const title = (await tp.system.prompt("학습 주제 (개념/원리/문제):", tp.file.title))?.trim() || tp.file.title;

const difficulty = await tp.system.suggester(
  ["🟢 Easy (기초)", "🟡 Medium (중급)", "🔴 Hard (심화)"],
  ["easy", "medium", "hard"]
) || "medium";

const taggingMode = await tp.system.suggester(["기본 태그만(나중에 태깅)", "지금 추가 태그 입력"], ["later","now"]);
let extraTags = [];
if (taggingMode === "now") {
  const raw = await tp.system.prompt("추가 tags(쉼표):", "");
  extraTags = (raw ?? "").split(",").map(s=>s.trim().replace(/^#/, "")).filter(Boolean);
}

let tags = ["merge", "feynman", "zettel", `difficulty/${difficulty}`, ...extraTags];
if (taggingMode === "later") tags.push("tagging/needed");

const fynTitle = `M - ${title}`;
try { await tp.file.rename(fynTitle); } catch(e) {}
try { await tp.file.move(`CMDS/200. CMDS/220. Merge/${fynTitle}`); } catch(e) {}
-%>
---
type: merge
title: "<% title %>"
created: <% NOW_DATE %>
updated: <% NOW_DT %>
author:
  - "<% ME %>"
CMDS: Merge
status:
  - "[[🌿Sapling]]"
group: <% group %>
difficulty: <% difficulty %>
tags:
<% tags.map(t=> `  - ${t}`).join("\n") %>
aliases: []
time_spent: 0
confidence: 0
last_review: <% NOW_DATE %>
---

# <% title %>

> [!abstract] 학습 목표
> 이 개념을 12살에게 설명할 수 있을 때까지 반복한다.

---

## 🎯 Step 1: Explain (설명하기)

> **12살에게 설명하듯이** 비유와 쉬운 단어로 6~10문장 작성

### 핵심 아이디어 (한 문장)
- 

### 쉬운 비유
- 이것은 마치 _______ 와 같다. 왜냐하면 _______

### 상세 설명 (6-10문장)
1. 
2. 
3. 
4. 
5. 
6. 

---

## 🔍 Step 2: Identify Gaps (갭 찾기)

> 설명하다가 **막히거나 불확실한 부분**을 솔직하게 기록

### 체크리스트
- [ ] 용어 정의가 명확한가?
- [ ] "왜?"에 답할 수 있는가?
- [ ] 구체적인 예시가 있는가?
- [ ] 반례/한계를 알고 있는가?

### 모르는 것들
| 갭 | 왜 모르지? | 어디서 찾지? |
|-----|------------|--------------|
| | | |
| | | |

### 착각하고 있던 것 (Misconceptions)
- 

---

## 🔧 Step 3: Repair (다시 공부하기)

> 갭을 메우기 위해 **원본 자료로 돌아가서** 다시 학습

### 참고 자료
- 원본 링크: [[ ]]
- 추가 자료: [[ ]]
- 영상/강의:

### 새로 알게 된 것
1. 
2. 
3. 

### 학습 시간 기록
- 시작: `<% tp.date.now("HH:mm") %>`
- 종료:
- 총 소요:

---

## 📢 Step 4: Teach-back (다시 설명하기)

> Step 1보다 **더 짧고 명확하게** 압축

### 6문장 버전
1. 
2. 
3. 
4. 
5. 
6. 

### 3문장 버전
1. 
2. 
3. 

### 1문장 버전 (엘리베이터 피치)
> 

---

## 📊 Self-Assessment (자가 평가)

### 이해도 점수 (1-5)
- [ ] 1: 전혀 모름
- [ ] 2: 대충 알지만 설명 못함
- [ ] 3: 기본은 설명 가능
- [ ] 4: 깊이 있게 설명 가능
- [ ] 5: 다른 사람 가르칠 수 있음

### 다음 복습
- 언제: 
- 무엇을:

---

## 💡 Examples & Exercises

### 예제 1
- 문제:
- 풀이:

### 예제 2
- 문제:
- 풀이:

### 연습 문제 (스스로 풀어보기)
- 

---

## 🔗 Cross-links

### 관련 개념
- 선행 지식: [[ ]]
- 후행 지식: [[ ]]
- 유사 개념: [[ ]]

### 프로젝트 연결
- [[ ]]

---

## 📝 Flashcards

#flashcards/<% group.toLowerCase() %>

<% title %> 정의:: 

<% title %> 예시:: 

<% title %> vs _____:: 차이점

왜 <% title %>이 중요한가?:: 

