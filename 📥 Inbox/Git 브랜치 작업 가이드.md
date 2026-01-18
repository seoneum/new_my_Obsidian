---
type: reference
title: Git 브랜치 작업 가이드
created: 2026-01-18
updated: 2026-01-18T16:42:53
author: [[김선음]]
tags:
  - git
  - reference
  - workflow
status:
  - "[[🌿Sapling]]"
group:
  - CS
migrated_from: CMDS/100. Inbox/110. Software/111. Git/Git 브랜치 작업 가이드.md
domain:
  - cs
cmds: inbox
---

# Git 브랜치 작업 가이드

> 다른 브랜치에 파일을 업로드하고 다시 돌아오는 전체 워크플로우

---

## 📌 핵심 명령어 요약

```bash
# 1. 현재 변경사항 임시 저장
git stash push -m "설명"

# 2. 브랜치 전환
git checkout 브랜치명

# 3. 다른 브랜치에서 특정 파일 가져오기
git checkout main -- "파일경로"

# 4. 커밋 & 푸시
git add .
git commit -m "메시지"
git push origin 브랜치명

# 5. 원래 브랜치로 복귀 & stash 복원
git checkout main
git stash pop
```

---

## 📖 상황별 가이드

### Case 1: 다른 브랜치에 파일 업로드하기

**상황**: main 브랜치에서 작업 중인데, student-distribution 브랜치에 특정 파일만 올리고 싶다.

#### Step 1: 현재 상태 확인
```bash
git status
git branch -a          # 모든 브랜치 보기
git remote -v          # 원격 저장소 확인
```

#### Step 2: 변경사항 임시 저장 (Stash)
```bash
git stash push -m "temp stash before switching"
```
> ⚠️ **왜 필요한가?**
> 커밋하지 않은 변경사항이 있으면 브랜치 전환이 안됨

#### Step 3: 대상 브랜치로 전환
```bash
git checkout student-distribution
```

#### Step 4: main 브랜치에서 파일 가져오기
```bash
# 단일 파일
git checkout main -- "경로/파일명.md"

# 여러 파일
git checkout main -- "파일1.md" "파일2.md" "파일3.md"

# 폴더 전체
git checkout main -- "폴더경로/"
```

#### Step 5: 커밋 & 푸시
```bash
git add .
git commit -m "feat: 설명"
git push origin student-distribution
```

#### Step 6: 원래 브랜치로 복귀
```bash
git checkout main
git stash pop          # 임시 저장한 변경사항 복원
```

---

### Case 2: 브랜치 전환 시 오류 해결

#### 오류: "Your local changes would be overwritten by checkout"

```
error: Your local changes to the following files would be overwritten by checkout:
        .obsidian/workspace.json
Please commit your changes or stash them before you switch branches.
```

**해결책 1: Stash 사용**
```bash
git stash
git checkout 브랜치명
# 작업 후
git checkout main
git stash pop
```

**해결책 2: 변경사항 버리기 (주의!)**
```bash
git restore 파일경로           # 특정 파일 복원
git restore .                 # 모든 변경 복원 (위험!)
```

**해결책 3: untracked 파일 문제**
```bash
# untracked 파일 삭제 (주의! 되돌릴 수 없음)
rm -rf .makemd .obsidian Tags
git checkout 브랜치명
```

---

### Case 3: Stash 관리

```bash
# stash 목록 보기
git stash list

# 가장 최근 stash 적용 (stash 유지)
git stash apply

# 가장 최근 stash 적용 & 삭제
git stash pop

# 특정 stash 적용
git stash apply stash@{1}

# stash 삭제
git stash drop           # 가장 최근
git stash drop stash@{1} # 특정 stash
git stash clear          # 모든 stash
```

---

## 🔧 자주 쓰는 명령어

### 기본 명령어

| 명령어 | 설명 |
|--------|------|
| `git status` | 현재 상태 확인 |
| `git branch` | 로컬 브랜치 목록 |
| `git branch -a` | 모든 브랜치 (원격 포함) |
| `git log -n 5` | 최근 5개 커밋 |

### 브랜치 관련

| 명령어 | 설명 |
|--------|------|
| `git checkout 브랜치명` | 브랜치 전환 |
| `git checkout -b 새브랜치` | 새 브랜치 생성 & 전환 |
| `git branch -d 브랜치명` | 브랜치 삭제 |
| `git merge 브랜치명` | 현재 브랜치에 병합 |

### 커밋 관련

| 명령어 | 설명 |
|--------|------|
| `git add .` | 모든 변경사항 스테이징 |
| `git add 파일` | 특정 파일만 스테이징 |
| `git commit -m "메시지"` | 커밋 |
| `git push origin 브랜치명` | 푸시 |
| `git pull origin 브랜치명` | 풀 (fetch + merge) |

### 되돌리기

| 명령어 | 설명 |
|--------|------|
| `git restore 파일` | 변경사항 버리기 |
| `git restore --staged 파일` | 스테이징 취소 |
| `git reset HEAD~1` | 마지막 커밋 취소 (변경사항 유지) |
| `git reset --hard HEAD~1` | 마지막 커밋 완전 삭제 ⚠️ |

---

## 📝 커밋 메시지 컨벤션

```
<타입>: <제목>

<본문 (선택)>
```

### 타입 종류
- `feat`: 새 기능
- `fix`: 버그 수정
- `docs`: 문서 수정
- `style`: 코드 포맷팅
- `refactor`: 리팩토링
- `chore`: 기타 작업

### 예시
```bash
git commit -m "feat: Add dynamic chapter count to Book_Template

- Added chapter count prompt
- Generate chapters dynamically based on user input"
```

---

## ⚠️ 자주 발생하는 오류

### 1. "Failed to push some refs"
```
! [rejected]        main -> main (fetch first)
error: failed to push some refs
```
**원인**: 원격에 새 변경사항이 있음
**해결**:
```bash
git pull origin main --rebase
git push origin main
```

### 2. "Merge conflict"
```
CONFLICT (content): Merge conflict in 파일명
```
**해결**:
1. 충돌 파일 열기
2. `<<<<<<<`, `=======`, `>>>>>>>` 사이 코드 정리
3. `git add 파일명`
4. `git commit`

### 3. "Detached HEAD"
```
You are in 'detached HEAD' state
```
**해결**:
```bash
git checkout main   # 또는 원하는 브랜치
```

---

## 🎯 오늘 사용한 실제 워크플로우

```bash
# 1. 브랜치 확인
git remote -v && git branch -a

# 2. 현재 변경사항 stash
git stash push -m "temp stash before switching to student-distribution"

# 3. student-distribution 브랜치로 전환
git checkout student-distribution

# 4. main 브랜치에서 템플릿 파일들 가져오기
git checkout main -- \
  "CMDS/500. setting/501. Template/Book_Template.md" \
  "CMDS/500. setting/501. Template/Concept_Template.md" \
  "CMDS/500. setting/501. Template/Problem_Template.md" \
  "CMDS/500. setting/501. Template/Thinking_Template.md" \
  "CMDS/500. setting/501. Template/Daily_Template.md"

# 5. 커밋 & 푸시
git commit -m "feat: Update templates with fixed Templater syntax"
git push origin student-distribution

# 6. main 브랜치로 복귀
git checkout main
git stash pop
```

---

## 🔗 관련 노트

- [[Git 기초]]
- [[GitHub 연동]]

