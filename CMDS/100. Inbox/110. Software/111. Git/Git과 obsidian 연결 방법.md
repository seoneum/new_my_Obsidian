- ## 0) 목표 정리(권장 구조)
    
    - **Repo 1: 개발(업데이트)용**
        - 소스 코드, 설정, 문서, 테스트, CI 등 “계속 작업하는 모든 것”
        - 브랜치: `main`(안정) + `dev`(개발) 정도만 유지(필요 시 기능 브랜치는 짧게)
    - **Repo 2: 배포판(릴리즈 산출물)용**
        - 빌드 결과물(예: `/dist`, `/build`, 실행파일, 패키지 zip 등)만 올리거나, “배포에 필요한 최소 파일”만 관리
        - 브랜치: `main` 하나만 (태그로 버전 표시)

---

- ## 1) 준비물(로컬/깃허브 인증)
    
    - ### 1-1. Git 설치 확인
        
        - `git --version`
    - ### 1-2. Git 사용자 정보 설정(최초 1회)
        
        - `git config --global user.name "내이름"`
        - `git config --global user.email "내이메일@example.com"`
    - ### 1-3. GitHub 로그인(택 1)
        
        - **(추천) SSH**
            - SSH 키 존재 확인: `ls -al ~/.ssh`
            - 새 키 생성(없으면):
                - `ssh-keygen -t ed25519 -C "내이메일@example.com"`
            - ssh-agent 등록:
                - `eval "$(ssh-agent -s)"`
                - `ssh-add ~/.ssh/id_ed25519`
            - 공개키 복사:
                - `cat ~/.ssh/id_ed25519.pub`
            - GitHub → **Settings → SSH and GPG keys** → **New SSH key**에 붙여넣기
            - 연결 테스트:
                - `ssh -T git@github.com`
        - **HTTPS**
            - GitHub는 비밀번호 대신 **PAT(Personal Access Token)** 필요
            - GitHub → Settings → Developer settings → Personal access tokens 발급 후 사용

---

- ## 2) “지금 폴더가 git에 연결돼 있음” 상태 점검(중요)
    
    - 작업 폴더로 이동:
        - `cd /path/to/my-folder`
    - 현재 Git 상태 확인:
        - `git status`
        - `git remote -v` (원격 연결 여부/주소 확인)
        - `git branch --all` (브랜치 난립 확인)
        - `git log --oneline --decorate --graph --all -n 30` (히스토리 확인)
    - **안전장치(강력 권장)**: 백업
        - 폴더를 통째로 복사(탐색기/파인더로 복사해도 됨)
        - 또는 현재 브랜치/커밋을 기록해두기:
            - `git rev-parse --abbrev-ref HEAD`
            - `git rev-parse HEAD`

---

- ## 3) 브랜치가 너무 복잡해서 “초기화(새로 시작)”하고 싶은 경우(권장 절차)
    
    - 여기서 말하는 초기화는 보통 둘 중 하나임:
        - **A안: Git 히스토리/브랜치 전부 버리고, 현재 파일 상태로 새 repo 시작(가장 깔끔)**
        - **B안: 기존 히스토리는 유지하되, 브랜치만 정리**
    - 사용자가 “repository를 초기화” + “브랜치 너무 분기”라고 했으니 **A안**을 먼저 제시함.

---

- ## 4) A안: 히스토리/브랜치 싹 버리고 “현재 작업폴더 내용만” 새 repo로 시작
    
    - ### 4-1. 기존 `.git` 제거(= Git 기록/브랜치/원격 연결 전부 제거)
        
        - **주의**: 이걸 하면 과거 커밋 히스토리 복구가 매우 번거로움(백업 권장).
        - 실행:
            - `rm -rf .git`
    - ### 4-2. 새 Git 저장소 초기화
        
        - `git init`
    - ### 4-3. 기본 브랜치 이름을 `main`으로 맞추기(권장)
        
        - `git branch -M main`
    - ### 4-4. 무시 파일 추가(필수)
        
        - 프로젝트에 맞는 `.gitignore` 생성/수정
        - 예시(일반):
            - `node_modules/`
            - `.env`
            - `dist/` (배포 repo로 따로 관리할 거면 개발 repo에서는 무시하는 편이 많음)
            - `.DS_Store`
            - `.idea/`
            - `.vscode/`(팀 규칙에 따라)
    - ### 4-5. 첫 커밋 만들기
        
        - `git add .`
        - `git commit -m "chore: initial commit"`

---

