---
type: reference
title: Oh My OpenCode 완벽 가이드
created: 2026-01-15
updated: 2026-01-18T16:42:53
author:
  - "[[김선음]]"
group: SE
status:
  - "[[🌲Evergreen]]"
tags:
  - opencode
  - ai-agent
  - claude
  - gemini
  - chatgpt
  - terminal
  - automation
  - coding
aliases:
  - oh-my-opencode
  - OpenCode 설정
  - Sisyphus
source: https://github.com/code-yeongyu/oh-my-opencode
migrated_from: CMDS/400. Reference/410. Software_Reference/R - Oh My OpenCode 완벽 가이드.md
domain:
  - cs
cmds: connect
---

# Oh My OpenCode 완벽 가이드

> [!abstract] TL;DR
> **OpenCode**를 위한 최고의 Agent Harness. Claude, ChatGPT, Gemini 구독을 활용해 AI 팀을 구성하고 자동화된 코딩 워크플로우를 구축할 수 있다.

---

## 📌 핵심 개념

### Oh My OpenCode란?
- **OpenCode**: Claude Code의 오픈소스 대안, 터미널 기반 AI 코딩 도구
- **Oh My OpenCode**: OpenCode를 위한 플러그인/설정 프레임워크
- **Sisyphus**: 메인 AI 에이전트 (Claude Opus 4.5)
- 장점:
	- 무한 확장 가능, 무한 커스터마이징
	- 화면 깜빡임 없음
	- LSP, 린터, 포맷터 자동 활성화
	- 모델 믹스 앤 매치 가능
	- 고성능, 아름다운 터미널 UI

### 🪄 매직 키워드: `ultrawork`
- 프롬프트에 `ultrawork` (또는 `ulw`) 포함하면 모든 기능 자동 활성화
- 병렬 에이전트, 백그라운드 태스크, 깊은 탐색, 완료까지 끊임없는 실행

---

## 🤖 Sisyphus 에이전트 팀

> [!info] 핵심 아이디어
> LLM 에이전트도 우리처럼 일할 수 있다 - 좋은 도구와 팀원만 주면 된다.

### 메인 에이전트
| 에이전트 | 모델 | 역할 |
|----------|------|------|
| **Sisyphus** | `anthropic/claude-opus-4-5` | 메인 오케스트레이터, 32k 사고 예산 |
| **Oracle** | `openai/gpt-5.2` | 아키텍처, 코드 리뷰, 전략 |
| **Librarian** | `opencode/glm-4.7-free` | 멀티 레포 분석, 문서 조회, 구현 예시 |
| **Explore** | `opencode/grok-code` | 빠른 코드베이스 탐색, 패턴 매칭 |

### 전문 에이전트
| 에이전트 | 모델 | 역할 |
|----------|------|------|
| **Frontend UI/UX Engineer** | `google/gemini-3-pro-preview` | 아름다운 UI 구축 |
| **Document Writer** | `google/gemini-3-flash` | 기술 문서 작성 |
| **Multimodal Looker** | `google/gemini-3-flash` | PDF, 이미지, 다이어그램 분석 |

### 에이전트 호출 방법
```
Ask @oracle to review this design and propose an architecture
Ask @librarian how this is implemented
Ask @explore for the policy on this feature
```

---

## 🛠️ 설치 가이드

### 사전 요구사항
- **Bun** 필수 (런타임 의존성)
```bash
curl -fsSL https://bun.sh/install | bash
```

### Step 1: OpenCode 설치
```bash
# 설치 확인
if command -v opencode &> /dev/null; then 
  echo "OpenCode $(opencode --version) is installed"
else
  echo "OpenCode is not installed"
  # https://opencode.ai/docs 참고
fi
```

### Step 2: Oh My OpenCode 설치
```bash
bunx oh-my-opencode install
# 또는
npx oh-my-opencode install
```

### Step 3: 구독별 설치 옵션
```bash
# 모든 구독 있는 경우 (Claude max20)
bunx oh-my-opencode install --no-tui \
  --claude=max20 --chatgpt=yes --gemini=yes

# Claude만 있는 경우
bunx oh-my-opencode install --no-tui \
  --claude=yes --chatgpt=no --gemini=no

# 구독 없는 경우
bunx oh-my-opencode install --no-tui \
  --claude=no --chatgpt=no --gemini=no
```

