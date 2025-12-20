---
type: meeting
date: <% tp.date.now("YYYY-MM-DD") %>
attendees: <%*
let attendees = await tp.system.prompt("참석자 명단을 입력하세요 (쉼표로 구분):");
%>
- "[[구요한]]"
- <% attendees.split(",").map(a => `"[[${a.trim()}]]"`).join("\n- ") %>
organization:
CMDS: 
index: "[[🏷 Meeting Notes]]"
tags:
  - "#MeetingMinutes"
---

>[!info]
>- Meeting Title: <% tp.file.title %> Meeting
>- Meeting Date: [[<% tp.date.now("YYYY-MM-DD") %>]]
>- Attendees: [[구요한]], <% attendees.split(",").map(a => `[[${a.trim()}]]`).join(", ") %>
>- Meeting Topic: <%*
let topic = await tp.system.prompt("회의 주제 입력:");
%><% topic %>

## Discussion
<%*
let keywords = await tp.system.prompt("논의 내용 작성(쉼표로 구분):");
%><% keywords.split(",").map(a => `#### ${a.trim()}`).join("\n\n") %>


## Next Steps
- 

# References
## Citations
1. 
2. 
3. 
## Reference
#### Original
- 
#### Additional
- 
## Appendices
- 

<% await tp.file.move("/70. Collections/74. Meetings/" + tp.date.now("YYYYMMDD") + "_" + tp.file.title + " Meeting" ) %>