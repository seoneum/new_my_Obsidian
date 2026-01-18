---
type: lecture
title: L - MIT_18.01_11
created: 2026-01-06
updated: 2026-01-18T16:42:53
author:
  - "[[David Jerison]]"
group: General
status: [[🚜In Progress]]
tags:
  - lecture
  - lecture/General
  - tagging/needed
aliases: []
course: Single value calculurs
session: 2026-01-06/03/11
migrated_from: CMDS/200. CMDS/201. Connect/202. Math/Calculurs/L - MIT_18.01_11.md
domain:
  - cs
cmds: connect
---

# L - MIT_18.01_11

## Meta
- Course: Single value calculurs
- Session: 2026-01-06/03/11
- Instructor: 
- URL: 

## Outline
- 

## Raw Notes

topic: "Curve Sketching and Max/Min Strategy"
---

# MIT 18.01 단일 변수 미적분학: 11강 - 스케치 전략과 극값 찾기

## 1. 예제 2: 도함수가 0이 아닐 때의 대처법

지난 시간에 이어 두 번째 예제를 봅시다.
$$f(x) = \frac{x+1}{x+2}$$

도함수를 구해보면 다음과 같습니다.
$$f'(x) = \frac{1}{(x+2)^2}$$

> [!warning] 함정 (The Trap)
> $f'(x)$는 절대 0이 될 수 없습니다. 임계점(Critical Point)이 없다는 뜻이죠.
> 많은 학생들이 여기서 "할 게 없는데?"라며 얼어붙습니다.

### 1.1. 해결책: 미적분학 이전으로 돌아가라 (Precalculus)
임계점이 없다고 해서 그래프를 못 그리는 건 아닙니다. **정의되지 않는 점(Singularity)** 을 찾아야 합니다. 분모가 0이 되는 $x = -2$가 바로 그 지점입니다.

### 1.2. 불연속점 분석 (Vertical Asymptotes)
$x = -2$ 근처에서의 극한을 조사합니다.
* **우극한 ($x \to -2^+$)**: 분자는 $-1$, 분모는 $0^+$ $\implies -\infty$
* **좌극한 ($x \to -2^-$)**: 분자는 $-1$, 분모는 $0^-$ $\implies +\infty$

이 불연속점을 무시하는 것은 **"에베레스트 산이나 그랜드 캐니언을 지도에서 빼먹는 것"** 과 같습니다.

### 1.3. 끝점 분석 (Horizontal Asymptotes)
$x \to \pm\infty$일 때의 거동을 봅니다.
$$f(x) = \frac{1 + 1/x}{1 + 2/x} \to 1$$
따라서 $y=1$이 수평 점근선입니다.

### 1.4. 도함수의 활용
이제 도함수 $f'(x) = \frac{1}{(x+2)^2}$를 다시 봅시다. 항상 **양수**입니다.
* 함수는 항상 **증가(Increasing)** 합니다. (단, $x=-2$에서 끊김)
* **Backtracking 없음**: 도함수가 0이 아니므로, 그래프는 가던 방향을 되돌려 내려왔다 올라갈 수 없습니다.



---

## 2. 그래프 스케치를 위한 일반적인 전략 (General Strategy)

복잡한 함수를 그릴 때는 다음 5단계를 따르세요.

```mermaid
graph TD
    A[<b>스케치 일반 전략</b>] --> B[<b>1. Precalculus Analysis</b>]
    B --> B1(불연속점/수직점근선 찾기)
    B --> B2(끝점/수평점근선 x->∞ 찾기)
    B --> B3(절편 등 쉬운 점 찍기)
    
    A --> C[<b>2. 1st Derivative</b>]
    C --> C1(임계점 f'=0 찾기)
    
    A --> D[<b>3. Direction Check</b>]
    D --> D1(증가/감소 구간 확인)
    D --> D2(1, 2단계와 모순 없는지 Double Check)
    
    A --> E[<b>4. 2nd Derivative</b> <br><i>(Optional & Painful)</i>]
    E --> E1(변곡점 f''=0 찾기)
    E --> E2(오목/볼록 확인)
    
    A --> F[<b>5. Final Sketch</b>]

## Questions
- 

## Merge Candidates
- [[ ]] 

## Priori Lecture
- [[ ]] 

