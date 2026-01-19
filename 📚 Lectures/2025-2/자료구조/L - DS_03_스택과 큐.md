# 스택과 큐

## 1. ADT (Abstract Data Type)

**ADT = What (무엇을), not How (어떻게)**
- 인터페이스 정의 (함수 이름, 매개변수, 반환값)
- 구현 방법은 별도로 결정
- 프로토콜, 표준 인터페이스, 약속

---

## 2. 스택 (Stack)

### 개념
- **LIFO** (Last-In First-Out): 후입선출
- 한쪽 끝(TOP)에서만 삽입/삭제
- History 저장에 유용

### ADT 정의
```cpp
template <typename Object>
class Stack {
public:
    int size() const;
    bool isEmpty() const;
    void push(const Object& obj);
    Object pop();  // throws StackEmptyException
    const Object& top();  // 맨 위 값 확인 (제거 안 함)
};
```

### 배열 기반 구현
```cpp
template <typename Object>
class ArrayStack {
private:
    Object* S;
    int capacity;
    int t;  // top 인덱스 (초기값 -1)
    
public:
    ArrayStack(int cap) : capacity(cap), t(-1) {
        S = new Object[capacity];
    }
    
    int size() const { return t + 1; }
    bool isEmpty() const { return (t < 0); }
    
    void push(const Object& obj) {
        if (size() == capacity)
            throw StackFullException("Stack overflow");
        S[++t] = obj;
    }
    
    Object pop() {
        if (isEmpty())
            throw StackEmptyException("Stack underflow");
        return S[t--];
    }
    
    const Object& top() const {
        if (isEmpty())
            throw StackEmptyException("Stack is empty");
        return S[t];
    }
};
```

### 시간 복잡도
| 연산 | 시간 |
|------|------|
| size() | O(1) |
| isEmpty() | O(1) |
| push() | O(1) |
| pop() | O(1) |
| top() | O(1) |

---

## 3. 큐 (Queue)

### 개념
- **FIFO** (First-In First-Out): 선입선출
- 뒤(rear)에서 삽입, 앞(front)에서 삭제
- 순서가 중요한 곳에 사용

### ADT 정의
```cpp
template <typename Object>
class Queue {
public:
    int size() const;
    bool isEmpty() const;
    void enqueue(const Object& obj);
    Object dequeue();  // throws QueueEmptyException
    const Object& front();
};
```

### 순환 큐 (Circular Queue) 구현
```cpp
template <typename Object>
class CircularQueue {
private:
    Object* Q;
    int capacity;
    int f;  // front
    int r;  // rear
    
public:
    CircularQueue(int cap) : capacity(cap), f(0), r(0) {
        Q = new Object[capacity];
    }
    
    int size() const {
        return (capacity - f + r) % capacity;
    }
    
    bool isEmpty() const {
        return (f == r);
    }
    
    void enqueue(const Object& obj) {
        if (size() == capacity - 1)
            throw QueueFullException("Queue overflow");
        Q[r] = obj;
        r = (r + 1) % capacity;  // 순환!
    }
    
    Object dequeue() {
        if (isEmpty())
            throw QueueEmptyException("Queue underflow");
        Object obj = Q[f];
        f = (f + 1) % capacity;  // 순환!
        return obj;
    }
};
```

---

## 4. 스택 응용 문제 ⭐

### 1) 괄호 매칭 (Parentheses Matching)

**알고리즘:**
1. 여는 괄호면 push
2. 닫는 괄호면 pop & 매칭 확인
3. 끝났을 때 스택이 비어있어야 함

```cpp
bool isMatching(char open, char close) {
    return (open == '(' && close == ')') ||
           (open == '[' && close == ']') ||
           (open == '{' && close == '}');
}

bool parenMatch(char X[], int n) {
    Stack<char> S;
    for (int i = 0; i < n; i++) {
        if (X[i] == '(' || X[i] == '[' || X[i] == '{')
            S.push(X[i]);
        else if (X[i] == ')' || X[i] == ']' || X[i] == '}') {
            if (S.isEmpty()) return false;
            if (!isMatching(S.pop(), X[i])) return false;
        }
    }
    return S.isEmpty();
}
```

### 2) Stock Span Problem ⭐⭐⭐ (시험 필출)

