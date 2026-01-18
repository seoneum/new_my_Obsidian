---
type: merge
title: M - MIT_18.01_PS1B
created: 2026-01-04
updated: 2026-01-18T16:42:53
author: [[김선음]]
group: Math
status: [[🌿Sapling]]
tags:
  - merge
  - feynman
  - tagging/needed
aliases: []
migrated_from: CMDS/200. CMDS/220. Merge/224. Problem/Math/P - MIT 18.01 PS1B.md
domain:
  - math
cmds: inbox
---

# M - MIT_18.01_PS1B

## 18.01 시험 1 대비 연습 문제


### Problem 1.

다음을 계산하고 가능한 경우 단순화하십시오. (b)번은 그 추론 과정을 명시하십시오. $a$와 $k$는 상수를 나타냅니다.

- **(a)** $\frac{d}{dt} \left( \frac{3t}{\ln t} \right) \Big|_{e^2}$
    
- **(b)** $\lim_{u \to 0} \frac{3u}{\tan 2u}$
    
- **(c)** $\frac{d^3}{dx^3} \sin kx$
    
- **(d)** $\frac{d}{d\theta} \sqrt[3]{a + k \sin^2 \theta}$
    

### Problem 2.

도함수의 정의로부터 직접 $x = x_0$ 지점에서의 $\frac{d}{dx} x^3$ 공식을 유도하십시오.

### Problem 3.

도함수와의 관계를 이용하여 다음 극한값을 구하십시오. (추론 과정을 명시하십시오.)

$$\lim_{h \to 0} \frac{1 - \sqrt[3]{1+h}}{h}$$

### Problem 4.

$-1 \le x \le 1$ 범위에서 곡선 $y = \sin^{-1} x$를 그리고, $\sin x$의 도함수를 이용하여 이 함수의 도함수 공식을 유도하십시오.

### Problem 5.

상수 $a, b$에 대하여 다음 함수가 주어질 때:

$$f(x) = \begin{cases} ax + b, & x > 0 \\ 1 - x + x^2, & x \le 0 \end{cases}$$

- **(a)** 함수가 연속이 되도록 하는 $a$와 $b$의 모든 값을 구하십시오.
    
- **(b)** 함수가 미분 가능하도록 하는 $a$와 $b$의 모든 값을 구하십시오.
    

### Problem 6.

방정식 $x^2y + y^3 + x^2 = 8$로 주어진 곡선에 대하여, 접선이 수평인 곡선 위의 모든 점을 찾으십시오.

### Problem 7.

점 $(x_0, y_0)$에서 $y = f(x)$의 그래프에 접하는 접선이 $x$축과 만나는 지점은 어디입니까?

### Problem 8.

구형 풍선의 부피가 반지름이 $20 \text{ cm}$인 순간에 $-10 \text{ cm}^3/\text{sec}$의 순시 변화율로 감소하고 있습니다. 그 순간에 반지름은 얼마나 빠르게 감소하고 있습니까?

### Problem 9.

다음 함수들은 어디에서 불연속입니까?

- **(a)** $\sec x$
	- **좌우 극한 비교:** $x = \frac{\pi}{2}$를 기준으로 보면,
		- **좌극한:** $x \to (\frac{\pi}{2})^-$일 때, cosx는 0보다 큰 쪽에서 0으로 가므로 secx→∞
		- **우극한:** $x \to (\frac{\pi}{2})^+$일 때, cosx는 0보다 작은 쪽에서 0으로 가므로 secx→−∞
- **(b)** $\frac{1 + x^2}{1 - x^2}$
    
- **(c)** $\frac{d}{dx} |x|$
    

### Problem 10.

방사성 물질은 $A = A_0 e^{-rt}$ 법칙에 따라 붕괴합니다. 여기서 $A(t)$는 시간 $t$에서의 현재 양이고, $r$은 양의 상수입니다.

- **(a)** 양이 초기 양 $A_0$의 $1/4$로 감소하는 데 걸리는 시간을 $r$에 관한 식으로 유도하십시오.
    
- **(b)** 양이 초기 양의 $1/4$로 감소한 순간, 그 양은 얼마나 빠르게 감소하고 있습니까? (단위: 그램, 초)

---

## 18.01 미적분학 연습 문제 (수정본)

### Problem 1. 다음을 계산하십시오.

- **a)** $\frac{d}{dx} \left( \frac{x}{1+2x} \right) \Big|_{x=1}$
    
- **b)** $\frac{d}{du} (u \ln 2u)$ (답을 가급적 단순화하십시오.)
    

### Problem 2.

- **a)** $\frac{d}{dt} \sqrt{1 - k \cos^2 t}$ 를 계산하십시오. (단, $k$는 상수입니다.)
    
- **b)** $k=1$일 때, 더 간단한 방법으로 계산한 미분 값과 (a)에서 구한 답이 일치하는지 확인하여 답을 검증하십시오.
    

### Problem 3.

도함수의 정의를 직접 사용하여 $\frac{d}{dx} \left( \frac{1}{x^2} \right)$ 공식을 유도하십시오.

(극한을 취하기 전에 차이 몫(difference quotient)을 대수적으로 변형해야 합니다.)

### Problem 4.

$y = \sin^{-1} x$를 $x$에 대해 정리하고 음함수의 미분법(implicit differentiation)을 사용하여 $\sin^{-1} x$의 도함수 공식을 유도하십시오.

(유도 과정에서 $\frac{d}{dx} \sin x$와 $\frac{d}{dx} \cos x$의 값은 그대로 사용해도 됩니다. 최종 답은 $x$에 관한 식으로 나타내어야 합니다.)

### Problem 5.

함수 $f(x)$가 다음과 같이 정의될 때, 이 함수가 미분 가능하도록 만드는 상수 $a$와 $b$의 모든 값을 구하십시오.

$$f(x) = \begin{cases} ax + b, & x > 1 \\ x^2 - 3x + 2, & x \le 1 \end{cases}$$

### Problem 6. 단순 추측이 아님을 보여줄 수 있는 충분한 근거와 함께 다음을 계산하십시오.

- **a)** $\lim_{u \to 0} \frac{\tan 2u}{u}$
    
- **b)** $\lim_{h \to 0} \frac{e^h - 1}{h}$ (이 식을 특정 도함수의 값과 연관 지어 설명하십시오.)
    

### Problem 7.

매 한 마리가 쥐를 쫓고 있습니다. 쥐는 $x$축을 따라 음의 방향으로 달리고 있고, 매는 $x$축 위를 비행하며 지수 곡선 $y = e^{kx}$ ($k$는 양의 상수)을 따라 하강하고 있습니다. 비행 중인 매의 시선은 항상 쥐를 향해 고정되어 있습니다. 현재 적도 근처이며 정오라 태양이 바로 머리 위에 있습니다.

매의 그림자가 지면의 $x_0$ 지점에 있을 때, 쥐는 어디에 있습니까?


## Feynman Step 1) Explain
- 

## Step 2) Gaps
- 

## Step 3) Repair
- Source: [[ ]] 

## Step 4) Teach-back
- 3문장:
- 1문장:

