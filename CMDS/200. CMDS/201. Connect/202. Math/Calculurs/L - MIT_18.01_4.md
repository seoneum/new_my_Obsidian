---
type: lecture
title: L - MIT_18.01_4
created: 2025-12-23
updated: 2025-12-23T14:30:26
author:
  - "[[David Jerison]]"
group:
  - Math
status: "[[🚜In Progress]]"
tags:
  - lecture
  - lecture/General
  - tagging/needed
aliases: []
session: 2025-12-23/01/02
---

# L - MIT_18.01_2

## Meta
- Course: "MIT 18.01: Single Variable Calculus"
- Session: 2025-12-23/01/04
- Instructor: [[David Jerison]]
- URL: 

## Outline
- 

## Raw Notes
# MIT 18.01 단일 변수 미적분학: 4강 - 미분 규칙의 확장

## 1. 강의 소개 (Introduction)

안녕하세요, 저는 **하네스 밀러(Hannes Miller)**입니다. 오늘은 데이비드 제리슨 교수님을 대신하여 보조 교사로 왔습니다. 그러니까 오늘은 대체 교사(substitute teacher)와 함께 하는 날입니다.

저는 여러분과 이 수업을 함께 하지 않았기 때문에, 지금 정확히 어디까지 진도를 나갔는지 완전히 확신하지는 못합니다. 아마도 여러분은 방금 미분(differentiation)에 대해 이야기했을 것이고, 몇 가지 기본적인 미분 예시들을 보았을 겁니다. 예를 들어, $x^n$의 미분은 $nx^{n-1}$이 된다는 것과, 아마도 최근에 사인(sine) 함수의 미분을 계산하는 데 시간을 보냈을 것입니다.

그리고 이 기본적인 계산들을 확장할 수 있는 몇 가지 규칙들도 알고 있을 겁니다.
* **상수배의 법칙**: $(cu)' = c(u')$ (상수는 밖으로 나옵니다.)
* **합의 법칙**: $(u+v)' = u' + v'$

저는 오늘 이 규칙들을 사용할 것입니다. 하지만 오늘의 진짜 목표는 다음 규칙들을 다루는 것입니다.

> [!abstract] **Today's Goals**
> 1.  **곱의 규칙 (Product Rule)**
> 2.  **몫의 규칙 (Quotient Rule)**
> 3.  **연쇄 규칙 (Chain Rule)**: 가장 중요한 합성(Composition)에 대한 규칙
> 4.  **고계 미분 (Higher Derivatives)**

---

## 2. 곱의 규칙 (Product Rule)

자, 그럼 곱의 규칙부터 시작해 봅시다. 곱의 규칙은 두 함수의 곱을 어떻게 미분하는지 알려줍니다. 일단 규칙부터 먼저 알려드리겠습니다.

> [!important] Product Rule Formula
> $$(UV)' = U'V + UV'$$

조금 이상하죠? 곱을 미분했는데 결과가 합(sum)으로 나오네요.

### 2.1. 예시: $x^n \sin(x)$의 미분

우리가 방금 이야기했던 두 가지 기본 함수를 곱한 예시를 들어봅시다. $x^n$과 $\sin(x)$의 곱을 미분하고 싶다고 가정해 봅시다. 이것은 곱의 규칙 없이는 할 수 없는 새로운 유형의 미분입니다.

* $U = x^n$
* $V = \sin(x)$

이 규칙을 적용해 봅시다.

1.  **$U'V$ 항**:
    $U' = nx^{n-1}$이고, 여기에 $V=\sin(x)$를 그대로 곱합니다.
    $\rightarrow (nx^{n-1})\sin(x)$
2.  **$UV'$ 항**:
    $U=x^n$을 그대로 두고, $V' = (\sin(x))' = \cos(x)$를 곱합니다.
    $\rightarrow x^n \cos(x)$

따라서,
$$\frac{d}{dx} (x^n \sin(x)) = nx^{n-1}\sin(x) + x^n \cos(x)$$

> [!note] 해설
> 곱의 규칙 $(UV)' = U'V + UV'$는 변화율(미분)을 측정할 때, **한 함수가 고정된 상태에서 다른 함수의 변화율을 더하는 방식**으로 전체 변화율을 측정한다는 개념을 반영합니다. 이는 마치 직사각형의 넓이 변화를 계산할 때, 한 변을 고정하고 다른 변의 변화를 곱하는 원리와 같습니다.

### 2.2. 곱의 규칙 증명: $\Delta (UV)$를 이용한 접근

자, 그럼 이 규칙이 왜 참인지 증명해 봅시다. 미분을 이해하는 표준적인 방법은 우리가 미분하려는 함수의 변화량($\Delta$)을 살펴보는 것입니다.

