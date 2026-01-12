<%*
const ROOT = "CMDS";

// 폴더 경로(리눅스 대소문자/이모지 정확히 일치해야 함)
const DAILY_FOLDER = ROOT + "/100. Inbox/102. ✅ Daily_Note";

const JOURNAL_FOLDER = ROOT + "/200. CMDS/220. Merge/221. Journaling - Daily";
const FLASH_FOLDER   = ROOT + "/200. CMDS/220. Merge/222. FlashCard - Daily";
const FEYN_FOLDER    = ROOT + "/200. CMDS/220. Merge/223. Feynman - Daily";

// 템플릿 이름(확장자 제외). 못 찾으면 fallback으로 생성됨
const TEMPLATE_JOURNAL_NAME = "Journal Template";
const TEMPLATE_FEYNMAN_NAME = "Feynman Template";

const today = tp.date.now("YYYY-MM-DD");
const yesterday = tp.date.now("YYYY-MM-DD", -1);
const nowDT = tp.date.now("YYYY-MM-DDTHH:mm:ss");

const dailyFileName = "D - " + today;

// preset 선택
const dayKind = await tp.system.suggester(
  ["학교 가는 날(수업)", "일하는 날", "쉬는 날"],
  ["school", "work", "rest"]
);

const preset =
  dayKind === "school" ? { label: "school", wake: "07:00", depart: "", note: "" } :
  dayKind === "work"   ? { label: "work", wake: "06:30", depart: "08:00 (8시 출발)", note: "9시 출근 기준" } :
                         { label: "rest", wake: "08:00", depart: "", note: "" };

const dayLabelKorean = (dayKind === "school") ? "학교" : (dayKind === "work") ? "일" : "휴식";

// ---------- utilities ----------
async function ensureFolder(path) {
  const parts = path.split("/").filter(Boolean);
  let cur = "";
  for (const part of parts) {
    cur = cur ? (cur + "/" + part) : part;
    if (!app.vault.getAbstractFileByPath(cur)) {
      try { await app.vault.createFolder(cur); } catch (e) {}
    }
  }
}
function exists(path) {
  return !!app.vault.getAbstractFileByPath(path);
}

// template find: exact name OR fuzzy search (contains string)
function findTemplateFile(name) {
  let f = tp.file.find_tfile(name);
  if (f) return f;

  const TEMPLATE_FOLDER = ROOT + "/500. setting/501. Template/";
  const files = app.vault.getMarkdownFiles().filter(x => x.path.startsWith(TEMPLATE_FOLDER));
  const lower = String(name).toLowerCase();
  const hit =
    files.find(x => x.basename.toLowerCase() === lower) ||
    files.find(x => x.basename.toLowerCase().includes(lower));
  return hit || null;
}

async function createFromTemplateOrFallback(templateName, fileName, folder, fallbackContentLines) {
  await ensureFolder(folder);
  const fullPath = folder + "/" + fileName + ".md";
  if (exists(fullPath)) return;

  const tfile = findTemplateFile(templateName);
  if (tfile) {
    try {
      await tp.file.create_new(tfile, fileName, false, folder);
      return;
    } catch (e) {}
  }
  await app.vault.create(fullPath, fallbackContentLines.join("\n"));
}

async function createPlain(fileName, folder, contentLines) {
  await ensureFolder(folder);
  const fullPath = folder + "/" + fileName + ".md";
  if (exists(fullPath)) return;
  await app.vault.create(fullPath, contentLines.join("\n"));
}

// ---------- Ensure daily note file is named & located ----------
await ensureFolder(DAILY_FOLDER);
try { if (tp.file.title !== dailyFileName) await tp.file.rename(dailyFileName); } catch (e) {}
try { await tp.file.move(DAILY_FOLDER + "/" + dailyFileName); } catch (e) {}

// ---------- Linked notes naming ----------
const journalName = "JRN - " + today;
const flashName   = "FC - " + today;
const feynName    = "FYN - " + today;

const LINK_J  = "[[" + journalName + "]]";
const LINK_FC = "[[" + flashName + "]]";
const LINK_FY = "[[" + feynName + "]]";

