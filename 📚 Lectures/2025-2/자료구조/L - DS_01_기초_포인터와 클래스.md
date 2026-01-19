# 자료구조 기초: 포인터, 배열, 클래스

## 1. 메모리 구조

### 메모리 영역
```
┌──────────────────┐ 낮은 주소
│   Code Area      │ ← 프로그램 코드
├──────────────────┤
│ Global/Static    │ ← 전역/정적 변수
├──────────────────┤
│   Heap (↓)       │ ← 동적 할당 (new)
│                  │
│   Free Space     │
│                  │
│   Stack (↑)      │ ← 지역 변수, 함수 호출
└──────────────────┘ 높은 주소
```

### Stack vs Heap
| 영역 | 특징 |
|------|------|
| **Stack** | 자동 메모리 할당/해제, 빠름, 컴파일 시점에 크기 결정 |
| **Heap** | 수동 관리 (new/delete), 런타임에 크기 결정, 느림 |

---

## 2. 포인터 핵심

### 기본 개념
```cpp
int b = 10;
int *ptr = &b;  // ptr은 b의 주소를 저장

cout << ptr;    // 주소 출력: 0xFF7C
cout << *ptr;   // 역참조: 10 출력
```

**포인터 = 주소값 + 자료형 정보**

### 포인터 자료형이 필요한 이유
1. **참조 크기 결정**: 몇 바이트를 읽을 것인가?
2. **연산 단위 결정**: `ptr + 1`이 몇 바이트 이동인가?
3. **타입 안전성**: 잘못된 타입 접근 방지

### 포인터 연산
```cpp
int arr[5] = {10, 20, 30, 40, 50};
int *ptr = arr;

ptr + 0  →  arr[0]  →  10
ptr + 1  →  arr[1]  →  20  (실제로는 +4바이트)
ptr + 2  →  arr[2]  →  30  (실제로는 +8바이트)

*(ptr + i) == arr[i]  // 동일한 표현!
```

---

## 3. 배열과 포인터

```cpp
int point[] = {95, 88, 76, 54, 85, 82};

// 배열 이름 = 첫 번째 원소의 주소 (포인터 상수)
point == &point[0]     // true
*point == point[0]     // true
*(point + 1) == point[1]  // true
```

### 배열 이름 vs 포인터 변수
```cpp
int arr[5];
int *ptr = arr;

arr++;   // ❌ 에러! 배열 이름은 상수
ptr++;   // ✅ OK! 포인터 변수는 변경 가능
```

---

## 4. Call by Value vs Reference

### Call by Value
```cpp
void swap(int a, int b) {
    int temp = a;
    a = b;
    b = temp;
    // 복사본만 바뀜! 원본은 그대로
}

int i = 4, j = 5;
swap(i, j);
cout << i << ", " << j;  // 여전히 4, 5
```

### Call by Reference (포인터)
```cpp
void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int i = 4, j = 5;
swap(&i, &j);  // 주소 전달
cout << i << ", " << j;  // 5, 4 (바뀜!)
```

### Call by Reference (레퍼런스)
```cpp
void swap(int &a, int &b) {  // 별명 생성
    int temp = a;
    a = b;
    b = temp;
}

int i = 4, j = 5;
swap(i, j);  // 자연스럽게 호출
cout << i << ", " << j;  // 5, 4
```

---

## 5. 동적 메모리 할당

```cpp
// Heap에 메모리 할당
int *arr = new int[100];

// 사용 후 반드시 해제!
delete[] arr;  // 메모리 누수 방지
```

---

## 6. 클래스 기초

### 클래스 정의
```cpp
class Shape {
private:
    int price;
    double x, y;
    char* owner;
    
public:
    // 생성자
    Shape(int p, double px, double py, char* o) {
        price = p;
        x = px;
        y = py;
        owner = new char[strlen(o) + 1];
        strcpy(owner, o);
    }
    
    // 소멸자
    ~Shape() {
        delete[] owner;  // 동적 메모리 해제
    }
};
```

### 객체 생성
```cpp
// Stack에 생성
Shape s1(100, 10.5, 20.3, "John");

// Heap에 생성 (동적 할당)
Shape *s2 = new Shape(200, 5.5, 15.3, "Jane");
delete s2;  // 사용 후 해제
```

---

## 7. this 포인터

```cpp
class Shape {
    int price;
public:
    void setPrice(int price) {
        this->price = price;  // this = 자기 자신의 주소
    }
    
    Shape& getThis() {
        return *this;  // 자기 자신 반환
    }
};
```

---

## 8. 복사 생성자

### Shallow Copy (얕은 복사) - 위험!
```cpp
class Shape {
    char* owner;
};

Shape s1("John");
Shape s2 = s1;  // owner 포인터만 복사
// s1.owner와 s2.owner가 같은 메모리 가리킴!
// 소멸자에서 2번 delete → 오류!
```

### Deep Copy (깊은 복사) - 안전!
```cpp
class Shape {
    char* owner;
public:
    // 사용자 정의 복사 생성자
    Shape(const Shape& other) {
        owner = new char[strlen(other.owner) + 1];
        strcpy(owner, other.owner);  // 새 메모리에 복사
    }
};
```

