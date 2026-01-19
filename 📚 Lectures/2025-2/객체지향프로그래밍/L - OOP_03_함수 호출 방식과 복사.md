# 함수 호출 방식과 복사

## 1. 함수 호출 방식 비교

### 세 가지 호출 방식

| 방식 | 전달 내용 | 원본 영향 | 메모리 |
|------|----------|----------|--------|
| **Call by Value** | 값의 복사본 | ❌ 영향 없음 | 별도 공간 (스택) |
| **Call by Address** | 주소의 복사본 | ✅ 직접 변경 | 포인터가 스택에 생성 |
| **Call by Reference** | 변수의 별명 | ✅ 직접 변경 | 메모리 공유 |

---

## 2. Call by Value (값에 의한 호출)

### 동작 방식
- 인자의 **값을 복사**하여 매개변수에 전달
- 호출하는 변수와 **별도의 메모리 공간** 할당
- 함수 내 변경이 원본에 영향 없음

```cpp
void swap(int a, int b) {
    int temp = a;
    a = b;
    b = temp;
}

int main() {
    int x = 10, y = 20;
    swap(x, y);
    // x = 10, y = 20 (변화 없음!)
}
```

### 객체 전달 시
- 객체 전체가 복사됨
- **생성자는 호출되지 않고, 복사 생성자가 실행**
- 큰 객체의 경우 오버헤드 발생

---

## 3. Call by Address (주소에 의한 호출)

### 동작 방식
- 인자의 **메모리 주소(포인터)**를 전달
- 포인터를 통해 원본에 **직접 접근**하여 값 변경 가능

```cpp
void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main() {
    int x = 10, y = 20;
    swap(&x, &y);
    // x = 20, y = 10 (교환됨!)
}
```

### 객체 전달 시
- 객체의 주소를 전달
- 포인터를 통해 원본 객체를 직접 변경 가능

---

## 4. Call by Reference (참조에 의한 호출)

### 동작 방식
- 매개변수가 실인자의 **별명(alias)**이 됨
- 메모리 공간을 공유
- 포인터보다 **문법이 간결**

```cpp
void swap(int &a, int &b) {
    int temp = a;
    a = b;
    b = temp;
}

int main() {
    int x = 10, y = 20;
    swap(x, y);
    // x = 20, y = 10 (교환됨!)
}
```

### 객체 전달 시
- 복사가 일어나지 않아 **효율적**
- 원본 보호가 필요하면 `const` 사용

```cpp
void printCircle(const Circle &c) {
    cout << c.getRadius();  // 읽기만 가능
}
```

---

## 5. 참조 리턴 (Reference Return)

### 개념
- 함수가 **메모리 공간에 대한 참조**를 리턴
- 값의 복사가 아닌 공간 자체를 반환
- 리턴된 참조로 값 변경 가능

```cpp
char& find(char str[], int index) {
    return str[index];  // 메모리 공간 참조 리턴
}

int main() {
    char name[] = "hello";
    find(name, 0) = 'H';  // 첫 글자를 'H'로 변경
    cout << name;         // "Hello"
}
```

---

## 6. 객체 치환과 리턴

### 객체 치환
```cpp
Circle c1(10), c2(20);
c1 = c2;  // c2의 모든 데이터가 c1에 비트 단위로 복사
// c1과 c2는 독립적인 메모리 공간 유지
```

### 객체 리턴
```cpp
Circle getCircle() {
    Circle tmp(10);
    return tmp;  // 복사본이 생성되어 전달
}

Circle c = getCircle();  // 복사 생성자 호출
```

---

## 7. 복사 생성자 (Copy Constructor)

### 개념
- 다른 객체로 **초기화될 때** 호출되는 특별한 생성자
- 한 클래스에 **하나만** 선언 가능
- 자기 클래스에 대한 **참조 매개변수**를 가짐

### 호출 시점
1. 이미 있는 객체로 새 객체 생성할 때
2. 함수 호출 시 값으로 객체 전달할 때
3. 함수에서 객체를 리턴할 때

