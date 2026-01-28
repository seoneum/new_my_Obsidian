---
type: concept
title: Bellman_Equation_proof
created: 2026-01-28
updated: 2026-01-28T21:07:29
author: "[[김선음]]"
domain: Math
level: adv
status: "[[🌿Sapling]]"
confidence: 0
tags:
  - concept
  - concept/math
  - level/adv
---
# Bellman_Equation_proof

> **한 줄 요약**: 

---

## 📖 정의

핵심은 **"무한한 미래의 합(Sum)"을 "현재와 바로 다음 순간의 관계(Recursion)"로 바꾸는 과정**입니다.

---

### 1. 벨만 방정식의 유도 (Bellman Equation)

가장 중요한 식인 $v(s) = R_s + \gamma \sum P_{ss'}v(s')$가 어떻게 튀어나왔는지 보겠습니다.

**1단계: 가치 함수(Value Function)의 정의에서 시작** 가치 함수 $v(s)$는 **"지금 상태 $s$에서 시작했을 때, 미래에 받을 보상 총합($G_t$)의 평균(기댓값)"**입니다.

$$v(s) = E[G_t | S_t = s]$$

**2단계: $G_t$ (반환값) 풀어헤치기**

$G_t$는 할인율 $\gamma$가 적용된 미래 보상들의 합입니다.

$$G_t = R_{t+1} + \gamma R_{t+2} + \gamma^2 R_{t+3} + \dots$$

**3단계: 공통인수 $\gamma$로 묶어내기 (핵심 트릭)**

첫 번째 보상 $R_{t+1}$만 남기고, 나머지 항들을 $\gamma$로 묶습니다.

$$G_t = R_{t+1} + \gamma (R_{t+2} + \gamma R_{t+3} + \dots)$$

괄호 안을 자세히 보세요. 시점만 $t$에서 $t+1$로 바뀌었을 뿐, 구조가 $G_{t+1}$과 똑같습니다.

$$G_t = R_{t+1} + \gamma G_{t+1}$$

**4단계: 기댓값의 선형성(Linearity of Expectation) 적용** 이제 3단계의 식을 1단계의 정의에 대입합니다.

$$v(s) = E[R_{t+1} + \gamma G_{t+1} | S_t = s]$$

기댓값 $E$는 덧셈에 대해 분리할 수 있습니다 ($E[A+B] = E[A] + E[B]$).

$$v(s) = E[R_{t+1} | S_t = s] + \gamma E[G_{t+1} | S_t = s]$$

- 앞부분 $E[R_{t+1} | S_t = s]$는 정의에 의해 **현재 상태의 즉각적 보상 $R_s$**가 됩니다.
    
- 뒷부분이 문제입니다. $E[G_{t+1} | S_t = s]$를 어떻게 처리할까요?
    

**5단계: 조건부 확률을 이용한 전개 (Law of Total Expectation)**

"현재 상태가 $s$일 때 다음 시점의 가치 $G_{t+1}$의 평균"을 구하려면, **갈 수 있는 모든 다음 상태 $s'$에 대한 경우의 수**를 따져야 합니다.

1. 상태 $s$에서 $s'$로 갈 확률은 $P_{ss'}$입니다.
    
2. 상태 $s'$에 도착했다면, 그곳의 가치는 $v(s')$입니다.
    

따라서 뒷항은 "확률 × 그 상태의 가치"의 합으로 바뀝니다.