**문제**: 오늘 주가보다 작거나 같은 가격이 연속으로 몇 일인가?

**Quadratic Solution - O(n²)**
```cpp
void computeSpans1(int P[], int S[], int n) {
    for (int i = 0; i < n; i++) {
        int k = 1;
        while (k <= i && P[i-k] <= P[i])
            k++;
        S[i] = k;
    }
}
```

**Linear Solution - O(n)** ⭐
```cpp
void computeSpans2(int P[], int S[], int n) {
    Stack<int> D;  // 인덱스 저장
    for (int i = 0; i < n; i++) {
        // 현재 가격보다 작거나 같은 것들 제거
        while (!D.isEmpty() && P[D.top()] <= P[i])
            D.pop();
        
        int h = D.isEmpty() ? -1 : D.top();
        S[i] = i - h;
        D.push(i);
    }
}
```

**예제:**
```
Price: 100 80 60 70 60 75 85
Span:    1  1  1  2  1  4  6
```

### 3) 중위→후위 표기법 변환 ⭐⭐⭐

**표기법:**
- **중위 (Infix)**: `A + B * C` (인간 친화적)
- **후위 (Postfix)**: `A B C * +` (컴퓨터 친화적)

**우선순위:**
```cpp
int precedence(char op) {
    if (op == '^') return 3;
    if (op == '*' || op == '/') return 2;
    if (op == '+' || op == '-') return 1;
    return 0;  // '('
}
```

**알고리즘:**
```cpp
string infixToPostfix(string infix) {
    Stack<char> S;
    string postfix = "";
    
    for (char token : infix) {
        if (isOperand(token)) {
            postfix += token;
        }
        else if (token == '(') {
            S.push(token);
        }
        else if (token == ')') {
            while (S.top() != '(')
                postfix += S.pop();
            S.pop();  // '(' 제거
        }
        else {  // 연산자
            while (!S.isEmpty() && 
                   precedence(S.top()) >= precedence(token))
                postfix += S.pop();
            S.push(token);
        }
    }
    
    while (!S.isEmpty())
        postfix += S.pop();
    
    return postfix;
}
```

**변환 예제:**
```
(A + B) * (C - D)  →  A B + C D - *
A * B + C * D^2    →  A B * C D 2 ^ * +
```

---

## 5. 연결 리스트 기반 스택

```cpp
template <typename Object>
class LinkedStack {
    struct Node {
        Object element;
        Node* next;
        Node(const Object& e, Node* n = nullptr) 
            : element(e), next(n) {}
    };
    
    Node* TOP;
    int count;
    
public:
    void push(const Object& e) {
        // ⭐ 핵심: 새 노드가 현재 TOP을 가리키게 함
        Node* temp = new Node(e, TOP);
        TOP = temp;
        count++;
    }
    
    Object pop() {
        if (isEmpty()) 
            throw StackEmptyException("Empty");
        
        Node* old = TOP;
        TOP = TOP->next;  // 다음 노드로 이동
        count--;
        
        Object result = old->element;
        delete old;  // 메모리 해제
        return result;
    }
};
```

---

## 6. 연결 리스트 기반 큐

```cpp
template <typename Object>
class LinkedQueue {
    Node* head;  // front
    Node* tail;  // rear
    int count;
    
public:
    void enqueue(const Object& e) {
        Node* v = new Node(e, nullptr);
        if (count == 0) 
            head = v;
        else 
            tail->next = v;
        tail = v;
        count++;
    }
    
    Object dequeue() {
        if (isEmpty()) 
            throw QueueEmptyException("Empty");
        
        Node* old = head;
        head = head->next;
        if (--count == 0) 
            tail = nullptr;
        
        Object result = old->element;
        delete old;
        return result;
    }
};
```

---

## 7. 효율적 구현 매핑

| 자료구조 | 연산 | 연결 리스트 매핑 | 시간 |
|----------|------|------------------|------|
| **Stack** | push | insertFirst | O(1) |
| | pop | removeFirst | O(1) |
| **Queue** | enqueue | insertLast | O(1) |
| | dequeue | removeFirst | O(1) |

> **주의**: Stack의 pop을 removeLast로 구현하면 O(n)이 되어 비효율적!
