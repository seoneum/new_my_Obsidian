# 형식적 도출 (Formal Derivation)

## 개요
형식적 도출은 **추론 규칙**을 사용하여 전제로부터 결론을 이끌어내는 체계적인 증명 방법이다.

---

## 1. 귀결관계 (Consequence Relation)

### 의미론적 귀결 (⊨)
```
Γ ⊨ φ
= 모든 해석에서, Γ의 문장들이 모두 참이면 φ도 참
= φ는 Γ의 의미론적 귀결
```

### 통사론적 귀결 (⊢)
```
Γ ⊢ φ
= 추론 규칙만으로 Γ에서 φ를 도출 가능
= φ는 Γ의 통사론적 귀결
```

### 완전성과 건전성
```
건전성 (Soundness): Γ ⊢ φ → Γ ⊨ φ
완전성 (Completeness): Γ ⊨ φ → Γ ⊢ φ
```

---

## 2. 양화사 규칙 개요

| 규칙 | 이름 | 기능 |
|:---:|:---|:---|
| **US** | Universal Specification | ∀ 제거 |
| **UG** | Universal Generalization | ∀ 도입 |
| **ES** | Existential Specification | ∃ 제거 |
| **EG** | Existential Generalization | ∃ 도입 |
| **Q** | Quantifier Negation | 양화사 전환 |

---

## 3. US (Universal Specification) - 보편예화

### 규칙
```
∀xφ(x)
─────── US
φ(a)
```

> 모든 x에 대해 φ가 성립하면, 특정 대상 a에 대해서도 성립

### 예시
```
1. ∀x(Fx → Gx)    전제
2. Fa             전제
3. Fa → Ga        1, US (x에 a 대입)
4. Ga             2, 3, MP
```

### 제한 조건
- 대입하는 상항(a)은 논의영역의 원소여야 함
- 자유롭게 대입 가능 (가장 자유로운 규칙)

---

## 4. UG (Universal Generalization) - 보편일반화

### 규칙
```
φ(a)
─────── UG (제한 조건 충족 시)
∀xφ(x)
```

> 임의의 대상 a에 대해 φ가 성립하면, 모든 x에 대해 성립

### 제한 조건 (중요!)
1. **a는 임의 선택된 대상**이어야 함
2. a에 대한 **특별한 가정이 없어야** 함
3. a가 **전제에 등장하지 않아야** 함
4. a가 **ES로 도입되지 않았어야** 함

### 올바른 예시
```
1. ∀x(Fx → Gx)    전제
2. ∀xFx           전제
3. Fa → Ga        1, US
4. Fa             2, US
5. Ga             3, 4, MP
6. ∀xGx           5, UG ✓ (a는 임의)
```

### 잘못된 예시
```
1. Fa             전제 (a 특정!)
2. ∀xFx           1, UG ✗ (a는 임의가 아님)
```

---

## 5. EG (Existential Generalization) - 존재일반화

### 규칙
```
φ(a)
─────── EG
∃xφ(x)
```

> 특정 대상 a에 대해 φ가 성립하면, 그런 x가 존재

### 예시
```
1. Fa ∧ Ga        전제
2. Fa             1, Simp
3. ∃xFx           2, EG ✓
```

### 제한 조건
- 자유롭게 사용 가능 (제한 거의 없음)
- 하나의 상항만 변항으로 바꿔야 함

---

## 6. ES (Existential Specification) - 존재예화

### 규칙
```
∃xφ(x)
─────── ES (새로운 상항 a 도입)
φ(a)
```

> 어떤 x에 대해 φ가 성립하면, 그것을 a라 부르자

### 제한 조건 (가장 엄격!)
1. **a는 새로운 상항**이어야 함 (증명에 처음 등장)
2. a는 **전제에 없어야** 함
3. a는 **이전 줄에 없어야** 함
4. 결론에 a가 **남아있으면 안 됨** (나중에 제거 필요)

### 올바른 예시
```
1. ∃x(Fx ∧ Gx)    전제
2. Fa ∧ Ga        1, ES (a는 새로운 이름)
3. Fa             2, Simp
4. ∃xFx           3, EG ✓ (a 제거됨)
```

### 잘못된 예시
```
1. Fa             전제
2. ∃xGx           전제
3. Ga             2, ES ✗ (a가 이미 사용됨)
```

---

## 7. Q (Quantifier Negation) - 양화사 전환

### 규칙
```
¬∀xφ ↔ ∃x¬φ
¬∃xφ ↔ ∀x¬φ
```

