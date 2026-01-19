# 템플릿과 STL

## 1. 제네릭 프로그래밍

### 개념
- 함수나 클래스를 **일반화**하여 데이터 타입에 독립적으로 작성
- 코드 재사용성 극대화

### 문제 상황
```cpp
// 타입별로 함수를 따로 만들어야 함
int maxInt(int a, int b) { return (a > b) ? a : b; }
double maxDouble(double a, double b) { return (a > b) ? a : b; }
// 비효율적!
```

---

## 2. 함수 템플릿

### 문법
```cpp
template <typename T>  // 또는 template <class T>
T functionName(T param1, T param2) {
    // 함수 본체
}
```

### 예제
```cpp
template <typename T>
T getMax(T a, T b) {
    return (a > b) ? a : b;
}

// 사용
int main() {
    cout << getMax(10, 20) << endl;        // int로 추론
    cout << getMax(3.14, 2.71) << endl;    // double로 추론
    cout << getMax<int>(10, 3.14) << endl; // 명시적 타입 지정
}
```

### 템플릿 특수화 (Template Specialization)
특정 타입에 대해 다른 동작을 정의

```cpp
template <typename T>
T getMax(T a, T b) {
    return (a > b) ? a : b;
}

// char* 타입에 대한 특수화
template <>
char* getMax<char*>(char* a, char* b) {
    return (strlen(a) > strlen(b)) ? a : b;  // 문자열 길이 비교
}
```

> **우선순위**: 일반 함수 > 특수화 템플릿 > 일반 템플릿

---

## 3. 클래스 템플릿

### 문법
```cpp
template <typename T>
class ClassName {
    T member;
public:
    T getMember() { return member; }
    void setMember(T value) { member = value; }
};
```

### 예제: 제네릭 스택
```cpp
template <typename T>
class Stack {
    T *data;
    int top;
    int capacity;
public:
    Stack(int cap = 100) : capacity(cap), top(-1) {
        data = new T[capacity];
    }
    
    void push(T item) {
        if (top < capacity - 1)
            data[++top] = item;
    }
    
    T pop() {
        if (top >= 0)
            return data[top--];
        throw "Stack is empty";
    }
    
    bool isEmpty() { return top == -1; }
    
    ~Stack() { delete[] data; }
};

// 사용
Stack<int> intStack(10);
Stack<string> strStack(5);
```

### 멤버 함수 외부 정의
```cpp
template <typename T>
class MyClass {
public:
    void func();
};

template <typename T>
void MyClass<T>::func() {
    // 구현
}
```

---

## 4. STL (Standard Template Library)

### 구성 요소
| 구성 요소 | 설명 |
|----------|------|
| **컨테이너** | 데이터를 저장하는 자료구조 |
| **반복자 (Iterator)** | 컨테이너 원소를 순회하는 포인터 |
| **알고리즘** | 정렬, 검색 등의 함수 |

---

## 5. 주요 컨테이너

| 컨테이너 | 특징 |
|----------|------|
| `vector` | 동적 크기 배열, 인덱스 접근 |
| `deque` | 앞뒤 양방향 삽입/삭제 |
| `list` | 양방향 연결 리스트 |
| `set` | 정렬된 고유 값 집합 |
| `map` | 키-값 쌍 (딕셔너리) |
| `stack` | LIFO 스택 |
| `queue` | FIFO 큐 |

---

## 6. vector 컨테이너

### 선언과 초기화
```cpp
#include <vector>

vector<int> v;                    // 빈 벡터
vector<int> v(10);                // 크기 10, 0으로 초기화
vector<int> v(10, 5);             // 크기 10, 5로 초기화
vector<int> v = {1, 2, 3, 4, 5};  // 초기화 리스트
```

### 주요 멤버 함수

| 함수 | 설명 |
|------|------|
| `push_back(elem)` | 마지막에 elem 추가 |
| `pop_back()` | 마지막 원소 삭제 |
| `at(index)` | index 위치 원소 참조 (범위 체크) |
| `operator[]` | index 위치 원소 참조 |
| `front()` | 첫 번째 원소 |
| `back()` | 마지막 원소 |
| `begin()` | 첫 원소 반복자 |
| `end()` | 끝 다음 반복자 |
| `size()` | 원소 개수 |
| `empty()` | 비어있으면 true |
| `clear()` | 모든 원소 삭제 |
| `insert(it, elem)` | it 위치에 elem 삽입 |
| `erase(it)` | it 위치 원소 삭제 |

