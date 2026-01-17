<%*
const ME = '[[김선음]]';
const NOW_DATE = tp.date.now("YYYY-MM-DD");
const NOW_DT = tp.date.now("YYYY-MM-DDTHH:mm:ss");
const TARGET_FOLDER = "CMDS/400. Reference/490. People_Reference/493. Philosophy";

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

let name = await tp.system.prompt("인물 이름:", tp.file.title);
name = (name ?? "").trim() || tp.file.title;

const nametag = slugNoSpace(name);
const school = await tp.system.prompt("사조/분야(예: 분석철학/현상학/윤리학):", "");
const thesis = await tp.system.prompt("핵심 주장(한 줄):", "");

let tags = ["people", `people/${nametag}`, "people/philosophy", ...extraTags];
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
+ `status:\n  - "[[🌿Sapling]]"\n`
+ `group:\n  - Phil\n`
+ `publishDate:\n`
+ `start_read_date:\n`
+ `finish_read_date:\n`
+ `---\n\n`
+ `# ${name}\n\n`
+ `## Snapshot\n- School/Area: ${school}\n- Core thesis: ${thesis}\n\n`
+ `## 주요 논증 구조(내가 이해한 방식)\n- Premises:\n- Conclusion:\n- Hidden assumptions:\n\n`
+ `## 핵심 개념 링크\n- [[ ]] [[ ]]\n\n`
+ `## 비판/반례/대안 관점\n- \n\n`
+ `## Works / Sources\n- \n`;
%>
