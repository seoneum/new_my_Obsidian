# new_my_Obsidian

이 레포지토리를 Obsidian과 연결하는 방법을 안내합니다.

## 방법 1: Obsidian Git 플러그인 사용 (추천)

가장 쉽고 자동화된 방법입니다.

### 1단계: 사전 준비
- Git이 컴퓨터에 설치되어 있어야 합니다
  - Windows: [Git for Windows](https://git-scm.com/download/win) 다운로드 및 설치
  - Mac: Terminal에서 `git --version` 입력 (없으면 자동 설치 안내)
  - Linux: `sudo apt install git` 또는 `sudo yum install git`
- GitHub 계정이 있어야 합니다
- Obsidian이 설치되어 있어야 합니다

### 2단계: 레포지토리 클론하기
- 레포지토리를 저장할 폴더를 선택합니다
  - 예: `C:\Users\사용자명\Documents\ObsidianVaults` (Windows)
  - 예: `~/Documents/ObsidianVaults` (Mac/Linux)
- Terminal 또는 명령 프롬프트를 열고 해당 폴더로 이동합니다
  ```bash
  cd ~/Documents/ObsidianVaults
  ```
- 다음 명령어로 레포지토리를 클론합니다
  ```bash
  git clone https://github.com/seoneum/new_my_Obsidian.git
  ```
- 클론이 완료되면 `new_my_Obsidian` 폴더가 생성됩니다

### 3단계: Obsidian에서 Vault로 열기
- Obsidian을 실행합니다
- 좌측 하단의 "Open another vault" 또는 "다른 보관함 열기" 아이콘을 클릭합니다
- "Open folder as vault" 또는 "폴더를 보관함으로 열기"를 선택합니다
- 클론한 `new_my_Obsidian` 폴더를 선택합니다
- "Trust author and enable plugins" 또는 "작성자 신뢰 및 플러그인 활성화"를 선택합니다 (나중에 플러그인 설치 시 필요)

### 4단계: Obsidian Git 플러그인 설치
- Obsidian 설정(⚙️)을 엽니다
- 왼쪽 메뉴에서 "Community plugins" 또는 "커뮤니티 플러그인"을 클릭합니다
- "Turn on community plugins" 또는 "커뮤니티 플러그인 켜기"를 활성화합니다
- "Browse" 또는 "찾아보기" 버튼을 클릭합니다
- 검색창에 "Obsidian Git"을 입력합니다
- "Obsidian Git" 플러그인을 찾아 "Install"을 클릭합니다
- 설치 완료 후 "Enable"을 클릭하여 활성화합니다

### 5단계: Obsidian Git 플러그인 설정
- 설정 > Community plugins > Obsidian Git 옆의 톱니바퀴 아이콘을 클릭합니다
- 주요 설정 항목:
  - **Vault backup interval**: 자동 백업 주기 (기본값: 0 = 비활성화)
    - 예: 10분마다 자동 백업하려면 `10` 입력
  - **Auto pull interval**: 자동 동기화 주기 (기본값: 0 = 비활성화)
    - 예: 10분마다 자동으로 받아오려면 `10` 입력
  - **Commit message**: 커밋 메시지 형식
    - 기본값: `vault backup: {{date}}`
  - **Pull updates on startup**: Obsidian 실행 시 자동으로 최신 내용 받아오기 (권장: 활성화)
  - **Push on backup**: 백업 시 자동으로 GitHub에 푸시하기 (권장: 활성화)

### 6단계: Git 인증 설정
GitHub에 푸시하려면 인증이 필요합니다.

#### 방법 A: Personal Access Token (추천)
- GitHub 웹사이트에 로그인합니다
- Settings > Developer settings > Personal access tokens > Tokens (classic)로 이동합니다
- "Generate new token (classic)"을 클릭합니다
- Note에 "Obsidian Git"이라고 입력합니다
- Expiration은 원하는 기간을 선택합니다 (예: 90 days 또는 No expiration)
- Scopes에서 `repo` 전체를 체크합니다
- "Generate token"을 클릭합니다
- 생성된 토큰을 복사합니다 (한 번만 표시되므로 안전한 곳에 보관)
- Terminal에서 다음 명령어를 실행합니다 (토큰을 비밀번호로 사용):
  ```bash
  cd ~/Documents/ObsidianVaults/new_my_Obsidian
  git config credential.helper store
  git pull
  ```
- Username에 GitHub 사용자명을 입력합니다
- Password에 복사한 Personal Access Token을 붙여넣습니다

#### 방법 B: SSH Key (고급 사용자용)
- SSH 키가 없다면 생성합니다:
  ```bash
  ssh-keygen -t ed25519 -C "your_email@example.com"
  ```
- 공개 키를 복사합니다:
  ```bash
  cat ~/.ssh/id_ed25519.pub
  ```
- GitHub Settings > SSH and GPG keys > New SSH key에 추가합니다
- 레포지토리 URL을 SSH로 변경합니다:
  ```bash
  cd ~/Documents/ObsidianVaults/new_my_Obsidian
  git remote set-url origin git@github.com:seoneum/new_my_Obsidian.git
  ```

### 7단계: 사용하기
- Obsidian에서 노트를 작성하거나 수정합니다
- 변경사항을 GitHub에 저장하는 방법:
  - **자동**: 플러그인 설정에서 지정한 시간마다 자동으로 백업됩니다
  - **수동**: Command Palette (Ctrl/Cmd + P)를 열고 "Obsidian Git: Commit all changes"를 검색하여 실행합니다
- 다른 기기의 변경사항을 받아오는 방법:
  - **자동**: 플러그인 설정에서 지정한 시간마다 자동으로 동기화됩니다
  - **수동**: Command Palette에서 "Obsidian Git: Pull"을 실행합니다

## 방법 2: Git 직접 사용

플러그인 없이 Git 명령어를 직접 사용하는 방법입니다.

### 1~3단계: 위의 방법 1과 동일
- 사전 준비, 레포지토리 클론, Obsidian에서 Vault로 열기는 동일합니다

### 4단계: Git 워크플로우
- 변경사항 확인:
  ```bash
  cd ~/Documents/ObsidianVaults/new_my_Obsidian
  git status
  ```
- 변경사항 스테이징:
  ```bash
  git add .
  ```
- 커밋:
  ```bash
  git commit -m "노트 업데이트"
  ```
- GitHub에 푸시:
  ```bash
  git push
  ```
- 최신 내용 받아오기:
  ```bash
  git pull
  ```

### 5단계: .gitignore 설정 (선택사항)
Obsidian 설정 파일 중 일부는 GitHub에 올리지 않는 것이 좋습니다.

`.gitignore` 파일을 생성하고 다음 내용을 추가합니다:
```
.obsidian/workspace.json
.obsidian/workspace-mobile.json
.obsidian/cache
.trash/
```

## 방법 3: 심볼릭 링크 사용

기존 Obsidian Vault가 있고 그것을 이 레포지토리와 연결하고 싶을 때 사용합니다.

### 1단계: 기존 Vault 백업
- 기존 Obsidian Vault를 다른 곳에 백업합니다

### 2단계: 레포지토리 클론
- 원하는 위치에 이 레포지토리를 클론합니다
  ```bash
  git clone https://github.com/seoneum/new_my_Obsidian.git
  ```

### 3단계: 기존 내용 복사
- 기존 Vault의 내용을 클론한 폴더로 복사합니다
  ```bash
  cp -r ~/기존Vault경로/* ~/Documents/ObsidianVaults/new_my_Obsidian/
  ```

### 4단계: Obsidian 재설정
- Obsidian에서 기존 Vault를 닫습니다
- 클론한 `new_my_Obsidian` 폴더를 Vault로 엽니다
- 이후 방법 1 또는 방법 2를 따라 Git 동기화를 설정합니다

## 여러 기기에서 사용하기

### 첫 번째 기기 (위의 설정 완료 후)
- 노트를 작성하고 변경사항을 커밋 및 푸시합니다

### 두 번째 기기
- 위의 1~3단계를 따라 레포지토리를 클론하고 Obsidian에서 엽니다
- Obsidian Git 플러그인을 설치하고 설정합니다 (방법 1 사용 시)
- 작업 전후로 항상 Pull과 Push를 수행하여 동기화합니다

### 충돌 해결
- 두 기기에서 동시에 같은 파일을 수정하면 충돌이 발생할 수 있습니다
- 충돌 발생 시:
  - Obsidian Git 플러그인이 자동으로 알림을 표시합니다
  - Terminal에서 `git status`로 충돌 파일을 확인합니다
  - 충돌 파일을 열어 수동으로 수정합니다
  - 수정 후 `git add .`, `git commit`, `git push`를 실행합니다

## 팁과 권장사항

- ✅ **정기적인 동기화**: 작업 시작 전에 Pull, 작업 완료 후에 Push를 습관화하세요
- ✅ **자동 백업 설정**: Obsidian Git 플러그인의 자동 백업을 활성화하면 편리합니다
- ✅ **의미 있는 커밋 메시지**: 변경사항을 쉽게 파악할 수 있도록 명확한 메시지를 작성하세요
- ✅ **.gitignore 활용**: 불필요한 파일은 제외하여 레포지토리를 깔끔하게 유지하세요
- ⚠️ **대용량 파일 주의**: Git은 대용량 파일(이미지, 동영상)에 적합하지 않습니다. 필요하다면 Git LFS를 고려하세요
- ⚠️ **민감한 정보**: 개인정보나 비밀번호가 포함된 노트는 private 레포지토리를 사용하세요

## 문제 해결

### "fatal: Authentication failed" 에러
- Personal Access Token이 만료되었거나 잘못되었습니다
- 6단계의 Git 인증 설정을 다시 수행하세요

### "conflict" 또는 충돌 메시지
- 여러 기기에서 동시에 수정하여 충돌이 발생했습니다
- 충돌 파일을 열어 수동으로 해결하고 다시 커밋하세요

### Obsidian Git 플러그인이 동작하지 않음
- 설정에서 플러그인이 활성화되어 있는지 확인하세요
- Git이 올바르게 설치되어 있는지 확인하세요 (Terminal에서 `git --version`)
- Obsidian을 재시작해보세요

### 푸시 권한 없음 ("Permission denied")
- 레포지토리에 대한 쓰기 권한이 있는지 확인하세요
- SSH를 사용하는 경우 SSH 키가 GitHub에 등록되어 있는지 확인하세요

## 추가 리소스

- [Obsidian 공식 문서](https://help.obsidian.md/)
- [Obsidian Git 플러그인 문서](https://github.com/denolehov/obsidian-git)
- [Git 기초 가이드](https://git-scm.com/book/ko/v2)
- [GitHub 문서](https://docs.github.com/ko)