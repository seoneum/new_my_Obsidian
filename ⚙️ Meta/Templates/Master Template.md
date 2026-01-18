---
migrated_from: CMDS/500. setting/501. Template/Master Template.md
updated: 2026-01-18T16:42:53
domain:
  - robotics
cmds: connect
---
<%*
/**
 * MASTER ROUTER - CMDS Vault v3.1
 * 
 * 노트 타입:
 * - 일상: DAILY, MEMO
 * - 학습: LECTURE, BOOK, CONCEPT, PROBLEM
 * - 정리: REFERENCE, WEB CLIP, DEVELOP
 * - 협업: PROJECT, MEETING
 * - 기타: QUESTION, PEOPLE, SHARE
 * - 복습: FC MORNING, FC EVENING, WEEKLY
 */

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
const slugNoSpace = (s) => String(s ?? "").trim().replace(/\s+/g,"");

async function pickStatus(def='[[🚜In Progress]]') {
  const labels = ["🌱Seed","🌿Sapling","🌲Evergreen","🍂Archive","🚜In Progress"];
  const values = ["[[🌱Seed]]","[[🌿Sapling]]","[[🌲Evergreen]]","[[🍂Archive]]","[[🚜In Progress]]"];
  return (await tp.system.suggester(labels, values)) ?? def;
}
async function pickGroup(def="General") {
  const labels = ["CS","EE","Phil","Math","General","Robotics","SLAM","AI"];
  const values = ["CS","EE","Phil","Math","General","Robotics","SLAM","AI"];
  return (await tp.system.suggester(labels, values)) ?? def;
}
async function renameAndMove(newTitle, folder) {
  try { await tp.file.rename(newTitle); } catch(e) {}
  if (folder) {
    try { await tp.file.move(`${folder}/${newTitle}`); } catch(e) {}
  }
}

// ===== Paths =====
const PATH = {
  // Inbox
  inbox: "📥 Inbox",
  inbox_quick: "📥 Inbox/_quick",
  inbox_webclip: "📥 Inbox/_webclip",

  // Daily
  daily: "📅 Daily",

  // Lectures (by semester)
  lectures: "📚 Lectures",
  lectures_26_1: "📚 Lectures/26-1",

  // Books
  books: "📖 Books",
  books_phil: "📖 Books/Philosophy",
  books_lit: "📖 Books/Literature",
  books_sci: "📖 Books/Science",

  // Notes
  notes: "💡 Notes",
  notes_concepts: "💡 Notes/Concepts",
  notes_problems: "💡 Notes/Problems",
  notes_flashcards: "💡 Notes/Flashcards",
  notes_feynman: "💡 Notes/Feynman",

  // Projects
  projects: "🎯 Projects",
  projects_active: "🎯 Projects/Active",

  // Archive
  archive: "🗃️ Archive",
  archive_meetings: "🗃️ Archive/Meetings",

  // Meta
  meta: "⚙️ Meta",
  templates: "⚙️ Meta/Templates",
  people_acq: "⚙️ Meta/People/Acquaintance",
  people_eng: "⚙️ Meta/People/Engineering",
  people_phil: "⚙️ Meta/People/Philosophy",
  people_unk: "⚙️ Meta/People/Unknown",
};

// ===== Index links =====
const INDEX = {
  daily: '[[🏷 Daily Notes]]',
  lecture: '[[🏷 Lecture Notes]]',
  webclips: '[[🏷 Web Clips]]',
  research: '[[🏷 Research Notes]]',
  books: '[[🏷 Books]]',
  people: '[[🏷 People]]',
  waypoint: '[[🏷 Waypoint]]',
  review: '[[🏷 Review Notes]]',
  software: '[[🏷️Software]]',
  thinking: '[[🏷 Thinking]]',
};

