# 🔌 추천 플러그인 및 설정 가이드

## 📦 필수 플러그인

### 1. Templater
> 고급 템플릿 기능

**설치**: 커뮤니티 플러그인 → Templater 검색 → 설치

**핵심 설정**:
```
Template folder location: 500. Setting/501. Template
Trigger Templater on new file creation: ON
```

**주요 문법**:
```
<% tp.date.now("YYYY-MM-DD") %>          // 오늘 날짜
<% tp.date.now("YYYY-MM-DD", -1) %>      // 어제 날짜
<% tp.file.title %>                       // 파일 제목
<% tp.file.cursor() %>                    // 커서 위치
```

---

### 2. Calendar
> 달력 보기 및 Daily Note 연동

**설치**: 커뮤니티 플러그인 → Calendar 검색 → 설치

**핵심 설정**:
```
Weekly note folder: 100. Inbox/102. Daily_Note
Weekly note template: 500. Setting/501. Template/Weekly_Review_Template.md
```

**사용법**:
- 사이드바에서 달력 클릭 → 해당 날짜 Daily Note 생성/이동

---

### 3. Periodic Notes
> 일간/주간/월간 노트 관리

**설치**: 커뮤니티 플러그인 → Periodic Notes 검색 → 설치

**핵심 설정**:
```
Daily Notes:
  - Folder: 100. Inbox/102. Daily_Note
  - Template: 500. Setting/501. Template/Daily_Template.md
  - Date format: YYYY-MM-DD

Weekly Notes:
  - Folder: 200. CMDS/220. Merge/221. Journaling
  - Template: 500. Setting/501. Template/Weekly_Review_Template.md
```

---

### 4. Spaced Repetition
> 플래시카드 학습

**설치**: 커뮤니티 플러그인 → Spaced Repetition 검색 → 설치

**핵심 설정**:
```
Flashcard separator: ?
Card separator: ---
Flashcard tags: #flashcard
```

**사용법**:
1. FC 파일 열기
2. 사이드바 "Review flashcards" 클릭
3. 카드 보고 난이도 선택 (Hard/Good/Easy)

---

### 5. Dataview
> 데이터 쿼리 및 자동 목록

**설치**: 커뮤니티 플러그인 → Dataview 검색 → 설치

**예시 쿼리**:
```dataview
// 이번 주 생성된 노트 목록
TABLE file.ctime as "생성일", tags
FROM ""
WHERE file.ctime >= date(today) - dur(7 days)
SORT file.ctime DESC
```

```dataview
// 미완료 할 일 목록
TASK
WHERE !completed
GROUP BY file.link
```

---

## ⭐ 강력 추천 플러그인

### 6. Excalidraw
> 다이어그램, 손그림

**용도**: 개념 시각화, 플로우차트, 마인드맵

**설정**:
```
Excalidraw folder: 100. Inbox/103. Excalidraw
```

---

### 7. Tasks
> 할 일 관리

**문법**:
```
- [ ] 할 일 📅 2024-03-15
- [ ] 긴급한 일 ⏫ 
- [x] 완료된 일 ✅ 2024-03-14
```

---

### 8. Quick Add
> 빠른 노트 생성

**설정 예시**:
- `Ctrl+Shift+D`: Daily Note 생성
- `Ctrl+Shift+L`: 강의 노트 생성
- `Ctrl+Shift+M`: 회의록 생성

---

### 9. Obsidian Git
> Git 자동 백업

**설정**:
```
Auto backup interval: 10분
Auto pull interval: 10분
Commit message: vault backup: {{date}}
```

---

## 🎨 선택 플러그인

| 플러그인 | 용도 | 추천도 |
|---------|------|--------|
| Kanban | 프로젝트 보드 | ⭐⭐⭐ |
| Mind Map | 마인드맵 시각화 | ⭐⭐⭐ |
| PDF Annotator | PDF 주석 | ⭐⭐ |
| Advanced Tables | 표 편집 | ⭐⭐⭐ |
| Outliner | 아웃라이너 기능 | ⭐⭐ |
| Sliding Panes | 여러 패널 보기 | ⭐⭐ |

---

## ⚙️ Obsidian 기본 설정 권장

### Editor
```
- Default view: Editing view
- Strict line breaks: OFF
- Auto pair brackets: ON
```

### Files & Links
```
- Default location for new notes: 100. Inbox/101. Anything
- New link format: Shortest path
- Use [[Wikilinks]]: ON
```

### Appearance
```
- Theme: 취향에 맞게 (추천: Minimal, Things)
- Show line numbers: ON
```

---

## 🚀 빠른 시작 체크리스트

- [ ] Templater 설치 및 템플릿 폴더 설정
- [ ] Calendar + Periodic Notes 설치 및 Daily Note 설정
- [ ] Spaced Repetition 설치 및 구분자 `?` 설정
- [ ] Dataview 설치
- [ ] 기본 설정에서 새 노트 위치를 Inbox로 설정
- [ ] (선택) Obsidian Git으로 자동 백업 설정