$$E[G_{t+1} | S_t = s] = \sum_{s' \in S} P_{ss'} v(s')$$

**결론 (벨만 방정식 완성):**

$$v(s) = R_s + \gamma \sum_{s' \in S} P_{ss'} v(s')$$

---

### 2. 행렬식 유도와 역행렬 풀이 (Matrix Solution)

왜 복잡한 합(Summation) 기호를 $v = (I - \gamma P)^{-1} R$이라는 깔끔한 행렬식으로 바꿀 수 있을까요?

**1단계: 연립방정식으로 바라보기**

상태가 $n$개(1, 2, ..., $n$) 있다고 가정합니다. 벨만 방정식은 모든 상태에 대해 성립하므로, $n$개의 식을 쭉 나열할 수 있습니다.

- 상태 1: $v(1) = R_1 + \gamma (P_{11}v(1) + P_{12}v(2) + \dots + P_{1n}v(n))$
- 상태 2: $v(2) = R_2 + \gamma (P_{21}v(1) + P_{22}v(2) + \dots + P_{2n}v(n))$
- ...

**2단계: 행렬 곱셈의 정의 활용** 위 식들의 괄호 안 부분($P_{11}v(1) + \dots$)은 행렬 $P$의 행과 벡터 $v$의 내적(Dot Product)과 정확히 일치합니다. 이를 벡터 형태로 묶으면 다음과 같습니다.

$$\begin{bmatrix} v(1) \\ \vdots \\ v(n) \end{bmatrix} = \begin{bmatrix} R_1 \\ \vdots \\ R_n \end{bmatrix} + \gamma \begin{bmatrix} P_{11} & \dots & P_{1n} \\ \vdots & \ddots & \vdots \\ P_{n1} & \dots & P_{nn} \end{bmatrix} \begin{bmatrix} v(1) \\ \vdots \\ v(n) \end{bmatrix}$$

이걸 기호로 쓰면:

$$v = R + \gamma Pv$$

**3단계: 이항 및 단위행렬($I$)의 등장**

$v$를 구하기 위해 $\gamma Pv$를 좌변으로 넘깁니다.

$$v - \gamma Pv = R$$

여기서 수학적 함정이 있습니다. $v$는 벡터이고 $\gamma Pv$도 벡터입니다. 하지만 $v$를 그냥 묶어내면 $(1 - \gamma P)v$가 되는데, **숫자 1에서 행렬 $\gamma P$를 뺄 수는 없습니다.** 차원을 맞춰주기 위해 숫자 1 역할을 하는 **단위행렬 $I$**가 반드시 필요합니다.

$$(I - \gamma P)v = R$$

**4단계: 역행렬을 이용한 해**

양변의 왼쪽에 $(I - \gamma P)$의 역행렬을 곱합니다.

$$v = (I - \gamma P)^{-1} R$$

이것이 가능한 이유는 $\gamma < 1$이면 $(I - \gamma P)$는 항상 역행렬이 존재하기 때문입니다 (이것은 선형대수학의 Neumann Series 정리에 의해 보장됩니다).

---

### 3. MDP에서의 최적 가치 함수 (Optimal Value Function)

왜 MDP의 최적 가치 함수 $v^*(s)$는 행렬 역행렬로 한 번에 못 풀까요?

**이유: Max 연산자의 비선형성**

벨만 최적 방정식은 다음과 같습니다.

$$v^*(s) = \max_{a} [R_s^a + \gamma \sum_{s'} P_{ss'}^a v^*(s')]$$

여기서 $\max$ 함수가 들어갑니다.

선형대수학의 기본 전제는 $f(x+y) = f(x) + f(y)$ 같은 선형성(Linearity)인데, $\max$는 이를 만족하지 않습니다.

예: $\max(2, 3) = 3$이지만, $\max(1+1, 1+2) \neq \max(1, 1) + \max(1, 2)$

행렬식 $Ax = b$는 오직 선형 방정식일 때만 쓸 수 있습니다. **Max 연산이 들어가는 순간 식은 비선형(Non-linear)이 되고, 행렬 역행렬 공식이 붕괴됩니다.**

그래서 강의 자료에서도 "No closed form solution (일반적으로 닫힌 해가 없음)"이라 하고, 대신 반복적으로 값을 갱신하는 알고리즘(Value Iteration 등)을 써야 한다고 말하는 것입니다.

---

## 💡 직관적 이해

- 이건 마치 _______ 같다
- 왜냐하면 _______

---

## 📐 핵심

### 공식
$$

$$

### 증명 (간략)
1. 
2. 

### 언제 사용?
- 

---

## 📝 예시

### 예시 1
- 

### 예시 2
- 

---

## ⚠️ 흔한 실수
- ❌ 
- ✅ 

---

## 🔗 연결
- 선행: [[ ]]
- 후행: [[ ]]
- 관련: [[ ]]

---

## 📚 출처
- 강의: [[ ]]
- 교재: 

---

## 📝 FC
#flashcards/math

Bellman_Equation_proof 정의:: 

Bellman_Equation_proof 예시:: 

Bellman_Equation_proof 주의점::