- ## 5) GitHub에 repo 2개 만들기(개발용/배포용)
    
    - ### 5-1. GitHub 웹에서 생성(기본)
        
        - GitHub → **New repository**
        - Repo 이름 예:
            - 개발용: `myproject`
            - 배포용: `myproject-release` 또는 `myproject-deploy`
        - 옵션:
            - **README, .gitignore, license**는 로컬에서 이미 만들었다면 GitHub에서 굳이 추가하지 않아도 됨(충돌 방지)
    - ### 5-2. (선택) GitHub CLI로 생성(편하면)
        
        - `gh auth login`
        - 개발 repo:
            - `gh repo create myproject --private --source=. --remote=origin --push`
                - 이 경우 자동으로 origin 연결 + 푸시까지 됨
        - 배포 repo는 별도 폴더/별도 작업 흐름이므로 보통 따로 생성만 해둠:
            - `gh repo create myproject-release --private`

---

- ## 6) 개발용 Repo에 “연결 + push” (로컬 폴더 → GitHub)
    
    - 아래는 GitHub 웹에서 repo 만든 뒤, 로컬에서 연결하는 표준 흐름.
    - ### 6-1. 원격(origin) 연결
        
        - SSH 예:
            - `git remote add origin git@github.com:<username>/myproject.git`
        - HTTPS 예:
            - `git remote add origin https://github.com/<username>/myproject.git`
        - 확인:
            - `git remote -v`
    - ### 6-2. 첫 push (업스트림 설정 포함)
        
        - `git push -u origin main`
    - ### 6-3. 이후부터는
        
        - `git push`
        - `git pull` 또는 `git pull --rebase`(팀 규칙에 따라)

---

- ## 7) 브랜치 전략(“딱 필요한 것만” 유지)
    
    - ### 7-1. 최소 브랜치 권장안
        
        - 개발 repo:
            - `main`: 안정/배포 기준(항상 빌드 가능 상태)
            - `dev`: 일상 개발
            - 기능 브랜치: 필요할 때만 `feat/...`, 끝나면 머지 후 삭제
        - 배포 repo:
            - `main`만
    - ### 7-2. dev 브랜치 생성 및 푸시
        
        - `git checkout -b dev`
        - `git push -u origin dev`
    - ### 7-3. 브랜치 목록 보기
        
        - 로컬:
            - `git branch`
        - 원격 포함:
            - `git branch -a`
    - ### 7-4. 브랜치 삭제(정리 핵심)
        
        - 로컬 브랜치 삭제(머지된 것만):
            - `git branch -d branch_name`
        - 로컬 브랜치 강제 삭제(주의):
            - `git branch -D branch_name`
        - 원격 브랜치 삭제:
            - `git push origin --delete branch_name`
    - ### 7-5. 브랜치 이름 변경(예: master → main)
        
        - 로컬 브랜치 rename:
            - `git branch -m old new`
        - 원격에 반영:
            - `git push origin -u new`
            - `git push origin --delete old`
    - ### 7-6. 기본 브랜치 설정(GitHub에서)
        
        - GitHub repo → **Settings → Branches → Default branch**를 `main`으로 지정
        - `main` 보호 규칙(선택):
            - PR로만 머지, 직접 push 제한 등

---

- ## 8) 버전 관리(릴리즈/태그) “배포판”을 깔끔하게 만드는 방법
    
    - ### 8-1. SemVer(권장): `MAJOR.MINOR.PATCH`
        
        - 예: `v1.0.0`, `v1.1.0`, `v1.1.1`
    - ### 8-2. 태그 찍기(개발 repo에서 안정 커밋에)
        
        - 현재 커밋에 태그:
            - `git tag v1.0.0`
        - 주석(annotated) 태그(권장):
            - `git tag -a v1.0.0 -m "release v1.0.0"`
        - 태그 푸시:
            - `git push origin v1.0.0`
        - 태그 전체 푸시:
            - `git push origin --tags`
    - ### 8-3. GitHub Release 만들기(선택)
        
        - GitHub → Releases → Draft a new release
        - Tag 선택 후 릴리즈 노트 작성, 빌드 산출물 첨부 가능

---

