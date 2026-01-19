---
created: 2026-01-20 03:20
modified: 2026-01-20 03:20
tags:
  - type/lecture
  - course/probability
  - semester/2025-2
aliases:
  - 확률변수 Chapter 3
  - Conditional Probability
  - Independence
source: "EEC 3210"
author: ""
---

# 📚 Chapter 3: Conditional Probability and Independence

## 🎯 Section 1: Conditional Probability (조건부 확률)

### 정의
$$P(A | B) = \frac{P(A \cap B)}{P(B)} \quad \text{(단, } P(B) > 0 \text{)}$$

**읽는 법**: "P(A given B)" - B가 주어졌을 때 A의 확률

### 직관적 이해
- B가 발생 = **B가 새로운 sample space**
- P(A|B) = "B 안에서 A가 차지하는 비율"

### 성질
- $P(A | A) = 1$
- $P(A^c | A) = 0$
- $P(A^c | B) = 1 - P(A | B)$

---

## 🎯 Section 2: Multiplication Rule (곱셈 법칙)

### 공식
$$P(A \cap B) = P(A | B) \times P(B)$$

### 용어
- **Marginal probability**: P(A), P(B)
- **Joint probability**: P(A ∩ B)
- **Conditional probability**: P(A | B)

---

## 🎯 Section 3: Chain Rule (연쇄 법칙)

$$P(A_1 \cap A_2 \cap \cdots \cap A_n) = P(A_1) \times P(A_2|A_1) \times P(A_3|A_1,A_2) \times \cdots$$

### 예제: 공 뽑기 (Without Replacement)
8개 흰 공, 4개 검은 공에서 3개를 replacement 없이 뽑을 때:

$$P(W_1 B_2 B_3) = \frac{8}{12} \times \frac{4}{11} \times \frac{3}{10}$$

---

## 🎲 Section 4: Law of Total Probability (전확률 법칙)

### Partition 정의
$\{A_1, A_2, \ldots, A_n\}$이 **partition** ⟺
1. **Disjoint**: $A_i \cap A_j = \emptyset$ (i ≠ j)
2. **Exhaustive**: $A_1 \cup A_2 \cup \cdots \cup A_n = S$

### 공식
$$P(B) = \sum_{i=1}^{n} P(B|A_i) \cdot P(A_i)$$

---

## 🔄 Section 5: Bayes Theorem (베이즈 정리)

### 공식
$$P(A_i | B) = \frac{P(B|A_i) \cdot P(A_i)}{\sum_{j=1}^{n} P(B|A_j) \cdot P(A_j)}$$

### 중요 용어
- **Prior Probability** P(Aᵢ): B 관찰 **전**의 확률
- **Posterior Probability** P(Aᵢ|B): B 관찰 **후**의 확률

> **베이즈 정리 = "관찰을 통해 믿음을 업데이트하는 과정"**

### 예제: 인하대 학생들의 데이트
- 전공 비율: 수학 25%, 음악 55%, 경제 20%
- 데이트 원하는 비율: 수학 90%, 음악 50%, 경제 10%
- 데이트한 사람이 수학 전공일 확률?

**결과**: 25% → **43%**로 업데이트!

---

## 🔀 Section 6: Independent Events (독립 사건)

### 정의
$$P(A \cap B) = P(A) \times P(B)$$

동등한 조건 (P(B) > 0일 때):
$$P(A|B) = P(A)$$

> **"B를 안다는 것이 A의 확률에 영향을 주지 않음!"**

### Independence의 성질
A와 B가 독립이면:
1. B와 A도 독립 (대칭성)
2. A와 Bᶜ도 독립
3. Aᶜ와 B도 독립
4. Aᶜ와 Bᶜ도 독립

---

## ⚠️ 중요: Independent ≠ Disjoint!

| 개념 | 의미 |
|------|------|
| **Disjoint** | $P(A \cap B) = 0$ |
| **Independent** | $P(A \cap B) = P(A) \times P(B)$ |

**대부분의 경우 정반대 개념!**

---

## 🔀 Section 7: Mutually Independent (상호 독립)

세 사건 A, B, C가 **mutually independent** ⟺

**조건 1 (Pairwise)**:
- $P(A \cap B) = P(A)P(B)$
- $P(B \cap C) = P(B)P(C)$
- $P(A \cap C) = P(A)P(C)$

**조건 2 (Triple)**:
- $P(A \cap B \cap C) = P(A)P(B)P(C)$

⚠️ **둘 다 만족해야 함!**

---

## 📊 문제 풀이 전략

| 상황 | 사용할 공식 |
|------|-------------|
| 조건부 확률 | $P(A|B) = \frac{P(A \cap B)}{P(B)}$ |
| 여러 단계 | Chain Rule |
| Partition 보임 | Law of Total Probability |
| 조건 역전 필요 | Bayes Theorem |
| 독립성 있음 | $P(A \cap B) = P(A) \times P(B)$ |

---

## ⚠️ 자주 하는 실수

1. **Disjoint와 Independent 혼동**
2. **P(A|B)와 P(B|A) 혼동** - 완전히 다름!
3. **Pairwise = Mutually라고 착각** - Triple도 확인 필요
4. **Partition 조건 확인 안 함**

---

## 🎓 교수님 핵심 포인트

1. **확률은 함수다!**
2. **B가 주어졌다 = Sample Space가 B로 바뀌었다!**
3. **문제를 수식으로 표현하는 연습**
4. **이벤트 설정이 핵심**
5. **Disjoint 확인은 필수**