// ---------- Auto-create linked notes ----------
await createFromTemplateOrFallback(
  TEMPLATE_JOURNAL_NAME,
  journalName,
  JOURNAL_FOLDER,
  [
    "---",
    "type: journal",
    "title: " + journalName,
    "created: " + today,
    "updated: \"" + nowDT + "\"",
    "author: [[김선음]]",
    "group: General",
    "status: [[🚜In Progress]]",
    "tags:",
    "  - journaling",
    "  - daily",
    "aliases: []",
    "---",
    "",
    "# " + journalName
  ]
);

await createPlain(
  flashName,
  FLASH_FOLDER,
  [
    "---",
    "type: flashcards",
    "title: " + flashName,
    "created: " + today,
    "updated: \"" + nowDT + "\"",
    "author: [[김선음]]",
    "group: General",
    "status: [[🚜In Progress]]",
    "tags:",
    "  - flashcards",
    "  - daily",
    "aliases: []",
    "---",
    "",
    "# " + flashName,
    "",
    "## Cards",
    "- Q:: A"
  ]
);

await createFromTemplateOrFallback(
  TEMPLATE_FEYNMAN_NAME,
  feynName,
  FEYN_FOLDER,
  [
    "---",
    "type: merge",
    "title: " + feynName,
    "created: " + today,
    "updated: \"" + nowDT + "\"",
    "author: [[김선음]]",
    "group: General",
    "status: [[🌿Sapling]]",
    "tags:",
    "  - merge",
    "  - feynman",
    "  - daily",
    "aliases: []",
    "---",
    "",
    "# " + feynName
  ]
);

// ---------- Checklist per preset ----------
let checklist = [];
if (dayKind === "school") {
  checklist = [
    "## Morning Routine (학교)",
    "- [ ] 독서 40분 (기상 직후)",
    "- [ ] 계획표 20분 (체크리스트)",
    "  - [ ] 오늘 아침 책 읽은 것 기록(책/페이지/한 줄)",
    "  - [ ] 계획표 쓰기 완료",
    "  - [ ] 오늘 수업 목록",
    "    - [ ] 수업 1:",
    "    - [ ] 수업 2:",
    "    - [ ] 수업 3:",
    "  - [ ] 수업 끝나고 할 것(After class)",
    "    - [ ]",
    "    - [ ]",
    "",
    "## Evening Routine (공통)",
    "- [ ] 운동",
    "- [ ] 명상 + 저널링 → " + LINK_J,
    "- [ ] 플래시 카드(하루 정리) → " + LINK_FC,
    "- [ ] 파인만 노트(오늘 공부 설명) → " + LINK_FY
  ];
} else if (dayKind === "work") {
  checklist = [
    "## Morning Routine (일)",
    "- [ ] 씻기",
    "- [ ] 커피 마시면서 독서 40분",
    "- [ ] 계획표 20분 (체크리스트)",
    "  - [ ] 오늘 아침 책 읽은 것 기록(책/페이지/한 줄)",
    "  - [ ] 계획표 쓰기 완료",
    "- [ ] 8시 출발(9시 출근 기준)",
    "",
    "## Commute",
    "- [ ] 출근길 책 읽기/청취(가능하면)",
    "",
    "## Workday",
    "- [ ] 일 하면서 가능한 범위로 책 읽기(짧게라도)",
    "",
    "## After Work",
    "- [ ] 동아리방에서 공부 할 것 작성",
    "  - [ ] 공부 주제 1:",
    "  - [ ] 공부 주제 2:",
    "",
    "## Evening Routine (공통)",
    "- [ ] 운동",
    "- [ ] 명상 + 저널링 → " + LINK_J,
    "- [ ] 플래시 카드(하루 정리) → " + LINK_FC,
    "- [ ] 파인만 노트(오늘 공부 설명) → " + LINK_FY
  ];
} else {
  checklist = [
    "## Morning Routine (휴식)",
    "- [ ] 독서 40분",
    "- [ ] 계획표 20분",
    "",
    "## Why Rest?",
    "- [ ] 왜 쉬는지 한 줄",
    "- 이유:",
    "",
    "## Light Study",
    "- [ ] 간단한 책 읽기",
    "- [ ] 감상/요약 5~10줄 → " + LINK_J,
    "",
    "## Weekly Review",
    "- [ ] 플래시 카드로 이번주 복습 → " + LINK_FC,
    "",
    "## Evening Routine (공통)",
    "- [ ] 운동",
    "- [ ] 명상 + 저널링 → " + LINK_J,
    "- [ ] 플래시 카드(하루 정리) → " + LINK_FC,
    "- [ ] 파인만 노트(오늘 공부 설명) → " + LINK_FY
  ];
}

