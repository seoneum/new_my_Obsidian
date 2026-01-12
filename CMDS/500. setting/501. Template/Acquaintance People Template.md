---
category: "[[Template]]"
---
<%*
const ME = '[[김선음]]';
const NOW_DATE = tp.date.now("YYYY-MM-DD");
const NOW_DT = tp.date.now("YYYY-MM-DDTHH:mm:ss");
const TARGET_FOLDER = "400. Reference/440. People/441. Acquaintance";

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

let name = await tp.system.prompt("이름:", tp.file.title);
name = (name ?? "").trim() || tp.file.title;

const nametag = slugNoSpace(name);

const group = await tp.system.suggester(["General","SE","EE","Phil","Math"], ["General","SE","EE","Phil","Math"]);
const statusOne = await tp.system.suggester(
  ["🌱Seed","🌿Sapling","🌲Evergreen","🍂Archive","🚜In Progress"],
  ["[[🌱Seed]]","[[🌿Sapling]]","[[🌲Evergreen]]","[[🍂Archive]]","[[🚜In Progress]]"]
) ?? "[[🌿Sapling]]";

const mobile = await tp.system.prompt("휴대폰(없으면 Enter):", "");
const email = await tp.system.prompt("이메일(없으면 Enter):", "");
const organization = await tp.system.prompt("소속/조직(없으면 Enter):", "");
const howMet = await tp.system.prompt("어떻게 알게 됐는지(짧게):", "");

let tags = ["people", `people/${nametag}`, "people/acquaintance", ...extraTags];
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
+ `status:\n  - ${q(statusOne)}\n`
+ `group:\n  - ${group}\n`
+ `publishDate:\n`
+ `start_read_date:\n`
+ `finish_read_date:\n`
+ `---\n\n`
+ `# ${name}\n\n`
+ `## 연락처\n- Mobile: ${mobile}\n- Email: ${email}\n- Organization: ${organization}\n\n`
+ `## 관계 메모\n- How we met: ${howMet}\n- 최근 이슈/관심사:\n- 다음에 물어볼 것:\n\n`
+ `## 기록(Log)\n- ${NOW_DATE} - \n`;
%>
