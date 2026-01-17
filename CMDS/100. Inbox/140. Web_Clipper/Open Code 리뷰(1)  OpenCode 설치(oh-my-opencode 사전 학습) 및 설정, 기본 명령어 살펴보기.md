---
title: "Open Code 리뷰(1) : OpenCode 설치(oh-my-opencode 사전 학습) 및 설정, 기본 명령어 살펴보기"
source_url: "https://goddaehee.tistory.com/484"
author:
  - "[[갓대희]]"
published: 2026-01-06
created: 2026-01-09
description: "안녕하세요! 갓대희 입니다.오늘은 최근 개발자 커뮤니티에서 주목받고 있는 오픈소스 AI 코딩 에이전트 OpenCode에 대해 알아보려고 한다.Claude Code의 대안을 찾거나, 다양한 LLM을 자유롭게 선택하고 싶은 개발자들에게 OpenCode가 좋은 선택지가 될 수 있다.(최종 목표로 하는 \"Oh My OpenCode\"에 대해 리뷰하기전 그 근본이 되는 \"Open Code\"에 대해 먼저 가볍게 살펴보는게 목적이다. 이후 포스팅에서 또한번 다룰 예정이니, 이번 세션에서는 가볍게 살펴보고 넘어가는 정도로 읽어봐 주시면 좋을 것 같다.)OpenCode 시리즈Part 1: OpenCode 입문 (현재 글) Part 2: oh-my-opencode 설치 및 사용방법Part 3: 오픈소스, 무료 및 저가 LL.."
tags:
  - "clippings"
---
> [!summary]+ 3줄 요약
> - OpenCode는 터미널, 데스크톱, IDE에서 사용 가능한 오픈소스 AI 코딩 에이전트로, 75개 이상의 LLM 제공자를 지원합니다.
> - 다양한 LLM 모델을 자유롭게 선택하고 로컬 모델(Ollama)을 사용하여 비용을 절감하거나 프라이버시를 강화할 수 있습니다.
> - `/init` 명령어로 프로젝트를 분석하고, `@` 문법으로 파일을 참조하며, `Tab` 키로 Build/Plan 에이전트를 전환하는 등 효율적인 개발 워크플로우를 지원합니다.


안녕하세요! 갓대희 입니다.

오늘은 최근 개발자 커뮤니티에서 주목받고 있는 오픈소스 AI 코딩 에이전트 **OpenCode** 에 대해 알아보려고 한다.  
Claude Code의 대안을 찾거나, 다양한 LLM을 자유롭게 선택하고 싶은 개발자들에게 OpenCode가 좋은 선택지가 될 수 있다.  
  
(**최종 목표로 하는 "** **Oh My OpenCode"** 에 대해 리뷰하기전 그 근본이 되는 **"Open Code"** 에 대해 먼저 가볍게 살펴보는게 목적이다. 이후 포스팅에서 또한번 다룰 예정이니, 이번 세션에서는 가볍게 살펴보고 넘어가는 정도로 읽어봐 주시면 좋을 것 같다.)

**OpenCode 시리즈**

Part 1: OpenCode 입문 (현재 글) [Part 2: oh-my-opencode 설치 및 사용방법](https://goddaehee.tistory.com/485) [Part 3: 오픈소스, 무료 및 저가 LLM 모델 활용](https://goddaehee.tistory.com/488)

### 목차

1. OpenCode란 무엇인가
	- 주요 특징
	- 왜 OpenCode인가: 비용 비교
2. 설치 방법
3. 초기 설정: LLM 제공자 연결
	- OpenCode Zen: 코딩 에이전트 최적화 모델
	- 주요 LLM 제공자 소개
4. 기본 사용법
	- 내장 명령어
	- 파일 참조하기: @ 문법
5. 에이전트 이해하기
	- Build vs Plan 에이전트
	- 커스텀 에이전트 만들기
6. 내장 도구
7. 유용한 키 바인딩
8. GitHub 연동하기
9. 실전 개발 워크플로우
10. MCP 서버 연동
11. 이상적인 유스케이스
12. 자주 묻는 질문
13. 참고 자료

**OpenCode 완전 입문 가이드**  
OpenCode는 터미널, 데스크톱, IDE에서 사용할 수 있는 오픈소스 AI 코딩 에이전트이다. 75개 이상의 LLM 제공자를 지원하며, 45,000개 이상의 GitHub 스타를 보유한 활발한 오픈소스 프로젝트이다. 이 글에서는 초급 개발자도 쉽게 따라할 수 있도록 설치부터 기본 사용법까지 단계별로 안내한다.

최근 AI 코딩 도구들이 빠르게 발전하면서 개발자들의 작업 방식도 변화하고 있다. Claude Code, Cursor, GitHub Copilot 등 다양한 도구들이 있지만, **오픈소스** 이면서 **다양한 LLM을 자유롭게 선택할 수 있는** 도구를 찾는 개발자들에게 OpenCode가 주목받고 있다.

OpenCode는 공식 문서에 따르면 "오픈소스 AI 코딩 에이전트"로, 코드를 저장하거나 외부로 전송하지 않아 프라이버시에 민감한 환경에서도 사용할 수 있다. 이 글에서는 OpenCode가 무엇인지, 어떻게 설치하고 설정하는지, 그리고 기본적인 사용법을 살펴보려고 한다.

## OpenCode란 무엇인가

OpenCode는 터미널 인터페이스, 데스크톱 앱, IDE 확장 프로그램의 세 가지 형태로 제공되는 AI 코딩 에이전트이다.

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdna%2FVc4aP%2FdJMcaaxcWoO%2FAAAAAAAAAAAAAAAAAAAAAHRTR09e7JCjayhvr4iLQMDrI8wHiLVBUFgy9g2K_wNQ%2Fimg.png%3Fcredential%3DyqXZFxpELC7KVnFOS48ylbz2pIh7yKj8%26expires%3D1769871599%26allow_ip%3D%26allow_referer%3D%26signature%3DJBsmP%252F2OeVsb7BobmQZ4b1fXF1c%253D)

**SST(Serverless Stack) 팀** 이 개발하고 있으며, 공식 웹사이트에 따르면 월 650,000명 이상의 개발자가 사용하고 있고 500명 이상의 기여자가 참여하는 활발한 오픈소스 프로젝트이다.

