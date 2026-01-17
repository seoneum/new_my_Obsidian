# n8n 완전 가이드 - Obsidian 플래시카드 자동화

> [!info] 문서 정보
> - 작성일: 2026-01-13
> - 목적: n8n + Gemini API로 Obsidian 플래시카드 자동 생성
> - 스케줄: 매일 8:00 AM (전날 복습), 10:00 PM (당일 정리)

---

## 1. Docker 기초

### 1.1 Docker란?
- 애플리케이션을 컨테이너로 패키징하여 어디서든 동일하게 실행
- n8n을 Docker로 실행하면 의존성 걱정 없이 바로 사용 가능

### 1.2 기본 명령어

```bash
# 컨테이너 목록 보기
docker ps              # 실행 중인 컨테이너
docker ps -a           # 모든 컨테이너 (중지된 것 포함)

# 컨테이너 제어
docker start n8n       # 시작
docker stop n8n        # 중지
docker restart n8n     # 재시작
docker rm n8n          # 삭제 (중지 후 가능)

# 로그 확인
docker logs n8n        # 전체 로그
docker logs n8n --tail 50   # 마지막 50줄
docker logs n8n -f     # 실시간 로그 (Ctrl+C로 종료)

# 이미지 관리
docker images          # 다운로드된 이미지 목록
docker pull n8nio/n8n  # 최신 버전 다운로드
```

---

## 2. n8n 설치

### 2.1 최초 설치 (권한 문제 해결 버전)

```bash
# 1. n8n 데이터 폴더 생성
rm -rf ~/.n8n && mkdir -p ~/.n8n

# 2. Docker 실행 (현재 사용자 권한으로)
docker run -d \
  --name n8n \
  --restart always \
  -p 5678:5678 \
  -e N8N_USER_FOLDER=/home/node \
  -v ~/.n8n:/home/node/.n8n \
  -v /home/seoneum/new_my:/data/obsidian \
  --user "$(id -u):$(id -g)" \
  n8nio/n8n
```

### 2.2 옵션 설명
| 옵션 | 설명 |
|------|------|
| `-d` | 백그라운드 실행 |
| `--name n8n` | 컨테이너 이름 |
| `--restart always` | 재부팅 시 자동 시작 |
| `-p 5678:5678` | 포트 매핑 (호스트:컨테이너) |
| `-v ~/.n8n:/home/node/.n8n` | 설정 데이터 영구 저장 |
| `-v /home/seoneum/new_my:/data/obsidian` | Obsidian 볼트 마운트 |
| `--user "$(id -u):$(id -g)"` | 현재 사용자 권한으로 실행 |

### 2.3 접속
- URL: **http://localhost:5678**
- 첫 접속 시 계정 생성 필요 (이메일/비밀번호)
id : seoneum02@inha.edu
pw : Seoneum845

---

## 3. 발생한 오류와 해결

### 3.1 Permission Denied 오류
```
Error: EACCES: permission denied, open '/home/node/.n8n/config'
```

**원인**: Docker 컨테이너 내부 사용자(node, UID 1000)와 호스트 사용자 권한 불일치

**해결**: `--user "$(id -u):$(id -g)"` 옵션 추가

```bash
# 기존 컨테이너 제거
docker stop n8n && docker rm n8n

# 폴더 재생성
rm -rf ~/.n8n && mkdir -p ~/.n8n

# 권한 맞춰서 재실행
docker run -d --name n8n --restart always \
  -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n \
  -v /home/seoneum/new_my:/data/obsidian \
  --user "$(id -u):$(id -g)" \
  n8nio/n8n
```

### 3.2 포트 충돌
```
Error: Bind for 0.0.0.0:5678 failed: port is already allocated
```

**해결**:
```bash
# 어떤 프로세스가 쓰는지 확인
sudo lsof -i :5678

# 다른 포트 사용
docker run ... -p 5679:5678 ...
# 접속: http://localhost:5679
```

### 3.3 컨테이너 시작 안 됨
```bash
# 상태 확인
docker ps -a | grep n8n

# 로그 확인
docker logs n8n

# 재생성
docker stop n8n && docker rm n8n
# 위 설치 명령 다시 실행
```

---

## 4. API 설정

### 4.1 Gemini API Key 발급

