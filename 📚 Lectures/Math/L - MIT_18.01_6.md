---
type: lecture
title: L - MIT_18.01_6
created: 2025-12-28
updated: 2026-01-18T16:42:53
author: [[김선음]]
group: General
status: [[🚜In Progress]]
tags:
  - lecture
  - lecture/General
  - tagging/needed
aliases: []
course: Single Variable Calculurs
session: 2025-12-28/02/06
migrated_from: CMDS/200. CMDS/201. Connect/202. Math/Calculurs/L - MIT_18.01_6.md
domain:
  - math
cmds: connect
---

# L - MIT_18.01_6

## Meta
- Course: Single Variable Calculurs
- Session: 2025-12-28/02/06
- Instructor: 
- URL: 

## Outline
- 

## Raw Notes

# MIT 18.01 단일 변수 미적분학: 6강 - 지수 함수와 로그 함수

## 1. 강의 소개: 마지막 기본 함수

자, 여섯 번째 강의를 시작해 봅시다. 오늘 다룰 내용은 **지수 함수(Exponentials)** 와 **로그 함수(Logarithms)** 입니다.
이 함수들은 여러분이 미적분학에서 다루어야 할 마지막 기본 함수들입니다. 삼각함수만큼이나, 어쩌면 그 이상으로 근본적인 함수들이죠.

### 지수 함수의 기본 정의
양수인 수 $a$를 하나 선택합시다. 이것을 **밑(base)** 이라고 부릅니다.
* $a^0 = 1$
* $a^1 = a$
* $a^2 = a \cdot a$
* ...

가장 근본적인 법칙은 이것입니다:
$$a^{x_1 + x_2} = a^{x_1} \cdot a^{x_2}$$

이로부터 거듭제곱의 거듭제곱 규칙이 나옵니다.
$$(a^{x_1})^{x_2} = a^{x_1 x_2}$$

### 연속성으로의 확장 (Filling in by Continuity)
지수가 정수나 유리수($m/n$)일 때는 정의가 쉽습니다. 하지만 $x = \sqrt{2}$나 $\pi$ 같은 무리수라면 $a^x$는 무엇일까요?
우리는 **연속성(Continuity)** 을 이용해 사이사이의 구멍을 메웁니다. 이것이 계산기가 작동하는 방식입니다. 계산기는 $\sqrt{2}$의 근사치를 이용해 값을 뱉어내죠.

**예시: $y = 2^x$의 그래프**
* $x=0 \to 1$
* $x=1 \to 2$
* $x=-1 \to 1/2$



이 함수는 놀라울 정도로 빠르게 증가합니다. 칠판 위쪽을 뚫고 나갈 기세죠.

---

## 2. 지수 함수의 도함수와 '수수께끼의 수' $M(a)$

우리의 목표는 미적분학을 하는 것입니다. 즉, $\frac{d}{dx} a^x$를 구하는 것이죠.
정의(Definition)로 돌아가 봅시다.

$$\frac{d}{dx} a^x = \lim_{\Delta x \to 0} \frac{a^{x + \Delta x} - a^x}{\Delta x}$$

여기서 지수 법칙 $a^{x + \Delta x} = a^x \cdot a^{\Delta x}$를 사용하는 것이 핵심 트릭입니다.

$$= \lim_{\Delta x \to 0} \frac{a^x \cdot a^{\Delta x} - a^x}{\Delta x} = \lim_{\Delta x \to 0} a^x \left( \frac{a^{\Delta x} - 1}{\Delta x} \right)$$

여기서 중요한 점은 **$x$는 극한의 입장에서 상수**라는 것입니다. $\Delta x$만 움직입니다. 따라서 $a^x$를 밖으로 뺄 수 있습니다.

$$\frac{d}{dx} a^x = a^x \cdot \underbrace{\left[ \lim_{\Delta x \to 0} \frac{a^{\Delta x} - 1}{\Delta x} \right]}_{\text{수수께끼의 수 } M(a)}$$

> [!important] The Mystery Number $M(a)$
> 우리는 아직 이 극한값이 무엇인지 모릅니다. 하지만 $a$에 따라 결정되는 어떤 숫자임은 확실합니다. 이를 $M(a)$라고 부릅시다.
> $$\frac{d}{dx} a^x = M(a) \cdot a^x$$

