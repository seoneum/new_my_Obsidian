# 연결 리스트

## 1. Array vs Linked List

| 특징 | Array | Linked List |
|------|-------|-------------|
| **크기** | 고정 (Fixed) | 가변 (Variable) |
| **공간** | 높은 효율 | 낮음 (포인터 공간 필요) |
| **접근** | O(1) Random Access | O(n) Sequential Access |
| **삽입/삭제** | O(n) Shift 필요 | O(1) 포인터 조작만 |

---

## 2. 단일 연결 리스트 (Singly Linked List)

### Node 구조
```cpp
template <typename Object>
struct Node {
    Object element;
    Node* next;
    
    Node(const Object& e = Object(), Node* n = nullptr) 
        : element(e), next(n) {}
};

typedef Node* NodePtr;
```

### 기본 연산

#### insertFirst - O(1)
```cpp
void insertFirst(const Object& e) {
    // ⭐ 핵심: 새 노드 생성 시 현재 head를 next로 연결
    NodePtr temp = new Node(e, head);
    head = temp;
    count++;
}
```

#### removeFirst - O(1)
```cpp
void removeFirst() {
    if (isEmpty()) throw Exception("Empty");
    
    NodePtr old = head;      // 삭제할 노드 저장
    head = head->next;       // head 이동
    count--;
    delete old;              // 메모리 해제
}
```

### 단점
- **removeLast가 O(n)**: 마지막 노드의 이전 노드를 찾으려면 처음부터 순회해야 함

---

## 3. 이중 연결 리스트 (Doubly Linked List) ⭐⭐⭐

### 왜 필요한가?
- 단일 연결 리스트의 removeLast O(n) 문제 해결
- 양방향 탐색 가능
- **모든 삽입/삭제 O(1)** 달성

### Node 구조
```cpp
struct Node {
    Object element;
    Node* next;   // 오른쪽 (다음 노드)
    Node* prev;   // 왼쪽 (이전 노드) ⭐ 추가!
    
    Node(const Object& e = Object(), Node* p = nullptr, Node* n = nullptr)
        : element(e), prev(p), next(n) {}
};
```

### 센티널 노드 (Sentinel Nodes)
```cpp
NodePtr header;   // 가장 앞 (데이터 없음)
NodePtr trailer;  // 가장 뒤 (데이터 없음)

// 초기화
LinkedList() {
    header = new Node();
    trailer = new Node();
    header->next = trailer;
    trailer->prev = header;
    count = 0;
}
```

**장점:**
- 빈 리스트, 맨 앞/뒤 삽입/삭제 시 예외 처리 불필요
- 코드가 간결해짐

---

## 4. 이중 연결 리스트 핵심 연산 ⭐⭐⭐

### insertFirst - O(1)
```cpp
void insertFirst(const Object& e) {
    NodePtr oldFirst = header->next;  // 0단계: 기존 첫 노드
    
    // 1단계: 새 노드 생성 (prev=header, next=oldFirst)
    NodePtr temp = new Node(e, header, oldFirst);
    
    // 2단계: 기존 첫 노드의 prev 연결
    oldFirst->prev = temp;
    
    // 3단계: header의 next 연결
    header->next = temp;
    
    count++;
}
```

### insertLast - O(1)
```cpp
void insertLast(const Object& e) {
    NodePtr oldLast = trailer->prev;
    
    NodePtr temp = new Node(e, oldLast, trailer);
    
    oldLast->next = temp;
    trailer->prev = temp;
    
    count++;
}
```

### removeFirst - O(1)
```cpp
void removeFirst() {
    if (isEmpty()) throw Exception("Empty");
    
    NodePtr old = header->next;       // 삭제할 노드
    NodePtr newFirst = old->next;     // 새로운 첫 노드
    
    header->next = newFirst;          // header 연결
    newFirst->prev = header;          // newFirst 연결
    
    count--;
    delete old;
}
```

### removeLast - O(1) ⭐
```cpp
void removeLast() {
    if (isEmpty()) throw Exception("Empty");
    
    NodePtr old = trailer->prev;      // 삭제할 노드
    NodePtr newLast = old->prev;      // 새로운 마지막 노드
    
    trailer->prev = newLast;          // trailer 연결
    newLast->next = trailer;          // newLast 연결
    
    count--;
    delete old;
}
```

---

## 5. 시험 핵심 포인트 ⭐⭐⭐

### 노드 생성자 인자 (5점짜리!)
```cpp
// insertFirst의 핵심
NodePtr temp = new Node(___①___, ___②___, ___③___);

// 정답:
// ① = e (삽입할 데이터)
// ② = header (새 노드의 prev)
// ③ = oldFirst 또는 header->next (새 노드의 next)
```

### 포인터 3개 운영 전략
삭제 시 최소 2~3개의 임시 포인터 필요:
- `old`: 삭제할 노드
- `newLast` / `newFirst`: 새로운 끝/시작 노드

### 연결 순서 중요!
1. **새 노드의 포인터를 먼저 설정**
2. 그 다음 기존 노드들의 포인터 변경
3. 순서가 바뀌면 포인터를 잃어버림!

---

## 6. 복사 생성자와 대입 연산자

### Self-copy 방지 ⭐
```cpp
LinkedList& operator=(const LinkedList& ls) {
    // ⭐ Self-copy 방지 (필수!)
    if (this != &ls) {
        removeAll();
        copyFrom(ls);
    }
    return *this;
}
```

### Deep Copy 구현
```cpp
void copyFrom(const LinkedList& other) {
    NodePtr p = other.header->next;
    while (p != other.trailer) {
        insertLast(p->element);  // 새 노드 생성
        p = p->next;
    }
}
```

---

## 7. Iterator (반복자)

### 개념
- 리스트 내부 구조를 몰라도 순회 가능
- `++` 연산자로 다음 노드 이동

### begin()과 end()
```cpp
iterator begin() { return iterator(header->next); }
iterator end() { return iterator(trailer); }  // trailer 자체!
```

> **주의**: `end()`는 마지막 데이터가 아니라 **trailer(끝 다음 위치)** 를 가리킴!

```cpp
for (auto it = L.begin(); it != L.end(); ++it) {
    cout << *it << " ";
}
```

---

## 8. Deque (Double-Ended Queue)

### 개념
- 양쪽 끝에서 삽입/삭제 가능
- Stack + Queue의 일반화

### 연산
```cpp
void insertFirst(const Object& e);
void insertLast(const Object& e);
Object removeFirst();
Object removeLast();
```

### Adapter Pattern
Deque로 Stack과 Queue 모두 구현 가능:

```cpp
// Stack = Deque의 한쪽만 사용
push()  → insertFirst()
pop()   → removeFirst()

// Queue = Deque의 양쪽 사용
enqueue() → insertLast()
dequeue() → removeFirst()
```

---

## 9. 시험 대비 체크리스트

- [ ] insertFirst/Last 코드 직접 작성
- [ ] removeFirst/Last 코드 직접 작성
- [ ] Node 생성자 인자 정확히 이해
- [ ] 포인터 3개 운영 전략 이해
- [ ] Self-copy 방지 코드 암기
- [ ] header/trailer 센티널 개념 이해
- [ ] Array vs List 장단점 설명 가능
- [ ] Big-O 시간복잡도 암기