// ===== Choose kind (NEW MENU) =====
const kind = await tp.system.suggester(
  [
    "━━━ 📅 일상 ━━━",
    "📅 DAILY: 하루 계획/마무리",
    "📝 MEMO: 빠른 메모",
    "━━━ 📚 학습 ━━━",
    "📚 LECTURE: 수업 노트",
    "📕 BOOK: 독서 노트 (다회독)",
    "💡 CONCEPT: 개념 정리",
    "📐 PROBLEM: 문제 풀이",
    "━━━ 📖 정리 ━━━",
    "📖 REFERENCE: 논문/책/자료",
    "🌐 WEB CLIP: 웹 저장",
    "📊 DEVELOP: 치트시트",
    "━━━ 🔧 협업 ━━━",
    "🔧 PROJECT: 프로젝트",
    "📋 MEETING: 회의록",
    "━━━ ❓ 기타 ━━━",
    "❓ QUESTION: 미해결 질문",
    "👤 PEOPLE: 인물 노트",
    "📤 SHARE: 외부 공유",
    "━━━ 🔄 복습 ━━━",
    "🌅 FC MORNING: 아침 복습",
    "🌙 FC EVENING: 저녁 복습",
    "📆 WEEKLY: 주간 복습"
  ],
  [
    null, "daily", "inbox",
    null, "connect_lecture", "book", "concept", "problem",
    null, "reference", "webclip", "develop",
    null, "project", "meeting",
    null, "question", "people", "share",
    null, "fc_morning", "fc_evening", "weekly"
  ]
);