### $M(a)$의 기하학적 의미
이 식에 $x=0$을 대입해 보면 $M(a)$의 정체가 드러납니다.
$$\left. \frac{d}{dx} a^x \right|_{x=0} = M(a) \cdot a^0 = M(a) \cdot 1 = M(a)$$

즉, **$M(a)$는 $x=0$ (y절편)에서의 접선의 기울기(Slope)** 입니다.



---

## 3. '수수께끼의 밑' $e$의 정의

지금 우리는 "도대체 $M(a)$가 뭐지?"라는 질문에 막혀 있습니다.
여기서 수학자들이 사용하는 아주 **영리한(clever)**, 혹은 사기 같은 방법이 있습니다. 답을 구하는 대신, 답이 우리가 원하는 것이 되도록 정의해 버리는 것이죠.

> [!define] Definition of $e$
> 우리는 $x=0$에서의 기울기가 정확히 **1**이 되는 밑을 **$e$**라고 부르기로 약속합니다.
> 즉, **$M(e) = 1$**입니다.

이 정의로부터 미적분학에서 가장 아름답고 중요한 공식이 탄생합니다.

$$\frac{d}{dx} e^x = 1 \cdot e^x = e^x$$

미분해도 자기 자신이 되는 유일한 함수, 이것이 바로 $e^x$입니다.

---

## 4. $e$의 존재성 증명: 스케일링(Scaling)

"좋아요, 교수님. 정의는 좋은데 그런 숫자가 실제로 존재합니까?"
이를 확인하기 위해 $y=2^x$ 그래프를 늘리거나 줄여(Scaling) 봅시다.

함수 $f(x) = 2^x$를 수평 방향으로 $k$배 스케일링하면 $2^{kx} = (2^k)^x$가 됩니다.
이것을 새로운 밑 $b = 2^k$를 가진 함수 $b^x$라고 생각할 수 있습니다.

연쇄 법칙(Chain Rule)에 의해:
$$\frac{d}{dx} 2^{kx} = k \cdot \ln 2 \cdot 2^{kx} \quad (\text{나중에 배울 내용을 미리 쓰자면})$$
핵심은 **그래프를 압축하거나 늘리면, $x=0$에서의 기울기도 비례해서 변한다**는 것입니다.

* $2^x$의 기울기 $M(2) \approx 0.69$
* 우리는 기울기가 1이 되도록 적절한 압축 비율 $k$를 찾을 수 있습니다. ($k = 1/M(2)$)
* 그렇게 만들어진 새로운 밑 $b$가 바로 $e$입니다. 따라서 $e$는 반드시 존재합니다.

> [!note] Analogy: Radians vs Degrees
> 이것은 삼각함수에서 **라디안(Radian)**을 쓰는 이유와 같습니다.
> 도(Degree)를 쓰면 $(\sin x)' = \frac{\pi}{180} \cos x$처럼 지저분한 상수가 붙습니다. 이 상수를 1로 만들기 위해 라디안을 쓰죠.
> 마찬가지로, 지수 함수 미분에서 지저분한 상수 $M(a)$를 1로 만들기 위해 우리는 **자연 밑(Natural Base) $e$**를 사용합니다.

---

## 5. 자연 로그 (Natural Logarithm)

자연 로그 $\ln x$는 $e^x$의 **역함수(Inverse Function)** 로 정의됩니다.
$$y = \ln x \iff x = e^y$$



* $e^x$가 $(0, 1)$을 지나므로, $\ln x$는 $(1, 0)$을 지납니다.
* $x=0$에서 $e^x$의 기울기가 1이므로, $x=1$에서 $\ln x$의 기울기도 1입니다.

### 자연 로그의 도함수 유도 (음함수 미분법)
우리는 음함수 미분법(Implicit Differentiation)이라는 강력한 무기가 있습니다.

1.  $w = \ln x$라고 둡시다.
2.  역함수 관계식으로 바꿉니다: $e^w = x$
3.  양변을 $x$로 미분합니다.
    $$\frac{d}{dx}(e^w) = \frac{d}{dx}(x)$$
    $$e^w \cdot \frac{dw}{dx} = 1 \quad (\text{연쇄 법칙: } \frac{d}{dw}e^w = e^w)$$
4.  $\frac{dw}{dx}$에 대해 풉니다.
    $$\frac{dw}{dx} = \frac{1}{e^w}$$