**공식 문서 출처**  
OpenCode는 코드나 컨텍스트 데이터를 저장하지 않으므로 프라이버시에 민감한 환경에서 운영할 수 있다.  
[OpenCode 공식 웹사이트](https://opencode.ai/)

### 주요 특징

| 특징 | 설명 |
| --- | --- |
| 다양한 실행 환경 | 터미널, 데스크톱 앱, IDE 확장 프로그램 지원 |
| 75+ LLM 제공자 | Claude, GPT, Gemini, 로컬 모델(Ollama) 등 |
| 프라이버시 보장 | 코드/컨텍스트 데이터 미저장 |
| 오픈소스 | GitHub에서 소스 코드 공개, 커뮤니티 기여 가능 |
| 병렬 에이전트 | 동일 프로젝트에서 여러 에이전트 동시 실행 가능 |

### 왜 OpenCode인가?: 비용 비교

AI 코딩 도구 시장에는 Cursor, Claude Code 등 여러 선택지가 있다.

OpenCode의 가장 큰 장점은 비용 효율성과 자유로운 모델 선택이다.

| 도구 | 비용 | 모델 선택 |
| --- | --- | --- |
| **Cursor** | 월 $20 구독료 | 제한적 |
| **Claude Code** | API 사용량 과금 또는 구독 | Claude만 사용 |
| **OpenCode** | 도구 무료 + API 사용량만 과금 | 75개 이상 자유 선택 |

OpenCode를 사용하면 기획 단계에서는 저렴한 Gemini를 사용하고, 실제 코딩에서는 Claude를 사용하는 등 상황에 맞게 모델을 전환하며 비용을 최적화할 수 있다. 로컬 모델(Ollama)을 사용하면 완전 무료로 사용하는 것도 가능하다.

## 설치 방법

OpenCode는 다양한 방법으로 설치할 수 있다. 운영체제별로 권장하는 설치 방법을 안내한다.

[https://opencode.ai/docs#install](https://opencode.ai/docs#install)

[

Intro

Get started with OpenCode.

opencode.ai

](https://opencode.ai/docs#install)

### macOS / Linux

macOS와 Linux에서는 curl 스크립트를 사용한 설치가 가장 간편하다.

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdna%2FJcpZJ%2FdJMcadm6IbB%2FAAAAAAAAAAAAAAAAAAAAACBnhiuF8CBmoefiabDm1zbVBn_h4Irkuv3jqVCHXDj1%2Fimg.png%3Fcredential%3DyqXZFxpELC7KVnFOS48ylbz2pIh7yKj8%26expires%3D1769871599%26allow_ip%3D%26allow_referer%3D%26signature%3Dkv0ImXv6qQ3HmWzkt%252FLbg%252BhJtG0%253D)

// 기본 설치 (권장)

```bash
curl -fsSL https://opencode.ai/install | bash
```

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdna%2F7OSiH%2FdJMcacIzsYs%2FAAAAAAAAAAAAAAAAAAAAAAYDUnERoiXFrld6QhRi2YWPnilwUzdQV04_0I78FcmU%2Fimg.png%3Fcredential%3DyqXZFxpELC7KVnFOS48ylbz2pIh7yKj8%26expires%3D1769871599%26allow_ip%3D%26allow_referer%3D%26signature%3D86wZ5PcK32TvvGcdvOHxRbthnNk%253D)

Homebrew를 사용하는 경우 다음 명령어로도 설치할 수 있다.

// Homebrew 설치

```armasm
brew install sst/tap/opencode
```

### Windows

Windows에서는 Chocolatey, Scoop, 또는 npm을 통해 설치할 수 있다.

// Chocolatey 설치

```cmake
choco install opencode
```

// Scoop 설치

```bash
scoop install opencode
```

### 공통: npm / Docker

Node.js가 설치되어 있다면 npm으로도 설치할 수 있다. 이 방법은 모든 운영체제에서 동일하게 작동한다.

// npm 전역 설치

```cmake
npm install -g opencode-ai
```

// pnpm, yarn, bun도 지원

```dockerfile
pnpm add -g opencode-ai
yarn global add opencode-ai
bun add -g opencode-ai
```

### 설치 확인

설치가 완료되면 터미널에서 다음 명령어로 정상 설치 여부를 확인할 수 있다.

// 버전 확인

```bash
opencode --version
```

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdna%2FbCh4Ep%2FdJMcai9NkDX%2FAAAAAAAAAAAAAAAAAAAAAOGYM4SleQbO3Z8zoUqBhSUGrq6B1rtrwu7BdcZA134T%2Fimg.png%3Fcredential%3DyqXZFxpELC7KVnFOS48ylbz2pIh7yKj8%26expires%3D1769871599%26allow_ip%3D%26allow_referer%3D%26signature%3DvO8E%252FA3eBVFpPOF5w6n7n9lVIDE%253D)

opencode 라고 입력하여 초기화면이 잘 노출되는지도 확인 가능 하다.

ex) 초기 화면

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdna%2FcnkLJp%2FdJMcacIztdu%2FAAAAAAAAAAAAAAAAAAAAAKpOtCVv_ID6iD0WZhGPcjOQzH_H8mz5DHkww3tDNnZ2%2Fimg.png%3Fcredential%3DyqXZFxpELC7KVnFOS48ylbz2pIh7yKj8%26expires%3D1769871599%26allow_ip%3D%26allow_referer%3D%26signature%3DyJLitjf71eKL5fsDeCHliKwsMrA%253D)

## 초기 설정: LLM 제공자 연결

OpenCode를 사용하려면 먼저 LLM(Large Language Model) 제공자를 연결해야 한다. OpenCode는 75개 이상의 LLM 제공자를 지원하므로, 원하는 서비스를 선택할 수 있다.

### /connect 명령으로 연결하기

가장 쉬운 방법은 `/connect` 명령을 사용하는 것이다. OpenCode를 실행한 후 이 명령을 입력하면 대화형으로 LLM 제공자를 선택하고 API 키를 입력할 수 있다.

// OpenCode 실행 후 LLM 제공자 연결

```bash
opencode
/connect
```

공식 문서에 따르면, `/connect` 명령으로 추가한 API 키는 `~/.local/share/opencode/auth.json` 에 저장된다.

**( 실제 모델 연결은 하기 별도의 섹션에서 진행 해보려 한다. 조금만 더 이론적인 내용, 최근 트렌드를 살펴보자. )**

### OpenCode Zen: 코딩 에이전트 최적화 모델