```cpp
class Circle {
public:
    Circle(Circle &c);  // 복사 생성자 선언
};

// 복사 생성자 구현
Circle::Circle(Circle &c) {
    radius = c.radius;
}

// 사용
Circle c1(10);
Circle c2 = c1;      // 복사 생성자 호출
Circle c3(c1);       // 복사 생성자 호출
```

### 디폴트 복사 생성자
- 명시적으로 구현하지 않으면 컴파일러가 자동 생성
- **얕은 복사(shallow copy)** 수행

---

## 8. 얕은 복사 vs 깊은 복사

### 얕은 복사 (Shallow Copy)

#### 동작 방식
- 멤버 변수를 **1:1로 단순 복사**
- 포인터의 경우 **주소 값만 복사** (같은 메모리 공유)

#### 비유
> "장난감의 위치가 적힌 쪽지만 다른 아이에게 건네주는 것"

#### 문제점
```cpp
class Person {
    char *name;
public:
    Person(const char* n) {
        name = new char[strlen(n) + 1];
        strcpy(name, n);
    }
    ~Person() { delete[] name; }
};

Person p1("Kim");
Person p2 = p1;  // 얕은 복사 - 같은 메모리 공유!

// p2 소멸 시 name 메모리 해제
// p1 소멸 시 이미 해제된 메모리 재해제 → 오류!
```

**문제점:**
1. **이중 해제 (Double-Free) 오류**: 같은 메모리를 두 번 delete
2. 한 객체의 수정이 다른 객체에도 영향

---

### 깊은 복사 (Deep Copy)

#### 동작 방식
- 포인터가 가리키는 **동적 메모리까지 새로 할당**하여 복사
- 원본과 사본이 **완전히 독립적**인 메모리 소유

#### 비유
> "완전히 동일한 새 장난감을 만들어 다른 아이에게 주는 것"

#### 구현
```cpp
class Person {
    char *name;
public:
    // 깊은 복사 생성자
    Person(Person &other) {
        name = new char[strlen(other.name) + 1];  // 새 메모리 할당
        strcpy(name, other.name);                  // 내용 복사
    }
    
    // 깊은 복사 대입 연산자
    Person& operator=(const Person &other) {
        if (this != &other) {           // 자기 자신 체크
            delete[] name;               // 기존 메모리 해제
            name = new char[strlen(other.name) + 1];
            strcpy(name, other.name);
        }
        return *this;
    }
    
    ~Person() { delete[] name; }
};
```

---

### 정리 비교표

| 구분 | 얕은 복사 | 깊은 복사 |
|------|----------|----------|
| 구현 | 디폴트 (자동) | 직접 구현 필요 |
| 포인터 복사 | 주소만 복사 | 새 메모리 할당 + 내용 복사 |
| 메모리 | 공유 | 독립적 |
| 소멸 시 | 이중 해제 위험 | 안전 |
| 적용 | 포인터 멤버 없을 때 | 포인터 멤버 있을 때 |

---

## 9. 함수 오버로딩과 디폴트 매개변수

### 함수 오버로딩 (Function Overloading)
- 동일한 이름의 함수를 **매개변수를 다르게** 하여 여러 개 정의

```cpp
int add(int a, int b) { return a + b; }
double add(double a, double b) { return a + b; }
int add(int a, int b, int c) { return a + b + c; }
```

> **주의**: 모호성(ambiguity) 오류 발생 가능

### 디폴트 매개변수 (Default Arguments)
- 함수 선언 시 매개변수에 기본값 지정
- 호출 시 생략하면 기본값 사용

```cpp
void greet(string name = "Guest", int times = 1) {
    for (int i = 0; i < times; i++)
        cout << "Hello, " << name << endl;
}

greet();              // "Hello, Guest" 1번
greet("Kim");         // "Hello, Kim" 1번
greet("Lee", 3);      // "Hello, Lee" 3번
```

> 오버로딩 함수 수를 줄이는 데 유용
