---
created: <% tp.file.creation_date() %>
aliases:
tags:
  - DailyNote
author:
source:
type:
  - note
index:
  - "[[🏷 Daily Notes]]"
CMDS:
---
# <% tp.file.title %>
## [[<% tp.date.now("YYYY-MM-DD", -1, tp.file.title, "YYYY-MM-DD") %> |◀︎]] <% tp.file.title %> [[<% tp.date.now("YYYY-MM-DD", 1, tp.file.title, "YYYY-MM-DD") %> |▶︎]]
---
## Summary
#### Highlight
- 
#### Gratitude
- 
## Schedule
#### Event
- 
#### To Do
#todo 
- [ ] 

## Note-taking
#### Created Today
```dataview
list
from ""
where file.day = date({{title}}) AND !contains(file.folder, "🏛️CMDS/100. 📦️Inbox/101. 🏦Daily_Note")
```
#### Modified Today
```dataview
list
from ""
where file.day = date({{title}}) AND !contains(file.folder, "🏛️CMDS/100. 📦️Inbox/101. 🏦Daily_Note") AND file.cday != date({{title}})
```
## Log
- 

--- 
# Reference
- 