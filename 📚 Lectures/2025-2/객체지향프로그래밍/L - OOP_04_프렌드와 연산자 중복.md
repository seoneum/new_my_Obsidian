# 프렌드와 연산자 중복

## 1. 프렌드 함수 (Friend Function)

### 개념
- 클래스의 멤버는 아니지만 **private와 protected에 접근 가능**한 함수
- 캡슐화의 예외적 허용

### 선언 방법 3가지

#### 1) 외부 함수를 프렌드로 선언
```cpp
// 전방 선언 (선참조 오류 방지)
class Circle;

// 외부 함수 정의
void printRadius(Circle &c) {
    cout << c.radius;  // private 멤버 접근
}

class Circle {
private:
    int radius;
public:
    friend void printRadius(Circle &c);  // 프렌드 선언
};
```

#### 2) 다른 클래스의 멤버 함수를 프렌드로 선언
```cpp
class Manager {
public:
    void showSalary(Employee &e);
};

class Employee {
private:
    int salary;
public:
    friend void Manager::showSalary(Employee &e);
};
```

#### 3) 다른 클래스 전체를 프렌드로 선언
```cpp
class Circle {
private:
    int radius;
public:
    friend class CircleManager;  // CircleManager의 모든 함수가 Circle의 private 접근 가능
};
```

---

## 2. 연산자 중복 (Operator Overloading)

### 개념
- 기존 연산자를 **새로운 연산 방법으로 재정의**
- 객체에 대해 연산자를 사용할 수 있게 함

### 규칙
1. 기존에 있는 연산자만 중복 가능 (새 연산자 생성 불가)
2. 피연산자 개수 변경 불가
3. 연산자 우선순위 변경 불가
4. 중복 불가능한 연산자: `.`, `.*`, `::`, `?:`

### 문법
```cpp
리턴타입 operator연산자(매개변수) {
    // 연산 구현
}
```

---

## 3. 연산자 중복 구현 방법

### 방법 1: 클래스 멤버 함수로 구현
```cpp
class Complex {
    double real, imag;
public:
    Complex(double r = 0, double i = 0) : real(r), imag(i) {}
    
    // + 연산자 중복 (멤버 함수)
    Complex operator+(const Complex &c) {
        return Complex(real + c.real, imag + c.imag);
    }
};

// 사용
Complex c1(1, 2), c2(3, 4);
Complex c3 = c1 + c2;  // c1.operator+(c2) 호출
```

### 방법 2: 외부 함수 + 프렌드 선언
```cpp
class Complex {
    double real, imag;
public:
    Complex(double r = 0, double i = 0) : real(r), imag(i) {}
    
    friend Complex operator+(const Complex &a, const Complex &b);
};

// 외부 함수로 구현
Complex operator+(const Complex &a, const Complex &b) {
    return Complex(a.real + b.real, a.imag + b.imag);
}
```

---

## 4. 다양한 연산자 중복 예제

### 비교 연산자
```cpp
bool operator==(const Complex &c) {
    return (real == c.real) && (imag == c.imag);
}

bool operator!=(const Complex &c) {
    return !(*this == c);
}
```

### 대입 연산자
```cpp
Complex& operator=(const Complex &c) {
    if (this != &c) {  // 자기 대입 체크
        real = c.real;
        imag = c.imag;
    }
    return *this;
}
```

### 복합 대입 연산자
```cpp
Complex& operator+=(const Complex &c) {
    real += c.real;
    imag += c.imag;
    return *this;
}
```

---

## 5. 단항 연산자 중복

### 전위 연산자 (Prefix)
```cpp
// ++c (전위 증가)
Complex& operator++() {
    real++;
    imag++;
    return *this;
}
```

### 후위 연산자 (Postfix)
```cpp
// c++ (후위 증가) - int 더미 매개변수로 구분
Complex operator++(int) {
    Complex temp = *this;  // 현재 값 저장
    real++;
    imag++;
    return temp;           // 증가 전 값 반환
}
```

> **구분법**: 후위 연산자는 `int` 더미 매개변수를 가짐

---

## 6. 입출력 연산자 중복

### << 연산자 (출력)
```cpp
class Complex {
    double real, imag;
public:
    friend ostream& operator<<(ostream &os, const Complex &c);
};

ostream& operator<<(ostream &os, const Complex &c) {
    os << c.real << " + " << c.imag << "i";
    return os;  // 연쇄 출력 가능하도록 반환
}

// 사용
Complex c(3, 4);
cout << c << endl;  // "3 + 4i"
```

### >> 연산자 (입력)
```cpp
friend istream& operator>>(istream &is, Complex &c);

istream& operator>>(istream &is, Complex &c) {
    is >> c.real >> c.imag;
    return is;
}

// 사용
Complex c;
cin >> c;  // 실수부, 허수부 입력
```

---

## 7. 인덱스 연산자 []
```cpp
class Array {
    int *data;
    int size;
public:
    Array(int n) : size(n) { data = new int[n]; }
    
    // [] 연산자 - 참조 반환으로 대입도 가능
    int& operator[](int index) {
        if (index < 0 || index >= size) {
            cout << "Index out of range!" << endl;
            exit(1);
        }
        return data[index];
    }
    
    ~Array() { delete[] data; }
};

// 사용
Array arr(5);
arr[0] = 10;        // 대입
cout << arr[0];     // 읽기
```

---

## 8. 연산자 중복 선택 가이드

| 연산자 | 권장 방식 | 이유 |
|--------|----------|------|
| `=`, `[]`, `()`, `->` | 멤버 함수 | 첫 번째 피연산자가 반드시 객체 |
| `+`, `-`, `*`, `/` | 둘 다 가능 | 교환법칙 필요시 프렌드 |
| `<<`, `>>` | 프렌드 함수 | 첫 번째 피연산자가 스트림 객체 |
| 단항 연산자 | 멤버 함수 | 피연산자가 객체 자신 |

---

## 9. 실전 예제: Point 클래스
```cpp
class Point {
    int x, y;
public:
    Point(int x = 0, int y = 0) : x(x), y(y) {}
    
    // 덧셈
    Point operator+(const Point &p) {
        return Point(x + p.x, y + p.y);
    }
    
    // 전위 ++
    Point& operator++() {
        x++; y++;
        return *this;
    }
    
    // 후위 ++
    Point operator++(int) {
        Point temp = *this;
        x++; y++;
        return temp;
    }
    
    // 비교
    bool operator==(const Point &p) {
        return (x == p.x) && (y == p.y);
    }
    
    // 출력
    friend ostream& operator<<(ostream &os, const Point &p) {
        os << "(" << p.x << ", " << p.y << ")";
        return os;
    }
};
```