1. [Google AI Studio](https://aistudio.google.com/apikey) 접속
2. **Create API Key** 클릭
3. 발급된 키 복사 (예: `AIzaSy...`)

### 4.2 GitHub Personal Access Token 발급

1. GitHub → Settings → Developer settings
2. Personal access tokens → Tokens (classic)
3. **Generate new token (classic)**
4. Note: `n8n-obsidian`
5. Expiration: 선택 (No expiration 가능)
6. Scopes: ✅ `repo` (전체)
7. **Generate token** → 복사

---

## 5. n8n Credentials 설정

### 5.1 GitHub Credential
1. n8n → Settings (⚙️) → Credentials
2. **Add Credential** → GitHub
3. Authentication: **Personal Access Token**
4. Token: [GitHub 토큰 붙여넣기]
5. **Save**

### 5.2 Gemini API Credential (HTTP Header Auth)
1. **Add Credential** → HTTP Header Auth
2. Name: `Gemini API`
3. Header Name: `x-goog-api-key`
4. Header Value: [Gemini API 키 붙여넣기]
5. **Save**

---

## 6. Workflow 구조

### 6.1 전체 흐름

```
[Schedule Trigger: 8:00, 22:00]
    ↓
[GitHub: 볼트 파일 목록 가져오기]
    ↓
[Code: 날짜 계산 (8시=어제, 22시=오늘)]
    ↓
[GitHub: 해당 날짜 노트 읽기]
    ↓
[HTTP Request: Gemini API로 플래시카드 생성]
    ↓
[Code: 마크다운 포맷팅]
    ↓
[GitHub: FC-날짜.md 파일 생성 + commit]
    ↓
[Obsidian Git: 자동 pull로 동기화]
```

### 6.2 각 노드 설명

#### 1) Schedule Trigger
- 매일 8:00, 22:00에 자동 실행
- Cron 표현식: `0 8,22 * * *`

#### 2) GitHub - List Files
- Repository: `seoneum/new_my_Obsidian`
- Path: `CMDS/`

#### 3) Code - Calculate Dates
```javascript
const now = new Date();
const hour = now.getHours();
const today = now.toISOString().slice(0, 10);
const yesterday = new Date(now - 86400000).toISOString().slice(0, 10);

// 8시면 어제 노트, 22시면 오늘 노트
const targetDate = hour < 12 ? yesterday : today;
const sessionType = hour < 12 ? 'Morning' : 'Evening';

return [{ json: { targetDate, sessionType, today, yesterday } }];
```

#### 4) Gemini API Prompt
```
다음 노트 내용을 분석해서 Obsidian Spaced Repetition 플러그인 형식의 플래시카드를 생성해줘.

규칙:
1. 형식: 질문:: 답변 (콜론 두 개)
2. 철학 내용은 개념 정의와 논증 구조 위주
3. 수학/코딩은 공식, 알고리즘, 시간복잡도 위주
4. 각 카드는 한 가지 개념만
5. 답변은 간결하게 (1-2문장)

노트 내용:
{노트 본문}
```

#### 5) Output Format
```markdown
---
type: flashcards
title: FC - 2026-01-13 (Morning)
created: 2026-01-13
author: "[[김선음]]"
tags:
  - flashcards
  - daily
  - auto-generated
---

# FC - 2026-01-13 (Morning)

## Cards

{Gemini가 생성한 플래시카드}
```

---

## 7. Workflow Import 방법

### 7.1 파일 위치
```
/home/seoneum/new_my/CMDS/500. setting/502. CMDS setting/n8n_flashcard_workflow.json
```

### 7.2 Import 단계
1. n8n → Workflows 메뉴
2. **Import from File** 클릭
3. `n8n_flashcard_workflow.json` 선택
4. Import 완료 후 Credentials 연결:
   - GitHub 노드들 → GitHub credential 선택
   - HTTP Request 노드 → Gemini API credential 선택
5. 우상단 토글 → **Active** 로 변경

---

## 8. 테스트 방법

### 8.1 수동 실행
1. Workflow 열기
2. 우상단 **Execute Workflow** 클릭
3. 각 노드 실행 결과 확인
4. 마지막 GitHub Create 노드에서 파일 생성 확인

### 8.2 결과 확인
```bash
# Git pull로 로컬에 가져오기
cd /home/seoneum/new_my
git pull

# 또는 Obsidian Git이 자동 pull 설정되어 있으면 대기
```

---

## 9. 유지 관리

### 9.1 n8n 업데이트
```bash
docker stop n8n
docker rm n8n
docker pull n8nio/n8n
# 위 설치 명령 다시 실행
```

### 9.2 백업
```bash
# 설정 백업
cp -r ~/.n8n ~/n8n_backup_$(date +%Y%m%d)

# Workflow JSON 내보내기
# n8n UI에서 Workflow → Export to File
```

### 9.3 로그 정리
```bash
# Docker 로그 크기 확인
docker system df

# 오래된 로그 정리
docker system prune
```

---

## 10. 관련 파일

| 파일 | 설명 |
|------|------|
| [[n8n_flashcard_workflow.json]] | n8n 워크플로우 정의 |
| [[FC_Morning_Template]] | 아침 플래시카드 수동 템플릿 |
| [[FC_Evening_Template]] | 저녁 플래시카드 수동 템플릿 |
| [[Feynman Tamplate]] | 파인만 학습법 템플릿 |

---

## 11. 문제 해결 체크리스트

- [ ] Docker 실행 중인가? (`docker ps`)
- [ ] n8n 컨테이너 실행 중인가? (`docker ps | grep n8n`)
- [ ] http://localhost:5678 접속 되는가?
- [ ] GitHub credential 설정했는가?
- [ ] Gemini API credential 설정했는가?
- [ ] Workflow Active 상태인가?
- [ ] Obsidian Git auto-pull 설정되어 있는가?