**[OpenCode Zen](https://opencode.ai/zen)** 은 OpenCode 팀이 코딩 에이전트를 위해 직접 테스트하고 벤치마킹한 큐레이션 모델 게이트웨이이다. 수많은 모델 중에서 코딩 작업에 효과적인 모델만 선별하여 제공한다. (출처: [OpenCode Zen 공식 문서](https://opencode.ai/docs/zen))

**무료 모델 (베타 기간 한정)**  
OpenCode Zen은 현재 베타 기간 동안 다음 모델들을 **무료** 로 제공한다:  
• **Grok Code Fast 2** - xAI의 최신 코딩 특화 모델 (2025년 말 업데이트)  
• **GLM 4.7** - 성능이 입증된 오픈소스 코딩 모델  
• **MiniMax M2.1** - 효율적인 중형 모델  
• **Big Pickle** - 경량 코딩 모델  
• **GPT 5 Nano** - OpenAI의 경량 버전  
※ 무료 제공 기간은 변경될 수 있으니 공식 사이트에서 확인 권장

#### GLM-4.7: 오픈소스 코딩의 새로운 표준

2025년 12월 출시된 **GLM-4.7** 은 이제 안정화 단계에 접어들었다. 약 400B 파라미터에 200K 토큰 컨텍스트를 지원하며, 유료 모델들과 대등한 성능을 보여준다.

| 벤치마크 | GLM-4.7 | 비교 |
| --- | --- | --- |
| AIME 2025 (수학 추론) | **95.7%** | GPT-5.1 (94.0%) 상회 |
| SWE-bench Verified (코딩) | **73.8%** | 오픈소스 모델 중 최상위권 |

**비용 절감 효과:**Claude 대비 약 **85% 비용 절감** 가능. "설계는 Claude, 구현은 GLM" 전략이 여전히 유효하다.

출처: [LLM Stats](https://llm-stats.com/models/glm-4.7) (2025년 12월 기준)

Zen의 가장 큰 장점은 **제로 마크업 가격 정책** 이다. 처리 수수료(신용카드 수수료 4.4% + $0.30)만 추가될 뿐, 모델 사용료는 원가 그대로 제공한다. Claude나 GPT를 직접 API로 사용하는 것과 거의 동일한 비용으로 사용할 수 있다.

**Zen 가격 예시 (100만 토큰 기준)**  
• Claude Sonnet 4.5: 입력 $3-6 / 출력 $15-22.50  
• GPT 5.2: 입력 $1.75 / 출력 $14  
• Gemini 3 Pro: 입력 $2-4 / 출력 $12-18  
※ 가격은 변동될 수 있음. [공식 페이지](https://opencode.ai/zen) 참조

프라이버시 측면에서도 Zen은 강점이 있다. 모든 모델이 미국에서 호스팅되며, 제공자들은 **제로 리텐션(zero-retention) 정책** 을 준수한다. 사용자 데이터는 모델 학습에 사용되지 않는다 (무료 모델 제외).

**Claude 비용이 부담된다면?**  
커뮤니티에서 "Claude Code 월 $100+ 나와서 OpenCode로 갈아탄다"는 후기가 종종 보인다. OpenCode + Zen 조합을 사용하면:  
• 무료 모델로 간단한 작업 처리  
• 복잡한 작업만 유료 모델 사용  
• 상황에 따라 모델 자유롭게 전환  
이런 방식으로 비용을 크게 절감할 수 있다.

### 주요 LLM 제공자 소개

| 제공자 | 특징 | API 키 발급 |
| --- | --- | --- |
| **Anthropic Claude** | 코딩 작업에 강점, 긴 컨텍스트 지원 | console.anthropic.com |
| **OpenAI GPT** | 범용성 높음, GPT-4 Turbo 지원 | platform.openai.com |
| **Google Gemini** | 멀티모달 지원, 무료 티어 제공 | aistudio.google.com |
| **Ollama (로컬)** | 로컬 실행, 무료, 프라이버시 완벽 보장 | API 키 불필요 |
| **Groq** | 빠른 추론 속도, 무료 티어 제공 | console.groq.com |

### 로컬 LLM (Ollama) 사용하기

보안이 중요하거나 비용을 절약하고 싶다면 로컬 LLM을 추천한다. **Ollama** 를 사용하면 인터넷 연결 없이도 고성능 코딩 모델을 무료로 사용할 수 있다.

#### OpenCode + Local LLM 퀵스타트

- **설치**: `brew install ollama`
- **모델 실행**: `ollama run deepseek-coder-v2`
- **OpenCode 설정**: `opencode.json` 에 로컬 주소(localhost:11434) 연결

[자세한 설정 방법: OpenCode + Local LLM 가이드 준비중](https://goddaehee.tistory.com/entry/opencode-local-llm-guide)

#### Anthropic Claude 연동 시 주의사항

OpenCode에서 Claude를 사용하는 방법은 **두 가지** 가 있으며, 각각 다른 약관이 적용된다:

| 방식 | 설명 | 위험도 |
| --- | --- | --- |
| **OAuth (Pro/Max 구독)** | Claude 구독료로 사용, 브라우저 인증 | **🔴 높음** |
| **API 키** | Console에서 키 발급, 사용량 별도 과금 | **🟢 낮음** |

**OAuth 방식의 문제점:**
- Claude Pro/Max OAuth는 원래 **Claude Code 전용** 으로 설계됨
- 제3자 도구(OpenCode)에서 사용 시 **ToS(서비스 약관) 위반 가능성** 존재
- GitHub에서 **다수의 계정 차단 사례** 가 보고됨 ([#115](https://github.com/code-yeongyu/oh-my-opencode/issues/115), [#158](https://github.com/code-yeongyu/oh-my-opencode/issues/158))
- 특히 **병렬 요청이 많은 에이전트** (Sisyphus 등) 사용 시 위험 증가

※ 정확한 차단 기준은 Anthropic이 공개하지 않음. 위 정보는 커뮤니티 보고 기반.  
약관 확인: [Consumer Terms](https://www.anthropic.com/legal/consumer-terms) (Pro/Max 구독) | [Commercial Terms](https://www.anthropic.com/legal/commercial-terms) (API 키)

### 설정 파일로 API 키 관리하기

`/connect` 외에도 설정 파일을 직접 편집하여 API 키를 관리할 수 있다. 설정 파일은 두 위치에 저장할 수 있다.

- **전역 설정**: `~/.config/opencode/opencode.json`
- **프로젝트 설정**: 프로젝트 루트의 `opencode.json`

#### opencode.json 예시

```json
{
  "model": "anthropic/claude-sonnet-4-5",
  "provider": {
    "anthropic": {
      "options": {
        "apiKey": "{env:ANTHROPIC_API_KEY}"
      }
    }
  }
}
```

공식 문서에 따르면 API 키는 환경변수(`{env:변수명}`)나 파일(`{file:경로}`)에서 읽어올 수 있어 보안에 유리하다.

**개발 팁**  
API 키를 직접 설정 파일에 입력하기보다는 환경변수를 사용하는 것이 권장된다. 이렇게 하면 설정 파일을 Git에 커밋해도 API 키가 노출되지 않는다.

ex) /connect 입력시 모델 선택 팝업이 노출된다.

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdna%2FAEdh7%2FdJMcahb1uZt%2FAAAAAAAAAAAAAAAAAAAAAH6Ri75hE1Wj3YsGM9AjxsFk8c6Jf-OEdOBp-KWDVo3S%2Fimg.png%3Fcredential%3DyqXZFxpELC7KVnFOS48ylbz2pIh7yKj8%26expires%3D1769871599%26allow_ip%3D%26allow_referer%3D%26signature%3D580TFm2RRRdIXQQYkd41GcRgloU%253D)

\- 위에서도 작성했듯이 Claude Code를 통해 사용하다 차단되는 사례가 있다고 하여 조심 스럽긴 한데, 지금은 튜토리얼이고 가볍게 사용해볼 예정이니 클로드 부터 연결해보도록 하자. ( Anthropic 선택 )

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdna%2FsW3O8%2FdJMcahb1uZY%2FAAAAAAAAAAAAAAAAAAAAAGx25PnhqEHvNwt0NyqiwfIX1xjM6PNcRn8ezSb9Oz9N%2Fimg.png%3Fcredential%3DyqXZFxpELC7KVnFOS48ylbz2pIh7yKj8%26expires%3D1769871599%26allow_ip%3D%26allow_referer%3D%26signature%3DOkuLsEgIHZmicxZWQ35yM3nFGbc%253D)

\- 위험 할 수 있다고 하는 구독형 인증 방식으로 진행 해보겠다. (Claude Pro/Max 선택)

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdna%2F2bjoq%2FdJMcacu1yVy%2FAAAAAAAAAAAAAAAAAAAAAJhKcvrc2x0UzL68KQ7qripRbM0Vw0wCbBh7Z-0I0UXL%2Fimg.png%3Fcredential%3DyqXZFxpELC7KVnFOS48ylbz2pIh7yKj8%26expires%3D1769871599%26allow_ip%3D%26allow_referer%3D%26signature%3DHg3MhVVkdfO4EAXUf4TV1bTz2cU%253D)

\- 인증 url 이 노출 된다. 클릭하여 인증을 진행하자. > 승인 클릭

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdna%2FHISO6%2FdJMcabXbQVG%2FAAAAAAAAAAAAAAAAAAAAABQwObJW3RV_8HjkAyKmeRwEGE5rBilou0Kh7HYsWn27%2Fimg.png%3Fcredential%3DyqXZFxpELC7KVnFOS48ylbz2pIh7yKj8%26expires%3D1769871599%26allow_ip%3D%26allow_referer%3D%26signature%3Ddn6MJ9pjccCKkcCXJ3OgbnofVWY%253D)

\- 제공되는 코드를 카피 > 다시 open code로 돌아와 입력하여 주자.

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdna%2FZ4cHA%2FdJMcahC5zQP%2FAAAAAAAAAAAAAAAAAAAAAE9pCBypsQITWyFYfIIOk6rjAbHgqQeyCy21YCd6ifY4%2Fimg.png%3Fcredential%3DyqXZFxpELC7KVnFOS48ylbz2pIh7yKj8%26expires%3D1769871599%26allow_ip%3D%26allow_referer%3D%26signature%3D6XHF6cT7a9ctOCp0hfv7qGdSHoM%253D)

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdna%2Fbkiel2%2FdJMcacIzurE%2FAAAAAAAAAAAAAAAAAAAAAIT_UW9fRLry9oOlX_HvHMk4uTgf7mD0isvDp0gqftUh%2Fimg.png%3Fcredential%3DyqXZFxpELC7KVnFOS48ylbz2pIh7yKj8%26expires%3D1769871599%26allow_ip%3D%26allow_referer%3D%26signature%3DmQAVWjzeHKunuGDsMdd%252B5%252F%252BJuTs%253D)

