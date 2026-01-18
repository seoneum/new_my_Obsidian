---
type: lecture
title: L - MIT_18.01_07
created: 2025-12-29
updated: 2026-01-18T16:42:53
author:
  - "[[David Jerison]]"
group: General
status:
  - "[[🌱Seed]]"
tags:
  - lecture
  - lecture/General
  - tagging/needed
aliases: []
course: Single Variable Calculurs
session: 2025-12-29/02/07
migrated_from: CMDS/200. CMDS/201. Connect/202. Math/Calculurs/L - MIT_18.01_07.md
domain:
  - math
cmds: connect
---

# L - MIT_18.01_07

## Meta
- Course: Single Variable Calculurs
- Session: 2025-12-29/02/07
- Instructor: 
- URL: 

## Outline
- 

## Raw Notes

# MIT 18.01 단일 변수 미적분학: 7강 - 1단원 총정리 및 시험 리뷰

## 1. 지수(Exponents)의 마지막 논평: $e$의 두 가지 정의

지난 시간에 다루었던 $e$의 정의에 대해 '철학적인 논평'을 덧붙이겠습니다.
우리는 다음 수열 $a_k$에 대해 이야기했습니다.
$$a_k = \left( 1 + \frac{1}{k} \right)^k$$

우리는 로그를 취하고 미분의 정의를 이용해 다음을 증명했습니다.
$$\lim_{k \to \infty} a_k = e$$

> [!abstract] Insight: 관점을 뒤집어라 (Reverse your perspective)
> 대부분의 등식은 양방향으로 읽힙니다. 우리는 보통 이 극한을 계산해서 $e$를 얻는다고 생각하지만, 거꾸로 **이 극한 자체가 $e$에 대한 정의**라고 볼 수도 있습니다.
>
> 1.  **미분적 정의**: $y=e^x$는 $x=0$에서의 접선의 기울기가 **1**인 함수이다.
> 2.  **극한적 정의**: $e = \lim_{k \to \infty} (1 + 1/k)^k$이다.
>
> 미적분학은 이 두 정의가 결국 **같은 대상**을 가리킨다는 것을 보여주는 과정입니다.

---

## 2. 모든 실수 $r$에 대한 멱함수의 도함수 ($x^r$)

우리는 이미 정수와 유리수 지수에 대해 $\frac{d}{dx} x^r = r x^{r-1}$임을 증명했습니다. 이제 무리수를 포함한 **모든 실수(Real numbers)** 에 대해 증명해 봅시다.

### 방법 1: 밑 $e$를 사용 (Base $e$)
$x^r = e^{\ln(x^r)} = e^{r \ln x}$로 바꿉니다.
연쇄 법칙(Chain Rule)을 적용하면:
$$\frac{d}{dx} (x^r) = \frac{d}{dx} (e^{r \ln x}) = e^{r \ln x} \cdot \frac{d}{dx}(r \ln x)$$
$$= x^r \cdot \frac{r}{x} = r x^{r-1}$$

