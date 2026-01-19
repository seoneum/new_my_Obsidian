---
created: 2026-01-20 03:20
modified: 2026-01-20 03:20
tags:
  - type/lecture
  - course/probability
  - semester/2025-2
aliases:
  - 확률변수 Chapter 1
  - Combinatorial Analysis
source: "EEC 3210: Combinatorial Analysis"
author: ""
---

# 📚 Chapter 1: Combinatorial Analysis (조합론)

## 🎯 강의 메타정보

- **교재**: Sheldon Ross (확률론 분야 가장 널리 사용되는 교재)
- **수업 언어**: 영어 (슬라이드, 시험 모두 영어)
- **평가 기준**: 중간 40% + 기말 50% + 출석 10%
- **시험 구성**: 수업 내용 40% + Exercise 문제 30% + 새로운 문제 30%

---

## 📖 1. The Basic Rule of Counting (기본 카운팅 원리)

### 핵심 개념
- **실험(Experiment)**: 관측 가능하고 정량화할 수 있는 사건
- **아웃컴(Outcome)**: 실험의 결과

### 공식
```
두 가지 아웃컴이 있을 때:
- Outcome 1의 가능성: n₁가지
- Outcome 2의 가능성: n₂가지
→ 총 가능성 = n₁ × n₂
```

### 일반화 공식
$$\text{총 가능성} = n_1 \times n_2 \times \cdots \times n_r = \prod_{i=1}^{r} n_i$$

### 예제
**자동차 번호판**: 알파벳 3자리 + 숫자 3자리
- **풀이**: $26 \times 26 \times 26 \times 10 \times 10 \times 10 = 17,576,000$가지

---

## 📖 2. Permutations (순열)

### 핵심 개념
- **순열(Permutation)**: 순서가 중요한 배열
- "The order matters!"

### 공식 1: n개 서로 다른 객체의 순열
$$n! = n \times (n-1) \times (n-2) \times \cdots \times 2 \times 1$$

### 공식 2: 중복된 객체가 있는 순열
$$\text{순열 개수} = \frac{n!}{n_1! \times n_2! \times \cdots \times n_r!}$$

**예제: "coffee"의 순열**
- 총 6개 문자: c(1), o(1), f(2), e(2)
- **정답**: $\frac{6!}{2! \times 2!} = 180$가지

### 공식 3: n개 중 r개 선택하는 순열
$$P(n,r) = \frac{n!}{(n-r)!}$$

---

## 📖 3. Combinations (조합)

### 핵심 개념
- **조합(Combination)**: 순서가 중요하지 않은 선택
- "Order doesn't matter!"

### 공식
$$C(n,r) = \binom{n}{r} = \frac{n!}{(n-r)! \times r!}$$

### 조합의 성질
1. $C(n,1) = n$
2. $C(n,n) = 1$
3. $C(n,r) = C(n, n-r)$ (대칭성)
4. $C(n,r) = C(n-1,r) + C(n-1,r-1)$ (파스칼의 삼각형)

### 예제: 포커 핸드
- 52장 카드 중 5장 선택
- $C(52,5) = 2,598,960$가지

---

## 📖 4. Binomial Theorem (이항정리)

### 공식
$$(a + b)^n = \sum_{k=0}^{n} \binom{n}{k} a^k b^{n-k}$$

### 응용: 부분집합 개수
- {1, 2, ..., n}의 부분집합 개수 = $2^n$

---

## 📖 5. Multinomial Coefficients (다항계수)

### 공식
$$\binom{n}{n_1, n_2, \ldots, n_r} = \frac{n!}{n_1! \times n_2! \times \cdots \times n_r!}$$

단, $n_1 + n_2 + \cdots + n_r = n$

### 예제: 경찰관 배치
- 10명을 순찰(5명), 서류작업(2명), 도넛가게(3명)로 배치
- **풀이**: $\frac{10!}{5! \times 2! \times 3!} = 2,520$가지

---

## 🧮 공식 총정리표

| 개념 | 공식 | 조건 |
|------|------|------|
| **기본 카운팅** | $n_1 \times n_2 \times \cdots \times n_r$ | r개 독립 선택 |
| **순열** | $n!$ | n개 전체 배열 |
| **중복 순열** | $\frac{n!}{n_1! \times n_2! \times \cdots \times n_r!}$ | 중복 객체 있을 때 |
| **부분 순열** | $\frac{n!}{(n-r)!}$ | n개 중 r개 선택 (순서 O) |
| **조합** | $\frac{n!}{(n-r)! \times r!}$ | n개 중 r개 선택 (순서 X) |
| **다항계수** | $\frac{n!}{n_1! \times n_2! \times \cdots \times n_r!}$ | n개를 r그룹으로 분할 |

---

## 🎓 문제풀이 전략

### 1. 순서 중요 여부 판단
- **순서 중요 (Permutation)**: "첫 번째, 두 번째..." 구분
- **순서 무관 (Combination)**: 악수, 팀 구성, 카드 선택

### 2. 중복 확인
- 같은 객체가 여러 개? → 해당 개수의 팩토리얼로 나누기

### 3. 제한 조건 처리
- **직접 계산**: 조건 만족하는 경우만 세기
- **차집합**: 전체 - 조건 위반 케이스

### 4. 단계별 분해
- 각각의 선택 단계를 나누어서 곱하기

---

## 💡 교수님 강조 포인트

1. **용어 이해**: 영어 용어 파악 필수 (Permutation, Combination)
2. **확률과의 연결**: 경우의 수로 확률을 정의하는 기초
3. **공식 암기보다 이해**: "왜 r!로 나누는가?" → 순서 제거
4. **중요도**: "확률론은 전기전자 전공의 가장 중요한 기초"
