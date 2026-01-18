---
type: lecture
title: L - MIT_18.01_3
created: 2025-12-23
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
session: 2025-12-23/01/03
migrated_from: CMDS/200. CMDS/201. Connect/202. Math/Calculurs/L - MIT_18.01_3.md
domain:
  - math
cmds: connect
---

# L - MIT_18.01_3

## Meta
- Course: "MIT 18.01: Single Variable Calculus" 
- Session: 2025-12-23/01/03
- Instructor: [[David Jerison]]
- URL: 

## Outline
- 

## Raw Notes

# MIT 18.01 단일 변수 미적분학: 3강 - 미분 공식 개발 (삼각함수, 곱/몫의 법칙)

## 1. 강의 소개: 미분 공식의 종류

오늘 강의에서는 우리의 최종 목표인 **"모든 함수를 미분할 수 있게 되는 것"** 에 도달하기 위해 몇 가지 중요한 공식을 더 다룰 것입니다. 이 공식들은 크게 두 가지 범주로 나뉩니다.

### 1.1. 특정 함수 공식 (Specific Formulas)
특정 함수의 미분 결과를 명확하게 제시하는 공식들입니다.
* **예시**: $\frac{d}{dx}(x^n) = nx^{n-1}$, $\frac{d}{dx}(\frac{1}{x}) = -\frac{1}{x^2}$
* 우리가 지난 몇 번의 강의에서 이미 다루었던 내용들입니다.

### 1.2. 일반 공식 (General Formulas)
함수 자체가 아니라, 함수들이 결합되거나 조작되었을 때 미분이 어떻게 작동하는지를 알려주는 규칙입니다.
* **예시**: $(u + v)' = u' + v'$, $(cu)' = c \cdot u'$ (여기서 $c$는 상수)

이 두 종류의 공식을 결합하면, 우리는 다항식뿐만 아니라 훨씬 더 복잡한 함수들도 다룰 수 있게 됩니다. 기본적인 벽돌(특정 공식)과 그것을 쌓는 방법(일반 공식)을 모두 갖추는 셈이죠.

---

## 2. 삼각함수의 미분 (Trigonometric Derivatives)

오늘 우리는 **삼각함수(Trigonometric functions)** 에 집중할 것입니다. $\sin x$와 $\cos x$의 미분 공식을 유도해 봅시다.

### 2.1. $\sin x$의 미분 유도

미분의 정의(차분 몫의 극한)에서 시작합니다.

$$
\frac{d}{dx} (\sin x) = \lim_{\Delta x \to 0} \frac{\sin(x + \Delta x) - \sin x}{\Delta x}
$$

여기서 우리가 할 수 있는 유일한 대수적 조작은 **사인 함수의 덧셈 공식(Addition Formula)** 을 사용하는 것입니다.
* $\sin(A+B) = \sin A \cos B + \cos A \sin B$

$A=x$, $B=\Delta x$를 대입하여 전개하면:

$$
= \lim_{\Delta x \to 0} \frac{[\sin x \cos(\Delta x) + \cos x \sin(\Delta x)] - \sin x}{\Delta x}
$$

> [!warning] 0/0 꼴의 처리
> $\Delta x \to 0$을 바로 대입하면 분모와 분자가 모두 0이 되어 $\frac{0}{0}$ 꼴이 됩니다. 의미 있는 값을 얻기 위해서는 식을 재정렬(regrouping)해야 합니다.

공통 인수인 $\sin x$로 묶어서 항을 분리해 봅시다.

$$
= \lim_{\Delta x \to 0} \left[ \sin x \left( \frac{\cos(\Delta x) - 1}{\Delta x} \right) + \cos x \left( \frac{\sin(\Delta x)}{\Delta x} \right) \right]
$$

이제 이 극한을 풀기 위해서는 $\Delta x$가 0으로 갈 때 괄호 안의 식들이 어디로 수렴하는지 알아야 합니다. 우리는 다음 **두 가지 극한 사실(Limit Facts)** 에 의존할 것입니다. (곧 증명할 겁니다!)

| 극한 사실 | 수식 | 결과값 |
| :--- | :--- | :--- |
| **극한 A** | $\lim_{\theta \to 0} \frac{\cos \theta - 1}{\theta}$ | **0** |
| **극한 B** | $\lim_{\theta \to 0} \frac{\sin \theta}{\theta}$ | **1** |

이 사실들을 적용하면:
1.  **첫 번째 항**: $\sin x \cdot 0 = 0$
2.  **두 번째 항**: $\cos x \cdot 1 = \cos x$

