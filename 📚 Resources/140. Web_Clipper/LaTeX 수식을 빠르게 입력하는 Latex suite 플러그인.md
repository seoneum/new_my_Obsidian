---
title: LaTeX 수식을 빠르게 입력하는 Latex suite 플러그인
source_url: https://kaminik.tistory.com/entry/LaTeX-%EC%88%98%EC%8B%9D%EC%9D%84-%EB%B9%A0%EB%A5%B4%EA%B2%8C-%EC%9E%85%EB%A0%A5%ED%95%98%EB%8A%94-Latex-suite-%ED%94%8C%EB%9F%AC%EA%B7%B8%EC%9D%B8
author:
  - "[[제이닉]]"
published: 2024-04-11
created: 2025-12-22
description: obsidian 활용법, 옵시디언, 지식관리방법론, 제2의뇌, 노트관리방법론, 세컨드브레인
tags:
  - "clippings"
migrated_from: CMDS/100. Inbox/140. Web_Clipper/LaTeX 수식을 빠르게 입력하는 Latex suite 플러그인.md
updated: 2026-01-18T16:42:53
domain:
  - math
cmds: connect
---
> [!summary]+ 3줄 요약
> - LaTeX Suite는 옵시디언에서 LaTeX 수식을 빠르게 입력할 수 있도록 도와주는 플러그인입니다.
> - 단축키, 텍스트 확장, 자동 완성 등 다양한 기능을 제공합니다.
> - 행렬, 분수, 그리스 문자 등을 손쉽게 입력하고 가독성을 높일 수 있습니다.


Latex

Mathematics

옵시디언

mathematics

Obsidian

Plugin

플러그인

math

LaTex

수학

![옵시디언 플러그인/커뮤니티 플러그인](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdna%2FdDznhl%2FbtsGvsCnauO%2FAAAAAAAAAAAAAAAAAAAAACRWclCPbnycKfk-P5tFtscGqx6jIjagMs5Z7zwfxJs6%2Fimg.webp%3Fcredential%3DyqXZFxpELC7KVnFOS48ylbz2pIh7yKj8%26expires%3D1767193199%26allow_ip%3D%26allow_referer%3D%26signature%3Dwa3SB2YhjwKE9HzDTlk6y4tAEZU%253D)

옵시디언 플러그인/커뮤니티 플러그인

---

## 개요

LaTeX Suite는 옵시디언에서 LaTeX 수식을 손글씨만큼 빠르게 입력할 수 있도록 도와주는 플러그인입니다.

Plugin Info