우리가 구하려는 변화량 $\Delta(UV)$는 새로운 값에서 이전 값을 뺀 것입니다.
$$\Delta(UV) = U(x+\Delta x)V(x+\Delta x) - U(x)V(x)$$

여기서 핵심은 $U$만의 변화량($\Delta U$)과 $V$만의 변화량($\Delta V$)을 포함하도록 이 식을 조작하는 것입니다. 이를 위해 **교묘한 중간 항을 삽입**합니다. $U(x)V(x+\Delta x)$를 뺐다가 다시 더해줍니다. 이것이 핵심적인 대수학적 조작입니다.

$$\Delta(UV) = [U(x+\Delta x)V(x+\Delta x) - \mathbf{U(x)V(x+\Delta x)}] + [\mathbf{U(x)V(x+\Delta x)} - U(x)V(x)]$$

* 첫 번째 괄호에서 $V(x+\Delta x)$를 묶어내면:
    $$[U(x+\Delta x) - U(x)] V(x+\Delta x) = \Delta U \cdot V(x+\Delta x)$$
* 두 번째 괄호에서 $U(x)$를 묶어내면:
    $$U(x) [V(x+\Delta x) - V(x)] = U(x) \cdot \Delta V$$

따라서 $\Delta(UV)$는 다음과 같이 정리됩니다.
$$\Delta(UV) = \Delta U \cdot V(x+\Delta x) + U(x) \cdot \Delta V$$

### 2.3. 극한 취하기

이제 미분계수(difference quotient)를 구하기 위해 이 전체 식을 $\Delta x$로 나누고, 극한을 취합니다.

$$\frac{\Delta (UV)}{\Delta x} = \left(\frac{\Delta U}{\Delta x}\right) V(x+\Delta x) + U(x) \left(\frac{\Delta V}{\Delta x}\right)$$

이제 $\Delta x \to 0$ 극한을 취하면:
1.  $\frac{\Delta U}{\Delta x} \to U'$
2.  $\frac{\Delta V}{\Delta x} \to V'$
3.  **중요**: $V(x+\Delta x) \to V(x)$ (연속성이므로)

결과적으로 우리가 원하는 미분 공식을 얻습니다.

$$\frac{d}{dx} (UV) = \frac{dU}{dx} V + U \frac{dV}{dx}$$

이로써 곱의 규칙은 증명되었습니다. 이 규칙 덕분에 우리는 이제 훨씬 더 많은 함수의 도함수를 구할 수 있게 되었으니, 우리는 더 강해진 것입니다.

---

## 3. 몫의 규칙 (Quotient Rule)

이제 함수들의 몫(Quotient), 즉 $\frac{U}{V}$를 어떻게 미분하는지 알아봅시다. 다시 한번 답부터 알려드리고, 그다음에 증명해 보겠습니다.

> [!important] Quotient Rule Formula
> $$\left(\frac{U}{V}\right)' = \frac{U'V - UV'}{V^2}$$

이것이 여러분이 이 과정에서 보게 될 가장 기이한(weirdest) 규칙일 수도 있습니다. 하지만 분명히 존재합니다.

> [!warning] 주의: 순서가 중요합니다!
> 몫의 규칙은 $U'V - UV'$의 순서를 절대 잊어서는 안 됩니다. 분자 미분($U'$)이 먼저 나오고, 나중에 분모 미분($V'$)을 뺍니다. 분모는 항상 $V^2$입니다.

### 3.1. 몫의 규칙 증명: $\frac{U}{V}$의 변화량

다시 한번 $\Delta x$에 대한 몫의 변화량 $\Delta (\frac{U}{V})$을 계산해 봅시다.

$$\Delta \left(\frac{U}{V}\right) = \frac{U+\Delta U}{V+\Delta V} - \frac{U}{V}$$

이것을 통분합니다.
분자는 $(U+\Delta U)V - U(V+\Delta V)$가 되고, 분모는 $(V+\Delta V)V$가 됩니다.

분자를 전개해 봅시다.
$$(U V + \Delta U \cdot V) - (U V + U \cdot \Delta V)$$
여기서 $UV$ 항은 서로 상쇄됩니다. 따라서:

$$\Delta \left(\frac{U}{V}\right) = \frac{\Delta U \cdot V - U \cdot \Delta V}{(V+\Delta V)V}$$

### 3.2. 극한 취하기

이제 미분계수를 얻기 위해 $\Delta x$로 나누고 극한을 취합니다.

$$\frac{1}{\Delta x} \Delta \left(\frac{U}{V}\right) = \frac{\frac{\Delta U}{\Delta x} V - U \frac{\Delta V}{\Delta x}}{(V+\Delta V)V}$$