### 방법 2: 로그 미분법 (Logarithmic Differentiation)
$u = x^r$이라 두고 양변에 로그를 취합니다.
$\ln u = r \ln x$
양변을 미분합니다.
$$\frac{u'}{u} = \frac{r}{x} \implies u' = u \cdot \frac{r}{x} = x^r \cdot \frac{r}{x} = r x^{r-1}$$

두 방법 모두 동일한 결론에 도달합니다.

---

## 3. 왜 '자연'로그인가? (Why "Natural" Logarithm?)

경제학(Economics)을 예로 들어보겠습니다.
주식 가격이 1달러 떨어졌다는 말은 무의미합니다. 중요한 것은 **비율(Ratio)** 입니다.
변화율 $\frac{\Delta P}{P}$가 중요하며, 이를 무한소로 보내면 $\frac{P'}{P}$가 됩니다.

그런데 $\frac{P'}{P}$는 무엇입니까? 바로 **$(\ln P)'$** 입니다.
$$\frac{d}{dt} (\ln P) = \frac{P'}{P}$$

경제학자들은 변동성을 다룰 때 항상 **로그 가격(Log Price)** 을 사용합니다. 만약 밑이 10인 로그($\log_{10}$)를 쓴다면 불필요한 상수 $\ln 10$이 계속 따라다닐 것입니다. 자연로그는 이러한 비율 변화를 가장 자연스럽게 기술하는 언어입니다.

---

## 4. 1단원 총정리: 핵심 공식 요약

내일 시험을 위해 여러분이 머릿속에 반드시 넣어야 할 공식들입니다.

### 가. 일반 공식 (General Formulas)
1.  **합/차/상수배**: 선형성(Linearity)
2.  **곱의 법칙**: $(uv)' = u'v + uv'$
3.  **몫의 법칙**: $(u/v)' = \frac{u'v - uv'}{v^2}$
4.  **연쇄 법칙**: $\frac{d}{dx} f(g(x)) = f'(g(x)) \cdot g'(x)$
5.  **음함수 미분법**: $y$를 $x$의 함수로 보고 미분 (역함수 미분에 필수)

> [!tip] 몫의 법칙 유도 팁
> 몫의 법칙이 기억나지 않으면, $u \cdot v^{-1}$로 바꾸고 곱의 법칙과 연쇄 법칙을 쓰세요.
> $(v^{-1})' = -v^{-2}v'$임을 이용하면 유도할 수 있습니다.

### 나. 특정 함수 공식 (Specific Formulas)
이 목록은 암기해야 합니다.

| 함수 | 도함수 | 비고 |
| :--- | :--- | :--- |
| $x^n$ | $nx^{n-1}$ | 모든 실수 $n$에 대해 |
| $\sin x$ | $\cos x$ | |
| $\cos x$ | $-\sin x$ | 부호 주의 |
| $\tan x$ | $\sec^2 x$ | $1 + \tan^2 x$와 같음 |
| $\sec x$ | $\sec x \tan x$ | |
| $e^x$ | $e^x$ | 유일한 불변 함수 |
| $\ln x$ | $1/x$ | |
| $\arctan x$ | $\frac{1}{1+x^2}$ | 매우 중요 |
| $\arcsin x$ | $\frac{1}{\sqrt{1-x^2}}$ | |

---

## 5. 실전 연습 문제 (Practice Examples)

### 예제 1: $\sec x$의 도함수
$$\frac{d}{dx} (\sec x) = \frac{d}{dx} (\cos x)^{-1} = -(\cos x)^{-2} \cdot (-\sin x) = \frac{\sin x}{\cos^2 x} = \sec x \tan x$$

### 예제 2: $\ln(\sec x)$의 도함수
연쇄 법칙 사용: $(\ln u)' = u'/u$
$$\frac{d}{dx} \ln(\sec x) = \frac{(\sec x)'}{\sec x} = \frac{\sec x \tan x}{\sec x} = \tan x$$
*역사적 노트: 이 적분($\int \tan x$)은 항해술(Mercator projection)에서 지도 제작을 위해 네이피어가 로그를 발명하게 된 계기였습니다.*

### 예제 3: $(x^{10} + 8x)^6$
**나쁜 생각**: 전개하기. (시험 시간 다 갑니다.)
**좋은 생각**: 연쇄 법칙.
$$6(x^{10} + 8x)^5 \cdot (10x^9 + 8)$$

### 예제 4: $e^x \arctan x$
곱의 법칙을 적용합니다.
$$(e^x)' \arctan x + e^x (\arctan x)' = e^x \arctan x + \frac{e^x}{1+x^2} = e^x \left( \arctan x + \frac{1}{1+x^2} \right)$$

> [!question] 답을 꼭 단순화해야 하나요?
> 시험에서는 **미분이 정확히 수행되었는지**가 중요합니다. 굳이 식을 깔끔하게 정리하느라 시간을 낭비하거나 실수를 범하지 마세요. (물론 약분 같은 뻔한 건 하세요.)

---

## 6. 도함수의 정의와 해석

### 정의를 거꾸로 읽기 (Reading in Reverse)
시험 문제에 이런 극한이 나오면, "극한을 계산하라"는 뜻이 아니라 **"이것은 어떤 함수의 미분계수인가?"** 를 묻는 것입니다.

$$\lim_{h \to 0} \frac{e^h - 1}{h}$$
이것은 $f(x) = e^x$의 $x=0$에서의 미분계수 $f'(0)$입니다.
$f'(x) = e^x \implies f'(0) = 1$. 답은 1입니다.

### 도함수 그래프 그리기
함수 $f(x)$의 그래프를 보고 $f'(x)$의 개형을 그릴 수 있어야 합니다.
1.  **기울기 부호**: 증가($f' > 0$), 감소($f' < 0$)
2.  **극점**: 기울기 0인 지점 ($f' = 0$, x절편)
3.  **변곡점**: 기울기가 가장 가파른 곳 ($f'$의 극대/극소)

---

## [보너스] $\arctan x$의 도함수 유도 (2분 컷)

$y = \arctan x$
1.  뒤집습니다: $\tan y = x$
2.  음함수 미분: $\sec^2 y \cdot y' = 1$
3.  $y'$ 정리: $y' = \frac{1}{\sec^2 y} = \cos^2 y$
4.  **삼각형 그리기**:
    $\tan y = x/1$. 밑변 1, 높이 $x$, 빗변 $\sqrt{1+x^2}$.
    $\cos y = \frac{1}{\sqrt{1+x^2}}$.
5.  대입: $y' = \left( \frac{1}{\sqrt{1+x^2}} \right)^2 = \frac{1}{1+x^2}$

자, 시험 잘 보시고 내일 봅시다!

## Questions
- 

## Merge Candidates
- [[ ]] 

## Priori Lecture
- [[L - MIT_18.01_06]]
- 

