---
migrated_from: CMDS/500. setting/501. Template/Unknown People Template.md
updated: 2026-01-18T16:42:53
cmds: connect
---
<%*
const ME = '[[김선음]]';
const NOW_DATE = tp.date.now("YYYY-MM-DD");
const NOW_DT = tp.date.now("YYYY-MM-DDTHH:mm:ss");
const TARGET_FOLDER = "⚙️ Meta/People/Unknown";

const cleanTag = (s) => String(s ?? "").trim().replace(/^#/, "");
const slugNoSpace = (s) => String(s ?? "").trim().replace(/\s+/g,"");
const q = (s) => `"${String(s ?? "").replaceAll(`"`, `\\"`)}"`;

const taggingMode = await tp.system.suggester(
  ["기본 태그만(나중에 태깅)", "지금 추가 태그 입력"],
  ["later", "now"]
);
let extraTags = [];
if (taggingMode === "now") {
  const raw = await tp.system.prompt("추가 tags (쉼표):", "");
  extraTags = (raw ?? "").split(",").map(s => cleanTag(s)).map(s=>s.trim()).filter(Boolean);
}

let name = await tp.system.prompt("이름(불명확하면 'Unknown - ...'로):", tp.file.title);
name = (name ?? "").trim() || tp.file.title;

const nametag = slugNoSpace(name);
const context = await tp.system.prompt("어디서 봤는지/맥락:", "");
const clue = await tp.system.prompt("현재 알고 있는 단서(키워드):", "");

let tags = ["people", `people/${nametag}`, "people/unknown", ...extraTags];
if (taggingMode === "later") tags.push("tagging/needed");

try { await tp.file.rename(name); } catch(e) {}
try { await tp.file.move(`${TARGET_FOLDER}/${name}`); } catch(e) {}

tR += `---\n`
+ `tags:\n${tags.map(t=>`  - ${t}`).join("\n")}\n`
+ `aliases: []\n`
+ `index:\n  - "[[🏷 People]]"\n`
+ `type:\n  - basic\n`
+ `title: ${q(name)}\n`
+ `created: ${NOW_DATE}\n`
+ `cover_url:\n`
+ `updated: ${NOW_DT}\n`
+ `my_rate:\n`
+ `authors:\n  - "${ME}"\n`
+ `CMDS: []\n`
+ `started: ${NOW_DATE}\n`
+ `status:\n  - "[[🌱Seed]]"\n`
+ `group:\n  - General\n`
+ `publishDate:\n`
+ `start_read_date:\n`
+ `finish_read_date:\n`
+ `---\n\n`
+ `# ${name}\n\n`
+ `## Context\n- Where/How: ${context}\n- Clues: ${clue}\n\n`
+ `## What I need to find out\n- [ ] full name?\n- [ ] field/role?\n- [ ] key works?\n- [ ] reliable sources?\n\n`
+ `## Notes\n- \n`;
%>