$\Delta x \to 0$ 극한을 취하면:
* 분자: $\frac{\Delta U}{\Delta x} \to U'$, $\frac{\Delta V}{\Delta x} \to V'$
* 분모: $\Delta V \to 0$이므로, $V \cdot V = V^2$이 됩니다.

$$\frac{d}{dx} \left(\frac{U}{V}\right) = \frac{U'V - UV'}{V^2}$$

### 3.3. 응용 예시: 음의 지수 ($x^{-n}$)

이 규칙을 활용해 봅시다. 가장 간단한 예시로 분자 $U=1$인 경우, 즉 $\frac{1}{V}$를 미분하는 경우입니다.
$U=1 \implies U'=0$ 이므로:

$$\frac{d}{dx} \left(\frac{1}{V}\right) = \frac{(0)V - (1)V'}{V^2} = -\frac{V'}{V^2}$$

이제 $x^{-n}$, 즉 $\frac{1}{x^n}$을 미분해 봅시다. ($V=x^n$)
* $V' = nx^{n-1}$
* $V^2 = (x^n)^2 = x^{2n}$

$$\frac{d}{dx} \left(\frac{1}{x^n}\right) = - \frac{nx^{n-1}}{x^{2n}} = -n x^{(n-1) - 2n} = -n x^{-n-1}$$

놀랍게도, 우리가 원래 알고 있던 거듭제곱 규칙 $\frac{d}{dx} x^k = k x^{k-1}$이 음의 지수 $k=-n$에 대해서도 정확히 성립합니다! 이 몫의 규칙을 통해 우리는 미분 규칙을 음의 지수까지 확장할 수 있게 된 것입니다.

---

## 4. 연쇄 규칙 (Chain Rule): 합성 함수의 미분

이제 연쇄 규칙(Chain Rule), 즉 **함수의 합성(Composition)** 에 대한 규칙을 살펴봅시다.

합성은 **대입(Substitution)** 에 관한 것입니다.
예를 들어, $Y=(\sin(T))^{10}$과 같은 함수입니다. 우리는 이전에 이런 종류의 함수를 미분하는 방법을 배운 적이 없습니다.

> [!tip] Notation Note
> 사람들은 $(\sin(T))^{10}$을 $\sin^{10}(T)$라고 표기하기도 합니다. 이 표기법은 $\sin(T)$를 먼저 계산한 다음 전체를 10제곱하라는 의미임을 기억하세요.

이러한 합성 함수를 다루는 방법은 **새로운 변수 이름**을 도입하는 것입니다.
1.  **내부 함수 (Inner Function)**: $X = \sin(T)$
2.  **외부 함수 (Outer Function)**: $Y = X^{10}$

 이처럼 편리한 경우에 새로운 문자를 도입하는 것은 좋은 습관입니다.

### 4.1. 연쇄 규칙의 유도

우리는 $Y$가 원래 변수 $T$에 대해 얼마나 변하는지, 즉 $\frac{dY}{dT}$에 관심이 있습니다.
중간 변수 $X$ 덕분에 우리는 변화량 비율을 다음과 같이 쓸 수 있습니다.

$$\frac{\Delta Y}{\Delta T} = \frac{\Delta Y}{\Delta X} \cdot \frac{\Delta X}{\Delta T}$$

$\Delta X$가 대수학적으로 상쇄되는 것처럼 보이죠? 이제 $\Delta T \to 0$ 극한을 취하면, 바로 미분 공식을 얻습니다.

> [!important] Chain Rule Formula
> $$\frac{dY}{dT} = \frac{dY}{dX} \cdot \frac{dX}{dT}$$

학생들은 종종 이 규칙을 $dX$가 상쇄되는 것처럼 기억하는데, 이는 진실과 크게 다르지 않은 좋은 사고방식입니다. 이것이 바로 **연쇄 규칙(Chain Rule)** 입니다. 합성 함수의 미분은 단순히 두 도함수의 곱이 됩니다.

### 4.2. 예시: $(\sin(T))^{10}$의 미분

다시 이 예시를 적용해 봅시다. $\frac{d}{dT} (\sin(T))^{10}$
1.  **바깥쪽 함수 미분 ($dY/dX$)**: $Y=X^{10} \implies 10X^9$
2.  **안쪽 함수 미분 ($dX/dT$)**: $X=\sin(T) \implies \cos(T)$

두 결과를 곱하고, $X$를 다시 원래대로 돌려놓습니다.

$$\frac{dY}{dT} = (10X^9) \cdot (\cos(T)) = 10 (\sin(T))^9 \cos(T)$$

> [!summary] Insight
> 연쇄 규칙은 미분 세계의 **'족쇄를 부수는(burst the chains)'** 규칙입니다. 연쇄 규칙을 터득하면 미분할 수 있는 함수의 종류가 기하급수적으로 늘어납니다. 핵심은 "바깥쪽을 미분하고, 안쪽은 그대로 둔 다음, 안쪽을 미분한 것을 곱한다"는 순서를 지키는 것입니다.