### Step 4: 설치 확인
```bash
opencode --version  # 1.0.150 이상
cat ~/.config/opencode/opencode.json  # oh-my-opencode 포함 확인
```

---

## 🔐 인증 설정

### Claude (Anthropic)
```bash
opencode auth login
# Provider: Anthropic 선택
# Login method: Claude Pro/Max 선택
# 브라우저에서 OAuth 진행
```

### Google Gemini (Antigravity OAuth)
1. **플러그인 추가** (`opencode.json`):
```json
{
  "plugin": [
    "oh-my-opencode",
    "opencode-antigravity-auth@1.2.8"
  ]
}
```

2. **모델 오버라이드** (`oh-my-opencode.json`):
```json
{
  "agents": {
    "frontend-ui-ux-engineer": {
      "model": "google/antigravity-gemini-3-pro-high"
    },
    "document-writer": {
      "model": "google/antigravity-gemini-3-flash"
    }
  }
}
```

3. **인증**:
```bash
opencode auth login
# Provider: Google 선택
# Login method: OAuth with Google (Antigravity) 선택
```

> [!tip] 멀티 계정 로드 밸런싱
> 최대 10개 Google 계정 지원. 한 계정 rate limit 시 자동 전환.

### GitHub Copilot (폴백)
```bash
bunx oh-my-opencode install --no-tui \
  --claude=no --chatgpt=no --gemini=no --copilot=yes
  
opencode auth login
# Provider: GitHub → OAuth
```

---

## 🔧 주요 도구들

### LSP 도구 (IDE 수준의 기능)
| 도구 | 설명 |
|------|------|
| `lsp_goto_definition` | 심볼 정의로 이동 |
| `lsp_find_references` | 워크스페이스 전체에서 사용처 찾기 |
| `lsp_symbols` | 파일/워크스페이스 심볼 조회 |
| `lsp_diagnostics` | 빌드 전 에러/경고 확인 |
| `lsp_rename` | 워크스페이스 전체 리네임 |
| `ast_grep_search` | AST 기반 코드 패턴 검색 (25개 언어) |
| `ast_grep_replace` | AST 기반 코드 치환 |

### 에이전트 도구
| 도구 | 설명 |
|------|------|
| `call_omo_agent` | 전문 에이전트 호출 (`run_in_background` 지원) |
| `sisyphus_task` | 카테고리 기반 태스크 위임 |
| `background_output` | 백그라운드 결과 조회 |
| `background_cancel` | 백그라운드 작업 취소 |

### 세션 도구
| 도구 | 설명 |
|------|------|
| `session_list` | 세션 목록 |
| `session_read` | 세션 내용 읽기 |
| `session_search` | 세션 전체 텍스트 검색 |
| `session_info` | 세션 메타데이터 |

### 내장 MCP
| MCP | 설명 |
|-----|------|
| **Exa** | 실시간 웹 검색 |
| **Context7** | 공식 문서 조회 |
| **Grep.app** | GitHub 코드 검색 |

---

## ⚙️ 설정 파일

### 설정 파일 위치 (우선순위 순)
1. `.opencode/oh-my-opencode.json` (프로젝트)
2. `~/.config/opencode/oh-my-opencode.json` (사용자)

### 스키마 자동완성
```json
{
  "$schema": "https://raw.githubusercontent.com/code-yeongyu/oh-my-opencode/master/assets/oh-my-opencode.schema.json"
}
```

### 에이전트 커스터마이징
```json
{
  "agents": {
    "explore": {
      "model": "anthropic/claude-haiku-4-5",
      "temperature": 0.5
    },
    "frontend-ui-ux-engineer": {
      "disable": true
    },
    "librarian": {
      "prompt_append": "Always use elisp-dev-mcp for Emacs Lisp."
    }
  }
}
```

### 권한 설정
```json
{
  "agents": {
    "explore": {
      "permission": {
        "edit": "deny",
        "bash": "ask",
        "webfetch": "allow"
      }
    }
  }
}
```

> [!info] 권한 옵션
> `allow` | `ask` | `deny`
> 항목: `edit`, `bash`, `webfetch`, `doom_loop`, `external_directory`

### 에이전트 비활성화
```json
{
  "disabled_agents": ["oracle", "frontend-ui-ux-engineer"]
}
```

