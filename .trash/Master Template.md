<%* 
const noteTypes =;


const templateFiles = {
  "📝 일반 노트 (Basic Note)": "T_Basic_Note",
  "📅 데일리 노트 (Daily Note)": "T_Daily_Note",
  "💻 강의: 소프트웨어 공학 (SW Eng)": "T_Lecture_SoftEng",
  "⚡ 강의: 전기/전자 공학 (EE Eng)": "T_Lecture_ElectricalEng",
  "🦉 강의: 철학 (Philosophy)": "T_Lecture_Philosophy",
  "🌐 강의: 외부/인터넷 (Inbox)": "T_Lecture_External",
  "🧠 지식/원자 노트 (Merge/Atomic)": "T_Knowledge_Merge",
  "📐 이론/개념 노트 (Theory)": "T_Theory_Note",
  "👥 인물 노트 (Person)": "T_Person",
  "📚 레퍼런스 (Reference/Book/Paper)": "T_Reference",
  "📊 CMDS 대시보드 (Dashboard)": "T_CMDS_Dashboard"
};


const folderPaths = {
  "📝 일반 노트 (Basic Note)": "00_Inbox",
  "📅 데일리 노트 (Daily Note)": "10_Daily/" + tp.date.now("YYYY/MM"),
  "💻 강의: 소프트웨어 공학 (SW Eng)": "20_Sources/21_University/SoftEng",
  "⚡ 강의: 전기/전자 공학 (EE Eng)": "20_Sources/21_University/ElectricalEng",
  "🦉 강의: 철학 (Philosophy)": "20_Sources/21_University/Philosophy",
  "🌐 강의: 외부/인터넷 (Inbox)": "20_Sources/22_External",
  "🧠 지식/원자 노트 (Merge/Atomic)": "30_Knowledge/31_Atomic",
  "📐 이론/개념 노트 (Theory)": "30_Knowledge/32_Theories",
  "👥 인물 노트 (Person)": "40_Entities/41_People",
  "📚 레퍼런스 (Reference/Book/Paper)": "40_Entities/42_References",
  "📊 CMDS 대시보드 (Dashboard)": "90_Admin"
};


const selection = await tp.system.suggester(noteTypes, noteTypes);

if (!selection) {
     선택 취소 시 실행 중단
    return;
}


let title = tp.file.title;
if (!selection.includes("Daily")) {
    title = await tp.system.prompt("노트 제목을 입력하세요:", title);
    if (title == null |

| title == "") { title = "Untitled_" + tp.date.now("YYYYMMDDHHmm"); }
    await tp.file.rename(title);
}

const targetFolder = folderPaths[selection];
if (targetFolder) {
     폴더가 없으면 생성 (Obsidian 설정에 따라 자동 생성되지만 안전장치)
    if (!app.vault.getAbstractFileByPath(targetFolder)) {
        await app.vault.createFolder(targetFolder);
    }
    await tp.file.move(targetFolder + "/" + title);
}


const templateName = templateFiles[selection];
if (templateName) {
    tR += await tp.file.include(`[[${templateName}]]`);
} else {
    tR += "⚠️ 템플릿을 찾을 수 없습니다.";
}%>