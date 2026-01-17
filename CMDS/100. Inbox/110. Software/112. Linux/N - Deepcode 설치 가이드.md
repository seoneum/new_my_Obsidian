---
type: inbox
title: N - Deepcode 설치 가이드
created: 2026-01-09
updated: 2026-01-09T13:21:57
author: "[[김선음]]"
group: SE
status: "[[🍂Archive]]"
tags:
  - inbox
  - note
  - tagging/needed
aliases: []
---

# N - Deepcode 설치 가이드

## Notes
- 사전 준비 - python 3.10+ , git있어야 함.
```shell
1.
git clone https://github.com/HKUDS/DeepCode.git //git clone
cd DeepCode //down파일로 이동
2.
brew install pipx
pipx install uv
->
uv --verison
3.
uv venv //아무 이름 없는 .venv 가상환경 제작
source .venv/bin/activate //가상환경 접속
4.
uv pip install -e . //종속성 패키지 설치
uv pip list

```

## Next
- [ ] 

