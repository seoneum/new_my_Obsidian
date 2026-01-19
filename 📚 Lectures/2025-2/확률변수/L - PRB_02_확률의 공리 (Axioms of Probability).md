---
created: 2026-01-20 03:20
modified: 2026-01-20 03:20
tags:
  - type/lecture
  - course/probability
  - semester/2025-2
aliases:
  - 확률변수 Chapter 2
  - Axioms of Probability
source: "EEC 3210"
author: ""
---

# 📚 Chapter 2: Axioms of Probability (확률의 공리)

## 🔍 Section 1: Sample Space (표본공간)

### 정의
> **Sample Space S**: 어떤 실험에서 발생할 수 있는 모든 가능한 결과들의 집합

### 예시
1. **동전 던지기 3번** (Discrete & Finite)
   - $S = \{HHH, HHT, HTH, HTT, THH, THT, TTH, TTT\}$
   - 총 $2^3 = 8$개

2. **주사위 한 번 던지기**
   - $S = \{1, 2, 3, 4, 5, 6\}$

3. **버스 기다리는 시간** (Continuous)
   - $S = [0, \infty)$

---

## 🔍 Section 2: Events (사건)

### 정의
> **Event E**: Sample space의 부분집합 ($E \subseteq S$)

### 특수한 Event
- **Empty Set (∅)**: Impossible event
- **Sample Space 자체 (S)**: Certain event

---

## 🔍 Section 3: Set Operations (집합 연산)

### Intersection (교집합) - AND
$$A \cap B = \text{"A와 B가 동시에 발생"}$$

### Union (합집합) - OR
$$A \cup B = \text{"A 또는 B 중 적어도 하나 발생"}$$

### Complement (여집합) - NOT
$$A^c = S \setminus A = \text{"A가 발생하지 않음"}$$

### Mutually Exclusive (상호배타적)
$$A \cap B = \emptyset$$

---

## 🔍 Section 4: 집합 법칙

### DeMorgan's Laws ⭐ 매우 중요!
$$(A \cup B)^c = A^c \cap B^c$$
$$(A \cap B)^c = A^c \cup B^c$$

**일반화**:
$$\left(\bigcup_{i=1}^{n} A_i\right)^c = \bigcap_{i=1}^{n} A_i^c$$

---

## 🔍 Section 5: Kolmogorov의 Axioms ⭐⭐⭐

> **"이거는 평생 외워야 합니다!"** - 교수님

**확률 P는 함수**: Event → [0, 1]

### Axiom 1: Non-negative (비음수)
$$0 \leq P(E) \leq 1$$

### Axiom 2: Total one (전체는 1)
$$P(S) = 1$$

### Axiom 3: Countable Addition (가산 가법성)
$$P\left(\bigcup_{i=1}^{\infty} E_i\right) = \sum_{i=1}^{\infty} P(E_i) \quad \text{if } E_i \cap E_j = \emptyset \text{ for } i \neq j$$

---

## 🔍 Section 6: 확률의 해석

### Frequentist Interpretation (빈도주의)
$$P(A) = \lim_{n \to \infty} \frac{\text{# times A happens}}{n}$$

### Bayesian Interpretation (베이지안)
- 확률 = 주관적인 믿음의 정도
- Prior 정보 활용, 새로운 데이터로 업데이트

---

## 🔍 Section 7: 주요 명제들

### Complement Rule
$$P(A^c) = 1 - P(A)$$
$$P(\emptyset) = 0$$

### Inclusion-Exclusion Principle ⭐
**2개 이벤트**:
$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$

**3개 이벤트**:
$$P(A \cup B \cup C) = P(A) + P(B) + P(C) - P(A \cap B) - P(A \cap C) - P(B \cap C) + P(A \cap B \cap C)$$

---

## 🔍 Section 8: Equally Likely Outcomes

모든 결과가 동일한 확률을 가질 때:
$$P(E) = \frac{\#(E)}{\#(S)}$$

### Birthday Problem ⭐
- 30명 중 생일이 같은 쌍이 있을 확률: **약 70.6%**
- **풀이**: 여사건 이용
  $$P(\text{at least a tie}) = 1 - P(\text{no match})$$

---

## 📊 문제 풀이 전략

1. **샘플 스페이스 먼저 정의**
2. **이벤트를 명확히 표현**
3. **중복 항상 체크** (Watch out for duplicates!)
4. **"적어도"는 여사건 이용**
5. **Venn Diagram 활용**

---

## 💡 핵심 키워드

| 연산 | 키워드 |
|------|--------|
| Intersection | **AND** |
| Union | **OR** |
| Complement | **NOT** |
| Disjoint | 중요한 조건! |