| 플러그인 명 | LaTeX Suite |
| --- | --- |
| 플러그인 설명 | LaTeX 수식을 빠르게 입력 |
| 플러그인 분류 | 입력 지원, [LaTex](https://kaminik.tistory.com/pages/%EC%98%B5%EC%8B%9C%EB%94%94%EC%96%B8-%ED%94%8C%EB%9F%AC%EA%B7%B8%EC%9D%B8-%EC%82%AC%EC%A0%84#%EC%88%98%EC%8B%9D-/-LaTex) |
| Github 링크 | [Github 링크](https://github.com/artisticat1/obsidian-latex-suite) |
| 옵시디언 링크 | [플러그인 링크](https://kaminik.tistory.com/entry/) |
| 별점 | ⭐⭐ |

---

## 예시

![옵시디언 플러그인/커뮤니티 플러그인](https://blog.kakaocdn.net/dna/eFcdu5/btsGkoT8hZE/AAAAAAAAAAAAAAAAAAAAALYNrram7m113KtDKeTh_ZItdLhD240VthV40jDUNzlo/img.gif?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1767193199&allow_ip=&allow_referer=&signature=7kbq7YqFZEwTWwCGO6FYMvn%2B6%2B8%3D)

옵시디언 플러그인/커뮤니티 플러그인

이 플러그인의 핵심 기능은 LaTeX를 더 빠르게 작성할 수 있도록 단축키와 텍스트 확장을 제공하는 **스니펫** 입니다. 예를 들어,

- "\\sqrt{x}" 대신 "sqx"를,
- "\\frac{a}{b}" 대신 "a/b"를,
- "\\frac{\\partial x}{\\partial y}" 대신 "par x y"를 입력합니다.

플러그인에는 Gilles Castel의 글을 기반으로 한 기본 스니펫이 포함되어 있으며, 이를 수정하거나 삭제하고, 자신만의 스니펫을 작성할 수 있습니다.

> [![How I'm able to take notes in mathematics lectures using LaTeX and Vim](https://blog.kakaocdn.net/dna/pkv4L/hyVJWmDihH/AAAAAAAAAAAAAAAAAAAAAOe2dLx6Zxl7AyVAcNWt1EtsETE1mbWtek8gmkG25FP6/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1767193199&allow_ip=&allow_referer=&signature=4BXltFWRS1a6BVL3tloWEQmOtgM%3D)
> 
> How I'm able to take notes in mathematics lectures using LaTeX and Vim
> 
> A while back I answered a question on Quora: Can people actually keep up with note-taking in Mathematics lectures with LaTeX. There, I explained my workflow of taking lecture notes in LaTeX using Vim and how I draw figures in Inkscape. However, a lot has
> 
> castel.dev
> 
> ](https://castel.dev/post/lecture-notes-1/)

더 자세한 정보는 위 링크을 참조하세요.

---

## 사용 방법

사용을 시작하려면 *dm* 을 입력하여 display math mode로 전환하세요. 다음을 시도해 보세요:

- "xsr" → "x^{2}".
- "x/y ~~Tab~~ " → "\\frac{x}{y}".
- "sin @t" → "\\sin \\theta".

[기본 스니펫](https://github.com/artisticat1/obsidian-latex-suite/blob/main/src/default_snippets.js) 에서 더 많은 명령어를 찾을 수 있습니다.

- "par ~~Tab~~ f ~~Tab~~ x ~~Tab~~ " → "\\frac{\\partial f}{\\partial x}".
- "dint ~~Tab~~ 2pi ~~Tab~~ sin @t ~~Tab~~ @t ~~Tab~~ " → "\\int\_{0}^{2\\pi} \\sin \\theta \\, d\\theta".

---

## 기능

### Auto-fraction

"\\frac{1}{x}" 대신 "1/x"를 입력할 수 있습니다.

예를 들어, 다음과 같은 확장을 제공합니다:

- `x/` → `\frac{x}{}`.
- `(a + b(c + d))/` → `\frac{a + b(c + d)}{}`.

그리고 커서를 괄호 안으로 이동합니다. 분모를 입력한 후, ~~Tab~~ 을 눌러 분수로 나옵니다.

![옵시디언 플러그인/커뮤니티 플러그인](https://blog.kakaocdn.net/dna/vzv31/btsGuN017df/AAAAAAAAAAAAAAAAAAAAAHC5CXsvxx1O1r5N6oDXU4fDELw813jJCUq1GapV7QMs/img.gif?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1767193199&allow_ip=&allow_referer=&signature=ClNr2IU7kp2Kox9fZ6MjogGnRmw%3D)

옵시디언 플러그인/커뮤니티 플러그인

### Matrix shortcuts

행렬, 배열, 정렬, 또는 경우 환경 내부에서,

- ~~Tab~~ 을 누르면 *&* 기호가 삽입됩니다.
- ~~Enter~~ 를 누르면 *\\\\* 가 삽입되고 새로운 줄로 이동합니다.
- ~~Shift + Enter~~ 를 누르면 다음 줄의 끝으로 이동합니다.
![옵시디언 플러그인/커뮤니티 플러그인](https://blog.kakaocdn.net/dna/bBPg8q/btsGwL8H1ES/AAAAAAAAAAAAAAAAAAAAAFTy_eeOlCeW00WPIQnAL8AR6WEHj95EkE03IXnRhzpO/img.gif?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1767193199&allow_ip=&allow_referer=&signature=1gyVhFzUklZG7FAARh%2BkGOvwyy4%3D)

옵시디언 플러그인/커뮤니티 플러그인

### Conceal

이 기능은 설정에서 활성화해야 합니다.

![옵시디언 플러그인/커뮤니티 플러그인](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdna%2Fbw7gLB%2FbtsGwDC5sXl%2FAAAAAAAAAAAAAAAAAAAAALr8FNmr2R4HE7zD6KMLLwr7aVXLbs99rjrS9uH4rOyz%2Fimg.png%3Fcredential%3DyqXZFxpELC7KVnFOS48ylbz2pIh7yKj8%26expires%3D1767193199%26allow_ip%3D%26allow_referer%3D%26signature%3DIsRoRyCEN7hYFvGOG%252Foq8VOF%252FuU%253D)

옵시디언 플러그인/커뮤니티 플러그인

LaTeX 코드를 숨김으로써 방정식을 더 읽기 쉽게 만들고, 예쁜 형식으로 렌더링합니다.

예를 들어, "\\dot{x}^{2} + \\dot{y}^{2}"는 "ẋ² + ẏ²"로 표시됩니다.

![옵시디언 플러그인/커뮤니티 플러그인](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdna%2FcnZ1uT%2FbtsGwNrXKWP%2FAAAAAAAAAAAAAAAAAAAAAOW1y_yMwuqtPJ71Fz_BLPTA3BdfI0nKKey2G3SDYzA1%2Fimg.png%3Fcredential%3DyqXZFxpELC7KVnFOS48ylbz2pIh7yKj8%26expires%3D1767193199%26allow_ip%3D%26allow_referer%3D%26signature%3DlNfG2AuqGsQQvLHu%252BG2wfQ7iOgI%253D)

옵시디언 플러그인/커뮤니티 플러그인

![옵시디언 플러그인/커뮤니티 플러그인](https://blog.kakaocdn.net/dna/OvFqt/btsGwQWkAzq/AAAAAAAAAAAAAAAAAAAAAHOkn7DSRENydHMA3bzU9y6j95vAbK68b-tXXqf_L08M/img.gif?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1767193199&allow_ip=&allow_referer=&signature=Jn6whdFy3SwE%2BOKHEX2gRRPgVaM%3D)

옵시디언 플러그인/커뮤니티 플러그인

### Tabout

- 방정식의 끝에서 커서를 누르면 커서가 $ 기호 밖으로 이동합니다.
- 그렇지 않으면, ~~Tab~~ 을 누르면 커서가 다음 닫는 괄호: ), \], }, >, 또는 |로 이동합니다.

### Preview inline math

inline math 내부에 커서가 있을 때, 렌더링된 math을 보여주는 팝업 창이 표시됩니다.

![옵시디언 플러그인/커뮤니티 플러그인](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdna%2FbNdMlF%2FbtsGwOjVFYh%2FAAAAAAAAAAAAAAAAAAAAAM5wuihS6tKBOExzl--Fuh7GfeRSo-vQSIcZfH6UW9b0%2Fimg.png%3Fcredential%3DyqXZFxpELC7KVnFOS48ylbz2pIh7yKj8%26expires%3D1767193199%26allow_ip%3D%26allow_referer%3D%26signature%3DotgcY0VPMAzL4mX2%252FDip%252FMjlFhw%253D)

옵시디언 플러그인/커뮤니티 플러그인

![옵시디언 플러그인/커뮤니티 플러그인](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdna%2FcPYxU3%2FbtsGvTNeJEF%2FAAAAAAAAAAAAAAAAAAAAAIJn4p7g0olocSCO1VXPOy9wlsXDpKZmsZMgljPHgJr8%2Fimg.png%3Fcredential%3DyqXZFxpELC7KVnFOS48ylbz2pIh7yKj8%26expires%3D1767193199%26allow_ip%3D%26allow_referer%3D%26signature%3D2Ga1zQXEN4jQ%252FFFVwmA%252B%252F1wknxM%253D)

옵시디언 플러그인/커뮤니티 플러그인

### 일치하는 괄호 및 색상 강조

- 일치하는 괄호는 동일한 색상으로 렌더링되어 가독성을 돕습니다.
- 커서가 괄호 옆에 있을 때, 해당 괄호와 짝이 되는 괄호가 강조됩니다.
- 커서가 괄호 내부에 있을 때, 포함하는 괄호가 강조됩니다.
![옵시디언 플러그인/커뮤니티 플러그인](https://blog.kakaocdn.net/dna/bycQoe/btsGuKiHZUF/AAAAAAAAAAAAAAAAAAAAALvtIHwqUZ386bKFNDz229AEXli8YjpvVlGjdrlSeuZK/img.gif?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1767193199&allow_ip=&allow_referer=&signature=gp1BphExHlS040F4PFBvdXqMALo%3D)

옵시디언 플러그인/커뮤니티 플러그인

### Visual snippets

수식을 주석 처리하거나 용어를 취소하거나 가로지르고 싶을 때, 커서로 일부 수식을 선택하고 입력하면,

- ~~U~~ 는 *\\underbrace* 로 둘러싸입니다.
- ~~O~~ 는 *\\overbrace* 로 둘러싸입니다.
- ~~C~~ 는 *\\cancel* 로 둘러싸입니다.
- ~~K~~ 는 *\\cancelto* 로 둘러싸입니다.
- ~~B~~ 는 *\\underset* 로 둘러싸입니다.
![옵시디언 플러그인/커뮤니티 플러그인](https://blog.kakaocdn.net/dna/O5Lni/btsGwzgdpB0/AAAAAAAAAAAAAAAAAAAAAEdMb9MoStz1jG9Emh6IJceZtMbE-jifFHnqT3A5rxr1/img.gif?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1767193199&allow_ip=&allow_referer=&signature=G8oW9RUmycBmLLlKfm6nhPMZmh0%3D)

옵시디언 플러그인/커뮤니티 플러그인

### Auto-enlarge brackets

*\\sum*, *\\int* 또는 *\\frac* 를 포함하는 스니펫이 트리거되면, 모든 포함 괄호가 "\\left"와 "\\right"로 확대됩니다.

![옵시디언 플러그인/커뮤니티 플러그인](https://blog.kakaocdn.net/dna/dRKtD1/btsGuL9Zr0v/AAAAAAAAAAAAAAAAAAAAAH0mx124COFDIeaEGx6cSHl0pTmBtPuPDx7dl30F23Wa/img.gif?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1767193199&allow_ip=&allow_referer=&signature=OshTdjxLA5Kr%2BgzTBT%2Ba5P9YXYY%3D)

옵시디언 플러그인/커뮤니티 플러그인

### Editor commands

- Box current equation – 현재 커서가 있는 방정식을 상자로 둘러쌉니다.
- Select current equation – 현재 커서가 있는 방정식을 선택합니다.

### Snippet

자신만의 스니펫을 추가할 수 있습니다. 스니펫은 다음과 같이 형식화됩니다:

```typescript
{

  trigger: string | RegExp,

  replacement: string,

  options: string,

  priority?: number,

  description?: string,

  flags?: string,

}
```
- `trigger`: 이 스니펫을 활성화하는 텍스트입니다.
	- 트리거는 정규 표현식일 수도 있습니다.
- `replacement`: `trigger` 를 대체할 텍스트입니다.
	- 대체문은 JavaScript 함수일 수도 있습니다.
	- 커서가 점프할 탭스탑은 *replacement* 에 $0, $1 등으로 작성합니다.
- `options`: 아래 참조.
- `priority` (선택 사항): 이 스니펫의 우선 순위입니다. 우선 순위가 높은 스니펫이 먼저 실행됩니다. 음수일 수 있습니다. 기본값은 0입니다.
- `description` (선택 사항): 이 스니펫에 대한 설명입니다.
- `flags` (선택 사항): 정규 표현식 스니펫에 대한 플래그입니다.

#### options

- `t`: 텍스트 모드. 이 snippet은 수식 밖에서만 실행됩니다.
- `m`: 수식 모드. 이 snippet은 수식 내에서만 실행됩니다.`M` 과 `n\` 의 약어입니다.
- `M`: 블록 수식 모드. 이 snippet은 `$$ ... $$` 블록 내에서만 실행됩니다.
- `n`: 인라인 수식 모드. 이 snippet은 `$ ... $` 블록 내에서만 실행됩니다.
- `A`: 자동. trigger가 입력되는 즉시 이 snippet을 확장합니다. 생략하면 snippet을 확장하려면 ~~Tab~~ 키를 눌러야 합니다.
- `r`: 정규 표현식. `trigger` 는 정규 표현식으로 처리됩니다.
- `v`: visual snippets. 이 snippet은 선택 영역에서만 실행됩니다. trigger는 단일 문자여야 합니다.
- `w`: 단어 경계. 이 snippet은 trigger가 `.`, `,`, 또는 `-` 와 같은 단어 구분자에 의해 앞뒤로 둘러싸일 때만 실행됩니다.
- `c`: 코드 모드. 이 snippet은 ` ``` ... ``` ` 블록 내에서만 실행됩니다.

스니펫을 작성하는 방법은 [문서를 참조하세요](https://kaminik.tistory.com/entry/DOCS.md). 다른 사람이 작성한 스니펫을 참고하시려면 [링크를 확인하세요.](https://github.com/artisticat1/obsidian-latex-suite/discussions/50)

> 스니펫 파일은 JavaScript로 해석되며 임의의 코드를 실행할 수 있습니다.  
> 악의적인 코드 실행을 방지하기 위해 다른 사람이 공유한 스니펫을 사용할 때는 항상 주의하세요.

---

## 치트시트

| 트리거 | 대체 |
| --- | --- |
| mk | $ $ |
| dm | $$      $$ |
| sr | ^{2} |
| cb | ^{3} |
| rd | ^{ } |
| \_ | \_{ } |
| sq | \\sqrt{ } |
| x/y Tab | \\frac{x}{y} |
| // | \\frac{ }{ } |
| te Tab | \\text{ } |
| x1 | x\_{1} |
| x,. | \\mathbf{x} |
| x., | \\mathbf{x} |
| xdot | \\dot{x} |
| xhat | \\hat{x} |
| xbar | \\bar{x} |
| xvec | \\vec{x} |
| xtilde | \\tilde{x} |
| xund | \\underline{x} |
| ee | e^{ } |

괄호 {} 안으로 커서가 이동하는 스니펫을 실행할 때,

Tab

을 눌러 괄호에서 나갑니다.

### 그리스 문자

| 트리거 | 대체           | 트리거 | 대체    |
| --- | ------------ | --- | ----- |
| @a  | \\alpha      | eta | \\eta |
| @b  | \\beta       | mu  | \\mu  |
| @g  | \\gamma      | nu  | \\nu  |
| @G  | \\Gamma      | xi  | \\xi  |
| @d  | \\delta      | Xi  | \\Xi  |
| @D  | \\Delta      | pi  | \\pi  |
| @e  | \\epsilon    | Pi  | \\Pi  |
| :e  | \\varepsilon | rho | \\rho |
| @z  | \\zeta       | tau | \\tau |
| @t  | \\theta      | phi | \\phi |
| @T  | \\Theta      | Phi | \\Phi |
| @k  | \\kappa      | chi | \\chi |
| @l  | \\lambda     | psi | \\psi |
| @L  | \\Lambda     | Psi | \\Psi |
| @s  | \\sigma      |     |       |
| @S  | \\Sigma      |     |       |
| @o  | \\omega      |     |       |
| ome | \\omega      |     |       |

짧은 이름(2-3글자)을 가진 그리스 문자의 경우, 그냥 이름을 입력하면 됩니다. 예를 들어, "pi" → "\\pi"

---

## 관련 글

> [![옵시디언 심화: LaTeX](https://blog.kakaocdn.net/dna/pTA6m/hyVMUiM3Xo/AAAAAAAAAAAAAAAAAAAAADlGTwbdNt_eMrm5qN1fgFLOpPlB_Ras5opPd_fST1dX/img.jpg?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1767193199&allow_ip=&allow_referer=&signature=nKtcxJLeeeBPkv8UsBtgnk%2BzTsc%3D)
> 
> 옵시디언 심화: LaTeX
> 
> 개요 옵시디언에서 LaTeX을 사용하면 복잡한 수학식을 깔끔하고 정확하게 문서에 표현할 수 있습니다. 옵시디언은 LaTeX 수식을 지원하여 복잡한 수학식을 쉽게 작성하고 관리할 수 있습니다. LaTeX
> 
> kaminik.tistory.com
> 
> ](https://kaminik.tistory.com/entry/%EC%98%B5%EC%8B%9C%EB%94%94%EC%96%B8-%EC%8B%AC%ED%99%94-LaTeX)

---

[저작자표시 비영리 변경금지 (새창열림)](https://creativecommons.org/licenses/by-nc-nd/4.0/deed.ko)[PREV](https://kaminik.tistory.com/entry/%EC%BA%94%EB%B2%84%EC%8A%A4%EC%97%90%EC%84%9C-%EC%B9%B4%EB%93%9C%EB%A5%BC-%EC%9D%B4%EB%AF%B8%EC%A7%80%EB%A1%9C-%EB%82%B4%EB%B3%B4%EB%82%B4%EB%8A%94-Canvas-Node-Screenshot-%ED%94%8C%EB%9F%AC%EA%B7%B8%EC%9D%B8)

[

캔버스에서 카드를 이미지로 내보내는 Node Screenshot 플러그인

](https://kaminik.tistory.com/entry/%EC%BA%94%EB%B2%84%EC%8A%A4%EC%97%90%EC%84%9C-%EC%B9%B4%EB%93%9C%EB%A5%BC-%EC%9D%B4%EB%AF%B8%EC%A7%80%EB%A1%9C-%EB%82%B4%EB%B3%B4%EB%82%B4%EB%8A%94-Canvas-Node-Screenshot-%ED%94%8C%EB%9F%AC%EA%B7%B8%EC%9D%B8)