따라서 결론은 다음과 같습니다.

> [!important] Derivative of Sine
> $$\frac{d}{dx} (\sin x) = \cos x$$

---

### 2.2. $\cos x$의 미분 유도

코사인 함수도 동일한 과정을 거칩니다. 이번에는 코사인의 덧셈 공식을 사용합니다.
* $\cos(A+B) = \cos A \cos B - \sin A \sin B$ (**부호 주의!**)

$$
\frac{d}{dx} (\cos x) = \lim_{\Delta x \to 0} \frac{\cos(x + \Delta x) - \cos x}{\Delta x}
$$

$$
= \lim_{\Delta x \to 0} \frac{[\cos x \cos(\Delta x) - \sin x \sin(\Delta x)] - \cos x}{\Delta x}
$$

항을 재정렬하면:

$$
= \lim_{\Delta x \to 0} \left[ \cos x \left( \frac{\cos(\Delta x) - 1}{\Delta x} \right) - \sin x \left( \frac{\sin(\Delta x)}{\Delta x} \right) \right]
$$

극한 사실 A와 B를 다시 적용합니다:
1.  **첫 번째 항**: $\cos x \cdot 0 = 0$
2.  **두 번째 항**: $-\sin x \cdot 1 = -\sin x$

> [!important] Derivative of Cosine
> $$\frac{d}{dx} (\cos x) = -\sin x$$

> [!note] 해설: 미분 공식의 구조
> 이 유도 과정에서 가장 흥미로운 점은, $\sin x$와 $\cos x$의 모든 미분값이 **$x=0$에서의 미분값(초기 조건)**에 의해 결정된다는 것입니다. 우리가 사용한 극한 A와 B는 사실 $x=0$에서의 코사인과 사인의 미분계수 정의와 정확히 일치합니다.

---

## 3. 극한 사실 A와 B의 기하학적 증명

이제 앞서 사용한 두 가지 극한($\theta \to 0$일 때)이 왜 참인지 **기하학적**으로 증명해야 합니다. 삼각함수는 기하학에서 왔으므로, 그림을 그려서 증명하는 것이 가장 타당합니다.



### 3.1. 극한 B: $\lim_{\theta \to 0} \frac{\sin \theta}{\theta} = 1$ 증명

단위 원(Unit Circle, 반지름=1)을 생각합시다. 중심각이 $\theta$일 때:
* **$\sin \theta$**: 높이, 즉 **현(Chord)** 의 절반 길이입니다. (정확히는 수직선)
* **$\theta$**: **호(Arc)** 의 길이입니다. (라디안 정의에 의해 $r\theta = 1\cdot\theta = \theta$)

우리가 구하려는 극한 $\frac{\sin \theta}{\theta}$는 기하학적으로 **$\frac{\text{현의 절반}}{\text{호의 길이}}$** 의 비율을 묻는 것입니다.

> [!tip] 기하학적 원리
> **"짧은 곡선은 거의 직선과 같다 (Short curves are nearly straight)."**
> 각 $\theta$가 작아질수록, 둥근 호(Arc)는 직선인 현(Chord)과 거의 겹쳐집니다.

$\theta \to 0$일 때, 호의 길이와 현의 길이는 같아집니다. 따라서 그 비율은 1이 됩니다.

$$\lim_{\theta \to 0} \frac{\sin \theta}{\theta} = 1$$

*(주의: 이 공식은 반드시 **라디안(Radian)** 단위를 쓸 때만 성립합니다. 도(Degree)를 쓰면 비율이 달라집니다.)*

---

### 3.2. 극한 A: $\lim_{\theta \to 0} \frac{\cos \theta - 1}{\theta} = 0$ 증명

이 식은 $\lim \frac{1 - \cos \theta}{\theta}$로 부호를 바꿔서 생각하는 것이 편합니다(길이는 양수니까요).



* **$1$**: 원의 반지름입니다.
* **$\cos \theta$**: 원점에서 수직선까지의 수평 거리입니다.
* **$1 - \cos \theta$**: 반지름과 코사인 거리 사이의 **작은 틈(Gap)**, 또는 화살의 **오늬(Sagitta)** 부분입니다.

우리는 **$\frac{\text{틈새(Gap)}}{\text{호의 길이}(\theta)}$** 의 극한을 구하는 것입니다.

$\theta$가 0으로 갈 때:
1.  분모($\theta$)도 0으로 갑니다.
2.  분자($1 - \cos \theta$)도 0으로 갑니다.
3.  하지만 **틈새(분자)가 호의 길이(분모)보다 훨씬 더 빠르게 사라집니다.**

