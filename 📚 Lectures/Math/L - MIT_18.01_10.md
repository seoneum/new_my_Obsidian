---
type: lecture
title: L - MIT_18.01_10
created: 2026-01-05
updated: 2026-01-18T16:42:53
author:
  - "[[David Jerison]]"
group: General
status: [[🚜In Progress]]
tags:
  - lecture
  - lecture/General
  - tagging/needed
aliases: []
course: Single value calculurs
session: 2026-01-05/03/10
migrated_from: CMDS/200. CMDS/201. Connect/202. Math/Calculurs/L - MIT_18.01_10.md
domain:
  - math
cmds: connect
---

# L - MIT_18.01_10

## Meta
- Course: Single value calculurs
- Session: 2026-01-05/03/10
- Instructor: 
- URL: 

## Outline
- 

## Raw Notes
---
tags:
  - math/calculus
  - MIT/18.01
  - lecture-note
date: 2025-12-30
course: "MIT 18.01: Single Variable Calculus"
instructor: "David Jerison"
topic: "Approximations and Curve Sketching"
---

# MIT 18.01 단일 변수 미적분학: 10강 - 근사의 통찰과 곡선 스케치

## 1. 근사의 통찰: 왜 선형 근사가 중요한가?

지난 시간에 다룬 **시간 지연(Time Dilation)** 공식을 다시 봅시다.
$$T' \approx T \left( 1 + \frac{1}{2} \frac{v^2}{c^2} \right)$$

이 식을 변화율의 관점에서 다시 쓰면 다음과 같습니다.
$$\frac{\Delta T}{T} \approx \frac{1}{2} \left( \frac{v}{c} \right)^2$$



### [Insight] 복잡한 세상을 단순화하는 힘
이 공식이 중요한 이유는 **비례성(Proportionality)** 때문입니다.
* 좌변: 시간 오차 비율 (무차원량)
* 우변: 속도 비율의 제곱 (무차원량)
* **$1/2$**: 이 둘을 연결하는 **비례 상수(Proportionality Factor)**

공학이나 과학에서 우리는 입력값의 작은 변화가 출력값에 어떤 영향을 미치는지 알고 싶어 합니다. 현실 세계(위성, 날씨, 경제 등)는 너무나 복잡해서 완벽한 공식을 세우기 어렵습니다. 그래서 우리는 **"입력이 $A$만큼 변하면 출력은 $kA$만큼 변한다"** 는 단순한 선형 규칙(Simple-minded Rules)을 찾아내는 데 집중합니다. 미분은 바로 그 **$k$(비례 상수)** 를 찾아주는 도구입니다.

> [!tip] 투구 속도 문제 (숙제 관련)
> 숙제에 나오는 투구 속도 문제도 마찬가지입니다. 마운드 높이의 변화($\Delta h$)가 속도 변화($\Delta v$)에 어떻게 비례하는지, 그 상수만 찾으면 됩니다. 기준점에 따라 상수가 조금 달라질 수 있지만, 이는 **2차적인 효과(Second Order Effect)**이므로 무시해도 좋습니다.

---

## 2. 2차 근사 (Quadratic Approximation)

선형 근사만으로는 부족할 때가 있습니다. (예: 경제학의 로그-2차 모델). 이때 우리는 **곡률(Curvature)** 까지 반영하는 2차 근사를 사용합니다.

