# 푸리에 급수 (Fourier Series)

## 개요

푸리에 급수는 주기 함수를 삼각함수(sin, cos)의 무한 합으로 표현하는 방법이다. 이는 편미분방정식의 해를 구하는 데 필수적인 도구이다.

---

## 1. 주기 2π 푸리에 급수 (Section 11.1)

### 기본 공식

주기가 $2\pi$인 함수 $f(x)$의 푸리에 급수:

$$f(x) = a_0 + \sum_{n=1}^{\infty}(a_n\cos(nx) + b_n\sin(nx))$$

### 푸리에 계수

$$a_0 = \frac{1}{2\pi}\int_{-\pi}^{\pi} f(x)dx$$

$$a_n = \frac{1}{\pi}\int_{-\pi}^{\pi} f(x)\cos(nx)dx$$

$$b_n = \frac{1}{\pi}\int_{-\pi}^{\pi} f(x)\sin(nx)dx$$

### 풀이 흐름

1. **구간 확인**: $-\pi \le x \le \pi$ 인지 체크
2. **$a_0$ 계산**: 함수 전체를 적분 (평균값)
3. **$a_n$ 계산**: $f(x) \times \cos(nx)$ 적분
4. **$b_n$ 계산**: $f(x) \times \sin(nx)$ 적분
5. **급수 조립**: 계산한 계수들을 대입

### 대칭성 활용 (계산량 50% 감소!)

| 함수 유형 | 특징 | 결과 |
|-----------|------|------|
| **홀함수** | $f(-x) = -f(x)$ | $a_n = 0$ (코사인 항 소멸) |
| **짝함수** | $f(-x) = f(x)$ | $b_n = 0$ (사인 항 소멸) |

> **예시**: $f(x) = x$ on $(-\pi, \pi)$ → 홀함수 → $a_n = 0$, $b_n$만 계산

---

## 2. 임의 주기 2L 푸리에 급수 (Section 11.2)

### 기본 공식

주기가 $2L$인 함수의 푸리에 급수:

$$f(x) = a_0 + \sum_{n=1}^{\infty}\left(a_n\cos\frac{n\pi x}{L} + b_n\sin\frac{n\pi x}{L}\right)$$

### 푸리에 계수

$$a_0 = \frac{1}{2L}\int_{-L}^{L} f(x)dx$$

$$a_n = \frac{1}{L}\int_{-L}^{L} f(x)\cos\frac{n\pi x}{L}dx$$

$$b_n = \frac{1}{L}\int_{-L}^{L} f(x)\sin\frac{n\pi x}{L}dx$$

### 풀이 흐름

1. **주기 L 파악**: 구간 길이의 절반
2. **$\frac{n\pi x}{L}$로 스케일링**: $2\pi \to 2L$로 확장
3. **적분 구간**: $[-L, L]$로 변경
4. **계수 계산**: $\frac{1}{L}$로 정규화
5. **급수 조립**

---

## 3. 직교성 (Orthogonality)

푸리에 급수의 핵심 원리:

$$\int_0^L \sin\frac{m\pi x}{L}\sin\frac{n\pi x}{L}dx = \begin{cases} \frac{L}{2} & m=n \\ 0 & m \neq n \end{cases}$$

$$\int_0^L \cos\frac{m\pi x}{L}\cos\frac{n\pi x}{L}dx = \begin{cases} \frac{L}{2} & m=n \\ 0 & m \neq n \end{cases}$$

$$\int_0^L \sin\frac{m\pi x}{L}\cos\frac{n\pi x}{L}dx = 0 \quad \text{(항상)}$$

---

## 4. 수렴 정리

### 불연속점에서의 수렴

**Dirichlet 조건**을 만족하면:
- 연속인 점: 함수값으로 수렴
- 불연속점: **좌극한과 우극한의 평균**으로 수렴

$$\frac{f(x^-) + f(x^+)}{2}$$

> 교수님 강조: "불연속점에서 좌극한+우극한의 평균으로 수렴"

---

## 5. 푸리에 사인/코사인 급수

### 반구간 전개

구간 $[0, L]$에서 정의된 함수를 전개할 때:

**푸리에 사인 급수** (홀함수 확장):
$$f(x) = \sum_{n=1}^{\infty} B_n \sin\frac{n\pi x}{L}$$
$$B_n = \frac{2}{L}\int_0^L f(x)\sin\frac{n\pi x}{L}dx$$

**푸리에 코사인 급수** (짝함수 확장):
$$f(x) = a_0 + \sum_{n=1}^{\infty} A_n \cos\frac{n\pi x}{L}$$
$$A_n = \frac{2}{L}\int_0^L f(x)\cos\frac{n\pi x}{L}dx$$

---

## 핵심 체크리스트

- [ ] 주기 확인 ($2\pi$ vs $2L$)
- [ ] 대칭성 판단 (홀함수/짝함수)
- [ ] 적분 구간 정확히 설정
- [ ] 정규화 계수 확인 ($\frac{1}{\pi}$ vs $\frac{1}{L}$)
- [ ] 불연속점 처리

---

## 관련 노트

- [[L - ENG_02_푸리에 변환 (Fourier Transform)]]
- [[L - ENG_03_편미분방정식 개요 (PDE Introduction)]]