// ---------- Render daily note ----------
let out = [];
out.push("---");
out.push("type: daily");
out.push("title: " + today);
out.push("created: " + today);
out.push("updated: \"" + nowDT + "\"");
out.push("author: [[김선음]]");
out.push("group: General");
out.push("status: [[🚜In Progress]]");
out.push("tags:");
out.push("  - daily");
out.push("  - day/" + preset.label);
out.push("aliases: []");
out.push("day_kind: " + preset.label);
out.push("wake_time_plan: \"" + preset.wake + "\"");
out.push("depart_time_plan: \"" + preset.depart + "\"");
out.push("journal_note: \"" + LINK_J + "\"");
out.push("flashcards_note: \"" + LINK_FC + "\"");
out.push("feynman_note: \"" + LINK_FY + "\"");
out.push("---");
out.push("");
out.push("# " + today + " — " + dayLabelKorean + " Day");
out.push("");
out.push("## Summary (Auto)");
out.push("```dataviewjs");
out.push("const todayStr = \"" + today + "\";");
out.push("const ydayStr  = \"" + yesterday + "\";");
out.push("const toYMD = (v) => {");
out.push("  if (!v) return null;");
out.push("  if (typeof v === 'string') return v.slice(0,10);");
out.push("  if (v && typeof v.toFormat === 'function') return v.toFormat('yyyy-MM-dd');");
out.push("  if (v instanceof Date) return dv.luxon.DateTime.fromJSDate(v).toFormat('yyyy-MM-dd');");
out.push("  if (typeof v === 'object' && v.year && v.month && v.day) {");
out.push("    return dv.luxon.DateTime.fromObject({year:v.year, month:v.month, day:v.day}).toFormat('yyyy-MM-dd');");
out.push("  }");
out.push("  return null;");
out.push("};");
out.push("const pages = dv.pages().where(p => p.file.path !== dv.current().file.path);");
out.push("const pagesToday = pages.where(p => toYMD(p.created) === todayStr);");
out.push("const pagesYday  = pages.where(p => toYMD(p.created) === ydayStr);");
out.push("const needTagging = dv.pages().where(p => Array.isArray(p.tags) && p.tags.includes('tagging/needed'));");
out.push("dv.paragraph(`- Notes created today: **${pagesToday.length}**`);");
out.push("dv.paragraph(`- Notes created yesterday: **${pagesYday.length}**`);");
out.push("dv.paragraph(`- tagging/needed remaining: **${needTagging.length}**`);");
out.push("```");
out.push("");
out.push("## Summary (Write)");
out.push("- Today in 1 line:");
out.push("- Top priority:");
out.push("- Biggest win:");
out.push("- Biggest gap:");
out.push("- Tomorrow focus:");
out.push("");
out.push("---");
out.push("");
out.push("## Linked Notes (자동 생성)");
out.push("- Journal: " + LINK_J);
out.push("- Flashcards: " + LINK_FC);
out.push("- Feynman: " + LINK_FY);
out.push("");
out.push("---");
out.push("");
out.push("## Day Setup");
out.push("- [ ] 기상: " + preset.wake);
if (preset.depart) out.push("- [ ] 출발: " + preset.depart + " _(" + preset.note + ")_");
out.push("");
out.push(checklist.join("\n"));
out.push("");
out.push("---");
out.push("");
out.push("## TODO (Today)");
out.push("- [ ]");

tR += out.join("\n");
%>