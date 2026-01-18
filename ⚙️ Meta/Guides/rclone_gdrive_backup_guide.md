---
type: reference
title: rclone Google Drive 자동 백업 가이드
created: 2026-01-13
updated: 2026-01-18T16:42:53
author:
  - "[[김선음]]"
group: SE
status:
  - "[[🌲Evergreen]]"
tags:
  - linux
  - rclone
  - google-drive
  - backup
  - obsidian
  - cron
  - setting
aliases:
  - rclone 백업
  - Google Drive 동기화
migrated_from: CMDS/500. setting/502. CMDS setting/rclone_gdrive_backup_guide.md
domain:
  - cs
cmds: connect
---

# rclone을 이용한 Google Drive 자동 백업 가이드

> [!info] 작성일
> 2026-01-13

## 📌 개요

Obsidian vault를 **Google Drive에 자동 백업**하는 방법을 정리한 문서입니다.
rclone + cron 조합을 사용합니다.

---

## 🤔 왜 GVFS 직접 사용을 피해야 하나?

Linux에서 GVFS로 마운트된 Google Drive 폴더(`/run/user/1000/gvfs/google-drive:...`)에 Obsidian vault를 직접 두는 것은 **권장하지 않습니다**.

| 문제점 | 설명 |
|--------|------|
| 동기화 충돌 | Obsidian 자동저장 + 네트워크 지연 = 충돌 위험 |
| 성능 저하 | 원격 파일 접근은 로컬보다 현저히 느림 |
| 오프라인 불가 | 인터넷 없으면 vault 접근 불가 |

> [!tip] 권장 방법
> **로컬에 vault** → **rclone으로 주기적 백업**

---

## 🛠️ 설치 및 설정

### Step 1: rclone 설치

```bash
sudo apt install rclone
```

### Step 2: Google Drive 연결

```bash
rclone config
```

#### 대화형 설정 순서:

1. `n` → new remote
2. name: `gdrive`
3. Storage: `drive` (Google Drive)
4. client_id: Enter (기본값)
5. client_secret: Enter (기본값)
6. scope: `1` (Full access)
7. root_folder_id: Enter
8. service_account_file: Enter
9. 고급 설정: `n`
10. 자동 설정: `y` → 브라우저에서 Google 로그인
11. 팀 드라이브: `n`
12. 확인: `y` → `q` 종료

### Step 3: 연결 테스트

```bash
rclone lsd gdrive:
```

Google Drive 폴더 목록이 보이면 성공! ✅

---

## 🔄 동기화 명령어

### 수동 동기화

```bash
# 미리보기 (실제 실행 안 함)
rclone sync ~/new_my gdrive:Obsidian_Backup/ --dry-run

# 실제 동기화
rclone sync ~/new_my gdrive:Obsidian_Backup/
```

### 유용한 옵션들

| 옵션 | 설명 |
|------|------|
| `--dry-run` | 미리보기만, 실제 실행 안 함 |
| `--progress` | 진행 상황 표시 |
| `--log-file=/path/to/log` | 로그 파일 저장 |
| `-v` | 상세 출력 |

---

## ⏰ cron 자동화 설정

### crontab 편집

```bash
crontab -e
```

### 추가할 내용 (30분마다 백업)

```cron
*/30 * * * * rclone sync /home/seoneum/new_my gdrive:Obsidian_Backup/ --log-file=/tmp/rclone.log
```

### cron 시간 형식

```
분 시 일 월 요일 명령어
```

| 예시 | 설명 |
|------|------|
| `*/30 * * * *` | 30분마다 |
| `0 * * * *` | 매시 정각 |
| `0 */2 * * *` | 2시간마다 |
| `0 9 * * *` | 매일 오전 9시 |
| `0 9 * * 1` | 매주 월요일 오전 9시 |

---

## 📋 자주 쓰는 명령어

```bash
# cron 작업 확인
crontab -l

# 백업 로그 확인
cat /tmp/rclone.log

# Google Drive 백업 파일 목록
rclone ls gdrive:Obsidian_Backup/

# cron 작업 전체 삭제
crontab -r
```

---

## ✅ 현재 설정 상태

| 항목 | 값 |
|------|-----|
| 백업 주기 | 30분마다 |
| 원본 경로 | `/home/seoneum/new_my` |
| 백업 위치 | `gdrive:Obsidian_Backup/` |
| 로그 파일 | `/tmp/rclone.log` |

---

## ⚠️ 주의사항

> [!warning] cron 동작 조건
> - 시스템이 **켜져 있을 때만** 동작
> - 절전 모드/종료 시에는 실행 안 됨

> [!caution] 경로 주의
> - `~`는 `/home/사용자명`을 의미
> - `~/home/seoneum/...` ❌ 잘못된 경로
> - `~/new_my` 또는 `/home/seoneum/new_my` ✅ 올바른 경로

---

## 🔗 관련 링크

- [rclone 공식 문서](https://rclone.org/docs/)
- [rclone Google Drive 설정](https://rclone.org/drive/)
- [[n8n_setup_guide|n8n 자동화 가이드]]
- [[Linux Syntax|Linux 명령어 문법]]