---

## 🏷️ 카테고리 (태스크 위임)

### 기본 카테고리
| 카테고리 | 모델 | 용도 |
|----------|------|------|
| `visual` | `google/gemini-3-pro-preview` | UI/UX |
| `business-logic` | `openai/gpt-5.2` | 비즈니스 로직 |

### 사용법
```javascript
// 카테고리로 위임
sisyphus_task(category="visual", prompt="Create a dashboard")
sisyphus_task(category="business-logic", prompt="Payment flow")

// 직접 에이전트 지정
sisyphus_task(agent="oracle", prompt="Review architecture")
```

### 커스텀 카테고리 추가
```json
{
  "categories": {
    "data-science": {
      "model": "anthropic/claude-sonnet-4-5",
      "temperature": 0.2,
      "prompt_append": "Focus on data analysis and ML pipelines."
    }
  }
}
```

---

## 🔄 백그라운드 작업

### 병렬 에이전트 사용 예시
- GPT가 디버깅하는 동안 Claude가 다른 접근법 시도
- Gemini가 프론트엔드 작업하는 동안 Claude가 백엔드 처리
- 대규모 병렬 검색 후 결과로 구현 완료

### 동시성 설정
```json
{
  "background_task": {
    "defaultConcurrency": 5,
    "providerConcurrency": {
      "anthropic": 3,
      "openai": 5,
      "google": 10
    },
    "modelConcurrency": {
      "anthropic/claude-opus-4-5": 2,
      "google/gemini-3-flash": 10
    }
  }
}
```

> [!info] 우선순위
> `modelConcurrency` > `providerConcurrency` > `defaultConcurrency`

---

## 📁 컨텍스트 자동 주입

### AGENTS.md 계층 주입
```
project/
├── AGENTS.md              # 프로젝트 전체 컨텍스트
├── src/
│   ├── AGENTS.md          # src 특화 컨텍스트
│   └── components/
│       ├── AGENTS.md      # 컴포넌트 특화 컨텍스트
│       └── Button.tsx     # 읽으면 3개 AGENTS.md 모두 주입
```

### 조건부 규칙 (.claude/rules/)
```yaml
---
globs: ["*.ts", "src/**/*.js"]
description: "TypeScript/JavaScript 코딩 규칙"
---
- Use PascalCase for interface names
- Use camelCase for function names
```

---

## 🧰 내장 스킬

| 스킬 | 설명 |
|------|------|
| **playwright** | 브라우저 자동화 (스크래핑, 테스트, 스크린샷) |
| **git-master** | Git 전문가 (커밋, rebase, bisect, log) |

### Git Master 설정
```json
{
  "git_master": {
    "commit_footer": true,
    "include_co_authored_by": true
  }
}
```

### 스킬 비활성화
```json
{
  "disabled_skills": ["playwright"]
}
```

---

## 🗑️ 삭제 방법

```bash
# jq 사용
jq 'del(.plugin[] | select(. == "oh-my-opencode"))' \
  ~/.config/opencode/opencode.json > tmp && mv tmp ~/.config/opencode/opencode.json

# 사용자 설정 삭제
rm ~/.config/opencode/oh-my-opencode.json

# 프로젝트 설정 삭제 (있는 경우)
rm .opencode/oh-my-opencode.json
```

---

## 🔗 관련 링크

- [GitHub Repository](https://github.com/code-yeongyu/oh-my-opencode)
- [OpenCode 공식 문서](https://opencode.ai/docs)
- [OpenCode LSP 문서](https://opencode.ai/docs/lsp/)
- [opencode-antigravity-auth](https://github.com/NoeFabris/opencode-antigravity-auth)
- [[n8n_setup_guide|n8n 자동화 가이드]]

---

## ✅ 빠른 시작 체크리스트

- [ ] Bun 설치 (`curl -fsSL https://bun.sh/install | bash`)
- [ ] OpenCode 설치 (https://opencode.ai/docs)
- [ ] oh-my-opencode 설치 (`bunx oh-my-opencode install`)
- [ ] 구독 정보에 맞게 옵션 설정
- [ ] Claude/Gemini/ChatGPT 인증 완료
- [ ] `opencode --version` 확인 (1.0.150+)
- [ ] 프롬프트에 `ultrawork` 입력하고 테스트!
