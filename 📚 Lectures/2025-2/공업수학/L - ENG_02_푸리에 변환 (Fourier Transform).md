# 푸리에 변환 (Fourier Transform)

## 개요

푸리에 적분과 변환은 **비주기 함수**를 다루기 위한 도구이다. 푸리에 급수의 주기 $L \to \infty$ 극한이라고 이해할 수 있다.

---

## 1. 푸리에 적분 (Section 11.7)

### 핵심 개념

주기 함수 $f_L(x)$에서 $L \to \infty$로 보내면:
- 푸리에 급수 → 푸리에 적분으로 변환
- 이산 주파수 → 연속 주파수

### 푸리에 적분 표현

$$f(x) = \int_0^{\infty} [A(w)\cos(wx) + B(w)\sin(wx)]dw$$

여기서:

$$A(w) = \frac{1}{\pi}\int_{-\infty}^{\infty} f(v)\cos(wv)dv$$

$$B(w) = \frac{1}{\pi}\int_{-\infty}^{\infty} f(v)\sin(wv)dv$$

### 적용 조건

**절대적분 가능**: $\int_{-\infty}^{\infty} |f(x)|dx < \infty$

### 풀이 흐름

1. **절대적분 가능성 확인**: $\int|f(x)|dx < \infty$
2. **구간 확인**: 보통 구간이 한정된 함수 (그 외 0)
3. **$A(w)$ 계산**: 코사인 적분 (짝함수면 이것만)
4. **$B(w)$ 계산**: 사인 적분 (홀함수면 이것만)
5. **적분 표현**: 결과 조립

### 예제

$f(x) = k$ ($-1 < x < 1$), 0 (그외)
- 짝함수 → 코사인 적분만 계산

---

## 2. 푸리에 코사인/사인 변환 (Section 11.8)

### 대칭성에 따른 변환

| 함수 유형 | 변환 종류 |
|-----------|-----------|
| 짝함수 | 코사인 변환 |
| 홀함수 | 사인 변환 |

### 코사인 변환

$$\mathcal{F}_c(w) = \int_0^{\infty} f(x)\cos(wx)dx$$

역변환:
$$f(x) = \frac{2}{\pi}\int_0^{\infty} \mathcal{F}_c(w)\cos(wx)dw$$

### 사인 변환

$$\mathcal{F}_s(w) = \int_0^{\infty} f(x)\sin(wx)dx$$

역변환:
$$f(x) = \frac{2}{\pi}\int_0^{\infty} \mathcal{F}_s(w)\sin(wx)dw$$

### 풀이 흐름

1. **함수 대칭성 판단**: 짝/홀 확인
2. **적분 구간**: $[0, \infty)$만 (양수 부분)
3. **적분 계산**: 코사인 또는 사인과 곱해서
4. **결과 정리**

---

## 3. 복소 푸리에 변환 (Section 11.9)

### 정의

$$F(w) = \mathcal{F}\{f(x)\} = \int_{-\infty}^{\infty} f(x)e^{-iwx}dx$$

### 역변환

$$f(x) = \mathcal{F}^{-1}\{F(w)\} = \frac{1}{2\pi}\int_{-\infty}^{\infty} F(w)e^{iwx}dw$$

### 풀이 흐름

1. **구간 확인**: 보통 유한 구간 (그 외 0)
2. **지수함수와 곱셈**: $e^{-iwx}$ 곱하기
3. **적분 실행**: 오일러 공식 활용
4. **복소수 결과 정리**

### 유용한 공식

$$\int e^{-iwx}dx = \frac{1}{-iw}e^{-iwx} = \frac{i}{w}e^{-iwx}$$

오일러 공식:
$$e^{i\theta} = \cos\theta + i\sin\theta$$

---

## 4. 주요 성질

### 선형성
$$\mathcal{F}\{af + bg\} = a\mathcal{F}\{f\} + b\mathcal{F}\{g\}$$

### 시간 이동
$$\mathcal{F}\{f(x-a)\} = e^{-iwa}F(w)$$

### 주파수 이동
$$\mathcal{F}\{e^{iax}f(x)\} = F(w-a)$$

### 미분 성질
$$\mathcal{F}\{f'(x)\} = iwF(w)$$

---

## 5. 푸리에 변환표

| $f(x)$ | $F(w)$ |
|--------|--------|
| $e^{-a\|x\|}$ $(a>0)$ | $\frac{2a}{a^2+w^2}$ |
| $e^{-ax^2}$ $(a>0)$ | $\sqrt{\frac{\pi}{a}}e^{-w^2/(4a)}$ |
| 사각파 $\Pi(x)$ | $\text{sinc}(w/2)$ |

---

## 핵심 체크리스트

- [ ] 절대적분 가능 조건 확인
- [ ] 짝함수/홀함수 판단
- [ ] 구간 명확히 설정
- [ ] 복소 지수 적분 정확히 계산

---

## 관련 노트

- [[L - ENG_01_푸리에 급수 (Fourier Series)]]
- [[L - ENG_03_편미분방정식 개요 (PDE Introduction)]]
