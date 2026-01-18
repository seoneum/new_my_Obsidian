---
migrated_from: CMDS/500. setting/501. Template/Book_Template.md
updated: 2026-01-18T16:42:53
domain:
  - phil
cmds: connect
---
<%*
const ME = '[[김선음]]';
const NOW_DATE = tp.date.now("YYYY-MM-DD");
const NOW_DT = tp.date.now("YYYY-MM-DDTHH:mm:ss");

const q = (s) => `"${String(s ?? "").replaceAll(`"`, `\\"`)}"`;
const cleanTag = (s) => String(s ?? "").trim().replace(/^#/, "");
const wikilink = (s) => {
  const t = String(s ?? "").trim();
  if (!t) return "";
  if (t.startsWith("[[") && t.endsWith("]]")) return t;
  return `[[${t}]]`;
};
const yamlList = (items, indent=2) => {
  const arr = (items ?? []).filter(Boolean);
  if (arr.length === 0) return " []";
  const pad = " ".repeat(indent);
  return "\n" + arr.map(x => `${pad}- ${x}`).join("\n");
};

// ===== 책 정보 입력 =====
const bookTitle = (await tp.system.prompt("📚 책 제목:", tp.file.title))?.trim() || tp.file.title;

const reading = await tp.system.suggester(
  ["1독 (초독)", "2독 (재독)", "3독", "4독", "5독"],
  ["1", "2", "3", "4", "5"]
);
if (!reading) {
  new Notice("❌ Book 노트 생성이 취소되었습니다.");
  return;
}

const genre = await tp.system.suggester(
  ["🏛️ 철학 (Philosophy)", "📖 문학 (Literature)", "📚 인문학 (Humanities)", "🔬 과학 (Science)", "💼 자기계발 (Self-help)", "📜 기타 (Other)"],
  ["Phil", "Lit", "Hum", "Sci", "Self", "Other"]
);
if (!genre) {
  new Notice("❌ Book 노트 생성이 취소되었습니다.");
  return;
}

const author = (await tp.system.prompt("✍️ 저자:", ""))?.trim() || "";
const translator = (await tp.system.prompt("🌐 역자 (없으면 Enter):", ""))?.trim() || "";
const publisher = (await tp.system.prompt("🏢 출판사 (없으면 Enter):", ""))?.trim() || "";
const publishYear = (await tp.system.prompt("📅 출판연도 (없으면 Enter):", ""))?.trim() || "";
const totalPages = (await tp.system.prompt("📄 총 페이지 (없으면 Enter):", ""))?.trim() || "";

// 챕터 수 입력
const chapterCountRaw = await tp.system.prompt("📖 챕터 수 (기본: 5):", "5");
const chapterCount = parseInt(chapterCountRaw) || 5;

// 태깅 모드
const taggingMode = await tp.system.suggester(
  ["기본 태그만(나중에 태깅)", "지금 추가 태그 입력"],
  ["later","now"]
);
let extraTags = [];
if (taggingMode === "now") {
  const raw = await tp.system.prompt("추가 tags (쉼표):", "");
  extraTags = (raw ?? "").split(",").map(s => cleanTag(s).trim()).filter(Boolean);
}

// ===== 폴더 결정 =====
let folder = "📖 Books";
let groupOne = genre;

if (genre === "Phil") {
  folder = "📖 Books/Philosophy";
  groupOne = "Phil";
} else if (genre === "Lit") {
  folder = "📖 Books/Literature";
  groupOne = "Lit";
} else {
  folder = `📖 Books/${genre}`;
}

// ===== 파일명 및 태그 =====
const readingLabel = reading === "1" ? "초독" : reading === "2" ? "재독" : `${reading}독`;
const title = `B - ${bookTitle} (${readingLabel})`;

let tags = [
  "book",
  `book/${genre.toLowerCase()}`,
  `reading/${reading}독`,
  ...extraTags
];
if (taggingMode === "later") tags.push("tagging/needed");

// 이전 독서 노트 링크
let prevReadingLink = "";
if (parseInt(reading) > 1) {
  const prevNum = parseInt(reading) - 1;
  const prevLabel = prevNum === 1 ? "초독" : prevNum === 2 ? "재독" : `${prevNum}독`;
  prevReadingLink = `[[B - ${bookTitle} (${prevLabel})]]`;
}

// 목표 텍스트 결정
let goalText = "";
if (reading === "1") {
  goalText = "전체 흐름 파악, 인상적인 구절 표시, 모르는 단어/개념 체크";
} else if (reading === "2") {
  goalText = "구조 분석, 핵심 논증 정리, 초독 때 놓친 부분 보완";
} else if (reading === "3") {
  goalText = "비판적 읽기, 다른 책/개념과 연결, 나만의 해석 발전";
} else {
  goalText = "심화 분석, 특정 주제 집중 탐구, 글쓰기/발표 준비";
}

// 다음 독서 계획 텍스트
let nextReadingPlan = "";
if (parseInt(reading) < 5) {
  const nextNum = parseInt(reading) + 1;
  const nextLabel = nextNum === 2 ? "재독" : `${nextNum}독`;
  nextReadingPlan = `- [ ] ${nextLabel} 예정일: \n- ${nextLabel} 때 집중할 점: `;
} else {
  nextReadingPlan = "- 5독 완료! 🎉\n- [ ] Merge 노트로 최종 정리: [[ ]]";
}

// 이전 독서 링크 줄
let prevReadingLine = prevReadingLink ? `> - **이전 독서**: ${prevReadingLink}` : "";

// 챕터 섹션 동적 생성
let chapterSections = "";
for (let i = 1; i <= chapterCount; i++) {
  chapterSections += `### Chapter ${i}: 
**핵심 내용**
- 

**인상적인 구절**
> p. 

**의문/생각**
- 

---

`;
}

// ===== 파일 이동 =====
try { await tp.file.rename(title); } catch(e) {}
try { await tp.file.move(`${folder}/${title}`); } catch(e) {}

-%>
---
tags:<% tags.map(t => `\n  - ${t}`).join("") %>
aliases:
  - "<% bookTitle %>"
index:
  - "[[🏷 Books]]"
type:
  - book
title: "<% title %>"
created: <% NOW_DATE %>
updated: <% NOW_DT %>
author: "<% author %>"
translator: "<% translator %>"
publisher: "<% publisher %>"
publish_year: "<% publishYear %>"
total_pages: <% totalPages || '""' %>
CMDS:
  - Connect
status:
  - "[[🚜In Progress]]"
group:
  - <% groupOne %>
reading_count: <% reading %>
start_date: <% NOW_DATE %>
finish_date: ""
prev_reading: "<% prevReadingLink %>"
---

# <% bookTitle %> (<% readingLabel %>)

> [!info] 책 정보
> - **저자**: <% author %>
> - **역자**: <% translator || "-" %>
> - **출판사**: <% publisher || "-" %>
> - **출판연도**: <% publishYear || "-" %>
> - **총 페이지**: <% totalPages || "-" %>
> - **독서 회차**: <% readingLabel %>
<% prevReadingLine %>

---

## 🎯 이번 독서 목표

> [!abstract] <% readingLabel %> 목표
> <% goalText %>

- [ ] 목표 1: 
- [ ] 목표 2: 
- [ ] 목표 3: 

---

## 📖 독서 진행

### 진행 기록
| 날짜 | 페이지 | 소요 시간 | 메모 |
|------|--------|-----------|------|
| <% NOW_DATE %> | p.1 - p. | | |
| | | | |

### 현재 진행률
- 현재: p. / <% totalPages || "?" %>
- 진행률: %

---

## 📝 챕터별 노트 (<% chapterCount %>개)

<% chapterSections %>

## ⭐ 핵심 구절 모음

> [!quote] p.
> 

> [!quote] p.
> 

---

## 💡 떠오른 생각들

### 연결되는 개념/책
- [[ ]] - 
- [[ ]] - 

### 나의 해석/비평
- 

### 삶에 적용할 점
- 

---

## ❓ 질문 & 탐구거리

### 해결된 질문
- [ ] Q: 
  - A: 

### 미해결 질문 (다음 독서에서)
- [ ] Q: 

---

## 📊 독서 완료 후 정리

### 한 줄 요약
> 

### 별점
⭐⭐⭐⭐⭐ ( /5)

### 추천 대상
- 

### 다음 독서 계획
<% nextReadingPlan %>

---

## 🔗 Cross-links

### 관련 Merge 노트
- [[ ]]

### 같은 저자의 다른 책
- [[ ]]

### 비슷한 주제의 책
- [[ ]]

---

## 📝 Flashcards

#flashcards/<% genre.toLowerCase() %>

<% bookTitle %>의 핵심 주제:: 

<% bookTitle %>에서 가장 인상적인 구절:: 

<% author %>의 핵심 사상:: 

