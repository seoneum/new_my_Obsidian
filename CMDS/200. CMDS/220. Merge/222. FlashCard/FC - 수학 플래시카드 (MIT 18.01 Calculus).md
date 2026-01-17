---
type: flashcard
title: FC - 수학 플래시카드 (MIT 18.01 Calculus)
created: 2026-01-17
updated: 2026-01-17
group: Math
status: "[[🌿Sprout]]"
tags:
  - flashcards
  - math
  - calculus
  - MIT
---

# 수학 플래시카드 (MIT 18.01 Calculus)

#flashcards/math

## 1. 도함수의 기본 개념

도함수(Derivative)의 기하학적 정의는 무엇인가?
?
점 $x_0$에서 함수 $f(x)$의 도함수 $f'(x_0)$는 그 점에서 그래프에 접하는 **접선(Tangent line)의 기울기**이다.

도함수의 공식적 정의(극한 공식)를 쓰시오.
?
$$f'(x_0) = \lim_{\Delta x \to 0} \frac{f(x_0 + \Delta x) - f(x_0)}{\Delta x}$$ "차이 몫(Difference Quotient)의 극한"

접선(Tangent line)과 할선(Secant line)의 관계는?
?
접선 = 할선의 극한 $$\text{접선} = \lim_{Q \to P} (\text{할선 } PQ)$$

$f(x) = 1/x$의 도함수는?
?
$$f'(x) = -\frac{1}{x^2}$$

멱함수의 미분 공식(Power Rule)은?
?
$$\frac{d}{dx} x^n = n x^{n-1}$$

$\Delta x$(델타 x)와 $\Delta f$(델타 f)의 의미는?
?
$\Delta x$: $x$의 변화량 (수평 거리), $\Delta f$: 함수값의 변화량 (수직 거리). 할선의 기울기 = $\frac{\Delta f}{\Delta x}$

뉴턴 표기법 vs 라이프니츠 표기법?
?
뉴턴: $f'(x)$ 또는 $y'$ (간결), 라이프니츠: $\frac{df}{dx}$ 또는 $\frac{dy}{dx}$ (미소 변화량 명시)

## 2. 극한과 연속성

평균 변화율과 순간 변화율의 차이는?
?
평균: $\frac{\Delta y}{\Delta x}$ (구간 평균), 순간: $\frac{dy}{dx} = \lim_{\Delta x \to 0} \frac{\Delta y}{\Delta x}$ (극한)

좌극한과 우극한의 표기법은?
?
우극한: $\lim_{x \to x_0^+} f(x)$, 좌극한: $\lim_{x \to x_0^-} f(x)$. 극한 존재 조건: 좌극한 = 우극한

연속성(Continuity)의 정의는?
?
$$\lim_{x \to x_0} f(x) = f(x_0)$$ 조건: (1) 극한값 존재 (2) 함수값 존재 (3) 둘이 같음

불연속의 종류 4가지는?
?
1. 점프 불연속 (좌극한≠우극한) 2. 제거 가능 불연속 (극한≠함수값) 3. 무한 불연속 ($\pm\infty$) 4. 진동 (극한 없음, 예: $\sin(1/x)$)

"미분 가능하면 연속이다"의 증명 핵심은?
?
$\lim[f(x)-f(x_0)] = f'(x_0) \cdot 0 = 0$ 이므로 연속. **역은 성립 안 함** (뾰족한 점)

## 3. 미분 규칙

곱의 규칙(Product Rule)은?
?
$$(UV)' = U'V + UV'$$

몫의 규칙(Quotient Rule)은?
?
$$\left(\frac{U}{V}\right)' = \frac{U'V - UV'}{V^2}$$ **순서 주의**: 분자 미분이 먼저!

연쇄 규칙(Chain Rule)은?
?
$$\frac{dY}{dT} = \frac{dY}{dX} \cdot \frac{dX}{dT}$$ 합성 함수 미분 = 바깥 × 안쪽

$(\sin T)^{10}$을 미분하면?
?
$$10(\sin T)^9 \cos T$$ (바깥 미분 × 안쪽 미분)

$\sin(10T)$를 미분하면?
?
$$10\cos(10T)$$
<!--SR:!2026-01-22,4,270-->

