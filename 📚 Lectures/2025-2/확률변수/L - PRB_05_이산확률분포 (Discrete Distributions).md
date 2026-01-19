# L - PRB_05_이산확률분포 (Discrete Distributions)

> 2025-2학기 확률변수 강의노트
> Chapter 4 Part 3: 주요 이산 확률 분포

---

## 1. Poisson Distribution (푸아송 분포)

### 1.1 개념

**단위 시간/공간에서 드문 사건(rare events)의 발생 횟수 모델링**

- 웹사이트 서버 다운 횟수
- 유리판의 흠집 개수
- 은행에 도착하는 고객 수
- 말에 치어 죽는 군인의 수 (역사적 예시)

### 1.2 이항 분포와의 관계

**n이 매우 크고 p가 매우 작을 때**, 이항 분포 → 푸아송 분포로 근사

$$\lambda = np$$

### 1.3 확률 질량 함수 (PMF)

$$P\{X = i\} = e^{-\lambda} \cdot \frac{\lambda^i}{i!}, \quad i = 0, 1, 2, ...$$

### 1.4 통계량

| 통계량 | 값 |
|--------|-----|
| **Mean** | $E[X] = \lambda$ |
| **Variance** | $Var(X) = \lambda$ |
| **MGF** | $M(t) = \exp\{\lambda(e^t - 1)\}$ |

> 💡 **핵심 특징:** 평균과 분산이 모두 $\lambda$로 동일!

### 1.5 언제 사용?

- 시행 횟수를 알 수 없음
- 성공 확률 p가 매우 작음
- n이 매우 큼
- 단일 파라미터 $\lambda$로 충분

---

## 2. Geometric Distribution (기하 분포)

### 2.1 개념

**첫 번째 성공이 나타날 때까지 필요한 시도 횟수**

### 2.2 확률 질량 함수 (PMF)

$$P\{X = n\} = (1-p)^{n-1} \cdot p$$

(n-1번 실패 후 n번째에 성공)

### 2.3 통계량

| 통계량 | 값 |
|--------|-----|
| **Mean** | $E[X] = 1/p$ |

---

## 3. Negative Binomial Distribution (음이항 분포)

### 3.1 개념

**r번째 성공이 나타날 때까지 필요한 총 시행 횟수**

기하 분포의 일반화 (기하 분포는 r=1인 특별한 경우)

---

## 4. Hypergeometric Distribution (초기하 분포)

### 4.1 개념

**유한 모집단에서 비복원추출(without replacement)**

### 4.2 이항 분포와의 차이

| 분포 | 추출 방법 | 확률 변화 |
|------|-----------|----------|
| **이항 분포** | 복원추출 | 매번 동일 (p 일정) |
| **초기하 분포** | 비복원추출 | 매번 변화 (p 변동) |

### 4.3 설정

- N개의 아이템 중 m개가 관심 유형
- n개 비복원추출
- k개가 관심 유형일 확률

### 4.4 통계량

$$E[X] = \frac{nm}{N}$$

---

## 5. 분포 선택 가이드

| 분포 | 핵심 가정 | 대표 예시 |
|------|-----------|-----------|
| **이항 분포** | 고정 n, 독립 시행, 일정한 p | 동전 n번 던지기 |
| **푸아송 분포** | 드문 사건, n↑ p↓ | 시간당 고객 수 |
| **기하 분포** | 첫 성공까지 | 첫 앞면까지 횟수 |
| **음이항 분포** | r번째 성공까지 | r번 성공까지 횟수 |
| **초기하 분포** | 비복원추출 | 카드 5장 중 스페이드 수 |

---

## 6. 핵심 공식 정리

### Poisson Distribution

$$X \sim Poisson(\lambda)$$
- PMF: $p(x) = \frac{e^{-\lambda}\lambda^x}{x!}$
- Mean: $\lambda$
- Variance: $\lambda$

### Geometric Distribution

$$X \sim Geo(p)$$
- PMF: $p(n) = (1-p)^{n-1}p$
- Mean: $1/p$

### Hypergeometric Distribution

$$X \sim HyperGeo(N, m, n)$$
- Mean: $nm/N$

---

## 7. Poisson으로 Binomial 근사

### 조건
- n이 충분히 큼 (n ≥ 20)
- p가 충분히 작음 (p ≤ 0.05)
- np가 적당한 크기

### 방법
$$Bin(n, p) \approx Poisson(\lambda), \quad \lambda = np$$

### 예시
n = 100, p = 0.02인 이항 분포
→ λ = 100 × 0.02 = 2인 푸아송 분포로 근사

---

#lecture #probability #statistics #poisson #geometric #hypergeometric #discrete-distribution
