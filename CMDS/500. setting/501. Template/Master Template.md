<%*
/**
 * MASTER ROUTER - CMDS Vault v3.0
 * 
 * 노트 타입:
 * - 일상: DAILY, MEMO
 * - 학습: LECTURE, CONCEPT, PROBLEM
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
  inbox_any: "CMDS/100. Inbox/101. 🚨Anything",
  inbox_daily: "CMDS/100. Inbox/102. 📝Daily_Note",
  inbox_excalidraw: "CMDS/100. Inbox/103. 🖌️Excalidraw",
  inbox_software: "CMDS/100. Inbox/110. Software",
  inbox_software_git: "CMDS/100. Inbox/110. Software/111. Git",
  inbox_software_linux: "CMDS/100. Inbox/110. Software/112. Linux",
  inbox_engineering: "CMDS/100. Inbox/120. Engineering",
  inbox_philosophy: "CMDS/100. Inbox/130. Philosophy",
  inbox_phil_book: "CMDS/100. Inbox/130. Philosophy/133. Book",
  inbox_phil_internet: "CMDS/100. Inbox/130. Philosophy/134. Internet&Others",
  inbox_phil_theory: "CMDS/100. Inbox/130. Philosophy/135. Theory",
  inbox_webclipper: "CMDS/100. Inbox/140. Web_Clipper",

  // CMDS
  connect: "CMDS/200. CMDS/201. Connect",
  merge: "CMDS/200. CMDS/220. Merge",
  merge_journal: "CMDS/200. CMDS/220. Merge/221. Journaling",
  merge_fc: "CMDS/200. CMDS/220. Merge/222. FlashCard",
  merge_concept: "CMDS/200. CMDS/220. Merge/223. Concept",
  merge_problem: "CMDS/200. CMDS/220. Merge/224. Problem",
  develop: "CMDS/200. CMDS/240. Develop",
  share: "CMDS/200. CMDS/260. Share",
  project: "CMDS/200. CMDS/280. Project",

  // Thinking
  thinking: "CMDS/300. Thinking",

  // Reference
  ref_any: "CMDS/400. Reference/401. Anything_Reference",
  ref_software: "CMDS/400. Reference/410. Software_Reference",
  ref_engineering: "CMDS/400. Reference/420. Engineering_Reference",
  ref_philosophy: "CMDS/400. Reference/430. Philosophy_Reference",
  ref_meeting: "CMDS/400. Reference/450. Meeting/26-1",

  // People
  people_acq: "CMDS/400. Reference/490. People_Reference/491. Acquaintance",
  people_eng: "CMDS/400. Reference/490. People_Reference/492. Engineering",
  people_phil:"CMDS/400. Reference/490. People_Reference/493. Philosophy",
  people_unk: "CMDS/400. Reference/490. People_Reference/494. Unknown",
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
    null, "connect_lecture", "concept", "problem",
    null, "reference", "webclip", "develop",
    null, "project", "meeting",
    null, "question", "people", "share",
    null, "fc_morning", "fc_evening", "weekly"
  ]
);

// ===== Redirect to specific templates =====
if (kind === "daily") {
  tR += await tp.file.include("[[Daily_Template]]");
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
let folder = PATH.inbox_any;

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
  const area = await tp.system.suggester(
    ["Anything", "Software", "Engineering", "Philosophy"],
    ["any","software","engineering","philosophy"]
  );

  if (area === "software") {
    const sub = await tp.system.suggester(["General", "Git", "Linux"], ["general","git","linux"]);
    folder = sub === "git" ? PATH.inbox_software_git : sub === "linux" ? PATH.inbox_software_linux : PATH.inbox_software;
    indexArr = [INDEX.software];
    groupOne = "CS";
  } else if (area === "engineering") {
    folder = PATH.inbox_engineering;
    indexArr = [INDEX.waypoint];
    groupOne = "EE";
  } else if (area === "philosophy") {
    const sub = await tp.system.suggester(
      ["General", "Book", "Internet&Others", "Theory"],
      ["general","book","internet","theory"]
    );
    folder =
      sub === "book" ? PATH.inbox_phil_book :
      sub === "internet" ? PATH.inbox_phil_internet :
      sub === "theory" ? PATH.inbox_phil_theory :
      PATH.inbox_philosophy;
    indexArr = [INDEX.waypoint];
    groupOne = "Phil";
  } else {
    folder = PATH.inbox_any;
    indexArr = [INDEX.waypoint];
    groupOne = "General";
  }

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
      "26-1-Phil-언어철학",
      "26-1-Phil-존재론과형이상학",
      "26-1-Phil-서양현대철학사",
      "26-1-Math-공업수학1",
      "26-1-Math-일반수학2",
      "26-1-EE-전자기학1",
      "other"
    ]
  ) || "other";

  let courseName = "";
  let courseFolder = PATH.connect;
  
  if (course === "other") {
    courseName = await tp.system.prompt("과목명:", "");
    const domain = await tp.system.suggester(
      ["CS", "EE", "Phil", "Math", "Robotics", "General"],
      ["CS","EE","Phil","Math","Robotics","General"]
    );
    groupOne = domain;
  } else {
    courseFolder = `CMDS/200. CMDS/201. Connect/26-1/${course}`;
    courseName = course.split("-").pop();
    // 자동 group 결정
    if (course.includes("Phil")) groupOne = "Phil";
    else if (course.includes("Math")) groupOne = "Math";
    else if (course.includes("EE")) groupOne = "EE";
  }

  folder = courseFolder;
  indexArr = [INDEX.lecture];
  typeArr = ["lecture"];
  cmdsArr = ["Connect"];
  authors = [];

  const session = await tp.system.prompt("주차/회차:", NOW_DATE);
  const instructor = await tp.system.prompt("교수(없으면 Enter):", "");

  title = withPrefix("L - ", title);
  tags = ["lecture", `lecture/${groupOne}`, `course/${courseName}`, ...extraTags];
  applyTaggingNeeded();

  var META_LECTURE = { course: courseName, session, instructor, source_url: "" };

} else if (kind === "webclip") {
  const keep = await tp.system.suggester(
    ["임시 클립 → Inbox", "보관할 가치 있음 → Reference"],
    ["inbox","reference"]
  );
  const url = await tp.system.prompt("URL:", "");
  const area = await tp.system.suggester(
    ["Anything", "Software", "Engineering", "Philosophy"],
    ["any","software","engineering","philosophy"]
  );

  if (keep === "inbox") {
    folder = PATH.inbox_webclipper;
    indexArr = [INDEX.webclips];
    typeArr = ["reference"];
    cmdsArr = ["Connect"];
    authors = [];
    title = withPrefix("W - ", title);
    tags = ["webclip", "inbox", ...extraTags];
    applyTaggingNeeded();
  } else {
    folder =
      area === "software" ? PATH.ref_software :
      area === "engineering" ? PATH.ref_engineering :
      area === "philosophy" ? PATH.ref_philosophy :
      PATH.ref_any;

    indexArr = [INDEX.webclips];
    typeArr = ["reference"];
    cmdsArr = ["Connect"];
    authors = [];
    title = withPrefix("R - ", title);
    tags = ["reference", "webclip", ...extraTags];
    applyTaggingNeeded();
  }

  groupOne =
    area === "software" ? "CS" :
    area === "engineering" ? "EE" :
    area === "philosophy" ? "Phil" : "General";

  var META_WEB = { url, keep, area };

} else if (kind === "reference") {
  const refKind = await tp.system.suggester(["Paper(논문)","Book(책)","Doc/Other(문서/기타)"], ["paper","book","doc"]);
  const area = await tp.system.suggester(["Anything","Software","Engineering","Philosophy"], ["any","software","engineering","philosophy"]);
  const url = await tp.system.prompt("URL(없으면 Enter):", "");
  publishDate = await tp.system.prompt("publishDate(없으면 Enter):", "");

  folder =
    area === "software" ? PATH.ref_software :
    area === "engineering" ? PATH.ref_engineering :
    area === "philosophy" ? PATH.ref_philosophy :
    PATH.ref_any;

  indexArr = [
    refKind === "paper" ? INDEX.research :
    refKind === "book" ? INDEX.books :
    INDEX.webclips
  ];

  typeArr = ["reference"];
  cmdsArr = ["Connect"];
  authors = [];
  title = withPrefix("R - ", title);
  tags = ["reference", refKind, ...extraTags];
  applyTaggingNeeded();

  groupOne =
    area === "software" ? "CS" :
    area === "engineering" ? "EE" :
    area === "philosophy" ? "Phil" : "General";

  var META_REF = { refKind, area, url };

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
  folder = PATH.project;
  indexArr = [INDEX.waypoint];
  typeArr = ["project"];
  cmdsArr = ["Develop"];
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
  folder = PATH.develop;
  indexArr = [INDEX.review];
  typeArr = ["develop"];
  cmdsArr = ["Develop"];
  authors = [q(ME)];
  title = withPrefix("DEV - ", title);

  tags = ["develop","theory", ...extraTags];
  applyTaggingNeeded();

} else if (kind === "share") {
  folder = PATH.share;
  indexArr = [INDEX.waypoint];
  typeArr = ["basic"];
  cmdsArr = ["Share"];
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

