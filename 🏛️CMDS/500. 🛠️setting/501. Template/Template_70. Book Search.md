---
tags:
  - 📚Book
  - 📘Books
title: "{{title}}"
subtitle: "{{subtitle}}"
author:
  - "[[{{author}}]]"
category:
  - "[[{{category}}]]" 
publisher: {{publisher}}
publish_date: {{publishDate}}
total_page:
  {{totalPage}}
isbn:
  {{isbn10}}
isbn13:
  {{isbn13}}
cover_url: {{coverUrl}}
status: unread
created: {{DATE: YYYY-MM-DD HH:mm:ss}}
updated: {{DATE: YYYY-MM-DD HH:mm:ss}}
---
<%* if (tp.frontmatter.cover && tp.frontmatter.cover.trim() !== "") { tR += `![cover|150](${tp.frontmatter.cover})` } %>
# {{title}}
## 책 소개
{{description}}

## 관련 노트


# References