# 열전도방정식 (Heat Equation)

## 1. 열전도방정식

$$\frac{\partial u}{\partial t} = c^2 \frac{\partial^2 u}{\partial x^2}$$

또는 $u_t = c^2 u_{xx}$

여기서 $c^2 = \frac{K}{\rho\sigma}$ (열확산계수)

### 물리 상수

| 기호 | 의미 | 단위 |
|------|------|------|
| $\rho$ | 밀도 | g/cm³ |
| $K$ | 열전도도 | cal/(cm·sec·°C) |
| $\sigma$ | 비열 | cal/(g·°C) |
| $c^2$ | 열확산계수 | cm²/sec |

---

## 2. 물리적 유도

### 푸리에 열전도 법칙

열은 높은 온도에서 낮은 온도로 흐름:
$$\vec{q} = -K\nabla u$$

### 에너지 보존

1차원 막대에서:
1. 구간 $[x, x+\Delta x]$ 내 열량: $Q = \rho\sigma u \cdot A\Delta x$
2. 시간 $\Delta t$ 동안 열량 변화 = 유입 - 유출
3. 극한을 취하면: $\rho\sigma u_t = K u_{xx}$

---

## 3. 변수 분리법 (Section 12.6)

### 문제 설정

**열전도방정식**: $u_t = c^2 u_{xx}$, $0 < x < L$, $t > 0$

**경계조건**: $u(0,t) = 0$, $u(L,t) = 0$ (양 끝 0°C 유지)

**초기조건**: $u(x,0) = f(x)$ (초기 온도 분포)

### STEP 1: 변수 분리

$u(x,t) = X(x)T(t)$로 가정

대입하면:
$$XT' = c^2 X''T$$

