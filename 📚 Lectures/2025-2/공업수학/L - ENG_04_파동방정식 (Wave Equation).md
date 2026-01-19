# 파동방정식 (Wave Equation)

## 1. 파동방정식

$$\frac{\partial^2 u}{\partial t^2} = c^2 \frac{\partial^2 u}{\partial x^2}$$

또는 $u_{tt} = c^2 u_{xx}$

여기서 $c$는 파동의 전파 속도

---

## 2. 변수 분리법 (Section 12.3)

### 문제 설정

**파동방정식**: $u_{tt} = c^2 u_{xx}$, $0 < x < L$, $t > 0$

**경계조건**: $u(0,t) = 0$, $u(L,t) = 0$ (양 끝 고정)

**초기조건**: 
- $u(x,0) = f(x)$ (초기 변위)
- $u_t(x,0) = g(x)$ (초기 속도)

### STEP 1: 변수 분리

$u(x,t) = X(x)T(t)$로 가정

대입하면:
$$X(x)T''(t) = c^2 X''(x)T(t)$$

양변을 $c^2 X(x)T(t)$로 나누면:
$$\frac{T''(t)}{c^2 T(t)} = \frac{X''(x)}{X(x)} = k \quad \text{(상수)}$$

### STEP 2: 두 개의 ODE

- 공간 부분: $X'' - kX = 0$
- 시간 부분: $T'' - c^2 k T = 0$

### STEP 3: 경계조건 적용

$u(0,t) = X(0)T(t) = 0$ → $X(0) = 0$
$u(L,t) = X(L)T(t) = 0$ → $X(L) = 0$

**k의 값 결정**:

| k 값 | 결과 |
|------|------|
| $k = 0$ | 자명한 해 (의미없음) |
| $k > 0$ | 자명한 해 (의미없음) |
| $k < 0$ | **의미있는 해!** |

$k = -p^2$로 두면:
$$X'' + p^2 X = 0 \quad \Rightarrow \quad X(x) = A\cos(px) + B\sin(px)$$

$X(0) = 0$ → $A = 0$
$X(L) = B\sin(pL) = 0$ → $pL = n\pi$ ($n = 1,2,3,...$)

### 고유값과 고유함수

**고유값**: $p_n = \frac{n\pi}{L}$, $\lambda_n = \frac{cn\pi}{L}$

**고유함수**: $X_n(x) = \sin\frac{n\pi x}{L}$

### STEP 4: 시간 부분 해결

$$T'' + \lambda_n^2 T = 0$$

$$T_n(t) = B_n \cos(\lambda_n t) + B_n^* \sin(\lambda_n t)$$

### STEP 5: 일반해 (중첩 원리)

$$u(x,t) = \sum_{n=1}^{\infty} \left(B_n \cos\frac{cn\pi t}{L} + B_n^* \sin\frac{cn\pi t}{L}\right) \sin\frac{n\pi x}{L}$$

### STEP 6: 초기조건으로 계수 결정

**초기 변위** $u(x,0) = f(x)$:
$$B_n = \frac{2}{L}\int_0^L f(x)\sin\frac{n\pi x}{L}dx$$

**초기 속도** $u_t(x,0) = g(x)$:
$$B_n^* = \frac{2}{cn\pi}\int_0^L g(x)\sin\frac{n\pi x}{L}dx$$

---

## 3. 달랑베르 해법 (Section 12.4)

### 핵심 아이디어

파동을 **진행파의 중첩**으로 해석

### 좌표변환

$v = x + ct$, $w = x - ct$

### 연쇄법칙 적용

$$u_x = u_v + u_w$$
$$u_t = c(u_v - u_w)$$
$$u_{xx} = u_{vv} + 2u_{vw} + u_{ww}$$
$$u_{tt} = c^2(u_{vv} - 2u_{vw} + u_{ww})$$

### 정규형으로 변환

