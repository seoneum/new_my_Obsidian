---
category: "[[Template]]"
---
<%*
const ME = '[[김선음]]';
const NOW_DATE = tp.date.now("YYYY-MM-DD");
const NOW_DT = tp.date.now("YYYY-MM-DDTHH:mm:ss");

const group = await tp.system.suggester(["EE","Phil","SE","Math","General","Japanese","Robotics"], ["EE","Phil","SE","Math","General","Japanese","Robotics"]);
const title = (await tp.system.prompt("내 지식 노트 제목(개념/문제/원리):", tp.file.title))?.trim() || tp.file.title;

const taggingMode = await tp.system.suggester(["기본 태그만(나중에 태깅)", "지금 추가 태그 입력"], ["later","now"]);
let extraTags = [];
if (taggingMode === "now") {
  const raw = await tp.system.prompt("추가 tags(쉼표):", "");
  extraTags = (raw ?? "").split(",").map(s=>s.trim().replace(/^#/, "")).filter(Boolean);
}

let tags = ["merge", "feynman", "zettel", ...extraTags];
if (taggingMode === "later") tags.push("tagging/needed");

try { await tp.file.rename(title); } catch(e) {}
try { await tp.file.move(`10. CMDS Process/12. Merge/${group}/${title}`); } catch(e) {}

tR += `---\n`
+ `tags:\n${tags.map(t=>`  - ${t}`).join("\n")}\n`
+ `aliases: []\n`
+ `index:\n  - "[[🏷 Waypoint]]"\n`
+ `type:\n  - merge\n`
+ `title: "${title.replaceAll('"','\\"')}"\n`
+ `created: ${NOW_DATE}\n`
+ `cover_url:\n`
+ `updated: ${NOW_DT}\n`
+ `my_rate:\n`
+ `authors:\n  - "${ME}"\n`   // ★ 내 글
+ `CMDS:\n  - Merge\n`
+ `started: ${NOW_DATE}\n`
+ `status:\n  - "[[🌿Sapling]]"\n`
+ `group:\n  - ${group}\n`
+ `publishDate:\n`
+ `start_read_date:\n`
+ `finish_read_date:\n`
+ `---\n\n`
+ `# ${title}\n\n`
+ `## Feynman Step 1) Explain to a 12-year-old\n- (비유/쉬운 단어로 6~10문장)\n\n`
+ `## Step 2) Identify gaps (막힌 지점)\n- 용어 정의가 불명확한 부분:\n- 왜?가 설명 안 되는 부분:\n- 예시가 없는 부분:\n\n`
+ `## Step 3) Repair (다시 공부해서 메우기)\n- 필요한 원본 링크: [[ ]] \n- 추가로 볼 것:\n\n`
+ `## Step 4) Teach-back (더 짧고 명확하게)\n- 3문장 버전:\n- 1문장 버전:\n\n`
+ `## Misconceptions (자주 하는 착각)\n- \n\n`
+ `## Examples / Exercises\n- 예제 1:\n- 예제 2:\n\n`
+ `## Cross-links\n- Related: [[ ]] [[ ]]\n\n`
+ `## Flashcards\n- Q:: A\n`;
%>
