# 가상함수와 추상클래스

## 1. 바인딩 (Binding)

### 정적 바인딩 (Static Binding)
- **컴파일 타임**에 함수 호출이 결정
- 일반 함수, 오버로딩된 함수에 적용
- 포인터의 **타입**에 따라 함수 결정

### 동적 바인딩 (Dynamic Binding)
- **런타임**에 함수 호출이 결정
- `virtual` 함수에 적용
- 포인터가 가리키는 **실제 객체**에 따라 함수 결정

---

## 2. 가상 함수 (Virtual Function)

### 문제 상황
```cpp
class Shape {
public:
    void draw() { cout << "Shape" << endl; }
};

class Circle : public Shape {
public:
    void draw() { cout << "Circle" << endl; }
};

int main() {
    Circle c;
    Shape *pShape = &c;  // 업캐스팅
    pShape->draw();      // "Shape" 출력 - 정적 바인딩!
}
```

### virtual로 해결
```cpp
class Shape {
public:
    virtual void draw() { cout << "Shape" << endl; }
};

class Circle : public Shape {
public:
    void draw() { cout << "Circle" << endl; }  // 자동으로 virtual
};

int main() {
    Circle c;
    Shape *pShape = &c;
    pShape->draw();      // "Circle" 출력 - 동적 바인딩!
}
```

### 특징
1. `virtual` 키워드로 선언
2. 오버라이딩하면 자식에서도 자동으로 virtual
3. 부모 포인터로 자식 객체를 가리킬 때 **실제 객체의 함수** 호출

---

## 3. 가상 함수 동작 원리

### 가상 함수 테이블 (vtable)
- 가상 함수를 가진 클래스는 vtable을 가짐
- vtable에는 가상 함수들의 주소가 저장
- 객체마다 vtable을 가리키는 **vptr** 포함

```cpp
class Shape {
    // vptr (숨겨진 포인터) → Shape의 vtable
    virtual void draw();
};

class Circle : public Shape {
    // vptr → Circle의 vtable (draw가 오버라이딩됨)
    void draw() override;
};
```

---

## 4. 오버라이딩 규칙

### 오버라이딩 조건
1. 함수 이름 동일
2. 리턴 타입 동일
3. 매개변수 타입과 개수 동일

### override 키워드 (C++11)
```cpp
class Shape {
public:
    virtual void draw() { }
};

class Circle : public Shape {
public:
    void draw() override { }  // 명시적 오버라이딩 선언
    // void draw(int x) override { }  // ❌ 컴파일 에러! 시그니처 다름
};
```

> `override`를 사용하면 실수로 새 함수를 만드는 것을 방지

---

## 5. 순수 가상 함수 (Pure Virtual Function)

### 개념
- 함수의 **선언만** 있고 구현은 없음
- 자식 클래스에서 **반드시 구현**해야 함
- 인터페이스 역할

### 문법
```cpp
class Shape {
public:
    virtual void draw() = 0;  // 순수 가상 함수
};
```

### 특징
- `= 0`으로 표시
- 해당 클래스는 **추상 클래스**가 됨
- 자식 클래스가 구현하지 않으면 자식도 추상 클래스

---

## 6. 추상 클래스 (Abstract Class)

### 정의
- **순수 가상 함수를 하나 이상** 포함한 클래스
- **객체 생성 불가능**
- 포인터 선언은 가능

```cpp
class Shape {  // 추상 클래스
public:
    virtual void draw() = 0;
    virtual double getArea() = 0;
};

// Shape s;  // ❌ 에러! 객체 생성 불가
Shape *pShape;  // ✅ 포인터 선언은 가능

class Circle : public Shape {
    double radius;
public:
    void draw() override { cout << "Circle" << endl; }
    double getArea() override { return 3.14 * radius * radius; }
};

Circle c;  // ✅ 모든 순수 가상 함수 구현했으므로 가능
```