### 대입 연산자 오버로딩 ⭐⭐⭐

> [!IMPORTANT]
> **교수님 강조**: "대입 연산자 오버로딩 할 때 assignment의 첫 번째는 무조건 if문이 나와요!"

```cpp
class Shape {
    char* owner;
public:
    // ⭐ Self-copy 방지가 핵심!
    Shape& operator=(const Shape& other) {
        if (this != &other) {  // ⭐ 자기 자신과의 대입 방지
            // 1. 기존 메모리 해제
            delete[] owner;
            
            // 2. 새로운 메모리 할당 및 복사 (Deep Copy)
            owner = new char[strlen(other.owner) + 1];
            strcpy(owner, other.owner);
        }
        return *this;
    }
};
```

**왜 Self-copy 방지가 필요한가?**
```cpp
Shape s1("John");
s1 = s1;  // 자기 자신에게 대입하면?
```
- `if` 문 없이 `delete[] owner`를 먼저 실행하면
- 이미 해제된 메모리에서 `strcpy`를 시도 → **오류 발생!**

**this vs &other**
| 표현 | 의미 |
|------|------|
| `this` | 자기 자신의 **주소** (포인터) |
| `&other` | 매개변수 other의 **주소** |
| `this != &other` | 두 주소가 다르면 = 다른 객체 |

---

## 9. const와 클래스

```cpp
class AAA {
    int value;
public:
    int getValue() const {  // const 멤버 함수
        // value = 10;  // ❌ 에러! 멤버 수정 불가
        return value;   // ✅ 읽기만 가능
    }
};

const AAA obj(10);
obj.getValue();   // ✅ OK
```

---

## 10. static 멤버

```cpp
class Shape {
    static int count;  // 모든 객체가 공유
    int price;         // 각 객체마다 별도
    
public:
    Shape() { count++; }
    static int getCount() { return count; }
};

// 클래스 외부에서 초기화 (필수!)
int Shape::count = 0;

Shape s1, s2, s3;
cout << Shape::getCount();  // 3 (객체 없이 호출 가능)
```

---

## 11. 상속

```cpp
class Shape {  // Base class (부모)
protected:
    int price;
    double x, y;
    
public:
    Shape(int p, double px, double py) 
        : price(p), x(px), y(py) {}
    
    virtual double getArea() { return 0; }
};

class Circle : public Shape {  // Derived class (자식)
private:
    double radius;
    
public:
    Circle(int p, double px, double py, double r)
        : Shape(p, px, py), radius(r) {}
    
    double getArea() override {
        return 3.14 * radius * radius;
    }
};
```

### IS-A vs HAS-A 관계
```cpp
// IS-A: Circle은 Shape이다
class Circle : public Shape { };  // 상속

// HAS-A: Drawing은 Circle을 가지고 있다
class Drawing {
    Circle circle;  // 포함 (Composition)
};
```

---

## 12. 가상 함수와 다형성

### Static vs Dynamic Binding
```cpp
class Shape {
public:
    virtual double getArea() { return 0; }  // virtual!
};

class Circle : public Shape {
public:
    double getArea() override { 
        return 3.14 * radius * radius; 
    }
};

Shape *shp = new Circle(100, 0, 0, 5);
shp->getArea();  // ✅ Circle::getArea() 호출! (동적 바인딩)
```

### 순수 가상 함수
```cpp
class Shape {  // Abstract class (추상 클래스)
public:
    virtual double getArea() = 0;  // 순수 가상 함수
};

// Shape s;  // ❌ 에러! 추상 클래스는 객체 생성 불가
```

### 가상 소멸자 ⭐⭐⭐

> [!IMPORTANT]
> **교수님 강조**: 상속 계층에서 동적 할당 시 가상 소멸자는 **메모리 누수 방지**에 필수!

#### 왜 가상 소멸자가 필요한가?

**문제 상황** (virtual 없을 때):
```cpp
class Shape {
public:
    ~Shape() { cout << "Shape 소멸" << endl; }  // virtual 없음!
};

class Circle : public Shape {
    char* data;
public:
    Circle() { data = new char[100]; }
    ~Circle() { 
        delete[] data;  // 이게 호출 안 됨!
        cout << "Circle 소멸" << endl; 
    }
};

Shape *shp = new Circle();
delete shp;  // ❌ Shape 소멸자만 호출! → 메모리 누수!
```

**해결책** (virtual 사용):
```cpp
class Shape {
public:
    virtual ~Shape() { }  // ⭐ virtual 추가!
};

Shape *shp = new Circle();
delete shp;  // ✅ Circle → Shape 순서로 소멸자 호출
```

#### 핵심 원리

| 구분 | virtual 없을 때 | virtual 있을 때 |
|------|----------------|-----------------|
| **바인딩** | 정적 바인딩 (컴파일 시점) | 동적 바인딩 (런타임) |
| **호출** | 포인터 타입(Shape)의 소멸자만 | 실제 객체(Circle)의 소멸자 먼저 |
| **결과** | 자식 클래스 리소스 누수 | 안전한 메모리 해제 |

**규칙**: 상속을 사용하고 동적 할당을 한다면, **부모 클래스의 소멸자는 반드시 virtual**로 선언!

