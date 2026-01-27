---
tags:
  - lecture
  - lecture/General
  - tagging/needed
aliases: []
index:
  - "[[🏷 Lecture Notes]]"
type:
  - lecture
title: L - MIT_18.01_14
created: 2026-01-12
cover_url: {}
updated: 2026-01-18T16:42:53
my_rate: {}
authors: []
CMDS:
  - Connect
started: 2026-01-12
status:
  - "[[🌱Seed]]"
group:
  - General
publishDate: {}
start_read_date: {}
finish_read_date: {}
migrated_from: CMDS/200. CMDS/201. Connect/202. Math/Calculurs/L - MIT_18.01_14.md
domain:
  - math
cmds: connect
---
# L - MIT_18.01_14

## Meta
- Course: 
- Session: 2026-01-12/04/01
- Instructor: 
- URL: 

## Outline
- 

## Raw Notes
topic: 뉴턴 방법의 정확도와 평균값 정리 (Newton's Method Accuracy & MVT)
---

# 18.01 뉴턴 방법의 정확도와 평균값 정리

> [!abstract] 강의 개요
> 오늘은 지난 시간 배운 **뉴턴 방법(Newton's Method)**이 *왜* 그렇게 빠르게 수렴하는지 그 수학적 이유(오차 분석)를 파헤칩니다. 
> 그리고 미분학의 꽃이자 적분으로 넘어가는 다리 역할을 하는 **평균값 정리(Mean Value Theorem, MVT)**의 직관적 이해와 강력한 응용(부등식 증명)을 다룹니다.

---

## 1. 뉴턴 방법의 정확도 분석 (Accuracy of Newton's Method)

우리는 근($x$)을 찾기 위해 접선을 따라가는 과정을 반복합니다.
$$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$$

[Image of Newton's method tangent line iteration]

### 1.1 오차의 이차 관계 (Quadratic Convergence)
현재 추측값 $x_n$과 실제 근 $x$ 사이의 오차를 $E_n = |x - x_n|$이라고 합시다.
뉴턴 방법의 핵심은 **오차가 줄어드는 속도**에 있습니다.

> [!success] 핵심 정리: 이차적 수렴
> 다음 단계의 오차는 이전 단계 오차의 **제곱**에 비례합니다.
> $$E_{n+1} \approx C \cdot (E_n)^2$$
> (여기서 $C$는 $f''(x)$와 관련된 상수)

### 1.2 정확도의 두 배 증가 (Doubling Accuracy)
이것이 숫자로 무엇을 의미할까요? 지난 시간 $\sqrt{5}$ 예제를 봅시다. 초기 오차가 $10^{-1}$ (소수점 첫째 자리 정확)이라고 가정하면:

| 단계 (Step) | 오차 ($E_n$) | 정확한 소수 자릿수 | 비고 |
| :--- | :--- | :--- | :--- |
| $x_0$ | $10^{-1}$ | **1자리** | 시작 |
| $x_1$ | $(10^{-1})^2 = 10^{-2}$ | **2자리** | 정확도가 2배! |
| $x_2$ | $(10^{-2})^2 = 10^{-4}$ | **4자리** | 또 2배! |
| $x_3$ | $(10^{-4})^2 = 10^{-8}$ | **8자리** | 기하급수적! |
| $x_4$ | $(10^{-8})^2 = 10^{-16}$ | **16자리** | 계산기 한계 돌파 |

> "정확한 자릿수가 매 단계마다 **두 배(Double)** 로 뜁니다. 이것은 정말 경이로운(Spectacular) 속도입니다."

### 1.3 성공 조건과 실패 유형
물론, 이 마법 같은 방법도 조건이 필요합니다.

**성공 조건:**
1. $|f'(x)|$가 너무 작지 않아야 함 (접선이 너무 완만하면 안 됨).
2. $|f''(x)|$가 너무 크지 않아야 함 (곡선이 너무 심하게 굽이치면 안 됨).
3. **초기값 $x_0$가 근처에 있어야 함.**

**실패 유형 (Failure Modes):**

[Image of Newton's method failure cases cycle and zero derivative]

1. **잘못된 근:** 엉뚱한 근으로 수렴.
2. **발산/정의 불가:** $f'(x_n) \approx 0$인 경우 접선이 평행해져서 다음 값을 못 찾음.
3. **무한 순환 (Cycle):** $x_0 \to x_1 \to x_0$ 로 핑퐁 치며 제자리걸음.

---

## 2. 평균값 정리 (Mean Value Theorem, MVT)

이제 미적분학의 이론적 심장부인 MVT로 넘어갑니다.

### 2.1 직관적

## Questions
- 

## Merge Candidates
- [[ ]] 
