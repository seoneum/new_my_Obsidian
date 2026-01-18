---
type: dashboard
title: Dashboard
created: 2026-01-18
---

# 🏠 Dashboard

## ⚡ Quick Actions
- [[📌Guidline|📌 가이드라인]]
- Create: `Ctrl+N` → Universal Template

---

## 📥 Inbox (처리 대기)
```dataview
TABLE WITHOUT ID
  file.link as "Note",
  dateformat(file.ctime, "MM-dd") as "Created"
FROM "📥 Inbox"
WHERE file.name != "_quick" AND file.name != "_webclip"
SORT file.ctime DESC
LIMIT 10
```

---

## 📅 Recent Daily Notes
```dataview
LIST
FROM "📅 Daily"
SORT file.name DESC
LIMIT 7
```

---

## 🎯 Active Projects
```dataview
TABLE WITHOUT ID
  file.link as "Project",
  progress as "Progress",
  deadline as "Deadline"
FROM "🎯 Projects"
WHERE type = "project"
SORT deadline ASC
```

---

## 📚 Recent Lectures
```dataview
TABLE WITHOUT ID
  file.link as "Lecture",
  course as "Course",
  week as "Week"
FROM "📚 Lectures"
SORT file.ctime DESC
LIMIT 10
```

---

## 💡 Recent Notes
```dataview
TABLE WITHOUT ID
  file.link as "Note",
  type as "Type",
  dateformat(file.mtime, "MM-dd") as "Updated"
FROM "💡 Notes"
SORT file.mtime DESC
LIMIT 10
```

---

## 📖 Reading List
```dataview
TABLE WITHOUT ID
  file.link as "Book/Paper",
  status as "Status"
FROM "📖 Books"
WHERE status != "completed"
SORT file.ctime DESC
LIMIT 5
```

---

## 📊 Vault Stats
```dataview
TABLE WITHOUT ID
  length(rows) as "Count",
  rows.file.folder[0] as "Folder"
FROM ""
WHERE file.name != "Dashboard"
GROUP BY file.folder
SORT length(rows) DESC
```