### 사용 예제
```cpp
#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> v;
    
    // 추가
    v.push_back(10);
    v.push_back(20);
    v.push_back(30);
    
    // 접근
    cout << v[0] << endl;      // 10
    cout << v.at(1) << endl;   // 20
    cout << v.front() << endl; // 10
    cout << v.back() << endl;  // 30
    
    // 반복자로 순회
    for (vector<int>::iterator it = v.begin(); it != v.end(); it++) {
        cout << *it << " ";
    }
    // 또는 범위 기반 for (C++11)
    for (int x : v) {
        cout << x << " ";
    }
    
    // 삽입/삭제
    v.insert(v.begin() + 1, 15);  // {10, 15, 20, 30}
    v.erase(v.begin());           // {15, 20, 30}
    
    return 0;
}
```

---

## 7. 반복자 (Iterator)

### 종류

| 반복자 | ++방향 | 권한 |
|--------|--------|------|
| `iterator` | 다음 원소 | read/write |
| `const_iterator` | 다음 원소 | read only |
| `reverse_iterator` | 이전 원소 | read/write |
| `const_reverse_iterator` | 이전 원소 | read only |

### 사용 예제
```cpp
vector<int> v = {1, 2, 3, 4, 5};

// 정방향
for (vector<int>::iterator it = v.begin(); it != v.end(); it++) {
    cout << *it << " ";  // 1 2 3 4 5
}

// 역방향
for (vector<int>::reverse_iterator rit = v.rbegin(); rit != v.rend(); rit++) {
    cout << *rit << " ";  // 5 4 3 2 1
}

// auto 키워드 사용 (C++11)
for (auto it = v.begin(); it != v.end(); it++) {
    cout << *it << " ";
}
```

---

## 8. stack과 queue

### stack
```cpp
#include <stack>

stack<int> s;
s.push(10);     // 삽입
s.push(20);
s.top();        // 최상단 확인 (20)
s.pop();        // 삭제 (반환 없음!)
s.empty();      // 비어있는지
s.size();       // 크기
```

> **주의**: `pop()`은 값을 반환하지 않음! `top()`으로 먼저 확인 후 `pop()`

### queue
```cpp
#include <queue>

queue<int> q;
q.push(10);     // 삽입
q.push(20);
q.front();      // 앞 원소 (10)
q.back();       // 뒤 원소 (20)
q.pop();        // 앞에서 삭제
q.empty();
q.size();
```

---

## 9. map 컨테이너

```cpp
#include <map>

map<string, int> scores;

// 삽입
scores["Kim"] = 90;
scores["Lee"] = 85;
scores.insert(make_pair("Park", 95));

// 접근
cout << scores["Kim"] << endl;  // 90

// 검색
if (scores.find("Lee") != scores.end()) {
    cout << "Found!" << endl;
}

// 순회
for (auto& p : scores) {
    cout << p.first << ": " << p.second << endl;
}
```

---

## 10. 알고리즘 (`<algorithm>`)

### 정렬
```cpp
#include <algorithm>
#include <vector>

vector<int> v = {5, 2, 8, 1, 9};

sort(v.begin(), v.end());                  // 오름차순
sort(v.begin(), v.end(), greater<int>());  // 내림차순

// 배열 정렬
int arr[] = {5, 2, 8, 1, 9};
sort(arr, arr + 5);
```

### 검색
```cpp
// 선형 검색
auto it = find(v.begin(), v.end(), 8);
if (it != v.end()) {
    cout << "Found at index: " << (it - v.begin()) << endl;
}

// 이진 검색 (정렬된 상태에서)
bool found = binary_search(v.begin(), v.end(), 5);
```

### 기타 유용한 함수
```cpp
// 최대/최소
int maxVal = *max_element(v.begin(), v.end());
int minVal = *min_element(v.begin(), v.end());

// 역순
reverse(v.begin(), v.end());

// 채우기
fill(v.begin(), v.end(), 0);

// 개수 세기
int count = count(v.begin(), v.end(), 5);
```

---

## 11. 시험 핵심

- [ ] 템플릿 함수/클래스 문법
- [ ] vector 주요 함수 (`push_back`, `at`, `begin`, `end`, `size`)
- [ ] iterator 사용법
- [ ] stack 사용법 (`push`, `top`, `pop` - pop은 반환 없음!)
- [ ] sort 알고리즘 사용법