// ===== Redirect to specific templates =====
if (kind === "daily") {
  tR += await tp.file.include("[[Daily_Template]]");
} else if (kind === "book") {
  tR += await tp.file.include("[[Book_Template]]");
} else if (kind === "concept") {
  tR += await tp.file.include("[[Concept_Template]]");
} else if (kind === "problem") {
  tR += await tp.file.include("[[Problem_Template]]");
} else if (kind === "meeting") {
  tR += await tp.file.include("[[Meeting_Template]]");
} else if (kind === "question") {
  tR += await tp.file.include("[[Thinking_Template]]");
} else if (kind === "weekly") {
  tR += await tp.file.include("[[Weekly_Review_Template]]");
} else if (kind === "fc_morning") {
  tR += await tp.file.include("[[FC_Morning_Template]]");
} else if (kind === "fc_evening") {
  tR += await tp.file.include("[[FC_Evening_Template]]");
} else if (kind === null) {
  // 구분선 선택시 아무것도 안함
  tR += "";
} else {

// ===== Tagging mode =====
const taggingMode = await tp.system.suggester(
  ["기본 태그만(나중에 태깅)", "지금 추가 태그 입력"],
  ["later","now"]
);
let extraTags = [];
if (taggingMode === "now") {
  const raw = await tp.system.prompt("추가 tags (쉼표):", "");
  extraTags = (raw ?? "").split(",").map(s => cleanTag(s).trim()).filter(Boolean);
}

// ===== Title =====
let title = (await tp.system.prompt("제목(title):", tp.file.title))?.trim() || tp.file.title;

// ===== Common fields =====
let tags = [];
let aliases = [];
let indexArr = [];
let typeArr = [];
let authors = [];
let cmdsArr = [];
let groupOne = await pickGroup();
let statusOne = await pickStatus();

let cover_url = "";
let my_rate = "";
let publishDate = "";
let started = NOW_DATE;
let start_read_date = "";
let finish_read_date = "";
let folder = PATH.inbox;

function applyTaggingNeeded() {
  if (taggingMode === "later") tags.push("tagging/needed");
}
function withPrefix(prefix, t) {
  const s = String(t ?? "").trim();
  if (!s) return s;
  if (s.startsWith(prefix)) return s;
  return `${prefix}${s}`;
}

// ===== Branches =====
if (kind === "inbox") {
  folder = PATH.inbox_quick;
  indexArr = [INDEX.waypoint];
  groupOne = "General";

  typeArr = ["basic"];
  cmdsArr = [];
  authors = [q(ME)];
  title = withPrefix("N - ", title);
  tags = ["inbox", "note", ...extraTags];
  applyTaggingNeeded();

} else if (kind === "connect_lecture") {
  // 26-1학기 과목 선택
  const course = await tp.system.suggester(
    [
      "🏛️ 언어철학",
      "🏛️ 존재론과형이상학", 
      "🏛️ 서양현대철학사",
      "🔢 공업수학1",
      "🔢 일반수학2",
      "⚡ 전자기학1",
      "📚 기타 (직접입력)"
    ],
    [
      "언어철학",
      "존재론과형이상학",
      "서양현대철학사",
      "공업수학1",
      "일반수학2",
      "전자기학1",
      "other"
    ]
  ) || "other";

  let courseName = "";
  let courseFolder = PATH.lectures_26_1;
  
  if (course === "other") {
    courseName = await tp.system.prompt("과목명:", "");
    const domain = await tp.system.suggester(
      ["CS", "EE", "Phil", "Math", "Robotics", "General"],
      ["CS","EE","Phil","Math","Robotics","General"]
    );
    groupOne = domain;
    courseFolder = `${PATH.lectures_26_1}/${courseName}`;
  } else {
    courseFolder = `${PATH.lectures_26_1}/${course}`;
    courseName = course;
    // 자동 group 결정
    if (["언어철학", "존재론과형이상학", "서양현대철학사"].includes(course)) groupOne = "Phil";
    else if (["공업수학1", "일반수학2"].includes(course)) groupOne = "Math";
    else if (course === "전자기학1") groupOne = "EE";
  }

  folder = courseFolder;
  indexArr = [INDEX.lecture];
  typeArr = ["lecture"];
  cmdsArr = [];
  authors = [];

  const session = await tp.system.prompt("주차/회차:", NOW_DATE);
  const instructor = await tp.system.prompt("교수(없으면 Enter):", "");

  title = withPrefix("L - ", title);
  tags = ["lecture", `lecture/${groupOne}`, `course/${courseName}`, ...extraTags];
  applyTaggingNeeded();

  var META_LECTURE = { course: courseName, session, instructor, source_url: "" };

} else if (kind === "webclip") {
  const url = await tp.system.prompt("URL:", "");

  folder = PATH.inbox_webclip;
  indexArr = [INDEX.webclips];
  typeArr = ["reference"];
  cmdsArr = [];
  authors = [];
  title = withPrefix("W - ", title);
  tags = ["webclip", "inbox", ...extraTags];
  applyTaggingNeeded();

  groupOne = "General";

  var META_WEB = { url, keep: "inbox", area: "any" };

} else if (kind === "reference") {
  const refKind = await tp.system.suggester(["Paper(논문)","Book(책)","Doc/Other(문서/기타)"], ["paper","book","doc"]);
  const url = await tp.system.prompt("URL(없으면 Enter):", "");
  publishDate = await tp.system.prompt("publishDate(없으면 Enter):", "");

  folder = PATH.books;

  indexArr = [
    refKind === "paper" ? INDEX.research :
    refKind === "book" ? INDEX.books :
    INDEX.webclips
  ];

  typeArr = ["reference"];
  cmdsArr = [];
  authors = [];
  title = withPrefix("R - ", title);
  tags = ["reference", refKind, ...extraTags];
  applyTaggingNeeded();

  groupOne = "General";

  var META_REF = { refKind, area: "any", url };

} else if (kind === "people") {
  const pType = await tp.system.suggester(
    ["지인", "공학 인물", "철학 인물", "불명(정보 부족)"],
    ["acq","eng","phil","unk"]
  );

  folder =
    pType === "acq" ? PATH.people_acq :
    pType === "eng" ? PATH.people_eng :
    pType === "phil" ? PATH.people_phil :
    PATH.people_unk;

  indexArr = [INDEX.people];
  typeArr = ["basic"];
  cmdsArr = [];
  authors = [q(ME)];
  title = withPrefix("PPL - ", title);

  const baseName = title.replace(/^PPL\s-\s*/,"");
  const nametag = slugNoSpace(baseName);

  tags = ["people", `people/${nametag}`, `people/${pType}`, ...extraTags];
  applyTaggingNeeded();

  var META_PPL = {
    organization: await tp.system.prompt("소속/조직(없으면 Enter):", ""),
    role: await tp.system.prompt("한줄 설명(없으면 Enter):", "")
  };

  groupOne = pType === "eng" ? "EE" : pType === "phil" ? "Phil" : "General";
  statusOne = pType === "unk" ? "[[🌱Seed]]" : "[[🌿Sapling]]";

} else if (kind === "project") {
  folder = PATH.projects;
  indexArr = [INDEX.waypoint];
  typeArr = ["project"];
  cmdsArr = [];
  authors = [q(ME)];
  title = withPrefix("PRJ - ", title);

  const domain = await tp.system.suggester(
    ["Robotics", "Engineering", "Software", "General"],
    ["Robotics","EE","CS","General"]
  );
  groupOne = domain;

  tags = ["project", "build", ...extraTags];
  applyTaggingNeeded();

  var META_PRJ = {
    goal: await tp.system.prompt("목표(한 줄):", ""),
    deadline: await tp.system.prompt("대회/마감일(없으면 Enter):", ""),
    repo: await tp.system.prompt("Repo/Drive 링크(없으면 Enter):", "")
  };

} else if (kind === "develop") {
  folder = PATH.notes;
  indexArr = [INDEX.review];
  typeArr = ["develop"];
  cmdsArr = [];
  authors = [q(ME)];
  title = withPrefix("DEV - ", title);

  tags = ["develop","theory", ...extraTags];
  applyTaggingNeeded();

} else if (kind === "share") {
  folder = PATH.archive;
  indexArr = [INDEX.waypoint];
  typeArr = ["basic"];
  cmdsArr = [];
  authors = [q(ME)];
  title = withPrefix("SHARE - ", title);

  tags = ["share","output", ...extraTags];
  applyTaggingNeeded();
}

// ===== Move file =====
await renameAndMove(title, folder);

// ===== Frontmatter =====
let fm = [];
fm.push("---");
fm.push(`tags:${yamlList(tags, 2)}`);
fm.push(`aliases:${yamlList(aliases, 2)}`);
fm.push(`index:${yamlList(indexArr.map(x => q(wikilink(x))), 2)}`);
fm.push(`type:${yamlList(typeArr, 2)}`);
fm.push(`title: ${q(title)}`);
fm.push(`created: ${NOW_DATE}`);
fm.push(`cover_url: ${q(cover_url)}`);
fm.push(`updated: ${NOW_DT}`);
fm.push(`my_rate: ${q(my_rate)}`);
fm.push(`authors:${yamlList(authors, 2)}`);
fm.push(`CMDS:${yamlList(cmdsArr, 2)}`);
fm.push(`started: ${q(started)}`);
fm.push(`status:${yamlList([q(wikilink(statusOne))], 2)}`);
fm.push(`group:${yamlList([groupOne], 2)}`);
fm.push(`publishDate: ${q(publishDate)}`);
fm.push(`start_read_date: ${q(start_read_date)}`);
fm.push(`finish_read_date: ${q(finish_read_date)}`);
fm.push("---");

// ===== Body =====
let body = `\n# ${title}\n`;

if (kind === "connect_lecture") {
  body += `\n## Meta\n- Course: ${META_LECTURE.course}\n- Session: ${META_LECTURE.session}\n- Instructor: ${META_LECTURE.instructor}\n`;
  body += `\n## Outline\n- \n\n## Notes\n- \n\n## Questions\n- \n\n## 개념 정리 필요\n- [[ ]] \n`;

} else if (kind === "webclip") {
  body += `\n## Source\n- URL: ${META_WEB.url}\n- Keep: ${META_WEB.keep}\n- Area: ${META_WEB.area}\n`;
  body += `\n## Snapshot\n- What it is:\n- Why clipped:\n`;
  body += `\n## Excerpts\n> \n\n## Next\n- [ ] 필요하면 Concept으로 발전\n`;

} else if (kind === "reference") {
  body += `\n## Source\n- URL: ${META_REF.url}\n- Kind: ${META_REF.refKind}\n- Area: ${META_REF.area}\n`;
  body += `\n## Summary (원문 기반)\n- \n\n## Quotes\n> \n\n## Next\n- [ ] Concept으로 발전\n`;

} else if (kind === "people") {
  body += `\n## Snapshot\n- Role: ${META_PPL.role}\n- Organization: ${META_PPL.organization}\n\n`;
  body += `## Key points\n- \n\n## Links\n- \n`;

} else if (kind === "project") {
  body += `\n## Goal\n- ${META_PRJ.goal}\n`;
  body += `\n## Deadline\n- ${META_PRJ.deadline}\n`;
  body += `\n## Repo/Drive\n- ${META_PRJ.repo}\n`;
  body += `\n## Requirements\n- \n\n## Constraints\n- \n\n## Plan\n- Milestone 1:\n- Milestone 2:\n- Milestone 3:\n`;
  body += `\n## Log\n- ${NOW_DATE} - \n`;
  body += `\n## Decisions\n- \n`;
  body += `\n## References\n- [[ ]] \n`;

} else if (kind === "develop") {
  body += `\n## Definitions\n- \n\n## Key results / Rules\n- \n\n## Examples\n- \n\n## Pitfalls\n- \n\n## References\n- [[ ]] \n`;

} else if (kind === "share") {
  body += `\n## Audience\n- \n\n## Outline\n- \n\n## Draft\n- \n\n## Sources\n- [[ ]] \n`;

} else {
  body += `\n## Notes\n- \n\n## Next\n- [ ] \n`;
}

tR += fm.join("\n") + body;
}
%>

