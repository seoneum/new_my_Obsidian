<%*
/**
 * MASTER ROUTER (Aligned to your vault structure)
 * Decisions applied:
 * - Lecture notes => 200. CMDS/201. Connect
 * - Project (robot/contest/build) => 200. CMDS/280. Project
 * - People => 400. Reference/490. People_Reference/{491..494}
 * - Web clips => Inbox(Web_Clipper) OR Reference (one question)
 * - 300. I don't know => not used by router (legacy box)
 *
 * Properties schema (yours):
 * tags, aliases, index[], type[], title, created, cover_url, updated,
 * my_rate, authors, CMDS[], started, status[], group[], publishDate,
 * start_read_date, finish_read_date
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
  const labels = ["SE","EE","Phil","Math","General","Japanese","Robotics"];
  const values = ["SE","EE","Phil","Math","General","Japanese","Robotics"];
  return (await tp.system.suggester(labels, values)) ?? def;
}
async function renameAndMove(newTitle, folder) {
  try { await tp.file.rename(newTitle); } catch(e) {}
  if (folder) {
    try { await tp.file.move(`${folder}/${newTitle}`); } catch(e) {}
  }
}

// ===== Paths (your screenshot) =====
const PATH = {
  // Inbox
  inbox_any: "100. Inbox/101. 🚨Anything",
  inbox_daily: "100. Inbox/102. ✅ Daily_Note",
  inbox_software: "100. Inbox/110. Software",
  inbox_software_git: "100. Inbox/110. Software/111. Git",
  inbox_software_linux: "100. Inbox/110. Software/112. Linux",
  inbox_engineering: "100. Inbox/120. Engineering",
  inbox_philosophy: "100. Inbox/130. Philosophy",
  inbox_phil_uni: "100. Inbox/130. Philosophy/131. University_Lecture",
  inbox_phil_thesis: "100. Inbox/130. Philosophy/132. Philosophy_Thesis",
  inbox_phil_book: "100. Inbox/130. Philosophy/133. Book",
  inbox_phil_internet: "100. Inbox/130. Philosophy/134. Internet&Others",
  inbox_phil_theory: "100. Inbox/130. Philosophy/135. Theory",
  inbox_webclipper: "100. Inbox/140. Web_Clipper",

  // CMDS
  connect: "200. CMDS/201. Connect",
  merge: "200. CMDS/220. Merge",
  develop: "200. CMDS/240. Develop",
  share: "200. CMDS/260. Share",
  project: "200. CMDS/280. Project",        // ✅ your decision

  // Reference
  ref_any: "400. Reference/400. Anything_Reference",
  ref_software: "400. Reference/410. Software_Reference",
  ref_engineering: "400. Reference/420. Engineering_Reference",
  ref_philosophy: "400. Reference/430. Philosophy_Reference",

  // People (✅ your decision: split)
  people_acq: "400. Reference/490. People_Reference/491. Acquaintance",
  people_eng: "400. Reference/490. People_Reference/492. Engineering",
  people_phil:"400. Reference/490. People_Reference/493. Philosophy",
  people_unk: "400. Reference/490. People_Reference/494. Unknown",
};

// ===== Index links (edit if your vault names differ) =====
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
};

// ===== Tagging mode (your #2) =====
const taggingMode = await tp.system.suggester(
  ["기본 태그만(나중에 태깅)", "지금 추가 태그 입력"],
  ["later","now"]
);
let extraTags = [];
if (taggingMode === "now") {
  const raw = await tp.system.prompt("추가 tags (쉼표):", "");
  extraTags = (raw ?? "").split(",").map(s => cleanTag(s).trim()).filter(Boolean);
}

// ===== Choose kind =====
const kind = await tp.system.suggester(
  [
    "INBOX: 아무거나 빠른 메모(내 글)",
    "DAILY: 데일리 노트(내 글)",
    "CONNECT: 강의 필기(받아쓰기/내 의견 없음)",
    "WEB CLIP: 웹 클립(임시 or 레퍼런스 분기)",
    "REFERENCE: 논문/책/문서(레퍼런스 저장)",
    "PEOPLE: 인물 노트(내 정리)",
    "PROJECT: 로봇/대회/제작 프로젝트(내 글)",
    "MERGE: 내 지식(파인만)",
    "DEVELOP: 이론 정리/치트시트",
    "SHARE: 산출물"
  ],
  ["inbox","daily","connect_lecture","webclip","reference","people","project","merge","develop","share"]
);

// ===== Title =====
let title = (await tp.system.prompt("제목(title):", tp.file.title))?.trim() || tp.file.title;

// ===== Common fields =====
let tags = [];
let aliases = [];
let indexArr = [];
let typeArr = [];       // single role (1-item array)
let authors = [];       // only when my writing
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
    groupOne = "SE";
  } else if (area === "engineering") {
    folder = PATH.inbox_engineering;
    indexArr = [INDEX.waypoint];
    groupOne = "EE";
  } else if (area === "philosophy") {
    const sub = await tp.system.suggester(
      ["General", "University_Lecture", "Thesis", "Book", "Internet&Others", "Theory"],
      ["general","uni","thesis","book","internet","theory"]
    );
    folder =
      sub === "uni" ? PATH.inbox_phil_uni :
      sub === "thesis" ? PATH.inbox_phil_thesis :
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

} else if (kind === "daily") {
  folder = PATH.inbox_daily;
  indexArr = [INDEX.daily];
  typeArr = ["daily"];
  cmdsArr = [];
  authors = [q(ME)];
  title = withPrefix("D - ", title);

  tags = ["daily", ...extraTags];
  applyTaggingNeeded();

} else if (kind === "connect_lecture") {
  folder = PATH.connect;
  indexArr = [INDEX.lecture];
  typeArr = ["lecture"];
  cmdsArr = ["Connect"];
  authors = []; // 받아쓰기

  const domain = await tp.system.suggester(
    ["Software", "Engineering", "Philosophy", "General"],
    ["SE","EE","Phil","General"]
  );
  groupOne = domain;

  const course = await tp.system.prompt("과목/강의명(없으면 Enter):", "");
  const session = await tp.system.prompt("회차/주차/날짜:", NOW_DATE);
  const instructor = await tp.system.prompt("교수/강사(없으면 Enter):", "");
  const source_url = await tp.system.prompt("강의 URL(없으면 Enter):", "");

  title = withPrefix("L - ", title);

  tags = ["lecture", `lecture/${domain}`, ...extraTags];
  applyTaggingNeeded();

  var META_LECTURE = { course, session, instructor, source_url };

} else if (kind === "webclip") {
  const keep = await tp.system.suggester(
    ["임시 클립(나중에 정리/삭제) → Inbox/Web_Clipper", "보관할 가치 있음 → Reference"],
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
    area === "software" ? "SE" :
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
    area === "software" ? "SE" :
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
    ["Robotics","EE","SE","General"]
  );
  groupOne = domain;

  tags = ["project", "build", ...extraTags];
  applyTaggingNeeded();

  var META_PRJ = {
    goal: await tp.system.prompt("목표(한 줄):", ""),
    deadline: await tp.system.prompt("대회/마감일(없으면 Enter):", ""),
    repo: await tp.system.prompt("Repo/Drive 링크(없으면 Enter):", "")
  };

} else if (kind === "merge") {
  folder = PATH.merge;
  indexArr = [INDEX.waypoint];
  typeArr = ["merge"];
  cmdsArr = ["Merge"];
  authors = [q(ME)];
  title = withPrefix("M - ", title);
  statusOne = "[[🌿Sapling]]";

  tags = ["merge","feynman","zettel", ...extraTags];
  applyTaggingNeeded();

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

if (kind === "daily") {
  body += `\n## Top 3\n- [ ] \n- [ ] \n- [ ] \n`;
  body += `\n## Log\n- \n\n## Study\n- \n\n## Review\n- \n`;

} else if (kind === "connect_lecture") {
  body += `\n## Meta\n- Course: ${META_LECTURE.course}\n- Session: ${META_LECTURE.session}\n- Instructor: ${META_LECTURE.instructor}\n- URL: ${META_LECTURE.source_url}\n`;
  body += `\n## Outline\n- \n\n## Raw Notes\n- \n\n## Questions\n- \n\n## Merge Candidates\n- [[ ]] \n`;

} else if (kind === "webclip") {
  body += `\n## Source\n- URL: ${META_WEB.url}\n- Keep: ${META_WEB.keep}\n- Area: ${META_WEB.area}\n`;
  body += `\n## Snapshot\n- What it is:\n- Why clipped:\n`;
  body += `\n## Excerpts\n> \n\n## Next\n- [ ] 필요하면 Merge로 발전\n`;

} else if (kind === "reference") {
  body += `\n## Source\n- URL: ${META_REF.url}\n- Kind: ${META_REF.refKind}\n- Area: ${META_REF.area}\n`;
  body += `\n## Summary (원문 기반)\n- \n\n## Quotes\n> \n\n## Next\n- [ ] Merge로 발전\n`;

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
  body += `\n## References (link)\n- [[ ]] \n`;
  body += `\n## Merge notes used\n- [[ ]] \n`;

} else if (kind === "merge") {
  body += `\n## Feynman Step 1) Explain (12살에게)\n- \n`;
  body += `\n## Step 2) Gaps\n- \n`;
  body += `\n## Step 3) Repair (근거 링크)\n- Source: [[ ]] \n`;
  body += `\n## Step 4) Teach-back\n- 3문장:\n- 1문장:\n`;
  body += `\n## Examples\n- \n\n## Flashcards\n- Q:: A\n`;

} else if (kind === "develop") {
  body += `\n## Definitions\n- \n\n## Key results / Rules\n- \n\n## Examples\n- \n\n## Pitfalls\n- \n\n## References\n- [[ ]] \n`;

} else if (kind === "share") {
  body += `\n## Audience\n- \n\n## Outline\n- \n\n## Draft\n- \n\n## Sources\n- [[ ]] \n`;

} else {
  body += `\n## Notes\n- \n\n## Next\n- [ ] \n`;
}

tR += fm.join("\n") + body;
%>