\- 당연히? Opus 모델을 선택하여 주도록 한다.

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdna%2Fn0AP3%2FdJMcagxpL3r%2FAAAAAAAAAAAAAAAAAAAAACSBefTmFFtEjg5AJ50gA8LyZMDn4yNTkcatStwhsEmk%2Fimg.png%3Fcredential%3DyqXZFxpELC7KVnFOS48ylbz2pIh7yKj8%26expires%3D1769871599%26allow_ip%3D%26allow_referer%3D%26signature%3D7T3RMLXS2CY3VZejNIX7UtsCNW0%253D)

\- 올바르게 적용된 것을 확인할 수 있다.

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdna%2FcWUiHP%2FdJMcahC5zSm%2FAAAAAAAAAAAAAAAAAAAAAOPJIq58USQFKvH2EZxT1NTRIlFB6MFAqjHK2Lur1Xac%2Fimg.png%3Fcredential%3DyqXZFxpELC7KVnFOS48ylbz2pIh7yKj8%26expires%3D1769871599%26allow_ip%3D%26allow_referer%3D%26signature%3Dy2gQj5SKRb5vbjoLnrJF9wNySd4%253D)

**\--------------------!!! 다음 인증을 진행하기 이전에 잠깐!!! ------------------**

[Open Code 리뷰(2): oh-my-opencode 설치 및 설정 방법(기본 명령어, 슬래시 명령어, 연동 방법 등)](https://goddaehee.tistory.com/485)

**상기 링크의 내용을 이후에 살펴보시면... oh-my-opencode를 사용하면 openAI도 codex, Google도 Antigravity를 활용하여 구독형인증이 가능 하니 하기에 작성하는 GPT랑 GEMINI API Key를 통한 연동 방식은 참고만 하자. 비용이 많이 발생할 것 이다.**

**\-------------------------------------------------------------------------**

ex) 이젠 GPT 연동을 진행 해보자.

\- 사전에 다음과 같이 open ai API key 발급을 받아 둬야 한다. (우측 상단 Create new secret key )  
[https://platform.openai.com/settings/organization/api-keys](https://platform.openai.com/settings/organization/api-keys)

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdna%2Fl2XnE%2FdJMcai21qKE%2FAAAAAAAAAAAAAAAAAAAAAA_wV18I3eZhCpIAtPkEuphgoflnMD-PGlCgHJfsfOox%2Fimg.png%3Fcredential%3DyqXZFxpELC7KVnFOS48ylbz2pIh7yKj8%26expires%3D1769871599%26allow_ip%3D%26allow_referer%3D%26signature%3D1cdnpuiMkJ%252Bj1w%252BCcP0afOF7w1g%253D)

\- 다시 /connect 를 입력하고 OpenAI 선택

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdna%2FbUYIph%2FdJMcadtSI5U%2FAAAAAAAAAAAAAAAAAAAAAF0B1nVXyzlePxwKNU5pf822sANA2ErYIeto0CRBPhz3%2Fimg.png%3Fcredential%3DyqXZFxpELC7KVnFOS48ylbz2pIh7yKj8%26expires%3D1769871599%26allow_ip%3D%26allow_referer%3D%26signature%3D3re0%252Fc4QA%252FMAI6spgzJBWLWoy18%253D)

\- 이전에 발급받은 open ai api key 를 입력 해 주자.

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdna%2FyQ3kX%2FdJMcaacT3gD%2FAAAAAAAAAAAAAAAAAAAAAIXjYZyS01gCcY4K3vd1GLFqZ2JMe3h8srI0B0f9QMkg%2Fimg.png%3Fcredential%3DyqXZFxpELC7KVnFOS48ylbz2pIh7yKj8%26expires%3D1769871599%26allow_ip%3D%26allow_referer%3D%26signature%3D4dI1daGmoh2LlUqcyqpbI9qEO5E%253D)

\- 현시점 제일 좋은 5.2 pro 모델을 선택하였다.

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdna%2FbkEf9r%2FdJMcai9NlQx%2FAAAAAAAAAAAAAAAAAAAAAO1euZpZ_1s8AGML-NzkMyaxQk6imSRWJriVvdCQb7Ef%2Fimg.png%3Fcredential%3DyqXZFxpELC7KVnFOS48ylbz2pIh7yKj8%26expires%3D1769871599%26allow_ip%3D%26allow_referer%3D%26signature%3DSrUlmzfE7iaL1VzKcJztea%252Fc8Gc%253D)

\- 연동 확인

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdna%2FdIseCw%2FdJMcaaYhF4v%2FAAAAAAAAAAAAAAAAAAAAAJTEInd9NzGhfVxI1MP_S0qgsLX6bsT04Pb_KkHGCAQE%2Fimg.png%3Fcredential%3DyqXZFxpELC7KVnFOS48ylbz2pIh7yKj8%26expires%3D1769871599%26allow_ip%3D%26allow_referer%3D%26signature%3Ds1f%252FFOLMhukfkKR5vF%252Bo4P3GNS0%253D)

ex) 이젠 gemini 연동을 진행 해보자.

\- 사전에 다음과 같이 ai API key 발급을 받아 둬야 한다. (우측 상단 API key 만들기를 통해 진행)

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdna%2Fcc7ny3%2FdJMcaaDYjRt%2FAAAAAAAAAAAAAAAAAAAAALvdTOs7Dp9CoEUETLF_M1_OqzKEXiY-mN31DIl9biGd%2Fimg.png%3Fcredential%3DyqXZFxpELC7KVnFOS48ylbz2pIh7yKj8%26expires%3D1769871599%26allow_ip%3D%26allow_referer%3D%26signature%3DEcgNtHzTH9aNEF8DNDErmDYdpRA%253D)

[https://aistudio.google.com/api-keys](https://aistudio.google.com/api-keys)

\- 다시 /connect 를 입력하고 Google 선택

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdna%2FbivN1q%2FdJMcabJFdXU%2FAAAAAAAAAAAAAAAAAAAAAI6O9d7n5_CrhYHbEsi9Yp5ph0He-8YQYz9rELXXFOOv%2Fimg.png%3Fcredential%3DyqXZFxpELC7KVnFOS48ylbz2pIh7yKj8%26expires%3D1769871599%26allow_ip%3D%26allow_referer%3D%26signature%3DZPCzx7iQyPbf%252FS03kzfVxWL1e%252Fc%253D)

\- 이전에 발급받은 api key 를 입력 해 주자.

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdna%2FyQ3kX%2FdJMcaacT3gD%2FAAAAAAAAAAAAAAAAAAAAAIXjYZyS01gCcY4K3vd1GLFqZ2JMe3h8srI0B0f9QMkg%2Fimg.png%3Fcredential%3DyqXZFxpELC7KVnFOS48ylbz2pIh7yKj8%26expires%3D1769871599%26allow_ip%3D%26allow_referer%3D%26signature%3D4dI1daGmoh2LlUqcyqpbI9qEO5E%253D)

