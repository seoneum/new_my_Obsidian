# L - PRB_04_확률변수 (Random Variables)

> 2025-2학기 확률변수 강의노트
> Chapter 4: Random Variables

---

## 1. Random Variable 정의

### 1.1 개념

**Random Variable X**는 **sample space S에서 실수(Real number)로 가는 함수**

$$X : S → ℝ$$

- "Random variable is a number associated with a random experiment"
- 확률 실험의 결과를 숫자로 변환하여 확률 계산 가능

### 1.2 표기법

| 표기 | 의미 |
|------|------|
| **Capital X** | Random variable 자체 (함수) |
| **Lowercase x** | Random variable이 가질 수 있는 실제 값 |

**예시:** P(X = 3)에서 X는 random variable, 3은 값

### 1.3 주사위 예제

두 개의 주사위를 던지는 실험에서 다양한 Random Variable 정의:

1. **X(a) = a₁** (첫 번째 주사위 값)
2. **Y(a) = |a₁ - a₂|** (두 주사위 차이의 절댓값)
3. **Z(a) = a₁ + a₂** (두 주사위 합)

---

## 2. Probability Mass Function (PMF)

### 2.1 Discrete Random Variable

**셀 수 있는(countable) 값만 가지는 확률 변수**

- Finite (유한개): 주사위 (1,2,3,4,5,6)
- Countably infinite (가산무한): 자연수 전체

### 2.2 PMF 정의

$$p(x) = P(X = x)$$

**PMF의 조건 (Well-defined):**
1. $p(x_i) > 0$ for i = 1, 2, ... (non-negative)
2. $p(x) = 0$ for all other values
3. $\sum_{i=1}^{\infty} p(x_i) = 1$ (모든 확률의 합 = 1)

---

## 3. Cumulative Distribution Function (CDF)

### 3.1 정의

$$F(x) = P(X ≤ x), \quad \text{for all } x ∈ ℝ$$

### 3.2 중요한 성질들

| Property | 설명 |
|----------|------|
| **Interval Probability** | $P(a < X ≤ b) = F(b) - F(a)$ |
| **Non-decreasing** | $x_1 < x_2$이면 $F(x_1) ≤ F(x_2)$ |
| **Limits** | $\lim_{x→∞} F(x) = 1$, $\lim_{x→-∞} F(x) = 0$ |
| **Right Continuous** | 오른쪽에서 연속 |

### 3.3 CDF에서 PMF 구하기

$$p(k) = P(X = k) = F(k) - F(k^-)$$

여기서 $F(k^-) = \lim_{x→k^-} F(x) = P(X < k)$

---

## 4. Expectation (기댓값)

### 4.1 정의

$$E[X] = \sum_{x:p(x)>0} x \cdot p(x)$$

- **Weighted average**: 각 값에 확률을 가중치로 곱한 합

### 4.2 Indicator Variable

$$X = \begin{cases} 1 & \text{if event A occurs} \\ 0 & \text{otherwise} \end{cases}$$

**놀라운 결과:** $E[X] = P(A)$

### 4.3 Function of Random Variable

$$E[g(X)] = \sum_{x:p_X(x)>0} g(x) \cdot p_X(x)$$

### 4.4 Linear Property (선형성)

$$E[aX + b] = aE[X] + b$$

- $E[aX] = aE[X]$
- $E[b] = b$

---

## 5. Variance (분산)

### 5.1 정의

$$\sigma^2 = Var(X) = E[(X - E[X])^2] = E[(X - \mu)^2]$$

**의미:** 확률 변수가 평균에서 얼마나 떨어져 있는지 (퍼짐의 척도)

### 5.2 계산 공식 (Computational Formula)

$$Var(X) = E[X^2] - (E[X])^2$$

> ⚠️ 이 공식이 계산하기 훨씬 쉬움!

### 5.3 Standard Deviation (표준편차)

$$\sigma = SD(X) = \sqrt{Var(X)}$$

### 5.4 분산의 성질

| Property | 공식 |
|----------|------|
| **Non-negative** | $Var(X) ≥ 0$ |
| **Constant** | $Var(X) = 0 ⟺ X$ is a constant |
| **Linear Transformation** | $Var(aX + b) = a^2 Var(X)$ |
| **Constant Addition** | $Var(X + b) = Var(X)$ |

---

## 6. Bernoulli Distribution

### 6.1 정의

$$X \sim Ber(p) \iff P(X = 1) = p, \quad P(X = 0) = 1 - p$$

**단일 시행에서 성공(1) 또는 실패(0)**

### 6.2 통계량

| 통계량 | 값 |
|--------|-----|
| **Mean** | $\mu = p$ |
| **Variance** | $\sigma^2 = p(1-p)$ |

> 💡 Indicator variable의 기댓값 = 사건의 확률!

---

## 7. Binomial Distribution

### 7.1 정의

$$X \sim Bin(n, p) \iff p(k) = \binom{n}{k} p^k (1-p)^{n-k}, \quad k = 0, 1, ..., n$$

### 7.2 사용 조건 (4가지 필수)

1. **Independent trials** - 각 시행이 독립
2. **Fixed n** - 시행 횟수가 고정
3. **Success/Failure** - 결과가 두 가지만
4. **Same p** - 매 시행 성공 확률 동일

### 7.3 통계량

| 통계량 | 값 |
|--------|-----|
| **Mean** | $\mu = np$ |
| **Variance** | $\sigma^2 = np(1-p)$ |

### 7.4 Bernoulli와의 관계

$$X = X_1 + X_2 + ... + X_n \sim Bin(n, p)$$

여기서 각 $X_i \sim Ber(p)$이고 독립

### 7.5 Variance 최대화

$Var(X) = np(1-p)$가 **p = 1/2**일 때 최대!
- 가장 불확실한 상황 (50-50)에서 분산 최대

---

## 8. 핵심 요약

| 분포 | PMF | Mean | Variance |
|------|-----|------|----------|
| **Bernoulli** | $p(1)=p, p(0)=1-p$ | $p$ | $p(1-p)$ |
| **Binomial** | $\binom{n}{k}p^k(1-p)^{n-k}$ | $np$ | $np(1-p)$ |

**기댓값 공식:**
- 정의: $E[X] = \sum x \cdot p(x)$
- 함수: $E[g(X)] = \sum g(x) \cdot p(x)$
- 선형: $E[aX+b] = aE[X] + b$

**분산 공식:**
- 정의: $Var(X) = E[(X-\mu)^2]$
- 계산: $Var(X) = E[X^2] - (E[X])^2$
- 선형: $Var(aX+b) = a^2 Var(X)$

---

#lecture #probability #statistics #random-variable #expectation #variance #binomial
