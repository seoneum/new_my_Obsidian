<%*
/**
 * CPZ Universal Template - 통합 노트 생성
 * CMDS + PARA + Zettelkasten
 */

const ME = '[[김선음]]';
const NOW = tp.date.now("YYYY-MM-DD");
const NOW_DT = tp.date.now("YYYY-MM-DDTHH:mm:ss");
const ID = tp.date.now("YYYYMMDDHHmm");

const noteType = await tp.system.suggester(
  [
    "━━━ 📅 일상 ━━━",
    "📅 Daily",
    "📝 Quick Memo",
    "━━━ 📚 학습 ━━━",
    "📖 Lecture",
    "💡 Concept (Zettel)",
    "📐 Problem",
    "━━━ 📁 자료 ━━━",
    "📄 Reference",
    "🌐 Web Clip",
    "━━━ 🎯 행동 ━━━",
    "🎯 Project",
    "📋 Meeting",
    "━━━ 💭 사유 ━━━",
    "❓ Question",
    "💡 Idea",
  ],
  [null, "daily", "quick", null, "lecture", "concept", "problem", null, "reference", "webclip", null, "project", "meeting", null, "question", "idea"]
);

if (!noteType) { tR += ""; return; }

async function pickDomain() {
  return await tp.system.suggester(
    ["💻 CS", "⚡ EE", "🏛️ Phil", "🔢 Math", "🤖 Robotics", "🌐 General"],
    ["cs", "ee", "phil", "math", "robotics", "general"]
  ) || "general";
}

let title = tp.file.title;
let folder = "📥 Inbox/_quick";
let fm = {
  id: ID,
  title: "",
  created: NOW,
  updated: NOW_DT,
  type: noteType,
  status: "seed",
  domain: [],
  tags: [],
};
let body = "";