### 4.3. 또 다른 예시: $\sin(10T)$의 미분

이번에는 $\sin(10T)$를 미분해 봅시다.
* 안쪽($X$): $10T$
* 바깥쪽($Y$): $\sin(X)$

$$\frac{dY}{dT} = \cos(X) \cdot 10 = 10 \cos(10T)$$

> [!example] Tip: Mental Shortcut (암산하는 법)
> 익숙해지면 중간 변수 $X$를 명시적으로 쓰지 않고도 할 수 있습니다.
> 1.  바깥 함수 $\sin(\cdot)$를 미분합니다. $\rightarrow \cos(\cdot)$
> 2.  안쪽 함수 $10T$는 그대로 둡니다. $\rightarrow \cos(10T)$
> 3.  이제 안쪽 함수 $10T$를 미분한 것($10$)을 곱합니다. $\rightarrow 10 \cos(10T)$
>
> 이러한 지름길에 익숙해지면, 연쇄 규칙을 가진 여러분은 세상을 정복할 수 있는 매우 강력한 위치에 있게 됩니다.

---

## 5. 고계 미분 (Higher Derivatives)

오늘 다룬 세 가지 규칙에 더해, 고계 미분에 대해 간단히 이야기하겠습니다. 고계 미분은 간단하게 말해, 함수를 계속해서 미분하는 것을 의미합니다.

### 5.1. 표기법 (Notation)

함수 $U$에 대하여:

| 미분 계수 | $U'$ 표기법 | $\frac{d}{dx}$ 표기법 | $D$ 연산자 표기법 | 설명 |
| :--- | :--- | :--- | :--- | :--- |
| **1계** | $U'$ | $\frac{dU}{dx}$ | $DU$ | 원래 함수를 미분한 것 |
| **2계** | $U''$ | $\frac{d^2U}{dx^2}$ | $D^2U$ | $U'$을 다시 미분한 것 |
| **3계** | $U'''$ | $\frac{d^3U}{dx^3}$ | $D^3U$ | $U''$을 다시 미분한 것 |
| **$n$계** | $U^{(n)}$ | $\frac{d^nU}{dx^n}$ | $D^nU$ | $n$번째 미분 |

$\frac{d^2U}{dx^2}$ 표기법은 조금 이상하게 보일 수 있는데, 여기서 분모는 $D$와 $X^2$가 곱해진 것이 아니라, $(DX)^2$을 의미하는, 즉 미분 연산자를 두 번 적용했다는 표기상의 약속입니다.
$D$ 표기법($D = \frac{d}{dx}$)은 미분을 함수에 적용되는 **연산자(Operator)** 로 간주하는 것입니다.

### 5.2. 예시: $\sin(x)$의 고계 미분

$U = \sin(x)$일 때 고계 미분을 계산해 봅시다.

1.  $U' = \cos(x)$
2.  $U'' = -\sin(x)$ (코사인을 미분하면 마이너스 사인이 되죠.)
3.  $U''' = -\cos(x)$
4.  $U^{(4)} = \sin(x)$

$\sin(x)$를 네 번 미분하면 다시 $\sin(x)$로 돌아옵니다. 정말 기묘하죠! 하지만 이것은 사인 및 코사인 함수에만 매우 특별하게 나타나는 현상입니다.

### 5.3. 예시: $x^n$의 $n$계 도함수

그럼 다른 예시를 봅시다. $x^n$의 $n$계 도함수, 즉 $D^n(x^n)$을 계산해 봅시다.

* $D(x^n) = nx^{n-1}$
* $D^2(x^n) = n(n-1)x^{n-2}$
* $D^3(x^n) = n(n-1)(n-2)x^{n-3}$

이러한 패턴을 계속 따라가서 $n$번 미분하면 어떻게 될까요? 마지막 남은 $x$의 1차 항을 미분하면 1이 되므로, $x$는 사라지고 상수가 남습니다.

$$D^n (x^n) = n \cdot (n-1) \cdot (n-2) \cdot \ldots \cdot 2 \cdot 1 = n!$$

이 숫자를 우리는 **$n$ 팩토리얼($n!$)** 이라고 부릅니다. 이것은 깔끔한 사실입니다.

그렇다면 **최종 질문**입니다. $x^n$의 $n+1$계 도함수, 즉 $D^{n+1}(x^n)$은 무엇일까요?

네, $n$계 도함수는 상수 $n!$ 이었고, **상수를 미분하면 0**이 됩니다. 훌륭합니다!

## Questions
- 

## Merge Candidates
- [[ ]] 

## Priori Lecture
- [[L - MIT_18.01_3]] 