\- 현시점 제일 좋은 Gemini 3 모델을 선택하였다.

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdna%2FbcOnTn%2FdJMcafyvJKt%2FAAAAAAAAAAAAAAAAAAAAAJtcJ5jmLEda2kWXw1cKvqEKzfkgcEQOG_ZxEjQYsslT%2Fimg.png%3Fcredential%3DyqXZFxpELC7KVnFOS48ylbz2pIh7yKj8%26expires%3D1769871599%26allow_ip%3D%26allow_referer%3D%26signature%3DxvSUsah1grXnZjHgaTLvWyfBnw8%253D)

\- 연동 확인

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdna%2F1r9ku%2FdJMcabJFdZq%2FAAAAAAAAAAAAAAAAAAAAANgkti6N8AiBjXnLon2M2G2jDQfYfkZJceGitQxV_pvP%2Fimg.png%3Fcredential%3DyqXZFxpELC7KVnFOS48ylbz2pIh7yKj8%26expires%3D1769871599%26allow_ip%3D%26allow_referer%3D%26signature%3DrGLUm2AzNEDLNzZlnytLJlfzgy8%253D)

## 기본 사용법

### 첫 실행

LLM 제공자를 연결한 후, 프로젝트 디렉토리에서 `opencode` 를 실행하면 된다.

// 프로젝트 디렉토리에서 실행

```applescript
cd my-project
opencode
```

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdna%2FcnkLJp%2FdJMcacIztdu%2FAAAAAAAAAAAAAAAAAAAAAKpOtCVv_ID6iD0WZhGPcjOQzH_H8mz5DHkww3tDNnZ2%2Fimg.png%3Fcredential%3DyqXZFxpELC7KVnFOS48ylbz2pIh7yKj8%26expires%3D1769871599%26allow_ip%3D%26allow_referer%3D%26signature%3DyJLitjf71eKL5fsDeCHliKwsMrA%253D)

### 내장 명령어

OpenCode에는 여러 내장 명령어가 있다. 모든 명령어는 슬래시(`/`)로 시작한다.

지금은 간단하게 몇개만 살펴볼 예정이다.

| 명령어 | 기능 |
| --- | --- |
| `/init` | 프로젝트 분석 및 AGENTS.md 생성 |
| `/undo` | 마지막 변경사항 되돌리기 |
| `/redo` | 되돌린 변경사항 다시 적용 |
| `/share` | 현재 대화를 공유 가능한 링크로 생성 |
| `/help` | 도움말 표시 |
| `/models` | 사용 가능한 LLM 모델 목록 표시 및 전환 |
| `/connect` | LLM 제공자 연결 및 API 키 설정 |
| `/clear` | 현재 대화 내용 초기화 |
| `/compact` | 대화 컨텍스트 요약/압축 (토큰 절약) |
| `/sessions` | 세션 목록 표시 및 이전 세션으로 전환 |
| `/export` | 현재 대화를 마크다운 파일로 내보내기 |

/init부터 시작하려고 하는데, 잠깐 openai모델로 변경 후 진행 해보려 한다.

### 모델 선택과 전환

작업 유형에 따라 적합한 모델과 온도(temperature) 설정이 다르다. 온도가 낮을수록 일관되고 정확한 출력을, 높을수록 창의적인 출력을 생성한다.

| 작업 유형 | 권장 모델 | 온도 |
| --- | --- | --- |
| 코드 생성/구현 | GPT-4 Turbo, Claude Sonnet | 0.1 (낮음) |
| 코드 검토/QA | Claude Opus | 0.05 (매우 낮음) |
| 테스트 생성 | Claude Sonnet | 0.15 (낮음) |
| 계획/아키텍처 설계 | Claude Sonnet | 0.2 (중간) |
| 문서화 | Claude Sonnet, GPT-4 | 0.2-0.3 (중간) |

**개발 팁**  
비용 최적화를 위해 계획 단계에서는 Gemini 같은 저렴한 모델을 사용하고, 실제 코딩 단계에서만 Claude나 GPT-4를 사용하는 전략이 효과적이다. Anthropic API 레이트 제한에 도달했을 때도 세션을 끊지 않고 다른 프로바이더로 전환하여 작업을 계속할 수 있다.

// 세션 중 모델 전환 - 두 가지 방법

```csharp
/models          // 슬래시 명령어로 모델 선택 메뉴 열기
Ctrl+X → m  // 키바인딩으로 모델 선택 메뉴 열기

// 목록에서 다른 프로바이더의 모델 선택
// 예: Claude Sonnet → GPT-4 → Gemini Pro 자유롭게 전환
```

ex) /models ( gemini 3 > GPT-5.2 )

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdna%2FT3uyM%2FdJMcachufPm%2FAAAAAAAAAAAAAAAAAAAAAG_-l4sZF-HwEc-6Ub2n3TKEZ6icfy9SFdTmLhCDmJAk%2Fimg.png%3Fcredential%3DyqXZFxpELC7KVnFOS48ylbz2pIh7yKj8%26expires%3D1769871599%26allow_ip%3D%26allow_referer%3D%26signature%3D3gmKbv0oWR3C2xPvy58Pdflf5Zk%253D)

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdna%2FcTCKFL%2FdJMcafSPtuL%2FAAAAAAAAAAAAAAAAAAAAAMlf3ixVOxrRGTB-1M30jCQKylcdTlfHYpD2Z9aD1r_g%2Fimg.png%3Fcredential%3DyqXZFxpELC7KVnFOS48ylbz2pIh7yKj8%26expires%3D1769871599%26allow_ip%3D%26allow_referer%3D%26signature%3D7D7zcroTq7j5GuOtxdg6CuSeOcw%253D)

### 프로젝트 초기화: /init

`/init` 명령을 사용하면 OpenCode가 프로젝트 구조를 분석하고 `AGENTS.md` 파일을 생성한다. 이 파일은 프로젝트에 대한 컨텍스트 정보를 담고 있어 AI가 더 정확한 응답을 제공하는 데 도움을 준다.

// 프로젝트 분석 및 AGENTS.md 생성

```csharp
/init
```

ex) /init

\- 하기와 같이 작업에 대한 설명과 함께 작업을 시작한다.

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdna%2FrAAws%2FdJMcaaqrjUi%2FAAAAAAAAAAAAAAAAAAAAANGYHobNHCPH5rzeB-C6vbT4jLxsi1j1mwsgjNeb6jfj%2Fimg.png%3Fcredential%3DyqXZFxpELC7KVnFOS48ylbz2pIh7yKj8%26expires%3D1769871599%26allow_ip%3D%26allow_referer%3D%26signature%3DQHx0nAYk%252ByvtR9T9ahKCQPmyoXs%253D)

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdna%2FHRTmF%2FdJMcaaRvXE7%2FAAAAAAAAAAAAAAAAAAAAAFPr40gCB4zo_8hSboxiD49mN6tEqaJlecEelqCH3sQ3%2Fimg.png%3Fcredential%3DyqXZFxpELC7KVnFOS48ylbz2pIh7yKj8%26expires%3D1769871599%26allow_ip%3D%26allow_referer%3D%26signature%3DwFaZD7gU7AZKLX9FQjPj%252FEhV4mQ%253D)