if (noteType === "daily") {
  title = `D - ${NOW}`;
  folder = "📅 Daily";
  const weekday = ["일","월","화","수","목","금","토"][new Date().getDay()];
  
  fm.type = "daily";
  fm.status = "sapling";
  fm.author = ME;
  fm.tags = ["daily"];
  
  body = `
# ${NOW} (${weekday})

## 🎯 Top 3
1. [ ] 
2. [ ] 
3. [ ] 

---

## 📚 Today

### 오전
- 

### 오후
- 

---

## 🌙 Evening

### 오늘 핵심 3줄
1. 
2. 
3. 

### 내일 우선
1. 
2. 

---

## 📎 메모

`;

} else if (noteType === "quick") {
  title = await tp.system.prompt("제목:", "N - ");
  if (!title.startsWith("N - ")) title = `N - ${title}`;
  
  fm.tags = ["inbox", "tagging/needed"];
  
  body = `
# ${title.replace("N - ", "")}

## Notes
- 

## Next
- [ ] 
`;

} else if (noteType === "lecture") {
  const course = await tp.system.suggester(
    ["🏛️ 언어철학", "🏛️ 존재론과형이상학", "🏛️ 서양현대철학사", "🔢 공업수학1", "🔢 일반수학2", "⚡ 전자기학1", "📚 기타"],
    ["언어철학", "존재론과형이상학", "서양현대철학사", "공업수학1", "일반수학2", "전자기학1", "other"]
  ) || "other";
  
  let courseName = course;
  if (course === "other") {
    courseName = await tp.system.prompt("과목명:", "");
  }
  
  const week = await tp.system.prompt("주차:", "");
  title = `L - ${courseName} ${week}주차`;
  folder = `📚 Lectures/${courseName}`;
  
  fm.type = "lecture";
  fm.status = "sapling";
  fm.course = courseName;
  fm.week = week;
  fm.domain = [course.includes("철학") ? "phil" : course.includes("수학") ? "math" : "ee"];
  fm.tags = ["lecture", `course/${courseName}`];
  
  body = `
# ${courseName} - ${week}주차

## 📋 Outline
- 

## 📝 Notes

### 핵심 1
- 

### 핵심 2
- 

---

## ❓ Questions
- [ ] 

## 🔗 Related
- [[ ]]

## 📝 FC
#flashcards/${fm.domain[0]}

핵심 개념:: 
`;

} else if (noteType === "concept") {
  title = await tp.system.prompt("개념명:", "C - ");
  if (!title.startsWith("C - ")) title = `C - ${title}`;
  const conceptName = title.replace("C - ", "");
  
  const domain = await pickDomain();
  folder = "💡 Notes";
  
  fm.type = "concept";
  fm.status = "sapling";
  fm.author = ME;
  fm.domain = [domain];
  fm.confidence = 0;
  fm.tags = ["concept", `domain/${domain}`];
  
  body = `
# ${conceptName}

> **한 줄 정의**: 

---

## 📖 Definition

> 

---

## 💡 Intuition

이건 마치 _______ 같다. 왜냐하면 _______

---

## 📐 Core

### 핵심 포인트
1. 
2. 
3. 

### 예시
- 

---

## ⚠️ Common Mistakes
- ❌ 
- ✅ 

---

## 🔗 Links

- 선행: [[ ]]
- 후행: [[ ]]
- 관련: [[ ]]

---

## 📝 FC
#flashcards/${domain}

${conceptName} 정의:: 

${conceptName} 예시:: 
`;

} else if (noteType === "problem") {
  const problemType = await tp.system.suggester(
    ["💻 코딩", "🔢 수학", "⚡ 공학"],
    ["coding", "math", "engineering"]
  ) || "coding";
  
  title = await tp.system.prompt("문제:", "P - ");
  if (!title.startsWith("P - ")) title = `P - ${title}`;
  
  folder = "💡 Notes";
  
  fm.type = "problem";
  fm.status = "seed";
  fm.author = ME;
  fm.problem_type = problemType;
  fm.solved = false;
  fm.tags = ["problem", `problem/${problemType}`];
  
  let solutionTemplate = "";
  if (problemType === "coding") {
    solutionTemplate = `
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
  } else {
    solutionTemplate = `
$$

$$
`;
  }
  
  body = `
# ${title.replace("P - ", "")}

> **Type**: ${problemType} | **Solved**: ❌

---

## 📋 Problem


---

## 🧠 Approach

### 첫 생각
- 

### 핵심 아이디어
- 

---

## ✏️ Solution
${solutionTemplate}

---

## 🔍 Review

### 배운 것
- 

### 더 좋은 방법
- 
`;

} else if (noteType === "reference") {
  title = await tp.system.prompt("자료명:", "R - ");
  if (!title.startsWith("R - ")) title = `R - ${title}`;
  
  const domain = await pickDomain();
  folder = "📖 Books";
  
  fm.type = "reference";
  fm.status = "seed";
  fm.domain = [domain];
  fm.source_url = "";
  fm.tags = ["reference", `domain/${domain}`];
  
  body = `
# ${title.replace("R - ", "")}

## 📋 Metadata
- URL: 
- Author: 
- Date: 

---

## 📝 Summary


---

## 💡 Key Points
1. 
2. 
3. 

---

## 📎 Quotes
> 

---

## 🔗 Related
- [[ ]]

## Next
- [ ] Concept으로 발전시키기
`;

} else if (noteType === "webclip") {
  title = await tp.system.prompt("제목:", "W - ");
  if (!title.startsWith("W - ")) title = `W - ${title}`;
  
  folder = "📥 Inbox/_webclip";
  
  fm.type = "webclip";
  fm.status = "seed";
  fm.source_url = await tp.system.prompt("URL:", "");
  fm.tags = ["webclip", "tagging/needed"];
  
  body = `
# ${title.replace("W - ", "")}

## Source
- URL: ${fm.source_url}

---

## 📝 Content


---

## 💡 Why Clipped
- 

## Next
- [ ] 필요시 Reference로 이동
`;

} else if (noteType === "project") {
  title = await tp.system.prompt("프로젝트명:", "PRJ - ");
  if (!title.startsWith("PRJ - ")) title = `PRJ - ${title}`;
  
  const domain = await pickDomain();
  folder = "🎯 Projects";
  
  fm.type = "project";
  fm.status = "sapling";
  fm.author = ME;
  fm.domain = [domain];
  fm.goal = await tp.system.prompt("목표:", "");
  fm.deadline = await tp.system.prompt("마감일 (YYYY-MM-DD):", "");
  fm.progress = 0;
  fm.tags = ["project", `domain/${domain}`];
  
  body = `
# ${title.replace("PRJ - ", "")}

> **Goal**: ${fm.goal}
> **Deadline**: ${fm.deadline}
> **Progress**: ${fm.progress}%

---

## 📋 Overview


---

## 🎯 Milestones
- [ ] Milestone 1: 
- [ ] Milestone 2: 
- [ ] Milestone 3: 

---

## 📝 Log

### ${NOW}
- 프로젝트 시작

---

## 🔗 Resources
- [[ ]]
`;

} else if (noteType === "meeting") {
  const meetingType = await tp.system.suggester(
    ["회장단", "Hexapod", "Bipedal", "기타"],
    ["회장단", "Hexapod", "Bipedal", "other"]
  ) || "other";
  
  let meetingName = meetingType;
  if (meetingType === "other") {
    meetingName = await tp.system.prompt("회의명:", "");
  }
  
  title = `MTG - ${NOW} ${meetingName}`;
  folder = "🗃️ Archive/Meetings";
  
  fm.type = "meeting";
  fm.status = "sapling";
  fm.meeting_type = meetingName;
  fm.attendees = [];
  fm.tags = ["meeting", `meeting/${meetingName}`];
  
  body = `
# ${meetingName} 회의 - ${NOW}

## 📋 Metadata
- 일시: ${NOW}
- 참석: 
- 장소: 

---

## 📝 Agenda
1. 
2. 
3. 

---

## 💬 Discussion


---

## ✅ Action Items
- [ ] @담당자 - 할일

---

## 📎 Notes

`;

} else if (noteType === "question") {
  title = await tp.system.prompt("질문:", "Q - ");
  if (!title.startsWith("Q - ")) title = `Q - ${title}`;
  
  const domain = await pickDomain();
  folder = "💡 Notes";
  
  fm.type = "question";
  fm.status = "seed";
  fm.author = ME;
  fm.domain = [domain];
  fm.resolved = false;
  fm.tags = ["question", `domain/${domain}`];
  
  body = `
# ${title.replace("Q - ", "")}

> **Status**: ❓ 미해결 | **Domain**: ${domain}

---

## ❓ Question

> 한 문장으로 정리

---

## 🤔 Context

### 이 질문이 생긴 맥락
- 

### 왜 중요한가?
- 

---

## 💭 Current Hypothesis
- 

---

## 🔍 Investigation

### 찾아볼 것
- [ ] 

### 발견한 것
- 

---

## ✅ Resolution

> 해결 시 작성

---

## 🔗 Related
- [[ ]]
`;

} else if (noteType === "idea") {
  title = await tp.system.prompt("아이디어:", "💡 ");
  
  const domain = await pickDomain();
  folder = "💡 Notes";
  
  fm.type = "idea";
  fm.status = "seed";
  fm.author = ME;
  fm.domain = [domain];
  fm.validated = false;
  fm.tags = ["idea", `domain/${domain}`];
  
  body = `
# ${title.replace("💡 ", "")}

> **Status**: 💡 검증 전 | **Domain**: ${domain}

---

## 💡 Idea Summary


---

## 🎯 Problem This Solves
- 

---

## ✅ Pros
- 

## ⚠️ Cons / Risks
- 

---

## 🧪 Validation

### 검증 방법
- [ ] 

### 결과
- 

---

## 🔗 Related
- [[ ]]
`;
}

fm.title = title.replace(/^[A-Z]+ - /, "").replace(/^💡 /, "");

try { await tp.file.rename(title); } catch(e) {}
try { await tp.file.move(`${folder}/${title}`); } catch(e) {}

let fmStr = "---\n";
for (const [key, value] of Object.entries(fm)) {
  if (Array.isArray(value)) {
    if (value.length === 0) {
      fmStr += `${key}: []\n`;
    } else {
      fmStr += `${key}:\n`;
      value.forEach(v => fmStr += `  - ${v}\n`);
    }
  } else if (value === null || value === undefined || value === "") {
    fmStr += `${key}: \n`;
  } else {
    fmStr += `${key}: ${typeof value === 'string' && value.includes(':') ? `"${value}"` : value}\n`;
  }
}
fmStr += "---";

tR += fmStr + body;
-%>