5.  $e^w = x$이므로 대입합니다.

> [!important] Derivative of $\ln x$
> $$\frac{d}{dx} \ln x = \frac{1}{x}$$

---

## 6. 일반 지수 함수의 도함수: $M(a)$의 정체

이제 다시 처음의 문제로 돌아갑시다. $\frac{d}{dx} a^x = M(a) a^x$에서 과연 $M(a)$는 무엇일까요?
두 가지 방법으로 풀 수 있습니다.

### 방법 1: 밑 변환 (Convert to Base $e$)
모든 수를 $e$로 표현할 수 있습니다. $a = e^{\ln a}$이므로,
$$a^x = (e^{\ln a})^x = e^{x \ln a}$$

이제 미분해 봅시다. (여기서 $\ln a$는 **상수**입니다!)
$$\frac{d}{dx} (e^{(\ln a) x}) = (\ln a) \cdot e^{(\ln a) x} = (\ln a) \cdot a^x$$

### 방법 2: 로그 미분법 (Logarithmic Differentiation)
이 방법은 복잡한 지수 함수를 다룰 때 매우 유용합니다.
$u = a^x$라고 두고 양변에 $\ln$을 취합니다.
$$\ln u = x \ln a$$

양변을 미분합니다.
$$\frac{u'}{u} = \ln a$$
$$u' = u (\ln a) = a^x (\ln a)$$

결국 우리는 $M(a)$의 정체를 밝혀냈습니다.
$$M(a) = \ln a$$

> [!summary] General Exponential Derivative
> $$\frac{d}{dx} a^x = (\ln a) a^x$$

---

## 7. 로그 미분법의 응용: 움직이는 지수 ($x^x$)

밑과 지수가 모두 변수인 함수, 예를 들어 $y = x^x$는 어떻게 미분할까요?
거듭제곱 법칙($nx^{n-1}$)도, 지수 법칙($a^x \ln a$)도 쓸 수 없습니다. 오직 **로그 미분법**만이 답입니다.

1.  양변에 로그를 취합니다.
    $$\ln y = \ln (x^x) = x \ln x$$
2.  양변을 미분합니다. (우변은 곱의 법칙 사용)
    $$\frac{y'}{y} = (1) \cdot \ln x + x \cdot \frac{1}{x} = \ln x + 1$$
3.  $y'$에 대해 정리합니다.
    $$y' = y (\ln x + 1) = x^x (\ln x + 1)$$

---

## 8. $e$의 엄밀한 계산: 극한을 이용한 정의

마지막으로, 우리가 정의만 하고 넘어갔던 $e$를 실제로 계산하는 방법(극한 공식)을 유도하며 강의를 마치겠습니다.

우리는 이 극한을 계산하고 싶습니다:
$$\lim_{n \to \infty} \left( 1 + \frac{1}{n} \right)^n$$

이 값을 $A$라고 하고 로그를 취해 봅시다.
$$\ln A = \lim_{n \to \infty} n \ln \left( 1 + \frac{1}{n} \right)$$

변수 변환을 합니다. $\Delta x = \frac{1}{n}$이라 하면, $n \to \infty$일 때 $\Delta x \to 0$입니다.
$$= \lim_{\Delta x \to 0} \frac{1}{\Delta x} \ln (1 + \Delta x) = \lim_{\Delta x \to 0} \frac{\ln(1 + \Delta x) - \ln 1}{\Delta x}$$
*($\ln 1 = 0$이므로 빼도 상관없습니다.)*

이 식의 형태를 잘 보세요. 이것은 정확히 **$f(x) = \ln x$의 $x=1$에서의 미분계수 정의**입니다!
우리는 이미 $(\ln x)' = 1/x$임을 알고 있습니다. 따라서 $x=1$에서의 미분계수는 $1/1 = 1$입니다.

결론적으로:
$$\ln A = 1 \implies A = e^1 = e$$

따라서,
$$e = \lim_{n \to \infty} \left( 1 + \frac{1}{n} \right)^n$$

이로써 우리는 $e$의 정의, 미분법, 그리고 계산 방법까지 하나의 완벽한 고리(Loop)를 완성했습니다.

## Questions
- 

## Merge Candidates
- [[ ]] 

## Priori Lecture
- [[ ]] 