### 용도
1. **인터페이스 정의**: 파생 클래스가 구현해야 할 함수 명세
2. **설계 강제**: 특정 함수의 구현을 강제
3. **다형성 활용**: 부모 포인터로 다양한 자식 객체 처리

---

## 7. 가상 소멸자 (Virtual Destructor)

### 문제 상황
```cpp
class Base {
public:
    ~Base() { cout << "Base 소멸자" << endl; }
};

class Derived : public Base {
    int *data;
public:
    Derived() { data = new int[100]; }
    ~Derived() { 
        delete[] data;
        cout << "Derived 소멸자" << endl; 
    }
};

int main() {
    Base *p = new Derived();
    delete p;  // Base 소멸자만 호출! → 메모리 누수!
}
```

### virtual 소멸자로 해결
```cpp
class Base {
public:
    virtual ~Base() { cout << "Base 소멸자" << endl; }
};

class Derived : public Base {
    int *data;
public:
    Derived() { data = new int[100]; }
    ~Derived() override { 
        delete[] data;
        cout << "Derived 소멸자" << endl; 
    }
};

int main() {
    Base *p = new Derived();
    delete p;  
    // Derived 소멸자 호출 → Base 소멸자 호출 (정상!)
}
```

> **규칙**: 상속 관계의 기본 클래스는 **반드시 가상 소멸자**를 선언!

---

## 8. 다형성 활용 예제

```cpp
#include <iostream>
#include <vector>
using namespace std;

// 추상 클래스
class Shape {
public:
    virtual void draw() = 0;
    virtual double getArea() = 0;
    virtual ~Shape() {}
};

class Circle : public Shape {
    double radius;
public:
    Circle(double r) : radius(r) {}
    void draw() override { cout << "○ Circle (r=" << radius << ")" << endl; }
    double getArea() override { return 3.14159 * radius * radius; }
};

class Rectangle : public Shape {
    double width, height;
public:
    Rectangle(double w, double h) : width(w), height(h) {}
    void draw() override { cout << "□ Rectangle (" << width << "x" << height << ")" << endl; }
    double getArea() override { return width * height; }
};

class Triangle : public Shape {
    double base, height;
public:
    Triangle(double b, double h) : base(b), height(h) {}
    void draw() override { cout << "△ Triangle" << endl; }
    double getArea() override { return 0.5 * base * height; }
};

int main() {
    vector<Shape*> shapes;
    shapes.push_back(new Circle(5));
    shapes.push_back(new Rectangle(4, 6));
    shapes.push_back(new Triangle(3, 4));
    
    // 다형성: 같은 코드로 다양한 객체 처리
    for (Shape* s : shapes) {
        s->draw();
        cout << "  Area: " << s->getArea() << endl;
    }
    
    // 메모리 해제
    for (Shape* s : shapes) {
        delete s;
    }
    
    return 0;
}
```

**출력:**
```
○ Circle (r=5)
  Area: 78.5398
□ Rectangle (4x6)
  Area: 24
△ Triangle
  Area: 6
```

---

## 9. 정리: 가상 함수 vs 순수 가상 함수

| 구분 | 가상 함수 | 순수 가상 함수 |
|------|----------|---------------|
| 선언 | `virtual void func()` | `virtual void func() = 0` |
| 구현 | 있음 | 없음 |
| 오버라이딩 | 선택 | 필수 |
| 클래스 | 일반 클래스 | 추상 클래스 |
| 객체 생성 | 가능 | 불가능 |

---

## 10. 시험 핵심 체크리스트

- [ ] 오버로딩 vs 오버라이딩 차이 설명 가능
- [ ] virtual 키워드의 역할 이해
- [ ] 순수 가상 함수 문법: `= 0`
- [ ] 추상 클래스의 특징과 용도
- [ ] 가상 소멸자가 필요한 이유
- [ ] 동적 바인딩 예제 코드 작성 가능