양변을 $c^2 XT$로 나누면:
$$\frac{T'}{c^2 T} = \frac{X''}{X} = -\lambda \quad \text{(상수)}$$

> **왜 $-\lambda$?** 지수 감쇠 해를 얻기 위해. 열은 시간이 지나면 식어야 함!

### STEP 2: 두 개의 ODE

- 공간 부분: $X'' + \lambda X = 0$
- 시간 부분: $T' + \lambda c^2 T = 0$

### STEP 3: 경계조건 적용 (Sturm-Liouville 고유값 문제)

$$X'' + \lambda X = 0, \quad X(0) = 0, \quad X(L) = 0$$

$\lambda > 0$일 때 ($\lambda = k^2$):
$$X(x) = A\cos(kx) + B\sin(kx)$$

$X(0) = 0$ → $A = 0$
$X(L) = B\sin(kL) = 0$ → $kL = n\pi$

### 고유값과 고유함수

**고유값**: $\lambda_n = \left(\frac{n\pi}{L}\right)^2$, $n = 1,2,3,...$

**고유함수**: $X_n(x) = \sin\frac{n\pi x}{L}$

### STEP 4: 시간 부분 해결

$$T' + \lambda_n c^2 T = 0$$

$$T_n(t) = e^{-\lambda_n c^2 t} = e^{-\left(\frac{n\pi c}{L}\right)^2 t}$$

**물리적 의미**: 지수적 감쇠! 시간이 지나면 온도가 0으로 수렴

### STEP 5: 일반해 (중첩 원리)

$$\boxed{u(x,t) = \sum_{n=1}^{\infty} B_n \sin\frac{n\pi x}{L} \cdot e^{-\left(\frac{n\pi c}{L}\right)^2 t}}$$

### STEP 6: 초기조건으로 푸리에 계수 결정

$$u(x,0) = \sum_{n=1}^{\infty} B_n \sin\frac{n\pi x}{L} = f(x)$$

이것은 $f(x)$의 **푸리에 사인 급수**!

$$B_n = \frac{2}{L}\int_0^L f(x)\sin\frac{n\pi x}{L}dx$$

---

## 4. 장기 거동 분석

### 지수 감쇠의 특성

$$e^{-\left(\frac{n\pi c}{L}\right)^2 t}$$

- $n=1$ 항: 가장 천천히 감쇠 (최소 고유값)
- $n$이 클수록: 기하급수적으로 빠르게 감쇠

### 장기 거동 ($t \to \infty$)

$$u(x,t) \approx B_1 \sin\frac{\pi x}{L} \cdot e^{-\left(\frac{\pi c}{L}\right)^2 t} \to 0$$

### 감쇠 시간 상수

$$\tau_1 = \frac{L^2}{\pi^2 c^2}$$

→ 시스템이 평형에 도달하는 "특성 시간"

**물리적 직관**: 
- 급격한 온도 변화(고주파)는 빨리 사라짐
- 부드러운 분포(저주파)만 오래 남음

---

## 5. 예제 풀이

### 예제 1: 단일 모드

$f(x) = 100\sin\frac{\pi x}{L}$

**풀이**: 초기조건이 이미 고유함수 형태!

$$B_1 = 100, \quad B_n = 0 \text{ (}n \neq 1\text{)}$$

$$u(x,t) = 100\sin\frac{\pi x}{L} \cdot e^{-\left(\frac{\pi c}{L}\right)^2 t}$$

### 예제 2: 구간별 정의 함수

$$f(x) = \begin{cases} x & 0 \le x \le 50 \\ 100-x & 50 < x \le 100 \end{cases}$$

**풀이**: 푸리에 계수를 적분으로 계산

$$B_n = \frac{2}{100}\left[\int_0^{50} x\sin\frac{n\pi x}{100}dx + \int_{50}^{100}(100-x)\sin\frac{n\pi x}{100}dx\right]$$

대칭성 활용: 삼각파 → 홀수 $n$만 비영 계수

---

## 6. 비동차 방정식 (열원이 있는 경우)

### 형태

$$u_t = c^2 u_{xx} + Q(x,t)$$

### 해법: 중첩 원리

1. **동차해** $u_h$ 구하기 ($Q=0$인 방정식)
2. **특수해** $u_p$ 구하기
   - $Q$가 시간 무관하면: 정상 상태 해
   - $0 = c^2 u_{xx}'' + Q(x)$
3. **일반해**: $u = u_h + u_p$

### 예제: 일정한 열원

$u_t = c^2 u_{xx} + A$

**Hint**: $u = v + w$로 분해
- $w$: 정상상태 ($w_t = 0$)
- $v$: 시간 의존 (동차 열방정식)

---

## 7. 파동방정식과의 비교

| 특성 | 파동방정식 | 열전도방정식 |
|------|-----------|-------------|
| 형태 | $u_{tt} = c^2 u_{xx}$ | $u_t = c^2 u_{xx}$ |
| 시간 미분 차수 | 2차 | 1차 |
| 시간 부분 해 | $\cos, \sin$ (진동) | $e^{-\lambda t}$ (감쇠) |
| 물리적 의미 | 에너지 보존 | 에너지 소산 |
| 장기 거동 | 계속 진동 | 평형 상태로 수렴 |

---

## 8. 물리량 계산

### 열확산계수 계산 예

주어진 값:
- 밀도 $\rho = 10.6$ g/cm³
- 열전도도 $K = 1.04$ cal/(cm·sec·°C)
- 비열 $\sigma = 0.056$ cal/(g·°C)

계산:
$$c^2 = \frac{K}{\rho\sigma} = \frac{1.04}{10.6 \times 0.056} = \frac{1.04}{0.5936} \approx 1.75 \text{ cm}^2/\text{sec}$$

---

## 핵심 체크리스트

- [ ] 경계조건 확인 (양 끝 온도 0?)
- [ ] 초기조건 확인 (초기 온도 분포)
- [ ] 분리 상수를 $-\lambda$로 설정 (감쇠 조건)
- [ ] 푸리에 사인 계수 정확히 계산
- [ ] 지수 감쇠항 확인
- [ ] 장기 거동 ($t \to \infty$) 물리적 타당성 검증

---

## 관련 노트

- [[L - ENG_04_파동방정식 (Wave Equation)]]
- [[L - ENG_03_편미분방정식 개요 (PDE Introduction)]]
- [[L - ENG_01_푸리에 급수 (Fourier Series)]]
