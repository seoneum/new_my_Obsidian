# 힙과 우선순위 큐

## 1. 우선순위 큐 (Priority Queue)

### 개념
- 일반 큐: 먼저 들어온 것이 먼저 나감 (FIFO)
- **우선순위 큐**: 우선순위가 높은 것이 먼저 나감

### 종류
- **Min-PQ (Min Heap)**: 가장 작은 값이 먼저 나옴
- **Max-PQ (Max Heap)**: 가장 큰 값이 먼저 나옴

> 교수님 비유: "들어올 때는 막 들어와도, 나갈 때는 '형님 먼저'라며 우선순위가 높은 사람이 먼저 나가는 것"

---

## 2. 힙 (Heap) ⭐⭐⭐

### 3가지 제약조건 (필수 암기!)

1. **Degree = 2**: 이진 트리
2. **Heap Order Property**:
   - Min Heap: 부모 ≤ 자식
   - Max Heap: 부모 ≥ 자식
3. **Complete Binary Tree ⭐**: 위에서 아래로, 왼쪽에서 오른쪽으로 빈틈없이 채워짐

### 배열 구현 (중요!)
```cpp
// 루트: index 1 (0번은 비워둠)
// i번 노드의 왼쪽 자식: 2*i
// i번 노드의 오른쪽 자식: 2*i + 1
// i번 노드의 부모: i / 2
```

**장점**: 포인터 없이 인덱스 계산만으로 이동 가능

---

## 3. 힙 연산

### 삽입 (Insert) - Upheap ⭐

1. **위치 선정**: 마지막 노드 다음 위치에 삽입
2. **Upheap (Bubble Up)**: 부모와 비교하며 위로 이동

```cpp
void insert(const Object& e) {
    // 마지막 위치에 삽입
    H[++size] = e;
    
    // Upheap
    int i = size;
    while (i > 1 && H[i] < H[i/2]) {  // Min Heap
        swap(H[i], H[i/2]);
        i = i / 2;
    }
}
```

**시간 복잡도**: O(log n)

### 삭제 (Remove Min/Max) - Downheap ⭐

1. **루트 삭제**: 루트 값 저장
2. **대체**: 마지막 노드를 루트로 이동
3. **Downheap (Bubble Down)**: 자식과 비교하며 아래로 이동

```cpp
Object removeMin() {
    Object min = H[1];      // 루트 저장
    H[1] = H[size--];       // 마지막 노드를 루트로
    
    // Downheap
    int i = 1;
    while (2*i <= size) {
        int child = 2*i;
        // 더 작은 자식 선택
        if (child < size && H[child+1] < H[child])
            child++;
        
        if (H[i] <= H[child]) break;
        swap(H[i], H[child]);
        i = child;
    }
    
    return min;
}
```

**시간 복잡도**: O(log n)

---

## 4. 힙 정렬 (Heap Sort) ⭐⭐⭐

### 알고리즘
1. **Phase 1**: 모든 데이터를 힙에 삽입 - O(n log n)
2. **Phase 2**: 하나씩 꺼내면 정렬된 순서 - O(n log n)

**총 시간 복잡도**: O(n log n)

```cpp
void heapSort(int arr[], int n) {
    // Phase 1: Build heap
    for (int i = 0; i < n; i++)
        heap.insert(arr[i]);
    
    // Phase 2: Extract in order
    for (int i = 0; i < n; i++)
        arr[i] = heap.removeMin();
}
```

### Bottom-up Construction
- 힙 구축을 O(n)에 가능
- 리프부터 시작해서 Downheap

---

## 5. 허프만 코딩 (Huffman Coding) ⭐⭐⭐

### 목적
- **데이터 압축**: 자주 나오는 문자는 짧은 코드, 드문 문자는 긴 코드

### Prefix Rule (접두어 규칙)
- 어떤 코드도 다른 코드의 접두어가 되면 안 됨
- 예: 'a' = `10`이면, 다른 문자는 `10`으로 시작 불가

### 알고리즘 (PQ 사용) ⭐

```cpp
while (PQ.size() > 1) {
    // 1. 가장 작은 2개 꺼내기
    Node* left = PQ.removeMin();
    Node* right = PQ.removeMin();
    
    // 2. 합쳐서 새 노드 만들기
    Node* parent = new Node(left->freq + right->freq);
    parent->left = left;
    parent->right = right;
    
    // 3. 다시 PQ에 넣기
    PQ.insert(parent);
}
// 마지막 남은 노드가 루트
```

### 예제 시뮬레이션
```
데이터: a(16), b(5), c(12), d(17), e(10), f(25)

1단계: {b:5, e:10, c:12, a:16, d:17, f:25}
2단계: b(5) + e(10) = be(15)
       {c:12, be:15, a:16, d:17, f:25}
3단계: c(12) + be(15) = cbe(27)
       {a:16, d:17, f:25, cbe:27}
4단계: a(16) + d(17) = ad(33)
       {f:25, cbe:27, ad:33}
5단계: f(25) + cbe(27) = fcbe(52)
       {ad:33, fcbe:52}
6단계: ad(33) + fcbe(52) = Total(85)
```

### 코드 생성
- 왼쪽 간선: 0
- 오른쪽 간선: 1
- 루트에서 리프까지 경로가 코드

---

## 6. 3진 허프만 코드 (심화)

- 0, 1, 2 세 가지 사용
- PQ에서 **3개를 꺼내서** 합침

```cpp
while (PQ.size() > 1) {
    Node* n1 = PQ.removeMin();
    Node* n2 = PQ.removeMin();
    Node* n3 = (PQ.size() > 0) ? PQ.removeMin() : nullptr;
    
    // 3개의 자식을 가진 노드 생성
    Node* parent = new Node(n1->freq + n2->freq + (n3 ? n3->freq : 0));
    parent->left = n1;
    parent->middle = n2;
    parent->right = n3;
    
    PQ.insert(parent);
}
```

---

## 7. 시험 핵심 체크리스트

- [ ] 힙의 3가지 제약조건 암기
- [ ] 배열에서 부모/자식 인덱스 계산
- [ ] Upheap, Downheap 알고리즘
- [ ] 힙 정렬 시간 복잡도: O(n log n)
- [ ] 허프만 코딩 알고리즘 (PQ 사용)
- [ ] 허프만 트리 손으로 그리기
- [ ] Prefix Rule 설명