파동방정식에 대입하면:
$$u_{tt} - c^2 u_{xx} = -4c^2 u_{vw} = 0$$

따라서:
$$u_{vw} = 0$$

### 적분

$v$로 적분: $u_w = h(w)$
$w$로 적분: $u = \phi(v) + \psi(w)$

### 일반해

$$u(x,t) = \phi(x+ct) + \psi(x-ct)$$

**물리적 의미**:
- $\phi(x+ct)$: 왼쪽으로 진행하는 파동 (후퇴파)
- $\psi(x-ct)$: 오른쪽으로 진행하는 파동 (진행파)

### 달랑베르 공식

초기조건 $u(x,0) = f(x)$, $u_t(x,0) = g(x)$ 적용:

$$\boxed{u(x,t) = \frac{1}{2}[f(x+ct) + f(x-ct)] + \frac{1}{2c}\int_{x-ct}^{x+ct} g(s)ds}$$

**특수 경우** (초기 속도 없음, $g(x) = 0$):
$$u(x,t) = \frac{1}{2}[f(x+ct) + f(x-ct)]$$

→ 초기 파형이 절반씩 양방향으로 전파

---

## 4. 두 해법의 연결

### 정상파 = 진행파의 중첩

삼각함수 곱셈 공식:
$$\sin A \cos B = \frac{1}{2}[\sin(A+B) + \sin(A-B)]$$

변수 분리법의 정상 모드:
$$u_n(x,t) = B_n \sin\frac{n\pi x}{L}\cos\frac{cn\pi t}{L}$$

를 변환하면:
$$u_n(x,t) = \frac{B_n}{2}\left[\sin\frac{n\pi(x+ct)}{L} + \sin\frac{n\pi(x-ct)}{L}\right]$$

**결론**: 정상파는 서로 반대 방향으로 진행하는 두 파동의 간섭!

---

## 5. PDE 형태 판별

### 판별식

$Au_{xx} + 2Bu_{xy} + Cu_{yy} = F$에서

$$\Delta = B^2 - AC$$

| 조건 | 유형 | 특성곡선 | 해법 |
|------|------|---------|------|
| $\Delta > 0$ | 쌍곡형 | 2개 실근 | 특성방정식 |
| $\Delta = 0$ | 포물형 | 1개 중근 | 변수분리 |
| $\Delta < 0$ | 타원형 | 복소근 | 변수분리 |

### 특성방정식

$$A\left(\frac{dy}{dx}\right)^2 - 2B\left(\frac{dy}{dx}\right) + C = 0$$

$$\frac{dy}{dx} = \frac{B \pm \sqrt{B^2-AC}}{A}$$

---

## 6. 공학적 의미

### 현악기의 원리

n번째 정상 모드의 주파수:
$$f_n = \frac{\lambda_n}{2\pi} = \frac{cn}{2L}$$

파동 속도 $c = \sqrt{T/\rho}$ ($T$: 장력, $\rho$: 선밀도)를 대입:
$$f_n = \frac{n}{2L}\sqrt{\frac{T}{\rho}}$$

**적용**:
- 장력 $T$ 증가 → 주파수 증가 (음이 높아짐)
- 길이 $L$ 감소 → 주파수 증가 (프렛을 누름)
- $n=1$: 기본음, $n=2,3,...$: 배음 (음색 결정)

---

## 핵심 체크리스트

- [ ] 경계조건 확인 (양 끝 고정?)
- [ ] 초기조건 확인 (변위? 속도?)
- [ ] 유한 영역 → 변수 분리법
- [ ] 무한 영역 → 달랑베르 해법
- [ ] 푸리에 계수 계산 정확히

---

## 관련 노트

- [[L - ENG_05_열전도방정식 (Heat Equation)]]
- [[L - ENG_03_편미분방정식 개요 (PDE Introduction)]]
- [[L - ENG_01_푸리에 급수 (Fourier Series)]]
