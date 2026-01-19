# 상속 (Inheritance)

## 1. 상속의 개념

### 정의
- 기존 클래스의 속성과 기능을 물려받아 **새로운 클래스**를 정의
- 코드 재사용성과 확장성 향상

### 용어
| 용어 | 설명 |
|------|------|
| **기본 클래스 (Base Class)** | 부모 클래스, 상속해주는 클래스 |
| **파생 클래스 (Derived Class)** | 자식 클래스, 상속받는 클래스 |

### 문법
```cpp
class DerivedClass : public BaseClass {
    // 추가 멤버 선언
};
```

---

## 2. 상속 관계의 종류

### IS-A 관계 (상속)
- "~은 ~이다" 관계
- UML에서 **빈 삼각형** 화살표

```cpp
class Shape { };
class Circle : public Shape { };  // Circle IS-A Shape
```

### HAS-A 관계 (포함/컴포지션)
- "~은 ~을 가지고 있다" 관계
- UML에서 **마름모** 표시

```cpp
class Engine { };
class Car {
    Engine engine;  // Car HAS-A Engine
};
```

---

## 3. 접근 지정자와 상속

### protected 접근 지정자
- `private`와 `public`의 중간
- **클래스 내부**, **자식 클래스**, **friend**에서 접근 가능

```cpp
class Base {
private:
    int privateVar;    // Base 내부에서만
protected:
    int protectedVar;  // Base + 파생 클래스에서
public:
    int publicVar;     // 어디서든
};

class Derived : public Base {
    void func() {
        // privateVar = 10;   // ❌ 접근 불가
        protectedVar = 10;    // ✅ 접근 가능
        publicVar = 10;       // ✅ 접근 가능
    }
};
```

### 상속 접근 지정자
```cpp
class Derived : public Base { };    // 가장 일반적
class Derived : protected Base { };
class Derived : private Base { };   // 디폴트
```

| 상속 방식 | Base의 public | Base의 protected | Base의 private |
|----------|---------------|------------------|----------------|
| public | public | protected | 접근불가 |
| protected | protected | protected | 접근불가 |
| private | private | private | 접근불가 |

---

## 4. 생성자와 소멸자 호출 순서

### 생성 순서
**Base → Derived** (부모 먼저, 자식 나중)

### 소멸 순서
**Derived → Base** (자식 먼저, 부모 나중)

```cpp
class Base {
public:
    Base() { cout << "Base 생성자" << endl; }
    ~Base() { cout << "Base 소멸자" << endl; }
};

class Derived : public Base {
public:
    Derived() { cout << "Derived 생성자" << endl; }
    ~Derived() { cout << "Derived 소멸자" << endl; }
};

int main() {
    Derived d;
}
// 출력:
// Base 생성자
// Derived 생성자
// Derived 소멸자
// Base 소멸자
```

### 부모 생성자에 인자 전달
```cpp
class Base {
public:
    Base(int x) { cout << "Base: " << x << endl; }
};

class Derived : public Base {
public:
    // 멤버 초기화 리스트로 부모 생성자 호출
    Derived(int x, int y) : Base(x) {
        cout << "Derived: " << y << endl;
    }
};
```

---

## 5. 업캐스팅과 다운캐스팅

### 업캐스팅 (Upcasting)
- **자식 객체**를 **부모 포인터/참조**로 가리킴
- 자동으로 수행 (암시적 형변환)
- 자식의 고유 멤버에는 접근 불가

```cpp
class Shape {
public:
    void draw() { cout << "Shape" << endl; }
};

class Circle : public Shape {
public:
    void draw() { cout << "Circle" << endl; }
    int radius;
};

int main() {
    Circle c;
    Shape *pShape = &c;  // 업캐스팅
    
    pShape->draw();      // "Shape" 출력 (Shape의 draw 호출)
    // pShape->radius;   // ❌ 에러! Shape에는 radius가 없음
}
```

### 다운캐스팅 (Downcasting)
- **부모 포인터**를 **자식 포인터**로 변환
- 명시적 형변환 필요
- 잘못 사용하면 위험!

```cpp
Shape *pShape = new Circle();
Circle *pCircle = (Circle*)pShape;  // 다운캐스팅
pCircle->radius = 10;  // ✅ 가능
```

---

## 6. 다중 상속

### 문법
```cpp
class Derived : public Base1, public Base2 {
    // Base1과 Base2 모두 상속
};
```

### 다이아몬드 문제
```
      Animal
      /    \
   Tiger  Lion
      \    /
       Liger
```

```cpp
class Animal {
public:
    int age;
};

class Tiger : public Animal { };
class Lion : public Animal { };

class Liger : public Tiger, public Lion { };
// Liger는 Animal을 두 번 상속받음!
// liger.age가 어느 경로인지 모호함
```

### 가상 상속으로 해결
```cpp
class Tiger : virtual public Animal { };
class Lion : virtual public Animal { };

class Liger : public Tiger, public Lion { };
// Animal은 한 번만 상속됨
```

---

## 7. 함수 오버라이딩 vs 오버로딩

### 오버로딩 (Overloading)
- **같은 클래스** 내에서
- 함수 이름은 같지만 **매개변수가 다름**

```cpp
class Calculator {
public:
    int add(int a, int b) { return a + b; }
    double add(double a, double b) { return a + b; }  // 오버로딩
};
```

### 오버라이딩 (Overriding)
- **상속 관계**에서
- 부모의 함수를 자식에서 **재정의**
- 함수 이름, 리턴 타입, 매개변수 **모두 동일**

```cpp
class Shape {
public:
    void draw() { cout << "Shape" << endl; }
};

class Circle : public Shape {
public:
    void draw() { cout << "Circle" << endl; }  // 오버라이딩
};
```

### 비교 정리

| 구분 | 오버로딩 | 오버라이딩 |
|------|----------|------------|
| 위치 | 같은 클래스 | 상속 관계 |
| 함수 이름 | 동일 | 동일 |
| 매개변수 | 다름 | 동일 |
| 리턴 타입 | 상관없음 | 동일 |
| 바인딩 | 정적 (컴파일 타임) | 동적 (virtual 사용 시) |

---

## 8. 상속 설계 예제

```cpp
// 기본 클래스
class Employee {
protected:
    string name;
    int salary;
public:
    Employee(string n, int s) : name(n), salary(s) {}
    
    virtual void printInfo() {
        cout << "Name: " << name << ", Salary: " << salary << endl;
    }
};

// 파생 클래스
class Manager : public Employee {
private:
    int bonus;
public:
    Manager(string n, int s, int b) : Employee(n, s), bonus(b) {}
    
    void printInfo() override {  // 오버라이딩
        cout << "Manager: " << name 
             << ", Salary: " << salary 
             << ", Bonus: " << bonus << endl;
    }
};

class Developer : public Employee {
private:
    string language;
public:
    Developer(string n, int s, string lang) 
        : Employee(n, s), language(lang) {}
    
    void printInfo() override {
        cout << "Developer: " << name 
             << ", Language: " << language << endl;
    }
};
```
