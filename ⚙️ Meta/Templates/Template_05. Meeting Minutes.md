---
migrated_from: CMDS/500. setting/501. Template/Template_05. Meeting Minutes.md
updated: 2026-01-18T16:42:53
domain:
  - robotics
cmds: connect
---
<%*
// 회의록 템플릿 - Meeting Minutes Template
let meetingTitle = await tp.system.prompt("회의 제목:", tp.file.title);
meetingTitle = meetingTitle ? meetingTitle.trim() : tp.file.title;

let attendeesRaw = await tp.system.prompt("참석자 명단 (쉼표로 구분):");
attendeesRaw = attendeesRaw ? attendeesRaw.trim() : "";
let attendeeArr = attendeesRaw.split(",").map(a => a.trim()).filter(a => a);

let topic = await tp.system.prompt("회의 주제:");
topic = topic ? topic.trim() : "";

let group = await tp.system.suggester(
  ["SLAM","AI","Robotics","EE","SE","Phil","Math","General"],
  ["SLAM","AI","Robotics","EE","SE","Phil","Math","General"]
) || "General";

// 저장 위치 선택
let folderChoice = await tp.system.suggester(
  ["현재 위치 유지", "CMDS/200. CMDS/201. Connect"],
  ["", "CMDS/200. CMDS/201. Connect"]
);

let fileName = tp.date.now("YYYYMMDD") + "_" + meetingTitle;
-%>
---
type: meeting
date: <% tp.date.now("YYYY-MM-DD") %>
attendees:
<% attendeeArr.map(a => `  - "[[${a}]]"`).join("\n") %>
group: "<% group %>"
tags:
  - meeting
  - MeetingMinutes
---

> [!info] Meeting Info
> - **Title**: <% meetingTitle %>
> - **Date**: [[<% tp.date.now("YYYY-MM-DD") %>]]
> - **Attendees**: <% attendeeArr.map(a => `[[${a}]]`).join(", ") || "TBD" %>
> - **Topic**: <% topic %>

## Agenda
1. 

## Discussion
### Topic 1
- 

### Topic 2
- 

## Decisions
- [ ] 

## Action Items
| Task | Assignee | Due Date | Status |
|------|----------|----------|--------|
| | | | ⏳ |

## Next Steps
- 

---

# References
## Related Notes
- [[ ]]

## Appendices
- 

<%*
if (folderChoice) {
  await tp.file.move(folderChoice + "/" + fileName);
} else {
  await tp.file.rename(fileName);
}
-%>