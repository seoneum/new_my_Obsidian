# 트리 (Tree)

## 1. 트리 기본 용어

### 계층 구조 (Hierarchy)
```
        A (root)
       / \
      B   C
     /|   |\
    D E   F G (leaves)
```

| 용어 | 설명 |
|------|------|
| **Root** | 부모가 없는 노드 (트리의 시작점) |
| **Leaf / External** | 자식이 없는 말단 노드 |
| **Internal** | 자식이 하나 이상인 노드 |
| **Sibling** | 같은 부모를 가진 노드들 |
| **Depth** | 루트 → 해당 노드까지의 거리 (루트 = 0) |
| **Height** | 가장 깊은 리프까지의 거리 |
| **Degree** | 노드가 가진 자식의 개수 |

---

## 2. 이진 트리 (Binary Tree)

### 정의
- 각 노드가 최대 2개의 자식 (left, right)을 가짐
- Degree = 2인 트리

### 구현 방법

#### 포인터 방식
```cpp
class Node {
public:
    Elem element;
    Node* parent;
    Node* left;
    Node* right;
};
```

#### 배열 방식 (완전 이진 트리)
```cpp
// 루트: index 1
// i번 노드의 왼쪽 자식: 2*i
// i번 노드의 오른쪽 자식: 2*i + 1
// i번 노드의 부모: i/2
```

### 특별한 형태

| 형태 | 설명 |
|------|------|
| **Full Binary Tree** | 모든 노드가 0개 또는 2개의 자식 |
| **Complete Binary Tree** | 위에서 아래로, 왼쪽에서 오른쪽으로 빈틈없이 채워짐 |

---

## 3. 트리 순회 (Traversal) ⭐⭐⭐

### Preorder (전위)
**Root → Left → Right**
```cpp
void preorder(Node* v) {
    if (v == nullptr) return;
    visit(v);           // 먼저 방문
    preorder(v->left);
    preorder(v->right);
}
```
- 복사할 때 유용

### Inorder (중위) ⭐
**Left → Root → Right**
```cpp
void inorder(Node* v) {
    if (v == nullptr) return;
    inorder(v->left);
    visit(v);           // 중간에 방문
    inorder(v->right);
}
```
- **BST에서 정렬된 순서로 출력!**

### Postorder (후위)
**Left → Right → Root**
```cpp
void postorder(Node* v) {
    if (v == nullptr) return;
    postorder(v->left);
    postorder(v->right);
    visit(v);           // 마지막에 방문
}
```
- 폴더 용량 계산, 삭제 시 유용

---

## 4. 이진 탐색 트리 (BST) ⭐⭐⭐

### 불변식 (Invariant)
**왼쪽 서브트리 < 현재 노드 < 오른쪽 서브트리**

```
        50
       /  \
      30   70
     / \   / \
    20 40 60 80
```

### 탐색 (Search) - O(h)
```cpp
Position treeSearch(const K& k, Position v) {
    if (v.isExternal()) return v;      // 못 찾음
    if (k < (*v).key())
        return treeSearch(k, v.left());
    else if (k > (*v).key())
        return treeSearch(k, v.right());
    else
        return v;                       // 찾음!
}
```

### 삽입 (Insert) - O(h)
1. 탐색으로 삽입할 위치 찾기 (외부 노드)
2. 해당 위치에 새 노드 생성

```cpp
void insert(const K& k, const V& x) {
    Position v = treeSearch(k, root());
    if (!v.isExternal()) {
        (*v).setValue(x);  // 이미 존재하면 값 갱신
        return;
    }
    expandExternal(v);
    (*v) = Entry(k, x);
    n++;
}
```

### 삭제 (Delete) - O(h) ⭐⭐⭐

#### Case 1: 자식이 0~1개
- 해당 노드 삭제, 자식을 부모에 연결

#### Case 2: 자식이 2개 ⭐
1. **Successor (후행자)** 또는 **Predecessor (선행자)** 찾기
2. 값만 교환
3. Successor/Predecessor 위치에서 삭제 (Case 1)

```cpp
void erase(const K& k) {
    Position v = treeSearch(k, root());
    if (v.isExternal()) return;  // 없음
    
    Position z;
    if (v.left().isExternal()) {
        z = v.left();
    } else if (v.right().isExternal()) {
        z = v.right();
    } else {
        // Case 2: 양쪽 자식 있음
        Position w = v.right();
        while (!w.left().isExternal())
            w = w.left();  // Successor 찾기
        
        Position u = w.parent();
        (*v) = (*u);       // 값 복사
        z = w;
    }
    removeAboveExternal(z);
    n--;
}
```

