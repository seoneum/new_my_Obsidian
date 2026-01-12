<%*
/**
 * MASTER ROUTER - Core v2 (author always + emoji status)
 * Root: CMDS/
 */

const ROOT = "CMDS";
const P = (sub) => `${ROOT}/${sub}`;

// === adjust if needed ===
const ANY_REFERENCE = P("400. Reference/400. Anything_Reference");
// ========================

const PATH = {
  // Inbox
  inbox_any: P("100. Inbox/101. 🚨Anything"),
  inbox_daily: P("100. Inbox/102. 📝Daily_Note"),
  inbox_software: P("100. Inbox/110. Software"),
  inbox_software_git: P("100. Inbox/110. Software/111. Git"),
  inbox_software_linux: P("100. Inbox/110. Software/112. Linux"),
  inbox_engineering: P("100. Inbox/120. Engineering"),
  inbox_philosophy: P("100. Inbox/130. Philosophy"),
  inbox_phil_uni: P("100. Inbox/130. Philosophy/131. University_Lecture"),
  inbox_phil_thesis: P("100. Inbox/130. Philosophy/132. Philosophy_Thesis"),
  inbox_phil_book: P("100. Inbox/130. Philosophy/133. Book"),
  inbox_phil_internet: P("100. Inbox/130. Philosophy/134. Internet&Others"),
  inbox_phil_theory: P("100. Inbox/130. Philosophy/135. Theory"),
  inbox_webclipper: P("100. Inbox/140. Web_Clipper"),

  // CMDS
  connect: P("200. CMDS/201. Connect"),
  merge: P("200. CMDS/220. Merge"),
  develop: P("200. CMDS/240. Develop"),
  share: P("200. CMDS/260. Share"),
  project: P("200. CMDS/280. Project"),

  // Reference
  ref_any: P("400. Reference/401. Anything_Reference"),
  ref_software: P("400. Reference/410. Software_Reference"),
  ref_engineering: P("400. Reference/420. Engineering_Reference"),
  ref_philosophy: P("400. Reference/430. Philosophy_Reference"),

  // People
  people_acq: P("400. Reference/490. People_Reference/491. Acquaintance"),
  people_eng: P("400. Reference/490. People_Reference/492. Engineering"),
  people_phil: P("400. Reference/490. People_Reference/493. Philosophy"),
  people_unk: P("400. Reference/490. People_Reference/494. Unknown"),
};

const ME = '[[김선음]]';
const NOW_DATE = tp.date.now("YYYY-MM-DD");
const NOW_DT = tp.date.now("YYYY-MM-DDTHH:mm:ss");