### 적용 예시
```
1. ¬∀xFx          전제
2. ∃x¬Fx          1, Q
```

```
1. ¬∃x(Fx ∧ Gx)   전제
2. ∀x¬(Fx ∧ Gx)   1, Q
3. ∀x(¬Fx ∨ ¬Gx)  2, DeM
```

---

## 8. 증명 예제

### 예제 1: 기본 삼단논법
```
전제: ∀x(Fx → Gx), ∀xFx
결론: ∀xGx

증명:
1. ∀x(Fx → Gx)    전제
2. ∀xFx           전제
3. Fa → Ga        1, US
4. Fa             2, US
5. Ga             3, 4, MP
6. ∀xGx           5, UG
```

### 예제 2: 존재 도입
```
전제: ∀x(Fx → Gx), Fa
결론: ∃xGx

증명:
1. ∀x(Fx → Gx)    전제
2. Fa             전제
3. Fa → Ga        1, US
4. Ga             2, 3, MP
5. ∃xGx           4, EG
```

### 예제 3: 존재 제거
```
전제: ∃xFx, ∀x(Fx → Gx)
결론: ∃xGx

증명:
1. ∃xFx           전제
2. ∀x(Fx → Gx)    전제
3. Fa             1, ES (새 이름 a)
4. Fa → Ga        2, US
5. Ga             3, 4, MP
6. ∃xGx           5, EG
```

### 예제 4: 이중 부정 제거
```
전제: ¬∃x¬Fx
결론: ∀xFx

증명:
1. ¬∃x¬Fx         전제
2. ∀x¬¬Fx         1, Q
3. ¬¬Fa           2, US
4. Fa             3, DN
5. ∀xFx           4, UG
```

### 예제 5: 복합 양화사
```
전제: ∀x(Fx → ∀yGy)
결론: ∃xFx → ∀yGy

증명:
1. ∀x(Fx → ∀yGy)  전제
2. | ∃xFx         가정 (조건문 도입 위해)
3. | Fa           2, ES
4. | Fa → ∀yGy    1, US
5. | ∀yGy         3, 4, MP
6. ∃xFx → ∀yGy    2-5, CP
```

---

## 9. 규칙 적용 순서 전략

### 일반적 전략
1. **ES를 먼저**: 새 상항 도입은 빨리
2. **US로 맞춤**: ES로 도입한 상항에 맞춰 US
3. **명제 규칙**: MP, MT, HS 등 적용
4. **EG로 정리**: 특정 상항을 존재문으로
5. **UG는 마지막**: 제한 조건 확인 후

### 주의사항
```
✗ ES 전에 그 상항으로 US 사용
✗ 전제의 상항으로 ES
✗ ES 상항이 결론에 남음
✗ 특정 상항에서 UG
```

---

## 10. 자주 쓰는 명제논리 규칙 복습

| 규칙 | 이름 | 형태 |
|:---:|:---|:---|
| MP | Modus Ponens | p, p→q ⊢ q |
| MT | Modus Tollens | p→q, ¬q ⊢ ¬p |
| HS | Hypothetical Syllogism | p→q, q→r ⊢ p→r |
| DS | Disjunctive Syllogism | p∨q, ¬p ⊢ q |
| Simp | Simplification | p∧q ⊢ p |
| Conj | Conjunction | p, q ⊢ p∧q |
| Add | Addition | p ⊢ p∨q |
| CP | Conditional Proof | (가정 p에서 q 도출) ⊢ p→q |
| RAA | Reductio ad Absurdum | (가정 ¬p에서 모순) ⊢ p |

---

## 11. 동일성 규칙

### =I (Identity Introduction)
```
─────── =I
a = a
```

### =E (Identity Elimination)
```
a = b, φ(a)
─────────── =E
φ(b)
```

### 예시
```
전제: a = b, Fa
결론: Fb

1. a = b          전제
2. Fa             전제
3. Fb             1, 2, =E
```

---

## 핵심 정리

1. **US**: ∀x → 특정 a (자유롭게)
2. **UG**: 특정 a → ∀x (a가 임의일 때만)
3. **EG**: 특정 a → ∃x (자유롭게)
4. **ES**: ∃x → 특정 a (새 이름만, 결론에서 제거)
5. **Q**: ¬∀ ↔ ∃¬, ¬∃ ↔ ∀¬
6. **순서**: ES 먼저 → US 맞춤 → 명제규칙 → EG/UG