---

## 5. Successor와 Predecessor ⭐⭐⭐

> [!IMPORTANT]
> **교수님 강조**: "15(프레데세서)와 27(석세서)이 24랑 제일 비슷한 놈이다."
> Successor/Predecessor는 **삭제 연산의 핵심**!

### 왜 중요한가?

**상황**: 자식이 2개인 노드를 삭제해야 할 때
- 그냥 삭제하면 트리가 두 동강남
- **해결책**: 나랑 제일 비슷한 값을 가진 노드를 대타로 데려옴

### Successor (후행자)
- **정의**: 나보다 **큰 것 중 가장 작은 노드**
- **의미**: Inorder 순서에서 **바로 다음** 노드

**찾는 방법:**
1. **오른쪽 서브트리**로 한 칸 이동 (나보다 큰 동네)
2. 거기서 **왼쪽으로 끝까지** 이동 (그 중 제일 작은 놈)

```cpp
Position successor(Position v) {
    Position w = v.right();       // 1. 오른쪽으로
    while (!w.left().isExternal())
        w = w.left();             // 2. 왼쪽 끝까지
    return w.parent();
}
```

**예시**:
```
         50
        /  \
       30   70
      / \   / \
     20 40 60 80
```
- 50의 Successor = **60** (오른쪽 70 → 왼쪽 끝 60)
- 30의 Successor = **40** (오른쪽 40, 왼쪽 없음)

### Predecessor (선행자)
- **정의**: 나보다 **작은 것 중 가장 큰 노드**
- **의미**: Inorder 순서에서 **바로 이전** 노드

**찾는 방법:**
1. **왼쪽 서브트리**로 한 칸 이동 (나보다 작은 동네)
2. 거기서 **오른쪽으로 끝까지** 이동 (그 중 제일 큰 놈)

```cpp
Position predecessor(Position v) {
    Position w = v.left();        // 1. 왼쪽으로
    while (!w.right().isExternal())
        w = w.right();            // 2. 오른쪽 끝까지
    return w.parent();
}
```

**예시**:
```
         50
        /  \
       30   70
      / \   / \
     20 40 60 80
```
- 50의 Predecessor = **40** (왼쪽 30 → 오른쪽 끝 40)
- 70의 Predecessor = **60** (왼쪽 60, 오른쪽 없음)

### 삭제에서의 활용

**24를 삭제하고 싶다면:**
```
... 15 ... [24] ... 27 ...  (Inorder 순서)
         ↑
    삭제할 노드
```

**방법 1**: Predecessor(15) 사용
1. 24 자리에 15 값 복사
2. 원래 15 위치 삭제 (15는 왼쪽 자식이 없으므로 Case 1)

**방법 2**: Successor(27) 사용
1. 24 자리에 27 값 복사
2. 원래 27 위치 삭제 (27은 왼쪽 자식이 없으므로 Case 1)

### 핵심 포인트 요약

| 구분 | Successor | Predecessor |
|------|-----------|-------------|
| **정의** | 큰 것 중 가장 작은 것 | 작은 것 중 가장 큰 것 |
| **위치** | 오른쪽 서브트리의 최솟값 | 왼쪽 서브트리의 최댓값 |
| **찾는 법** | 오른쪽 → 왼쪽 끝 | 왼쪽 → 오른쪽 끝 |
| **특징** | **왼쪽 자식 없음** | **오른쪽 자식 없음** |

---

## 6. BST 시간 복잡도

| 연산 | 평균 | 최악 (편향) |
|------|------|-------------|
| Search | O(log n) | O(n) |
| Insert | O(log n) | O(n) |
| Delete | O(log n) | O(n) |

### 편향 트리 문제
```
1 → 2 → 3 → 4 → 5
```
순서대로 삽입하면 한쪽으로만 자라남 → O(n)

### 해결책
- AVL 트리
- Red-Black 트리
- B-Tree

---

## 7. 시험 핵심 체크리스트

- [ ] Preorder, Inorder, Postorder 순회 순서
- [ ] BST에서 Inorder = 정렬된 순서
- [ ] BST 삽입 알고리즘
- [ ] BST 삭제 3가지 케이스
- [ ] Successor/Predecessor 찾는 방법
- [ ] 트리 높이와 시간복잡도 관계