const q = (s) => `"${String(s ?? "").replaceAll(`"`, `\\"`)}"`;
const cleanTag = (s) => String(s ?? "").trim().replace(/^#/, "");
const slugNoSpace = (s) => String(s ?? "").trim().replace(/\s+/g,"");

function yamlList(key, arr) {
  const a = (arr ?? []).filter(Boolean);
  if (a.length === 0) return `${key}: []`;
  return `${key}:\n` + a.map(v => `  - ${v}`).join("\n");
}
function yamlVal(key, val) {
  if (val === undefined || val === null) return "";
  const s = String(val).trim();
  if (!s) return "";
  // if already looks like wikilink or number-ish, keep as is? we keep quoted for safety except wikilinks
  if (s.startsWith("[[") && s.endsWith("]]")) return `${key}: ${q(s)}`; // keep as string to render in properties
  return `${key}: ${q(s)}`;
}

async function pickStatus(def='[[🚜In Progress]]') {
  const labels = ["🌱Seed","🌿Sapling","🌲Evergreen","🍂Archive","🚜In Progress"];
  const values = ["[[🌱Seed]]","[[🌿Sapling]]","[[🌲Evergreen]]","[[🍂Archive]]","[[🚜In Progress]]"];
  return (await tp.system.suggester(labels, values)) ?? def;
}
async function pickGroup(def="General") {
  const labels = ["SLAM","AI","Robotics","EE","SE","Phil","Math","General"];
  const values = ["SLAM","AI","Robotics","EE","SE","Phil","Math","General"];
  return (await tp.system.suggester(labels, values)) ?? def;
}
async function renameAndMove(newTitle, folder) {
  try { await tp.file.rename(newTitle); } catch(e) {}
  if (folder) {
    try { await tp.file.move(`${folder}/${newTitle}`); } catch(e) {}
  }
}
function withPrefix(prefix, t) {
  const s = String(t ?? "").trim();
  if (!s) return s;
  if (s.startsWith(prefix)) return s;
  return `${prefix}${s}`;
}

// tagging mode (your choice #2)
const taggingMode = await tp.system.suggester(
  ["기본 태그만(나중에 태깅)", "지금 추가 태그 입력"],
  ["later","now"]
);
let extraTags = [];
if (taggingMode === "now") {
  const raw = await tp.system.prompt("추가 tags (쉼표):", "");
  extraTags = (raw ?? "").split(",").map(s => cleanTag(s).trim()).filter(Boolean);
}
const needTagging = taggingMode === "later";

// kind
const kind = await tp.system.suggester(
  [
    "INBOX",
    "DAILY",
    "LECTURE (Connect)",
    "WEB CLIP (임시 vs Reference)",
    "REFERENCE (paper/book/doc/web)",
    "PEOPLE (4분류)",
    "PROJECT (로봇/대회/제작)",
    "MERGE (Feynman)",
    "DEVELOP",
    "SHARE"
  ],
  ["inbox","daily","lecture","webclip","reference","people","project","merge","develop","share"]
);

let title = (await tp.system.prompt("제목:", tp.file.title))?.trim() || tp.file.title;

// Core fields (always)
let type = kind;
let created = NOW_DATE;
let updated = NOW_DT;
let author = ME;                 // ✅ always
let group = await pickGroup();
let status = await pickStatus();
let tags = [];
let aliases = [];

// Optional fields by type
let extra = {};
let folder = PATH.inbox_any;

// ---- routes ----
if (kind === "inbox") {
  const area = await tp.system.suggester(
    ["Anything","Software","Engineering","Philosophy"],
    ["any","software","engineering","philosophy"]
  );

  if (area === "software") {
    const sub = await tp.system.suggester(["General","Git","Linux"], ["general","git","linux"]);
    folder = sub === "git" ? PATH.inbox_software_git : sub === "linux" ? PATH.inbox_software_linux : PATH.inbox_software;
    group = "SE";
  } else if (area === "engineering") {
    folder = PATH.inbox_engineering; group = "EE";
  } else if (area === "philosophy") {
    const sub = await tp.system.suggester(
      ["General","University_Lecture","Thesis","Book","Internet&Others","Theory"],
      ["general","uni","thesis","book","internet","theory"]
    );
    folder =
      sub === "uni" ? PATH.inbox_phil_uni :
      sub === "thesis" ? PATH.inbox_phil_thesis :
      sub === "book" ? PATH.inbox_phil_book :
      sub === "internet" ? PATH.inbox_phil_internet :
      sub === "theory" ? PATH.inbox_phil_theory :
      PATH.inbox_philosophy;
    group = "Phil";
  } else {
    folder = PATH.inbox_any; group = "General";
  }

  type = "inbox";
  title = withPrefix("N - ", title);
  tags = ["inbox","note", ...extraTags];
  if (needTagging) tags.push("tagging/needed");

} else if (kind === "daily") {
  folder = PATH.inbox_daily;
  type = "daily";
  title = withPrefix("D - ", title);
  tags = ["daily", ...extraTags];

} else if (kind === "lecture") {
  folder = PATH.connect;
  type = "lecture";
  title = withPrefix("L - ", title);

  const domain = await tp.system.suggester(["SLAM","AI","Robotics","EE","SE","Phil","Math","General"], ["SLAM","AI","Robotics","EE","SE","Phil","Math","General"]);
  group = domain;
  status = '[[🚜In Progress]]';

  extra.course = await tp.system.prompt("과목/강의명(없으면 Enter):", "");
  extra.session = await tp.system.prompt("회차/주차/날짜:", NOW_DATE);
  extra.instructor = await tp.system.prompt("교수/강사(없으면 Enter):", "");
  extra.source_url = await tp.system.prompt("강의 URL(없으면 Enter):", "");

  tags = ["lecture", `lecture/${domain}`, ...extraTags];
  if (needTagging) tags.push("tagging/needed");

} else if (kind === "webclip") {
  const keep = await tp.system.suggester(
    ["임시(나중에 정리/삭제) → Inbox/Web_Clipper", "보관 가치 있음 → Reference"],
    ["inbox","reference"]
  );
  const area = await tp.system.suggester(["Anything","Software","Engineering","Philosophy"], ["any","software","engineering","philosophy"]);

  type = "webclip";
  status = '[[🌱Seed]]';
  extra.source_url = await tp.system.prompt("URL:", "");

  if (keep === "inbox") {
    folder = PATH.inbox_webclipper;
    title = withPrefix("W - ", title);
    tags = ["webclip","inbox", ...extraTags];
  } else {
    folder =
      area === "software" ? PATH.ref_software :
      area === "engineering" ? PATH.ref_engineering :
      area === "philosophy" ? PATH.ref_philosophy :
      PATH.ref_any;
    title = withPrefix("R - ", title);
    tags = ["webclip","reference", ...extraTags];
  }

  group =
    area === "software" ? "SE" :
    area === "engineering" ? "EE" :
    area === "philosophy" ? "Phil" : "General";

  if (needTagging) tags.push("tagging/needed");

} else if (kind === "reference") {
  const source_kind = await tp.system.suggester(["paper","book","doc","web"], ["paper","book","doc","web"]);
  const area = await tp.system.suggester(["Anything","Software","Engineering","Philosophy"], ["any","software","engineering","philosophy"]);

  folder =
    area === "software" ? PATH.ref_software :
    area === "engineering" ? PATH.ref_engineering :
    area === "philosophy" ? PATH.ref_philosophy :
    PATH.ref_any;

  type = "reference";
  status = '[[🌱Seed]]';
  title = withPrefix("R - ", title);

  extra.source_kind = source_kind;
  extra.source_url = await tp.system.prompt("URL(없으면 Enter):", "");
  extra.publish_date = await tp.system.prompt("publish_date(없으면 Enter):", "");
  const sa = await tp.system.prompt("source_authors(쉼표, 없으면 Enter):", "");
  if (sa?.trim()) extra.source_authors = sa;

  tags = ["reference", source_kind, ...extraTags];
  if (needTagging) tags.push("tagging/needed");

  group =
    area === "software" ? "SE" :
    area === "engineering" ? "EE" :
    area === "philosophy" ? "Phil" : "General";

} else if (kind === "people") {
  const pk = await tp.system.suggester(
    ["acquaintance(지인)","engineering(공학)","philosophy(철학)","unknown(불명)"],
    ["acquaintance","engineering","philosophy","unknown"]
  );
  folder =
    pk === "acquaintance" ? PATH.people_acq :
    pk === "engineering" ? PATH.people_eng :
    pk === "philosophy" ? PATH.people_phil :
    PATH.people_unk;

  type = "people";
  title = withPrefix("PPL - ", title);

  const baseName = title.replace(/^PPL\s-\s*/,"");
  const nametag = slugNoSpace(baseName);

  extra.people_kind = pk;
  extra.organization = await tp.system.prompt("소속/조직(없으면 Enter):", "");
  extra.role = await tp.system.prompt("한줄 설명(없으면 Enter):", "");
  if (pk === "acquaintance") {
    extra.mobile = await tp.system.prompt("휴대폰(없으면 Enter):", "");
    extra.email = await tp.system.prompt("이메일(없으면 Enter):", "");
  }

  tags = ["people", `people/${nametag}`, `people/${pk}`, ...extraTags];
  if (needTagging) tags.push("tagging/needed");

  group = pk === "engineering" ? "EE" : pk === "philosophy" ? "Phil" : "General";
  status = pk === "unknown" ? '[[🌱Seed]]' : '[[🌿Sapling]]';

} else if (kind === "project") {
  folder = PATH.project;
  type = "project";
  title = withPrefix("PRJ - ", title);

  group = await tp.system.suggester(["SLAM","AI","Robotics","EE","SE","General"], ["SLAM","AI","Robotics","EE","SE","General"]);
  status = '[[🚜In Progress]]';

  extra.goal = await tp.system.prompt("목표(한 줄):", "");
  extra.deadline = await tp.system.prompt("대회/마감일(없으면 Enter):", "");
  extra.repo = await tp.system.prompt("Repo/Drive 링크(없으면 Enter):", "");

  tags = ["project","build", ...extraTags];
  if (needTagging) tags.push("tagging/needed");

} else if (kind === "merge") {
  folder = PATH.merge;
  type = "merge";
  title = withPrefix("M - ", title);
  status = '[[🌿Sapling]]';

  tags = ["merge","feynman", ...extraTags];
  if (needTagging) tags.push("tagging/needed");

} else if (kind === "develop") {
  folder = PATH.develop;
  type = "develop";
  title = withPrefix("DEV - ", title);
  status = '[[🚜In Progress]]';

  tags = ["develop","theory", ...extraTags];
  if (needTagging) tags.push("tagging/needed");

} else if (kind === "share") {
  folder = PATH.share;
  type = "share";
  title = withPrefix("SHARE - ", title);
  status = '[[🚜In Progress]]';

  tags = ["share","output", ...extraTags];
  if (needTagging) tags.push("tagging/needed");
}

// Move
await renameAndMove(title, folder);

// Body
let body = `# ${title}\n`;

if (kind === "lecture") {
  body += `\n## Meta\n- Course: ${extra.course ?? ""}\n- Session: ${extra.session ?? ""}\n- Instructor: ${extra.instructor ?? ""}\n- URL: ${extra.source_url ?? ""}\n`;
  body += `\n## Outline\n- \n\n## Raw Notes\n- \n\n## Questions\n- \n\n## Merge Candidates\n- [[ ]] \n`;
  body += `\n## Priori Lecture\n- [[ ]] \n`;
} else if (kind === "project") {
  body += `\n## Goal\n- ${extra.goal ?? ""}\n\n## Deadline\n- ${extra.deadline ?? ""}\n\n## Repo\n- ${extra.repo ?? ""}\n`;
  body += `\n## Requirements\n- \n\n## Constraints\n- \n\n## Plan\n- \n\n## Log\n- ${NOW_DATE} - \n`;
} else if (kind === "merge") {
  body += `\n## Feynman Step 1) Explain\n- \n\n## Step 2) Gaps\n- \n\n## Step 3) Repair\n- Source: [[ ]] \n\n## Step 4) Teach-back\n- 3문장:\n- 1문장:\n`;
} else {
  body += `\n## Notes\n- \n\n## Next\n- [ ] \n`;
}

// YAML (Core v2 + optional extras)
let fm = [];
fm.push("---");
fm.push(yamlVal("type", type));
fm.push(yamlVal("title", title));
fm.push(yamlVal("created", created));
fm.push(yamlVal("updated", updated));
fm.push(yamlVal("author", author));
fm.push(yamlVal("group", group));
fm.push(yamlVal("status", status));
fm.push(yamlList("tags", tags));
fm.push(yamlList("aliases", aliases));

// extras (only when filled)
for (const [k,v] of Object.entries(extra)) {
  if (v !== undefined && v !== null && String(v).trim() !== "") fm.push(yamlVal(k, v));
}

fm.push("---");

tR += fm.join("\n") + "\n\n" + body;
%>
