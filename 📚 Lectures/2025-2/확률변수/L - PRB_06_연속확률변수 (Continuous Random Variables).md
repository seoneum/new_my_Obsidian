# L - PRB_06_연속확률변수 (Continuous Random Variables)

> 2025-2학기 확률변수 강의노트
> Chapter 5: Continuous Random Variables

---

## 1. 이산 → 연속: 패러다임 전환

### 1.1 왜 새로운 개념이 필요한가?

**이산 확률 변수:** 셀 수 있는 값 (주사위 눈, 동전 앞면 횟수)
**연속 확률 변수:** 모든 실수 값 가능 (버스 대기 시간, 키)

| 질문 | 문제점 |
|------|--------|
| "버스를 정확히 5분 기다릴 확률?" | 가능한 값이 무한 → 확률 = 0 |
| "키가 정확히 175.0000cm일 확률?" | 연속적인 값 → PMF 불가 |

### 1.2 핵심 패러다임

> ⚠️ **"특정 한 점에서의 확률은 항상 0"**

$$P(X = c) = 0 \quad \text{(for any constant c)}$$

**따라서 연속 확률에서는 '점'이 아닌 '구간'의 확률을 다룸**

---

## 2. Probability Density Function (PDF)

### 2.1 정의

**확률 밀도 함수 f(x)**: 특정 구간 [a, b]에 대한 확률 = 곡선 아래 면적

$$P(a ≤ X ≤ b) = \int_a^b f(x) \, dx$$

### 2.2 PDF의 두 가지 핵심 속성

| 속성 | 공식 | 확률 공리 연결 |
|------|------|---------------|
| **Non-negative** | $f(x) ≥ 0$ (모든 x) | 공리 1: $P(A) ≥ 0$ |
| **Total = 1** | $\int_{-\infty}^{\infty} f(x) \, dx = 1$ | 공리 2: $P(S) = 1$ |

### 2.3 중요한 결과

등호 포함 여부가 확률에 영향 없음:

$$P(a ≤ X ≤ b) = P(a < X ≤ b) = P(a ≤ X < b) = P(a < X < b)$$

---

## 3. Cumulative Distribution Function (CDF)

### 3.1 정의

$$F(x) = P(X ≤ x) = \int_{-\infty}^{x} f(t) \, dt$$

### 3.2 PDF와 CDF의 관계

$$f(x) = \frac{d}{dx} F(x)$$

**적분 → CDF, 미분 → PDF**

---

## 4. 기댓값과 분산

### 4.1 기댓값 (Expected Value)

$$E[X] = \int_{-\infty}^{\infty} x \cdot f(x) \, dx$$

**이산 vs 연속:**
- 이산: $E[X] = \sum x \cdot p(x)$
- 연속: $E[X] = \int x \cdot f(x) \, dx$

> Σ → ∫, PMF → PDF

### 4.2 분산 (Variance)

$$Var(X) = E[X^2] - (E[X])^2$$

$$E[X^2] = \int_{-\infty}^{\infty} x^2 \cdot f(x) \, dx$$

---

## 5. Uniform Distribution (균등 분포)

### 5.1 정의

$$X \sim U(\alpha, \beta)$$

구간 $(\alpha, \beta)$ 내의 모든 값이 동일한 확률

### 5.2 확률 밀도 함수 (PDF)

$$f(x) = \begin{cases} \frac{1}{\beta - \alpha} & \alpha < x < \beta \\ 0 & \text{otherwise} \end{cases}$$

**그래프:** 밑변 $(\beta-\alpha)$, 높이 $\frac{1}{\beta-\alpha}$인 **직사각형**

### 5.3 누적 분포 함수 (CDF)

$$F(x) = \begin{cases} 0 & x ≤ \alpha \\ \frac{x - \alpha}{\beta - \alpha} & \alpha < x < \beta \\ 1 & x ≥ \beta \end{cases}$$

### 5.4 통계량

| 통계량 | 값 | 의미 |
|--------|-----|------|
| **Mean** | $\frac{\alpha + \beta}{2}$ | 구간의 중점 |
| **Variance** | $\frac{(\beta - \alpha)^2}{12}$ | 퍼짐 정도 |

### 5.5 구간 확률 계산

$$P(a < X < b) = \frac{b - a}{\beta - \alpha}$$

(길이의 비율!)

---

## 6. 예제

### 예제 1: PDF 상수 결정

$f(x) = C(4x - 2x^2)$, $0 < x < 2$일 때 C는?

**풀이:** $\int_0^2 C(4x - 2x^2) \, dx = 1$

$$C \left[ 2x^2 - \frac{2}{3}x^3 \right]_0^2 = 1$$
$$C \left[ 8 - \frac{16}{3} \right] = 1$$
$$C \cdot \frac{8}{3} = 1$$
$$C = \frac{3}{8}$$

### 예제 2: 기댓값 계산

$f(x) = 2x$, $0 ≤ x ≤ 1$일 때 $E[X]$는?

**풀이:**
$$E[X] = \int_0^1 x \cdot 2x \, dx = \int_0^1 2x^2 \, dx = \left[ \frac{2}{3}x^3 \right]_0^1 = \frac{2}{3}$$

### 예제 3: 분산 계산

같은 f(x)에서 $Var(X)$는?

**풀이:**
$$E[X^2] = \int_0^1 x^2 \cdot 2x \, dx = \int_0^1 2x^3 \, dx = \left[ \frac{1}{2}x^4 \right]_0^1 = \frac{1}{2}$$

$$Var(X) = E[X^2] - (E[X])^2 = \frac{1}{2} - \left(\frac{2}{3}\right)^2 = \frac{1}{2} - \frac{4}{9} = \frac{1}{18}$$

---

## 7. 핵심 공식 비교

| 개념 | 이산 | 연속 |
|------|------|------|
| **확률 함수** | PMF: $p(x)$ | PDF: $f(x)$ |
| **기댓값** | $\sum x \cdot p(x)$ | $\int x \cdot f(x) \, dx$ |
| **분산** | $E[X^2] - (E[X])^2$ | $E[X^2] - (E[X])^2$ |
| **CDF** | $F(x) = \sum_{t≤x} p(t)$ | $F(x) = \int_{-\infty}^x f(t) \, dt$ |
| **P(X=c)** | $p(c) > 0$ 가능 | $P(X=c) = 0$ 항상 |

---

## 8. 다음 강의 예고

- **정규분포 (Normal Distribution)**: 현실 세계 모델링의 핵심
- **지수분포 (Exponential Distribution)**: 사건 발생 대기 시간

---

#lecture #probability #statistics #continuous #pdf #cdf #uniform-distribution