\- 중간에 권한 요청을 요구하는데, 보안상 어떤 작업을 요청하는지 한건씩 권한 허용하는게 좋다.

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdna%2FcFnKIg%2FdJMcab3W5P1%2FAAAAAAAAAAAAAAAAAAAAAPOmTuYnpo0RATzdCGd1ncJp0j3Eh7ay_ciQiViKRfCr%2Fimg.png%3Fcredential%3DyqXZFxpELC7KVnFOS48ylbz2pIh7yKj8%26expires%3D1769871599%26allow_ip%3D%26allow_referer%3D%26signature%3DtXGGdWdn7dfuKdTD%252F5lFFiAR6ZQ%253D)

\- 다음과 같이 프로젝트 전반적인 내용을 참조 할 수 있는 AGENTS.md 파일을 만드는것을 볼 수 있다.

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdna%2FNP0gO%2FdJMcagRIOFI%2FAAAAAAAAAAAAAAAAAAAAAH_mtNEzHGgAU-F8lDdzzweRhWnA81t8unccWnYnCQZX%2Fimg.png%3Fcredential%3DyqXZFxpELC7KVnFOS48ylbz2pIh7yKj8%26expires%3D1769871599%26allow_ip%3D%26allow_referer%3D%26signature%3DCrq7p23fVw%252B55DeSqAJW8dxnsO0%253D)

### 파일 참조하기: @ 문법

질문이나 요청에서 특정 파일을 참조하고 싶을 때는 `@` 기호 뒤에 파일 경로를 입력하면 된다.

#### 파일 참조 예시

```bash
@src/auth.ts 이 파일의 인증 로직을 설명해줘

@package.json 에 있는 의존성을 분석해줘

@src/components/Button.tsx 이 컴포넌트에 hover 효과 추가해줘
```

ex) 동일한 세션창(대화창)에서 /models로 gemini모델로 변경 후 방금 생성한 AGENTS.md 파일에 대한 요약을 요청 하였다.

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdna%2Fc0lJB4%2FdJMcaiaWvZ0%2FAAAAAAAAAAAAAAAAAAAAAARa8qr61HZrNOZZjIHc2GmXuhmvDSRhSU5aO39K5Jay%2Fimg.png%3Fcredential%3DyqXZFxpELC7KVnFOS48ylbz2pIh7yKj8%26expires%3D1769871599%26allow_ip%3D%26allow_referer%3D%26signature%3DspNnYTrTnQnAneDxrS81bMgiTPs%253D)

### 이미지 활용

공식 문서에 따르면 디자인 이미지나 스크린샷을 드래그 앤 드롭으로 추가하여 참고 자료로 활용할 수 있다. 예를 들어 UI 디자인 이미지를 첨부하고 "이 디자인대로 구현해줘"라고 요청할 수 있다.

## 에이전트 이해하기

OpenCode의 에이전트는 특정 작업과 워크플로우를 위해 구성된 AI 어시스턴트이다. 공식 문서에 따르면 기본적으로 두 개의 주요 에이전트가 제공된다.

### Build vs Plan 에이전트

| **Build** | 모든 도구가 활성화된 기본 에이전트. 파일 생성, 수정, 셸 명령어 실행 등 모든 작업이 가능하다. 실제로 코드를 작성하고 구현할 때 사용한다. |
| --- | --- |
| **Plan** | 계획 및 분석을 위한 제한된 에이전트. 파일 편집과 bash 명령 실행 시 확인을 요청한다. 구현 전 설계를 논의하거나 코드를 분석할 때 사용한다. |

### 에이전트 전환하기

`Tab` 키를 누르면 Build와 Plan 에이전트 사이를 전환할 수 있다.

**개발 팁**  
새로운 기능을 구현할 때 권장되는 워크플로우는 다음과 같다:  
1\. Plan 에이전트에서 구현 방식 논의  
2\. 계획이 확정되면 Tab 키로 Build 에이전트로 전환  
3\. Build 에이전트에서 실제 구현 진행

ex) 에이전트 전환 해보기

\- 현재 에이전트의 종류와 Tab키를 통해 전환 가능함을 알 수 있다.

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdna%2Fc4wfiI%2FdJMcajt5UuI%2FAAAAAAAAAAAAAAAAAAAAADJGdN6k_HIc96745GXww4ihVrH6DRnkGmDeFcqEeODx%2Fimg.png%3Fcredential%3DyqXZFxpELC7KVnFOS48ylbz2pIh7yKj8%26expires%3D1769871599%26allow_ip%3D%26allow_referer%3D%26signature%3DtVCh4Vi3rxOsxkezXImRASg3%252FoA%253D)

\- tab키 입력 후 Plan 에이전트로 변경되는것을 볼 수 있다.

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdna%2FbfKbev%2FdJMcaaYhMYn%2FAAAAAAAAAAAAAAAAAAAAACJsBTGjX9ROYVxle0gtPQRP8vH8RqDMjHOnyQ5QpDaZ%2Fimg.png%3Fcredential%3DyqXZFxpELC7KVnFOS48ylbz2pIh7yKj8%26expires%3D1769871599%26allow_ip%3D%26allow_referer%3D%26signature%3DS19TOZ9fVBKrwahZJ7kSrCgozRY%253D)

### 서브 에이전트 호출하기

`@` 멘션을 사용하여 서브 에이전트를 호출할 수 있다. 공식 문서에 따르면 기본 제공되는 서브 에이전트는 다음과 같다.

- **@General**: 복잡한 질문 연구 및 다단계 작업용
- **@Explore**: 코드베이스 탐색에 특화

ex) Explore 서브 에이전트 호출

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdna%2FcKp5eB%2FdJMcaiIJNGi%2FAAAAAAAAAAAAAAAAAAAAAKHGvbQsNfpNiMCjRaC_2-9gl7nbyf90RZLe3g5RRha5%2Fimg.png%3Fcredential%3DyqXZFxpELC7KVnFOS48ylbz2pIh7yKj8%26expires%3D1769871599%26allow_ip%3D%26allow_referer%3D%26signature%3DlbiOHRpfzMSVffQLU5qXGZeDsRo%253D)

\- 클로드 코드와 거의 동일 한것 같다. explore 서브 에이전트가 동작하고 있으며, ctrl + x right 를 통해 해당 서브에이전트를 탐색할수도 있다.

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdna%2FtwU8i%2FdJMcacaIYOa%2FAAAAAAAAAAAAAAAAAAAAAKbElAYfmVcnKcsBlj5vm1ZQ6zZC6gfNUT6oKrh3LUev%2Fimg.png%3Fcredential%3DyqXZFxpELC7KVnFOS48ylbz2pIh7yKj8%26expires%3D1769871599%26allow_ip%3D%26allow_referer%3D%26signature%3DfJ9Yoa4XQ%252BID%252BJYhJkGMzUc6WxY%253D)

\- 작업 결과

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdna%2FOy0dg%2FdJMcagYtRNo%2FAAAAAAAAAAAAAAAAAAAAAHnl6-Ony7XJU2vF-IaGKzXoXHyz47WuS6h8DH0CCWiI%2Fimg.png%3Fcredential%3DyqXZFxpELC7KVnFOS48ylbz2pIh7yKj8%26expires%3D1769871599%26allow_ip%3D%26allow_referer%3D%26signature%3Demge0eFKDHZbK4DhUfQPCl%252BqEtA%253D)

### 커스텀 에이전트 만들기

OpenCode는 프로젝트에 맞는 커스텀 에이전트를 만들 수 있다. 프로젝트 루트에 `.opencode/agent/` 폴더를 만들고 에이전트 정의 파일을 추가하면 된다.

#### 커스텀 에이전트 폴더 구조

```cmake
my-project/
├── .opencode/
│   └── agent/
│       ├── reviewer.md         # @reviewer로 호출
│       ├── docs-writer.md      # @docs-writer로 호출
│       └── test-generator.md   # @test-generator로 호출
├── src/
└── package.json
```