### 기본 공식 (Base point $x=0$)
$$f(x) \approx \underbrace{f(0) + f'(0)x}_{\text{선형 근사}} + \underbrace{\frac{f''(0)}{2}x^2}_{\text{2차 보정항}}$$

### 왜 분모에 2가 붙는가? (Why the $1/2$?)
가장 단순한 2차 함수인 포물선 $f(x) = A + Bx + Cx^2$를 생각해 봅시다.
이 함수를 두 번 미분하면:
1. $f'(x) = B + 2Cx$
2. $f''(x) = 2C$

따라서 $x^2$의 계수 $C$를 구하려면 $f''(0)$을 **2로 나누어야** 합니다 ($C = f''(0)/2$).
이것이 공식에 $1/2$이 반드시 들어가야 하는 이유입니다. **"최적의 포물선(Best fit parabola)"** 을 찾기 위해서죠.



---

## 3. 주요 2차 근사 공식 목록 ($x \approx 0$)

이 목록은 암기해 두는 것이 좋습니다. 직접 미분해서 유도할 수도 있지만, 레고 블록처럼 활용하기 위해서입니다.

| 함수 $f(x)$ | 선형 근사 | **2차 근사** | 비고 |
| :--- | :--- | :--- | :--- |
| $\sin x$ | $x$ | **$x$** | $f''(0)=0$ (변곡점) |
| $\cos x$ | $1$ | **$1 - \frac{1}{2}x^2$** | 위로 볼록 |
| $e^x$ | $1+x$ | **$1 + x + \frac{1}{2}x^2$** | |
| $\ln(1+x)$ | $x$ | **$x - \frac{1}{2}x^2$** | |
| $(1+x)^r$ | $1+rx$ | **$1 + rx + \frac{r(r-1)}{2}x^2$** | 이항 정리의 확장 |

---

## 4. 2차 근사의 위력: 대수적 조합 (Algebraic Combination)

이차 근사의 진정한 힘은 **복잡한 함수를 직접 미분하지 않고** 기본 블록들을 조립해서 풀 때 나옵니다.

**예제: $f(x) = e^{-3x}(1+x)^{-1/2}$ 의 2차 근사** ($x \approx 0$)

이걸 몫의 법칙과 연쇄 법칙으로 두 번 미분하려면 끔찍합니다. 대신 기본 공식을 씁니다.

1.  **$e^{-3x}$ 근사**: ($x$ 자리에 $-3x$ 대입)
    $$e^{-3x} \approx 1 + (-3x) + \frac{1}{2}(-3x)^2 = 1 - 3x + \frac{9}{2}x^2$$

2.  **$(1+x)^{-1/2}$ 근사**: ($r = -1/2$ 대입)
    $$(1+x)^{-1/2} \approx 1 - \frac{1}{2}x + \frac{(-1/2)(-3/2)}{2}x^2 = 1 - \frac{1}{2}x + \frac{3}{8}x^2$$

3.  **두 식 곱하기 (Multiplication)**:
    $$(1 - 3x + \frac{9}{2}x^2) \left( 1 - \frac{1}{2}x + \frac{3}{8}x^2 \right)$$

4.  **중요한 요령**: 우리는 **$x^2$ 항까지만** 필요합니다. $x^3, x^4$ 등 고차항은 **과감히 버립니다 (Discard)**.
    * 상수항: $1 \cdot 1 = 1$
    * $x$ 항: $-\frac{1}{2}x - 3x = -\frac{7}{2}x$
    * $x^2$ 항: $\frac{3}{8}x^2 + (-3x)(-\frac{1}{2}x) + \frac{9}{2}x^2 = (\frac{3}{8} + \frac{12}{8} + \frac{36}{8})x^2 = \frac{51}{8}x^2$

**최종 결과**:
$$f(x) \approx 1 - \frac{7}{2}x + \frac{51}{8}x^2$$

> [!note] 왜 고차항을 버리나요?
> $x \approx 0.01$이라면, $x^3 \approx 0.000001$입니다. 근사의 정확도에 거의 영향을 주지 않으므로 무시하는 것이 공학적으로 타당합니다.

---

## 5. 곡선 스케치 (Curve Sketching) 시작

이제 미분의 또 다른 응용인 그래프 그리기로 넘어갑니다. 계산기 화면 밖의 세상을 보기 위함입니다.

**예시: $y = 3x - x^3$**

**1. 미적분학 이전의 정보 (Pre-calculus info)**
* **y절편**: $f(0) = 0$. 원점 통과.
* **끝 행동 (End behavior)**:
    * $x \to \infty \implies y \approx -x^3 \to -\infty$
    * $x \to -\infty \implies y \approx -x^3 \to \infty$
    (왼쪽 위에서 시작해 오른쪽 아래로 떨어지는 모양)

**2. 1계 도함수 ($f'$) - 증가/감소 및 임계점**
$$f'(x) = 3 - 3x^2 = 3(1-x)(1+x)$$
* **임계점 (Critical Points)**: $f'(x)=0$ 인 지점. $x = 1, -1$.
* **부호 변화**:
    * $x < -1$: $f' < 0$ (감소)
    * $-1 < x < 1$: $f' > 0$ (증가)
    * $x > 1$: $f' < 0$ (감소)

**3. 2계 도함수 ($f''$) - 볼록성 (Concavity)**
$$f''(x) = -6x$$
* $x < 0$: $f'' > 0$ (아래로 볼록, Concave Up)
* $x > 0$: $f'' < 0$ (위로 볼록, Concave Down)
* $x = 0$: 변곡점 (Inflection Point)



이 모든 정보를 종합하면 우리는 그래프의 개형을 완벽하게 그릴 수 있습니다.
다음 시간에는 더 복잡한 그래프를 그리는 방법을 배우겠습니다.

## Questions
- 

## Merge Candidates
- [[ ]] 

## Priori Lecture
- [[ ]] 