- ## 9) “배포판 Repo” 운영 방식(2가지 중 선택)
    
    - 사용 목적에 따라 달라짐. 아래 중 하나를 고르면 깔끔해짐.
        
    - ### 9-A) 수동 업로드(가장 단순)
        
        - 배포 repo를 별도 폴더로 클론:
            - `cd ..`
            - `git clone git@github.com:<username>/myproject-release.git`
        - 배포 산출물(예: 개발 repo의 `dist/`)만 복사해서 커밋/푸시
            - `cp -R ../myproject/dist/* ./` (환경에 맞게)
            - `git add .`
            - `git commit -m "release: v1.0.0"`
            - `git tag -a v1.0.0 -m "release v1.0.0"` (배포 repo에도 동일 태그 권장)
            - `git push --follow-tags`
    - ### 9-B) 개발 repo에서 “서브트리(subtree)로 배포 repo에 푸시”(깔끔/자동화 쉬움)
        
        - 장점: 개발 repo에서 한 번의 명령으로 배포 repo에 `dist/`만 밀어넣기 가능
        - 흐름(개념):
            - 개발 repo는 정상대로 관리
            - 빌드 결과가 `dist/`에 생성되면 그 폴더만 배포 repo의 `main`으로 푸시
        - 예시(개발 repo에서):
            - 배포 원격 추가:
                - `git remote add deploy git@github.com:<username>/myproject-release.git`
            - 빌드 산출물 생성(프로젝트별):
                - `npm run build` 또는 `pnpm build` 등
            - `dist/`만 커밋되도록 별도 커밋(또는 임시 커밋) 만든 뒤 subtree push:
                - (중요) 개발 repo에서는 보통 `dist/`를 `.gitignore` 처리하는데, subtree 방식은 설정이 좀 더 필요함
                - 이 부분은 프로젝트 스택(Node/파이썬/Unity 등)에 따라 “추천 방식”이 갈려서, 네 프로젝트 종류를 알면 딱 맞춰 정리해줄 수 있음
        - 대안(현실적으로 많이 씀):
            - GitHub Actions로 빌드 → 배포 repo로 push(가장 자동화/안전)

---

- ## 10) 자주 쓰는 기본 명령어 모음(실수 방지용)
    
    - ### 변경 확인/스테이징/커밋
        
        - `git status`
        - `git diff`
        - `git add .`
        - `git commit -m "type: message"`
    - ### 최신 반영
        
        - `git pull`
        - (rebase 선호 시) `git pull --rebase`
    - ### 로그/히스토리
        
        - `git log --oneline --decorate --graph -n 20`
    - ### 원격/브랜치
        
        - `git remote -v`
        - `git fetch --all --prune` (원격에서 삭제된 브랜치 정리)
    - ### 태그
        
        - `git tag`
        - `git show v1.0.0`

---

- ## 11) 자주 터지는 문제 & 해결
    
    - ### 11-1. push 거부(권한/인증)
        
        - SSH 확인: `ssh -T git@github.com`
        - 원격 주소가 HTTPS인데 토큰이 필요한 경우:
            - 원격 URL 확인: `git remote -v`
            - SSH로 변경:
                - `git remote set-url origin git@github.com:<username>/myproject.git`
    - ### 11-2. “현재 브랜치가 main이 아닌데 push가 이상함”
        
        - 현재 브랜치 확인:
            - `git branch --show-current`
        - main으로 이동/생성:
            - `git checkout -B main`
            - `git push -u origin main`
    - ### 11-3. 원격 브랜치가 너무 많음(정리)
        
        - 원격 브랜치 확인:
            - `git branch -r`
        - 필요 없는 원격 브랜치 삭제:
            - `git push origin --delete <branch>`
        - 로컬에 남은 추적 브랜치 정리:
            - `git fetch --prune`

---

- ## 12) 네 상황에 맞춘 “가장 깔끔한 실행 순서”(요약 체크리스트)
    
    - 백업 폴더 복사
    - 작업 폴더에서 `.git` 제거 → `git init`
    - `.gitignore` 정리 → `git add .` → `git commit`
    - GitHub에 개발 repo 생성 → `git remote add origin ...` → `git push -u origin main`
    - `dev` 브랜치 생성 → `git push -u origin dev`
    - GitHub에서 기본 브랜치 `main` 설정 + 보호 규칙(선택)
    - 배포 repo 생성
    - 배포 방식 선택(수동 / Actions / subtree)
    - 릴리즈 시점에 태그(`vX.Y.Z`) 찍고 Release 작성

---

- ## 13) 내가 너한테 확인해야 “배포 repo”까지 완벽하게 맞춰줄 수 있는 질문(짧게 답해줘)
    
    - 프로젝트 종류가 뭐야? (예: React/Vite, Next.js, Python, Unity, Rust 등)
    - 배포 repo에는 **정적 파일(dist)**만 올릴 거야, 아니면 **소스+빌드** 둘 다?
    - GitHub Pages 배포가 목적이야, 아니면 서버/스토어에 업로드할 실행파일 배포야?
    - 지금 로컬 폴더가 하나야, 아니면 여러 폴더를 각각 GitHub에 올릴 거야?