그림을 상상해보세요. 각도가 줄어들면 수직선은 원의 가장자리에 아주 빠르게 달라붙습니다. 틈새는 $\theta$의 제곱($\approx \theta^2/2$)에 비례하여 작아지기 때문에, 1차인 $\theta$로 나누면 결과는 0이 됩니다.

$$\lim_{\theta \to 0} \frac{\cos \theta - 1}{\theta} = 0$$

---

## 4. $\sin x$ 미분 공식의 기하학적 재증명

앞서 대수적으로(덧셈 공식을 써서) 유도했던 $(\sin x)' = \cos x$를, 이번에는 그림을 통해 **직관적으로** 증명해 보겠습니다. 이 과정은 물리나 공학적 직관을 기르는 데 매우 유용합니다.



**상황 설정**:
1.  단위 원 위에 점 $P$가 있고, 각도는 $\theta$입니다. 이때 $P$의 높이는 $y = \sin \theta$입니다.
2.  각도가 아주 조금 $\Delta \theta$만큼 증가하여 점 $Q$로 이동했다고 합시다.
3.  우리의 목표는 높이의 변화량 $\Delta y$와 각도 변화량 $\Delta \theta$의 비율을 찾는 것입니다.

**기하학적 분석**:
* 점 $P$에서 $Q$까지의 **호의 길이**는 $\Delta \theta$입니다. ( $\Delta \theta$가 매우 작으면 직선 **현(Chord)** 의 길이와 같습니다.)
* 우리는 직각삼각형 $PQR$을 만듭니다. 여기서 빗변은 $PQ \approx \Delta \theta$이고, 높이 $PR$은 $\Delta y$입니다.
* **핵심 질문**: 이 작은 삼각형 $PQR$의 각도 $\angle QPR$은 얼마일까요?

> [!quote] Hannes Miller's Insight
> "이것은 **90도 회전**의 원리입니다."
> * 원의 반지름 $OP$는 수평선과 $\theta$의 각을 이룹니다.
> * 접선(빗변 $PQ$)은 반지름 $OP$와 수직입니다.
> * 따라서 작은 삼각형 $PQR$은 원래의 큰 삼각형을 90도 회전시킨 것과 유사합니다. 즉, **$\angle QPR \approx \theta$**가 됩니다.

**계산**:
작은 삼각형 $PQR$에서:
$$\Delta y = \text{빗변} \times \cos(\text{사이각})$$
$$\Delta y \approx \Delta \theta \cdot \cos \theta$$


![[Recording 20251223203108.m4a]]
양변을 $\Delta \theta$로 나누면:
$$\frac{\Delta y}{\Delta \theta} \approx \cos \theta$$

극한 $\Delta \theta \to 0$을 취하면 등호가 성립합니다. 이것이 바로 기하학적 증명입니다!

---

## 5. 일반 미분 공식 (General Differentiation Rules)

시간 관계상 오늘은 증명 없이 공식만 소개하겠습니다. 하지만 이들은 미분학의 **엔진**과도 같은 매우 중요한 공식들입니다. 다음 시간에 엄밀하게 증명할 것이며, 여러분은 이 증명들을 반드시 숙지해야(responsible for) 합니다.

### 5.1. 곱의 법칙 (Product Rule)



두 함수 $u$와 $v$의 곱을 미분할 때 사용하는 공식입니다.

$$
(uv)' = u'v + uv'
$$

> [!tip] 암기법
> **"한 번에 하나씩 변화시킨다."**
> $u$가 변할 때($u'$) $v$는 가만히 있고, $v$가 변할 때($v'$) $u$는 가만히 있어서 그 효과를 더합니다. 직사각형 넓이의 변화를 상상하면 이해가 쉽습니다.

### 5.2. 몫의 법칙 (Quotient Rule)

두 함수의 나눗셈 형태를 미분하는 공식입니다. (단, $v \neq 0$)

$$
\left(\frac{u}{v}\right)' = \frac{u'v - uv'}{v^2}
$$

> [!warning] 주의: 순서가 중요함
> 덧셈인 곱의 법칙과 달리, 몫의 법칙은 뺄셈이므로 **순서**가 매우 중요합니다.
> "분자 미분 곱하기 분모 **빼기** 분자 곱하기 분모 미분"입니다.

자, 오늘은 여기까지입니다. 다음 시간에는 이 일반 공식들의 증명과 함께 더 깊은 미분의 세계로 들어가 보겠습니다.

## Questions
- 

## Merge Candidates
- [[ ]] 

## Priori Lecture
- [[L - MIT_18.01_2]] 

