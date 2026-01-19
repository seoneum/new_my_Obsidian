# 포인터와 메모리 관리

## 1. 포인터 기초

### 개념
- **포인터**: 메모리 주소를 저장하는 변수
- 모든 포인터 변수의 크기는 **4바이트** (32비트 시스템) 또는 8바이트 (64비트)

### 선언과 사용
```cpp
int x = 10;
int *ptr = &x;       // ptr은 x의 주소를 저장

cout << ptr;         // 주소 출력: 0x7fff...
cout << *ptr;        // 역참조: 10 출력
*ptr = 20;           // x의 값이 20으로 변경
```

### 연산자 정리
| 연산자 | 위치 | 의미 |
|--------|------|------|
| `&` | 변수 앞 | 주소 연산자 - 변수의 주소 반환 |
| `*` | 선언 시 | 포인터 변수 선언 |
| `*` | 사용 시 | 역참조 - 주소가 가리키는 값 |

### NULL 포인터
```cpp
int *ptr = NULL;    // 또는
int *ptr = nullptr; // C++11 이후 권장
```
- 정의되지 않은 상태를 명시
- NULL 반환으로 에러 판단 가능

---

## 2. const와 포인터

### const의 위치에 따른 의미
```cpp
const int *ptr = &x;       // 가리키는 값 상수화 (값 변경 불가)
int const *ptr = &x;       // 위와 동일
int *const ptr = &x;       // 포인터 자체 상수화 (다른 주소 대입 불가)
const int *const ptr = &x; // 둘 다 상수화
```

### 멤버함수의 const
```cpp
class MyClass {
    int getValue() const;  // 함수가 객체를 수정하지 않음을 보장
};

// 구현
int MyClass::getValue() const {
    // this 객체의 멤버 변수 수정 불가
    return value;
}
```

> **핵심**: 
> - 변수 앞 `const` → 데이터 보호
> - 함수 뒤 `const` → 호출하는 객체 자신을 보호

---

## 3. 객체 포인터

### 선언과 접근
```cpp
Circle c;
Circle *pCircle = &c;

// 멤버 접근 방법 2가지
(*pCircle).radius = 10;    // 역참조 후 접근
pCircle->radius = 10;      // 화살표 연산자 (권장)

pCircle->getArea();        // 멤버 함수 호출
```

| 연산자 | 사용법 | 설명 |
|--------|--------|------|
| `->` | `p->member` | 포인터가 가리키는 객체의 멤버에 직접 접근 |
| `*` + `.` | `(*p).member` | 역참조 후 멤버 접근 |

---

## 4. 객체 배열

### 정적 배열
```cpp
Circle circles[3];                          // 기본 생성자 3번 호출
Circle circles[3] = {Circle(1), Circle(2), Circle(3)};  // 초기화

// 2차원 배열
Circle grid[2][3];  // 2행 3열
```

> **주의**: 매개변수 있는 생성자만 있고 기본 생성자가 없으면 `Circle arr[3];`은 **컴파일 오류**!

### 배열과 포인터 관계
```cpp
int arr[] = {1, 2, 3};
// arr == &arr[0]  → 배열 이름은 첫 요소의 주소(포인터 상수)
// *arr == arr[0]  → 첫 요소 값
```

### 포인터 연산
```cpp
int *p = arr;
p++;      // 다음 요소로 이동 (4바이트 증가)
*(p+2)    // p[2]와 동일
```
- `+`, `-`, `++`, `--` 연산만 가능

---

## 5. 동적 메모리 할당

### 정적 vs 동적 할당
| 구분 | 정적 할당 | 동적 할당 |
|------|----------|----------|
| 방식 | 변수 선언 | `new`/`delete` |
| 위치 | 스택 | 힙 |
| 크기 | 컴파일 시 결정 | 런타임 시 결정 |
| 소멸 | 자동 | 수동 (`delete` 필요) |

### 기본 문법
```cpp
// 단일 변수
int *ptr = new int;           // 할당
int *ptr = new int(10);       // 할당 + 초기화
delete ptr;                    // 해제

// 배열
int *arr = new int[10];        // 배열 할당
delete[] arr;                  // 배열 해제 ([] 필수!)
```

### 객체의 동적 생성
```cpp
// 단일 객체
Circle *pCircle = new Circle;           // 기본 생성자
Circle *pCircle = new Circle(10);       // 매개변수 생성자
delete pCircle;

// 객체 배열
Circle *circles = new Circle[5];        // 기본 생성자 5번 호출
delete[] circles;                        // 소멸자 5번 호출
```

> **중요**: 배열은 반드시 `delete[]`로 해제! 그렇지 않으면 메모리 누수 발생

---

## 6. this 포인터

### 개념
- 멤버 함수 내에서 **현재 객체 자신**을 가리키는 포인터
- 컴파일러가 자동 선언 (개발자가 선언하지 않음)

### 용도
```cpp
class Circle {
    int radius;
public:
    // 1. 매개변수와 멤버변수 이름이 같을 때 구분
    void setRadius(int radius) {
        this->radius = radius;  // this->멤버변수 = 매개변수
    }
    
    // 2. 자기 자신 반환 (메서드 체이닝)
    Circle& grow() {
        radius++;
        return *this;
    }
};
```

### 사용 불가 상황
- 멤버 함수가 아닌 함수
- `static` 멤버 함수 (객체 생성 전 호출 가능하므로)

---

## 7. 참조 변수 (Reference)

### 개념
- 이미 존재하는 변수에 대한 **별명(alias)**
- 새로운 메모리 공간 할당 없음
- **선언과 동시에 반드시 초기화**

### 문법
```cpp
int n = 10;
int &refn = n;     // refn은 n의 별명

refn = 20;         // n도 20으로 변경
cout << n;         // 20
```

### 특징
- 한 번 참조하면 대상 변경 불가
- 상수는 참조 불가
- 없는 대상 참조 불가

### 포인터 vs 참조
| 구분 | 포인터 | 참조 |
|------|--------|------|
| 문법 | `*`, `->` 필요 | 일반 변수처럼 사용 |
| NULL | 가능 | 불가능 |
| 대상 변경 | 가능 | 불가능 |
| 초기화 | 선택 | 필수 |

---

## 8. 문자열

### C-스타일 문자열 (C-string)
```cpp
char str[20] = "Hello";  // 마지막에 '\0' 자동 추가
// 실제 저장: ['H']['e']['l']['l']['o']['\0']...

// 주요 함수 (<cstring>)
strlen(str);            // 길이 (5, '\0' 제외)
strcpy(dest, src);      // 복사
strcat(str1, str2);     // 연결
strcmp(str1, str2);     // 비교 (같으면 0)
```

### C++ string 클래스
```cpp
#include <string>

string str = "Hello";

// 기본 함수
str.length();          // 길이
str.size();            // 길이 (동일)
str.capacity();        // 할당된 메모리 크기
str.empty();           // 비어있는지

// 조작
str.append(" World");  // 뒤에 추가
str.substr(0, 3);      // 부분 문자열 "Hel"
str.find("lo");        // 위치 찾기 (3)
str.replace(0, 2, "XX"); // 교체

// 입력
getline(cin, str);     // 공백 포함 한 줄 입력
```

### 문자열 변환
```cpp
string numStr = "123";
int num = stoi(numStr);    // string → int (C++11)
// atoi()는 C-style, 지금은 stoi() 권장
```

### 동적 생성
```cpp
string *pStr = new string("Hello");
delete pStr;
```
