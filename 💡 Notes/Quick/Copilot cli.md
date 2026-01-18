---
aliases:
  - Copilot
tags:
  - Git
  - Github
  - Guideline
  - Linux
  - Terminal
  - Syntax
author:
  - "[[김선음]]"
created: 2025-12-18
index: 🏷️Software
migrated_from: CMDS/100. Inbox/110. Software/111. Git/Copilot cli.md
updated: 2026-01-18T16:42:53
cmds: inbox
---
# Download copilot cli

## nvm 설치 (이미 있다면 생략)
```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
source ~/.zshrc  # 또는 source ~/.bashrc
```

## Node.js v22 설치 및 사용
```bash
nvm install 22
nvm use 22
```

## Copilot 설치
```bash
npm install -g @github/copilot
```
나머지는 로그인해서 고고링~~