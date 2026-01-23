<%*
/**
 * MASTER TEMPLATE v4.0 - All-in-One
 * 모든 노트 타입을 내부에서 직접 처리
 */

const ME = '[[김선음]]';
const NOW_DATE = tp.date.now("YYYY-MM-DD");
const NOW_DT = tp.date.now("YYYY-MM-DDTHH:mm:ss");
const WEEKDAY = tp.date.now("ddd");
const WEEK_NUM = tp.date.now("WW");

// ===== Helper Functions =====
const q = (s) => `"${String(s ?? "").replaceAll(`"`, `\\"`)}"`;
const cleanTag = (s) => String(s ?? "").trim().replace(/^#/, "");

async function renameAndMove(newTitle, folder) {
  try { await tp.file.rename(newTitle); } catch(e) {}
  if (folder) {
    try { await tp.file.move(`${folder}/${newTitle}`); } catch(e) {}
  }
}

// ===== Choose Note Type =====
const kind = await tp.system.suggester(
  [
    "━━━ 📝 메모 ━━━",
    "📝 MEMO: 빠른 메모",
    "━━━ 📚 학습 ━━━",
    "📚 LECTURE: 수업 노트",
    "📕 BOOK: 독서 노트",
    "💡 CONCEPT: 개념 정리",
    "📐 PROBLEM: 문제 풀이",
    "🧠 FEYNMAN: 페인만 학습",
    "━━━ 📖 정리 ━━━",
    "📖 REFERENCE: 논문/책/자료",
    "🌐 WEB CLIP: 웹 저장",
    "━━━ 🔧 협업 ━━━",
    "🔧 PROJECT: 프로젝트",
    "📋 MEETING: 회의록",
    "━━━ ❓ 기타 ━━━",
    "❓ QUESTION: 미해결 질문",
    "👤 PEOPLE: 인물 노트",
  ],
  [
    null, "memo",
    null, "lecture", "book", "concept", "problem", "feynman",
    null, "reference", "webclip",
    null, "project", "meeting",
    null, "question", "people"
  ]
);

// 취소 또는 구분선 선택시 종료
if (!kind) {
  tR += "";
} else {

let title = "";
let folder = "";
let fm = "";
let body = "";

// ==================== MEMO ====================
if (kind === "memo") {
  title = await tp.system.prompt("메모 제목:", "N - ");
  if (!title) { tR += ""; }
  else {
    if (!title.startsWith("N - ")) title = `N - ${title}`;
    folder = "📥 Inbox/_quick";
    await renameAndMove(title, folder);

    fm = `---
type: memo
title: "${title}"
created: ${NOW_DATE}
updated: ${NOW_DT}
author: "${ME}"
tags:
  - inbox
  - memo
  - tagging/needed
---`;

    body = `
# ${title.replace("N - ", "")}

## Notes
- 

## Next
- [ ] 
`;
    tR += fm + body;
  }

// ==================== LECTURE ====================
} else if (kind === "lecture") {
  const course = await tp.system.suggester(
    ["🏛️ 언어철학", "🏛️ 존재론과형이상학", "🏛️ 서양현대철학사", "🔢 공업수학1", "🔢 일반수학2", "⚡ 전자기학1", "📚 기타"],
    ["언어철학", "존재론과형이상학", "서양현대철학사", "공업수학1", "일반수학2", "전자기학1", "other"]
  );
  if (!course) { tR += ""; }
  else {
    let courseName = course;
    let group = "General";
    
    if (course === "other") {
      courseName = await tp.system.prompt("과목명:", "") || "기타";
    }
    
    if (["언어철학", "존재론과형이상학", "서양현대철학사"].includes(course)) group = "Phil";
    else if (["공업수학1", "일반수학2"].includes(course)) group = "Math";
    else if (course === "전자기학1") group = "EE";
    
    const session = await tp.system.prompt("주차/회차:", "1");
    title = await tp.system.prompt("강의 제목:", `${courseName} ${session}주차`);
    if (!title.startsWith("L - ")) title = `L - ${title}`;
    
    folder = `📚 Lectures/26-1/${courseName}`;
    await renameAndMove(title, folder);

    fm = `---
type: lecture
title: "${title}"
created: ${NOW_DATE}
updated: ${NOW_DT}
course: ${courseName}
session: ${session}
group: ${group}
tags:
  - lecture
  - course/${courseName}
---`;

    body = `
# ${title.replace("L - ", "")}

> **${courseName}** | ${session}주차

---

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

---

## 📝 FC
#flashcards/${group.toLowerCase()}

핵심 개념:: 
`;
    tR += fm + body;
  }

// ==================== BOOK ====================
} else if (kind === "book") {
  const bookTitle = await tp.system.prompt("📚 책 제목:", tp.file.title);
  if (!bookTitle) { tR += ""; }
  else {
    const reading = await tp.system.suggester(
      ["1독 (초독)", "2독 (재독)", "3독", "4독", "5독"],
      ["1", "2", "3", "4", "5"]
    ) || "1";

    const genre = await tp.system.suggester(
      ["🏛️ 철학", "📖 문학", "📚 인문학", "🔬 과학", "💼 자기계발", "📜 기타"],
      ["Phil", "Lit", "Hum", "Sci", "Self", "Other"]
    ) || "Other";
    
    const author = await tp.system.prompt("✍️ 저자:", "") || "";
    const translator = await tp.system.prompt("🌐 역자 (없으면 Enter):", "") || "";
    const publisher = await tp.system.prompt("🏢 출판사 (없으면 Enter):", "") || "";
    const publishYear = await tp.system.prompt("📅 출판연도 (없으면 Enter):", "") || "";
    const totalPages = await tp.system.prompt("📄 총 페이지 (없으면 Enter):", "") || "";
    const chapterCount = parseInt(await tp.system.prompt("📖 챕터 수 (기본: 5):", "5")) || 5;

    const readingLabel = reading === "1" ? "초독" : reading === "2" ? "재독" : `${reading}독`;
    
    // 이전 독서 링크 (2독 이상)
    let prevReadingLink = "";
    if (parseInt(reading) > 1) {
      const prevNum = parseInt(reading) - 1;
      const prevLabel = prevNum === 1 ? "초독" : prevNum === 2 ? "재독" : `${prevNum}독`;
      prevReadingLink = `[[B - ${bookTitle} (${prevLabel})]]`;
    }

    // 회차별 목표 텍스트
    let goalText = "";
    if (reading === "1") goalText = "전체 흐름 파악, 인상적인 구절 표시, 모르는 단어/개념 체크";
    else if (reading === "2") goalText = "구조 분석, 핵심 논증 정리, 초독 때 놓친 부분 보완";
    else if (reading === "3") goalText = "비판적 읽기, 다른 책/개념과 연결, 나만의 해석 발전";
    else goalText = "심화 분석, 특정 주제 집중 탐구, 글쓰기/발표 준비";

    // 챕터 섹션 동적 생성
    let chapterSections = "";
    for (let i = 1; i <= chapterCount; i++) {
      chapterSections += `### Chapter ${i}: \n**핵심 내용**\n- \n\n**인상적인 구절**\n> p. \n\n---\n\n`;
    }

    title = `B - ${bookTitle} (${readingLabel})`;
    folder = genre === "Phil" ? "📖 Books/Philosophy" : 
             genre === "Lit" ? "📖 Books/Literature" : 
             `📖 Books/${genre}`;
    await renameAndMove(title, folder);

    fm = `---
type: book
title: "${bookTitle}"
created: ${NOW_DATE}
updated: ${NOW_DT}
author: "${author}"
translator: "${translator}"
publisher: "${publisher}"
publish_year: "${publishYear}"
total_pages: ${totalPages || '""'}
genre: ${genre}
reading_count: ${reading}
prev_reading: "${prevReadingLink}"
status: "[[🚜In Progress]]"
tags:
  - book
  - book/${genre.toLowerCase()}
  - reading/${reading}독
---`;

    const prevLine = prevReadingLink ? `> - **이전 독서**: ${prevReadingLink}` : "";

    body = `
# ${bookTitle} (${readingLabel})

> [!info] 책 정보
> - **저자**: ${author}
> - **역자**: ${translator || "-"}
> - **출판사**: ${publisher || "-"}
> - **출판연도**: ${publishYear || "-"}
> - **총 페이지**: ${totalPages || "-"}
> - **독서 회차**: ${readingLabel}
${prevLine}

---

## 🎯 이번 독서 목표

> [!abstract] ${readingLabel} 목표
> ${goalText}

- [ ] 목표 1: 
- [ ] 목표 2: 
- [ ] 목표 3: 

---

## 📖 독서 진행

| 날짜 | 페이지 | 소요 시간 | 메모 |
|------|--------|-----------|------|
| ${NOW_DATE} | p.1 - p. | | |

### 현재 진행률
- 현재: p. / ${totalPages || "?"}
- 진행률: %

---

## 📝 챕터별 노트 (${chapterCount}개)

${chapterSections}

## ⭐ 핵심 구절 모음

> [!quote] p.
> 

---

## 💡 떠오른 생각들

### 연결되는 개념/책
- [[ ]] - 
- [[ ]] - 

### 나의 해석/비평
- 

---

## ❓ 질문 & 탐구거리

- [ ] Q: 
  - A: 

---

## 🔗 Cross-links

### 관련 Merge 노트
- [[ ]]

### 같은 저자의 다른 책
- [[ ]]

---

## 📝 FC
#flashcards/${genre.toLowerCase()}

${bookTitle} 핵심 주제:: 

${bookTitle}에서 가장 인상적인 구절:: 
`;
    tR += fm + body;
  }

// ==================== CONCEPT ====================
} else if (kind === "concept") {
  const domain = await tp.system.suggester(
    ["💻 CS", "🔢 Math", "⚡ EE", "🏛️ Phil", "🤖 Robotics"],
    ["CS", "Math", "EE", "Phil", "Robotics"]
  );
  if (!domain) { tR += ""; }
  else {
    // 세부 도메인 선택
    let subDomain = "";
    if (domain === "CS") {
      subDomain = await tp.system.suggester(
        ["C++", "Python", "알고리즘", "자료구조", "기타"],
        ["cpp", "python", "algorithm", "ds", "other"]
      ) || "cpp";
    } else if (domain === "Math") {
      subDomain = await tp.system.suggester(
        ["공업수학1", "일반수학2", "선형대수", "미적분", "기타"],
        ["공업수학", "일반수학", "linear", "calculus", "other"]
      ) || "other";
    } else if (domain === "Phil") {
      subDomain = await tp.system.suggester(
        ["언어철학", "존재론과형이상학", "서양현대철학사", "기타"],
        ["언어철학", "존재론", "현대철학", "other"]
      ) || "other";
    } else if (domain === "EE") {
      subDomain = await tp.system.suggester(
        ["전자기학1", "회로", "기타"],
        ["전자기학", "circuit", "other"]
      ) || "other";
    }

    title = await tp.system.prompt("개념 이름:", tp.file.title);
    if (!title) { tR += ""; }
    else {
      // 난이도 선택
      const level = await tp.system.suggester(
        ["🟢 기초", "🟡 중급", "🔴 심화"],
        ["basic", "mid", "adv"]
      ) || "mid";

      if (!title.startsWith("C - ")) title = `C - ${title}`;
      const conceptName = title.replace("C - ", "");
      folder = "💡 Notes/Concepts";
      await renameAndMove(title, folder);

      // 태그 구성
      let tags = ["concept", `concept/${domain.toLowerCase()}`];
      if (subDomain && subDomain !== "other") tags.push(`topic/${subDomain}`);
      tags.push(`level/${level}`);

      fm = `---
type: concept
title: "${conceptName}"
created: ${NOW_DATE}
updated: ${NOW_DT}
author: "${ME}"
domain: ${domain}
${subDomain && subDomain !== "other" ? `topic: ${subDomain}` : ""}
level: ${level}
status: "[[🌿Sapling]]"
confidence: 0
tags:
${tags.map(t => `  - ${t}`).join("\n")}
---`;

      // 정의 섹션 결정
      let definitionSection = "";
      if (domain === "CS") {
        definitionSection = "```cpp\n// 기본 형태\n\n```";
      } else if (domain === "Math" || domain === "EE") {
        definitionSection = "$$\n\n$$";
      } else {
        definitionSection = "> ";
      }

      // 핵심 섹션 결정 (도메인별)
      let coreSection = "";
      if (domain === "CS") {
        coreSection = `### 문법
\`\`\`cpp

\`\`\`

### 예시
\`\`\`cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    
    return 0;
}
\`\`\`

### 주의
- `;
      } else if (domain === "Math") {
        coreSection = `### 공식
$$

$$

### 증명 (간략)
1. 
2. 

### 언제 사용?
- `;
      } else if (domain === "EE") {
        coreSection = `### 원리
- 

### 수식
$$

$$

### 적용
- `;
      } else if (domain === "Phil") {
        coreSection = `### 핵심 논증
1. 전제: 
2. 전제: 
3. 결론: 

### 주요 철학자
- 

### 비판
- `;
      } else {
        coreSection = `### 핵심 포인트
1. 
2. 
3. `;
      }

      body = `
# ${conceptName}

> **한 줄 요약**: 

---

## 📖 정의

${definitionSection}

---

## 💡 직관적 이해

- 이건 마치 _______ 같다
- 왜냐하면 _______

---

## 📐 핵심

${coreSection}

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
#flashcards/${domain.toLowerCase()}

${conceptName} 정의:: 

${conceptName} 예시:: 

${conceptName} 주의점::
`;
      tR += fm + body;
    }
  }

// ==================== PROBLEM ====================
} else if (kind === "problem") {
  const problemType = await tp.system.suggester(
    ["🔢 수학 문제", "💻 코딩 문제", "⚡ 공학 문제", "🏛️ 철학 문제"],
    ["math", "coding", "engineering", "philosophy"]
  );
  if (!problemType) { tR += ""; }
  else {
    let source = "";
    let problemId = "";
    
    if (problemType === "coding") {
      source = await tp.system.suggester(
        ["백준", "LeetCode", "프로그래머스", "기타"],
        ["baekjoon", "leetcode", "programmers", "other"]
      ) || "baekjoon";
      problemId = await tp.system.prompt("문제 번호:", "") || "";
    } else if (problemType === "math") {
      source = await tp.system.suggester(
        ["공업수학1", "일반수학2", "기출문제", "기타"],
        ["공업수학1", "일반수학2", "exam", "other"]
      ) || "other";
      problemId = await tp.system.prompt("챕터/문제번호:", "") || "";
    } else if (problemType === "engineering") {
      source = await tp.system.suggester(
        ["전자기학1", "기타"],
        ["전자기학1", "other"]
      ) || "other";
      problemId = await tp.system.prompt("문제 번호:", "") || "";
    } else {
      source = await tp.system.prompt("출처:", "") || "";
      problemId = await tp.system.prompt("문제:", "") || "";
    }

    const difficulty = await tp.system.suggester(
      ["🟢 Easy", "🟡 Medium", "🔴 Hard"],
      ["easy", "medium", "hard"]
    ) || "medium";

    title = await tp.system.prompt("문제 제목:", problemId);
    if (!title) { tR += ""; }
    else {
      if (!title.startsWith("P - ")) title = `P - ${title}`;
      
      // 문제 타입별 폴더 분류
      const folderMap = {
        "math": "📝 Problems/Math",
        "coding": "📝 Problems/Coding",
        "engineering": "📝 Problems/Engineering",
        "philosophy": "📝 Problems/Philosophy"
      };
      folder = folderMap[problemType] || "📝 Problems";
      await renameAndMove(title, folder);

      let codeLang = "";
      if (problemType === "coding") {
        codeLang = await tp.system.suggester(
          ["C++", "Python", "둘 다"],
          ["cpp", "python", "both"]
        ) || "cpp";
      }

      let tags = ["problem", `problem/${problemType}`, `difficulty/${difficulty}`];
      if (source && source !== "other") tags.push(`source/${source}`);

      fm = `---
type: problem
title: "${title}"
created: ${NOW_DATE}
updated: ${NOW_DT}
problem_type: ${problemType}
source: ${source}
difficulty: ${difficulty}
${codeLang ? `language: ${codeLang}` : ""}
status: "[[🚜In Progress]]"
solved: false
tags:
${tags.map(t => `  - ${t}`).join("\n")}
---`;

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

      body = `
# ${title.replace("P - ", "")}

> **${problemType}** | 난이도: **${difficulty}** | 출처: ${source} ${problemId}

---

## 📋 문제

${problemSection}

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

${solutionSection}

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
#flashcards/${problemType}

${title.replace("P - ", "")} 핵심:: 
`;
      tR += fm + body;
    }
  }

// ==================== FEYNMAN ====================
} else if (kind === "feynman") {
  const group = await tp.system.suggester(
    ["EE (전기전자)", "Phil (철학)", "SE (소프트웨어)", "Math (수학)", "Robotics", "SLAM", "AI", "General"],
    ["EE", "Phil", "SE", "Math", "Robotics", "SLAM", "AI", "General"]
  );
  if (!group) { tR += ""; }
  else {
    title = await tp.system.prompt("학습 주제:", tp.file.title);
    if (!title) { tR += ""; }
    else {
      const feynmanName = title;
      title = `FYN - ${NOW_DATE} ${feynmanName}`;
      
      const difficulty = await tp.system.suggester(
        ["🟢 Easy (기초)", "🟡 Medium (중급)", "🔴 Hard (심화)"],
        ["easy", "medium", "hard"]
      ) || "medium";
      
      folder = "💡 Notes/Feynman";
      await renameAndMove(title, folder);

      fm = `---
type: feynman
title: "${feynmanName}"
created: ${NOW_DATE}
updated: ${NOW_DT}
author: "${ME}"
group: ${group}
difficulty: ${difficulty}
status: "[[🌿Sapling]]"
tags:
  - feynman
  - merge
  - domain/${group.toLowerCase()}
  - difficulty/${difficulty}
confidence: 0
last_review: ${NOW_DATE}
time_spent: 0
---`;

      body = `
# ${feynmanName}

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
- 시작: \`${tp.date.now("HH:mm")}\`
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

## 📝 FC
#flashcards/${group.toLowerCase()}

${feynmanName} 정의:: 

${feynmanName} 예시:: 

${feynmanName} vs _____:: 차이점

왜 ${feynmanName}이 중요한가?::
`;
      tR += fm + body;
    }
  }

// ==================== REFERENCE ====================
} else if (kind === "reference") {
  title = await tp.system.prompt("자료명:", "R - ");
  if (!title) { tR += ""; }
  else {
    if (!title.startsWith("R - ")) title = `R - ${title}`;
    const url = await tp.system.prompt("URL (없으면 Enter):", "") || "";
    folder = "📖 Books";
    await renameAndMove(title, folder);

    fm = `---
type: reference
title: "${title}"
created: ${NOW_DATE}
updated: ${NOW_DT}
source_url: "${url}"
tags:
  - reference
  - tagging/needed
---`;

    body = `
# ${title.replace("R - ", "")}

## 📋 Metadata
- URL: ${url}
- Author: 
- Date: 

---

## 📝 Summary
- 

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
`;
    tR += fm + body;
  }

// ==================== WEB CLIP ====================
} else if (kind === "webclip") {
  title = await tp.system.prompt("제목:", "W - ");
  if (!title) { tR += ""; }
  else {
    if (!title.startsWith("W - ")) title = `W - ${title}`;
    const url = await tp.system.prompt("URL:", "") || "";
    folder = "📥 Inbox/_webclip";
    await renameAndMove(title, folder);

    fm = `---
type: webclip
title: "${title}"
created: ${NOW_DATE}
updated: ${NOW_DT}
source_url: "${url}"
tags:
  - webclip
  - inbox
---`;

    body = `
# ${title.replace("W - ", "")}

## Source
- URL: ${url}

---

## 📝 Content


---

## 💡 Why Clipped
- 

## Next
- [ ] 필요시 Reference로 이동
`;
    tR += fm + body;
  }

// ==================== PROJECT ====================
} else if (kind === "project") {
  title = await tp.system.prompt("프로젝트명:", "PRJ - ");
  if (!title) { tR += ""; }
  else {
    if (!title.startsWith("PRJ - ")) title = `PRJ - ${title}`;
    const goal = await tp.system.prompt("목표 (한 줄):", "") || "";
    const deadline = await tp.system.prompt("마감일 (없으면 Enter):", "") || "";
    folder = "🎯 Projects";
    await renameAndMove(title, folder);

    fm = `---
type: project
title: "${title}"
created: ${NOW_DATE}
updated: ${NOW_DT}
goal: "${goal}"
deadline: "${deadline}"
status: "[[🚜In Progress]]"
progress: 0
tags:
  - project
---`;

    body = `
# ${title.replace("PRJ - ", "")}

> **Goal**: ${goal}
> **Deadline**: ${deadline}

---

## 📋 Overview


---

## 🎯 Milestones
- [ ] Milestone 1: 
- [ ] Milestone 2: 
- [ ] Milestone 3: 

---

## 📝 Log

### ${NOW_DATE}
- 프로젝트 시작

---

## 🔗 Resources
- [[ ]]
`;
    tR += fm + body;
  }

// ==================== MEETING ====================
} else if (kind === "meeting") {
  const meetingType = await tp.system.suggester(
    ["🏛️ 회장단", "🦿 Hexapod", "🚶 Bipedal", "📚 기타"],
    ["회장단", "Hexapod", "Bipedal", "other"]
  );
  if (!meetingType) { tR += ""; }
  else {
    let meetingName = meetingType;
    if (meetingType === "other") {
      meetingName = await tp.system.prompt("회의명:", "") || "기타";
    }
    const num = await tp.system.prompt("회차:", "1") || "1";
    const attendees = await tp.system.prompt("참석자 (쉼표):", "") || "";
    
    title = `MTG - ${NOW_DATE} ${meetingName} ${num}회`;
    folder = "🗃️ Archive/Meetings";
    await renameAndMove(title, folder);

    fm = `---
type: meeting
title: "${meetingName} ${num}회"
created: ${NOW_DATE}
updated: ${NOW_DT}
meeting_type: ${meetingName}
meeting_num: ${num}
attendees: [${attendees.split(",").map(a => `"${a.trim()}"`).join(", ")}]
tags:
  - meeting
  - meeting/${meetingName}
---`;

    body = `
# ${meetingName} ${num}회 회의록

> 📅 **${NOW_DATE}** | 참석: ${attendees}

---

## 📋 안건
1. [ ] 
2. [ ] 
3. [ ] 

---

## 📝 내용

### 1. 
- 

### 2. 
- 

---

## ✅ Action Items

| 담당 | 할 일 | 마감 |
|-----|------|-----|
| | | |
| | | |

---

## 📅 다음 회의
- 일시: 
- 안건: 

---

## 🔗 관련
- 이전: [[ ]]
- 프로젝트: [[ ]]
`;
    tR += fm + body;
  }

// ==================== QUESTION ====================
} else if (kind === "question") {
  const thinkingType = await tp.system.suggester(
    ["❓ 미해결 질문", "💡 아이디어", "🤔 고민/딜레마", "🔗 연결점"],
    ["question", "idea", "dilemma", "connection"]
  );
  if (!thinkingType) { tR += ""; }
  else {
    title = await tp.system.prompt("질문/아이디어 제목:", tp.file.title);
    if (!title) { tR += ""; }
    else {
      if (!title.startsWith("Q - ")) title = `Q - ${title}`;
      folder = "💡 Notes";
      await renameAndMove(title, folder);

      fm = `---
type: thinking
title: "${title}"
created: ${NOW_DATE}
updated: ${NOW_DT}
thinking_type: ${thinkingType}
status: "[[🌱Seed]]"
resolved: false
tags:
  - thinking
  - thinking/${thinkingType}
---`;

      body = `
# ${title.replace("Q - ", "")}

> **${thinkingType}**

---

## ❓ 핵심 질문/아이디어

> 한 문장으로 정리

---

## 🤔 Context

### 이 질문이 생긴 맥락
- 

### 왜 중요한가?
- 

---

## 💭 현재 가설
- 

---

## 🔍 조사

### 찾아볼 것
- [ ] 

### 발견한 것
- 

---

## ✅ Resolution (해결되면 작성)

> 해결 여부: ⬜ 미해결 / ⬜ 해결됨 / ⬜ 보류

### 결론/답변
- 

---

## 🔗 Related
- [[ ]]
`;
      tR += fm + body;
    }
  }

// ==================== PEOPLE ====================
} else if (kind === "people") {
  const pType = await tp.system.suggester(
    ["지인", "공학 인물", "철학 인물", "불명"],
    ["acq", "eng", "phil", "unk"]
  );
  if (!pType) { tR += ""; }
  else {
    title = await tp.system.prompt("인물 이름:", tp.file.title);
    if (!title) { tR += ""; }
    else {
      if (!title.startsWith("PPL - ")) title = `PPL - ${title}`;
      const org = await tp.system.prompt("소속/조직 (없으면 Enter):", "") || "";
      const role = await tp.system.prompt("한줄 설명 (없으면 Enter):", "") || "";
      
      folder = pType === "acq" ? "⚙️ Meta/People/Acquaintance" :
               pType === "eng" ? "⚙️ Meta/People/Engineering" :
               pType === "phil" ? "⚙️ Meta/People/Philosophy" :
               "⚙️ Meta/People/Unknown";
      await renameAndMove(title, folder);

      fm = `---
type: people
title: "${title}"
created: ${NOW_DATE}
updated: ${NOW_DT}
organization: "${org}"
role: "${role}"
tags:
  - people
  - people/${pType}
---`;

      body = `
# ${title.replace("PPL - ", "")}

## Snapshot
- **Role**: ${role}
- **Organization**: ${org}

---

## Key points
- 

---

## Links
- 
`;
      tR += fm + body;
    }
  }

} // end of else (kind was not null)
}
%>