## 4. 고계 미분

$\sin(x)$의 고계 미분 패턴은?
?
$\sin x \to \cos x \to -\sin x \to -\cos x \to \sin x$ (**4번 미분하면 원점 회귀**)

$x^n$의 $n$계 도함수 $D^n(x^n)$은?
?
$$D^n(x^n) = n!$$ (n 팩토리얼), $(n+1)$계 도함수는 **0**

## 5. 음함수 미분법

음함수 미분법(Implicit Differentiation)이란?
?
$y$를 $x$로 정리하지 않고 방정식을 그대로 $x$에 대해 미분. 예: $x^2+y^2=1$ → $2x+2yy'=0$ → $y'=-\frac{x}{y}$

$y = x^{m/n}$의 도함수 음함수 미분법 유도?
?
$y^n = x^m$ → $ny^{n-1}y' = mx^{m-1}$ → $y' = \frac{m}{n}x^{\frac{m}{n}-1}$ (Power Rule 유리수 확장)

$\tan^{-1}x$의 도함수는?
?
$$\frac{d}{dx}(\tan^{-1}x) = \frac{1}{1+x^2}$$

$\sin^{-1}x$의 도함수는?
?
$$\frac{d}{dx}(\sin^{-1}x) = \frac{1}{\sqrt{1-x^2}}$$

## 6. 지수 함수와 로그 함수

$e$의 정의는?
?
$x=0$에서 $e^x$의 접선 기울기가 **1**인 밑. $\frac{d}{dx}e^x = e^x$ (미분해도 자기 자신)

$e$의 극한 표현은?
?
$$e = \lim_{n \to \infty} \left(1 + \frac{1}{n}\right)^n$$

$a^x$의 도함수는?
?
$$\frac{d}{dx}a^x = (\ln a) \cdot a^x$$

$\ln x$의 도함수는?
?
$$\frac{d}{dx}\ln x = \frac{1}{x}$$

로그 미분법으로 $x^x$를 미분하면?
?
$\ln y = x\ln x$ → $\frac{y'}{y} = \ln x + 1$ → $y' = x^x(\ln x + 1)$

## 7. 최대/최소 문제

최대/최소 문제에서 반드시 확인할 것은?
?
**경계점(End Points)** 확인! 임계점만 보면 50% 확률로 반대 답을 얻음

최소값(Minimum Value) vs 최소점(Minimum Point)?
?
최소값: 출력값 $y$, 최소점(위치): 입력값 $x$, 최소점(좌표): $(x, y)$

뚜껑 없는 상자 최적 비율(표면적 최소, 부피 일정)?
?
$$x : y = 2 : 1$$ (밑면 너비 : 높이)

## 8. 관련 변화율

관련 변화율(Related Rates) 문제 풀이 절차?
?
1. 다이어그램 + 변수 설정 2. 기하학적 관계식 3. **시간 $t$에 대해 미분** 4. 값 대입 5. 계산

"미분 후 대입" 순서가 중요한 이유?
?
상수를 미분하면 0이 됨! 올바른 순서: 미분 → 대입 → 계산

원뿔형 물탱크에서 $\frac{dh}{dt}$와 $h$의 관계?
?
$$\frac{dh}{dt} \propto \frac{1}{h^2}$$ 물이 찰수록 수면 상승 속도 감소

현수교 문제에서 가장 낮은 지점의 특징?
?
$$\alpha = \beta$$ 양쪽 끈이 수직선과 이루는 각도가 같음 (힘 평형)

## 9. 뉴턴 방법

뉴턴 방법(Newton's Method) 공식?
?
$$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$$

뉴턴 방법의 이차적 수렴이란?
?
$$E_{n+1} \approx C \cdot (E_n)^2$$ 정확도가 매 단계 **두 배**로 증가!

뉴턴 방법 성공 조건 3가지?
?
1. $|f'(x)|$가 너무 작지 않음 2. $|f''(x)|$가 너무 크지 않음 3. 초기값이 근처에 있음

뉴턴 방법 실패 유형 3가지?
?
1. 잘못된 근으로 수렴 2. $f'(x_n) \approx 0$으로 발산 3. 무한 순환
