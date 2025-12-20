<%*
const NOW_DATE = tp.date.now("YYYY-MM-DD");
const NOW_DT = tp.date.now("YYYY-MM-DDTHH:mm:ss");

const refKind = await tp.system.suggester(["Paper","Book","Website"], ["paper","book","web"]);
const group = await tp.system.suggester(["EE","Phil","SE","Math","General","Japanese","Robotics"], ["EE","Phil","SE","Math","General","Japanese","Robotics"]);
const title = (await tp.system.prompt("제목:", tp.file.title))?.trim() || tp.file.title;
const url = await tp.system.prompt("URL(없으면 Enter):", "");

const taggingMode = await tp.system.suggester(["기본 태그만(나중에 태깅)", "지금 추가 태그 입력"], ["later","now"]);
let extraTags = [];
if (taggingMode === "now") {
  const raw = await tp.system.prompt("추가 tags(쉼표):", "");
  extraTags = (raw ?? "").split(",").map(s=>s.trim().replace(/^#/, "")).filter(Boolean);
}

let baseTag = refKind === "paper" ? "paper" : refKind === "book" ? "book" : "webclip";
let tags = ["reference", baseTag, ...extraTags];
if (taggingMode === "later") tags.push("tagging/needed");

const indexLink =
  refKind === "paper" ? '[[🏷 Research Notes]]' :
  refKind === "book" ? '[[🏷 Books]]' :
  '[[🏷 Web Clips]]';

const targetFolder =
  refKind === "paper" ? `80. References/82. Academic Sources` :
  refKind === "book" ? `20. Literature Notes` :
  `00. Inbox/07. Clippings`;

try { await tp.file.rename(title); } catch(e) {}
try { await tp.file.move(`${targetFolder}/${title}`); } catch(e) {}

tR += `---\n`
+ `tags:\n${tags.map(t=>`  - ${t}`).join("\n")}\n`
+ `aliases: []\n`
+ `index:\n  - "${indexLink}"\n`
+ `type:\n  - reference\n`
+ `title: "${title.replaceAll('"','\\"')}"\n`
+ `created: ${NOW_DATE}\n`
+ `cover_url:\n`
+ `updated: ${NOW_DT}\n`
+ `my_rate:\n`
+ `authors: []\n` // ★ 내 글 아님
+ `CMDS:\n  - Connect\n`
+ `started: ${NOW_DATE}\n`
+ `status:\n  - "[[🌱Seed]]"\n`
+ `group:\n  - ${group}\n`
+ `publishDate:\n`
+ `start_read_date:\n`
+ `finish_read_date:\n`
+ `---\n\n`
+ `# ${title}\n\n`
+ `## Source\n- URL: ${url}\n\n`
+ `## Quick Capture\n- What it is:\n- Why saved:\n\n`
+ `## Key Excerpts\n> \n\n`
+ `## Notes (내 의견은 여기 쓰지 말고, Merge에서 쓰기)\n- \n\n`
+ `## Next\n- [ ] Merge로 만들기\n`;
%>