마크다운 파일명이 곧 에이전트명이 된다. 파일 안에 에이전트의 역할, 사용할 도구, 시스템 프롬프트를 정의한다. 예를 들어 `reviewer.md` 파일을 만들면 `@reviewer` 로 호출하여 코드 리뷰에 특화된 응답을 받을 수 있다.

**개발 팁**  
팀에서 자주 사용하는 작업(리뷰, 문서화, 테스트 작성 등)을 커스텀 에이전트로 만들어두면, 일관된 품질의 결과를 빠르게 얻을 수 있다. 에이전트 정의 파일은 Git에 커밋하여 팀원들과 공유할 수 있다.

## 내장 도구

OpenCode는 LLM이 코드베이스에서 작업을 수행할 수 있도록 다양한 내장 도구를 제공한다. 공식 문서에 따르면 기본적으로 모든 도구가 활성화되어 있으며, 설정 파일에서 비활성화할 수 있다.

| 도구 | 기능 |
| --- | --- |
| **bash** | 셸 명령어 실행 (npm install, git 등) |
| **edit** | 정확한 문자열 교체로 파일 수정 |
| **write** | 새 파일 생성 또는 기존 파일 덮어쓰기 |
| **read** | 파일 내용 읽기 |
| **grep** | 정규표현식으로 파일 내용 검색 |
| **glob** | 패턴 매칭으로 파일 찾기 |
| **list** | 디렉토리 내용 나열 |
| **webfetch** | 웹 콘텐츠 가져오기 |

공식 문서에 따르면 내부적으로 ripgrep을 사용하며 `.gitignore` 패턴을 존중한다.

## 유용한 키 바인딩

OpenCode는 터미널 충돌을 피하기 위해 리더 키(leader key) 기반의 키 바인딩 시스템을 사용한다. 공식 문서에 따르면 기본 리더 키는 `Ctrl+X` 이다.

리더 키를 먼저 누른 후 다음 키를 누르면 해당 기능이 실행된다. 예를 들어 새 세션을 시작하려면 `Ctrl+X` 를 누른 후 `n` 을 누르면 된다.

| 단축키 | 기능 |
| --- | --- |
| `Ctrl+X` → `n` | 새 세션 시작 |
| `Ctrl+X` → `l` | 세션 목록 보기 |
| `Ctrl+X` → `m` | 모델 선택 |
| `Ctrl+X` → `e` | 편집기 열기 |
| `Ctrl+X` → `t` | 테마 변경 |
| `Tab` | Build/Plan 에이전트 전환 |

**개발 팁**  
키 바인딩을 비활성화하거나 변경하려면 `opencode.json` 의 `keybinds` 섹션에서 해당 키를 `"none"` 으로 설정하면 된다.

## GitHub 연동하기

OpenCode는 GitHub와 연동하여 PR 리뷰, 이슈 관리 등 GitHub 워크플로우를 자동화할 수 있다. GitHub 연동을 설정하면 `/oc` 명령어를 사용하여 PR에 AI 리뷰어를 호출하는 등의 기능을 활용할 수 있다.

### GitHub 앱 설치

GitHub 연동을 위해서는 먼저 OpenCode GitHub 앱을 설치해야 한다. 터미널에서 다음 명령어를 실행하면 브라우저가 열리고 GitHub 앱 설치 페이지로 이동한다.

// GitHub 앱 설치 (브라우저 열림)

```javascript
opencode github install
```

브라우저에서 연동할 저장소를 선택하고 권한을 승인하면 설정이 완료된다.

ex) opencode github install

\- 다음과 같은 메세지 출력과 함께 설치 페이지가 열리게 된다.

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdna%2Fc0TXYU%2FdJMcad1Ipal%2FAAAAAAAAAAAAAAAAAAAAAO7OAmza9ppSSFgXOW-HSPjVD-1tqS0SSu90RMumDv1n%2Fimg.png%3Fcredential%3DyqXZFxpELC7KVnFOS48ylbz2pIh7yKj8%26expires%3D1769871599%26allow_ip%3D%26allow_referer%3D%26signature%3DG6n6eKC%252FsY0OmvpvkJZU52IQw3o%253D)

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdna%2FbaEnVv%2FdJMcahJSprv%2FAAAAAAAAAAAAAAAAAAAAAAV4kNDvH6qkFtNKl1YrHhGb2cXgsdBE59QRGFnUxlVD%2Fimg.png%3Fcredential%3DyqXZFxpELC7KVnFOS48ylbz2pIh7yKj8%26expires%3D1769871599%26allow_ip%3D%26allow_referer%3D%26signature%3DPudXWyLn6WIWTL3s0LFZ%252B6rwl9c%253D)

\- 본인이 원하는 repository를 선택하고 설치를 완료하여 준다.

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdna%2FGKSgm%2FdJMcabplflU%2FAAAAAAAAAAAAAAAAAAAAAGR5K4Fjz42XMZxXnBCWGwRgTzkwFijbcj_sX486e6lE%2Fimg.png%3Fcredential%3DyqXZFxpELC7KVnFOS48ylbz2pIh7yKj8%26expires%3D1769871599%26allow_ip%3D%26allow_referer%3D%26signature%3DM%252BCgU9YayAGr2Z38QWHX%252F9ZXvp4%253D)

\- 다음과 같이 간단히 사용 방법에 대해 안내해 준다.

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdna%2FH6ZX5%2FdJMcabCSn3L%2FAAAAAAAAAAAAAAAAAAAAAHM17JOmzfkAB90YGpHYeLMpMjUDggiM5X7sxuU6xNPW%2Fimg.png%3Fcredential%3DyqXZFxpELC7KVnFOS48ylbz2pIh7yKj8%26expires%3D1769871599%26allow_ip%3D%26allow_referer%3D%26signature%3Dd%252BC%252FD3jrcc8Nz61UN0OHXIYzj2E%253D)

### /oc 명령어로 PR 리뷰 요청하기

GitHub 연동이 완료되면 PR 코멘트에서 `/oc` 명령어를 사용하여 AI에게 작업을 요청할 수 있다. 이 기능은 코드 리뷰 자동화에 유용하다.

#### /oc 명령어 사용 예시

```bash
/oc 이 PR의 코드를 리뷰해줘

/oc 보안 취약점이 있는지 확인해줘

/oc 테스트 커버리지를 개선할 방법을 제안해줘
```

PR 코멘트에 위와 같이 입력하면 OpenCode가 해당 PR의 변경 사항을 분석하고 리뷰 결과를 코멘트로 남긴다. 팀 협업 시 코드 리뷰 부담을 줄이는 데 효과적이다.

**개발 팁**  
GitHub 연동은 팀 프로젝트에서 특히 유용하다. PR이 올라오면 자동으로 AI 리뷰를 받고, 리뷰어가 직접 확인하기 전에 기본적인 코드 품질 검사를 수행할 수 있다.

## 실전 개발 워크플로우

OpenCode를 활용하면 기능 개발의 전체 생명주기를 체계적으로 관리할 수 있다. 다음은 실무에서 권장되는 6단계 워크플로우이다.

### 6단계 개발 파이프라인

| **1\. 계획 (Plan)** | 기능 요청을 분석하고 작업 단위로 분해. 수정할 파일 식별 |
| --- | --- |
| **2\. 코딩 (Code)** | 계획을 바탕으로 실제 코드 구현. 기존 코드 스타일 준수 |
| **3\. 테스트 (Test)** | 단위 테스트, 통합 테스트 자동 생성 |
| **4\. 문서화 (Docs)** | 관련 문서 업데이트, API 문서 생성 |
| **5\. 품질검사 (QA)** | 코드 품질, 스타일, 아키텍처 준수 검토 |
| **6\. 최종검토 (Review)** | 전체 결과물 종합 검토 |

