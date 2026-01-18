---
tags:
  - dashboard
  - home
type: dashboard
created: 2026-01-18
---

# 🏠 Dashboard

> **CPZ Vault** - CMDS + PARA + Zettelkasten 통합 시스템

---

## 📥 Inbox (미처리)

```dataview
TABLE WITHOUT ID
  link(file.link, file.name) as "노트",
  cmds as "단계",
  dateformat(file.mtime, "MM-dd HH:mm") as "수정"
FROM ""
WHERE cmds = "inbox" OR contains(tags, "tagging/needed")
SORT file.mtime DESC
LIMIT 10
```

---

## 🎯 Active Projects

```dataview
TABLE WITHOUT ID
  link(file.link, title) as "프로젝트",
  progress + "%" as "진행",
  deadline as "마감",
  default(date(deadline) - date(today), "∞") as "D-day"
FROM "🎯 Projects"
WHERE type = "project" AND status != "archive"
SORT deadline ASC
LIMIT 5
```

---

## 📚 Recent Work

### 최근 수정된 노트
```dataview
TABLE WITHOUT ID
  link(file.link, file.name) as "노트",
  type as "타입",
  domain as "분야",
  dateformat(file.mtime, "MM-dd") as "수정"
FROM ""
WHERE file.name != "Dashboard" AND !contains(file.path, "Meta")
SORT file.mtime DESC
LIMIT 10
```

---

## 💎 Knowledge Base

### CMDS 단계별 현황
```dataview
TABLE WITHOUT ID
  cmds as "단계",
  length(rows) as "노트 수"
FROM ""
WHERE cmds != null
GROUP BY cmds
```

### 도메인별 현황
```dataview
TABLE WITHOUT ID
  domain as "도메인",
  length(rows) as "노트 수"
FROM ""
WHERE domain != null AND length(domain) > 0
FLATTEN domain
GROUP BY domain
SORT length(rows) DESC
```

---

## ❓ Open Questions

```dataview
TABLE WITHOUT ID
  link(file.link, title) as "질문",
  domain as "분야",
  dateformat(file.ctime, "MM-dd") as "생성"
FROM "💎 Zettel/Questions"
WHERE resolved = false OR resolved = null
SORT file.ctime DESC
LIMIT 5
```

---

## 📊 Statistics

### 이번 주 생성
```dataview
LIST WITHOUT ID length(rows) + " notes"
FROM ""
WHERE file.cday >= date(today) - dur(7 days)
```

### 총 노트 수
```dataview
LIST WITHOUT ID length(rows) + " total notes"
FROM ""
WHERE !contains(file.path, ".obsidian")
```

---

## 🔗 Quick Links

- [[📌Guidline|📌 가이드라인]]
- [[UNIFIED_METHODOLOGY|🧠 CPZ 방법론]]
- **폴더**: [[📥 Inbox]] | [[🎯 Projects]] | [[💎 Zettel]]