이 워크플로우를 활용하려면 먼저 Plan 에이전트(Tab 키로 전환)에서 기능을 설계하고, 설계가 확정되면 Build 에이전트로 전환하여 구현한다. 각 단계를 순차적으로 진행하면 품질을 유지하면서 개발 속도를 높일 수 있다.

이 워크플로우의 효과를 극대화하려면 각 단계에 적합한 LLM 모델을 선택하는 것이 중요하다. OpenCode는 세션 중간에도 모델을 전환할 수 있어 비용과 품질을 모두 최적화할 수 있다.

**실전 활용**  
`/models` 명령어를 사용하면 대화 중간에 모델을 바꿀 수 있다. 예를 들어 설계 논의는 저렴한 Gemini로 하다가, 실제 코딩은 Claude Sonnet으로 전환하는 식이다.

## MCP 서버 연동

MCP(Model Context Protocol) 서버를 연동하면 OpenCode의 기능을 확장할 수 있다. 예를 들어 Playwright MCP를 연동하면 AI가 직접 브라우저를 제어하여 웹 애플리케이션을 테스트할 수 있다.

### 자주 사용되는 MCP 서버

| MCP 서버 | 용도 |
| --- | --- |
| **Playwright** | 브라우저 자동화, E2E 테스트, UI 디버깅 |
| **Context7** | 라이브러리 문서 읽기, API 레퍼런스 조회 |
| **Database** | 데이터베이스 스키마 조회, 쿼리 실행 |

MCP 서버를 설정하면 다음과 같은 자동화 시나리오가 가능해진다: OpenCode가 서버를 백그라운드에서 실행하고, Playwright로 브라우저를 열어 애플리케이션을 테스트하고, 발견된 문제를 자동으로 수정한 후 재테스트하는 일련의 과정을 한 번의 지시로 수행할 수 있다.

## 이상적인 유스케이스

OpenCode는 다음과 같은 상황에서 특히 효과적이다.

#### OpenCode가 적합한 경우

- **터미널 중심 워크플로우**: CLI 환경에서 주로 작업하는 개발자
- **반복 작업 자동화**: 보일러플레이트 코드, 테스트 생성, 문서화 등 반복적인 작업
- **빠른 프로토타이핑**: 아이디어를 빠르게 코드로 구현해보고 싶을 때
- **디버깅 지원**: 에러 분석과 해결책 제안이 필요할 때
- **비용 최적화**: 구독료 없이 API 사용량만 지불하고 싶을 때
- **다양한 모델 활용**: 작업에 따라 다른 LLM을 사용하고 싶을 때

#### 다른 도구가 더 적합할 수 있는 경우

- **GUI 선호**: 시각적 인터페이스를 선호하는 경우 → Cursor, VS Code Copilot
- **CLI 경험 부족**: 터미널 사용이 익숙하지 않은 경우
- **올인원 솔루션**: 설정 없이 바로 사용하고 싶은 경우 → Claude Code

## 자주 묻는 질문

Q: OpenCode는 무료인가?

A: OpenCode 자체는 무료 오픈소스이다. 다만 사용하는 LLM 제공자에 따라 API 비용이 발생할 수 있다. Ollama 같은 로컬 모델을 사용하면 완전 무료로 사용할 수 있다.

Q: Claude Code와 무엇이 다른가?

A: Claude Code는 Anthropic에서 제공하는 공식 도구로 Claude 모델만 사용할 수 있다. OpenCode는 오픈소스로 75개 이상의 LLM 제공자를 지원하여 원하는 모델을 선택할 수 있다.

Q: 기존 프로젝트에서 바로 사용할 수 있는가?

A: 가능하다. 프로젝트 디렉토리에서 `opencode` 를 실행하고 `/init` 명령으로 프로젝트를 분석하면 된다.

Q: 내 코드가 외부로 전송되는가?

A: 공식 문서에 따르면 OpenCode는 코드나 컨텍스트 데이터를 저장하지 않는다. 다만 선택한 LLM 제공자에게는 프롬프트와 함께 코드가 전송될 수 있으므로, 민감한 프로젝트에서는 로컬 모델 사용을 고려할 수 있다.

최대한 간단하게 open code에 설치 및 기본 슬래시 명령어몇가지를 탐색해 보았다.

OpenCode가 유명해지게된건 사실 "Oh My OpenCode"의 영향이 매우 큰것으로 알고있다.

그럼 다음 섹션에서 실제 목표인 Oh My OpenCode에 대해 알아 가 보도록 하겠다.

## 참고 자료

### 공식 자료

- [OpenCode 공식 문서](https://opencode.ai/docs) - 상세한 기능 설명과 고급 설정
- [OpenCode 공식 웹사이트](https://opencode.ai/) - 프로젝트 개요와 최신 소식
- [GitHub 저장소](https://github.com/sst/opencode) - 소스 코드와 이슈 트래커

### 커뮤니티 리뷰 및 가이드

- [OpenCode 도구 리뷰 (drose.io)](https://drose.io/aitools/tools/opencode) - 터미널 워크플로 관점에서 정리한 주요 기능과 유스케이스
- [AI-Powered Development Workflow Guide (neilpatterson.dev)](https://www.neilpatterson.dev/writing/opencode-ai-development-workflow-guide) - 6단계 개발 파이프라인과 모델 조합 전략
- [OpenCode Tool Review (elite-ai-assisted-coding.dev)](https://elite-ai-assisted-coding.dev/p/opencode-tool-review) - MCP 연동, VS Code 통합 등 고급 기능 실사용기

### 다음 단계

이 글에서 다룬 기본 사용법을 익힌 후 다음 주제를 학습하면 OpenCode를 더 효과적으로 활용할 수 있다.

- **[oh-my-opencode 설치 및 사용방법](https://goddaehee.tistory.com/485)** — 다음 글
- 커스텀 에이전트 생성하기
- 커스텀 명령어 정의하기
- MCP 서버 연동하기
- 권한 설정으로 안전하게 사용하기

이 글은 2025년 1월 기준 OpenCode 공식 문서를 바탕으로 작성되었다. OpenCode는 활발히 개발되고 있는 프로젝트이므로, 최신 정보는 공식 문서에서 확인하는 것이 좋다.

[저작자표시 비영리 변경금지 (새창열림)](https://creativecommons.org/licenses/by-nc-nd/4.0/deed.ko)

#### ' > ' 카테고리의 다른 글

| [Open Code 리뷰(3): 오픈소스, 무료 및 저가 LLM 모델 활용 해보기 with Ollama, Qwen3 등](https://goddaehee.tistory.com/488) (1) | 2026.01.08 |
| --- | --- |
| [Open Code 리뷰(2): oh-my-opencode 설치 및 설정 방법(기본 명령어, 슬래시 명령어, 연동 방법 등) with Claude,OpenAI,Gemini](https://goddaehee.tistory.com/485) (5) | 2026.01.07 |

### TAG

, , , , , , , , ,[PREV](https://goddaehee.tistory.com/485)

[

### Open Code 리뷰(2): oh-my-opencode 설치 및 설정 방법(기본 명령어, 슬래시 명령어, 연동 방법 등) with Claude,OpenAI,Gemini

](https://goddaehee.tistory.com/485)

[댓글 1](https://goddaehee.tistory.com/#0)

**소중한 공감 감사합니다**

💡 AI 관련 질문이 있나요? 눌러보세요!