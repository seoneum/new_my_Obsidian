---
type: concept
title: Modern C++ Array 완벽 가이드
created: 2026-01-16
updated: 2026-01-18T16:42:53
author: "[[김선음]]"
status: sprout
tags:
  - concept
  - domain/cs
  - cpp
  - modern-cpp
  - vector
  - array
domain:
  - cs
---

# Modern C++ Array 완벽 가이드

> [!NOTE] 개요
> C++ 표준 배열인 `std::vector`를 활용한 Modern C++ 스타일의 배열 프로그래밍 가이드입니다.

---

## 1. std::vector 기본 사용법

### 1.1 Vector란?

- **동적 배열** - 크기가 자동으로 조절됨
- **길이 정보 내장** - `v.size()`로 크기 확인 가능퓨전
- **연속된 메모리(Heap)** 에 저장

### 1.2 Vector 선언 방법

```cpp
// 크기 n으로 선언 (자동 초기화)
std::vector<자료형> 이름(n);

// 특정 값으로 초기화
std::vector<int> v(크기, 특정값);

// 직접 값 대입
std::vector<int> v = {1, 2, 3, 4};

// 다른 벡터 복사
std::vector<int> v(다른벡터);
```

### 1.3 주요 멤버 함수

| 함수 | 설명 |
|:-----|:-----|
| `push_back(값)` | 맨 뒤에 값 추가 |
| `emplace_back(값)` | push_back과 동일 (더 빠름) |
| `pop_back()` | 맨 뒤 값 삭제 (리턴 없음) |
| `clear()` | 모든 원소 삭제 |
| `resize(n)` | 크기를 n으로 변경 |
| `size()` | 현재 크기 반환 |

### 1.4 범위 기반 for문으로 입력받기

```cpp
// 참조 연산자 &를 사용하여 직접 값 수정
for (auto& x : v) {
    std::cin >> x;
}
```

> [!TIP] 참조(Reference)란?
> - 변수의 **별명**을 설정하는 것
> - 주소 값을 가지므로 **복사 없이** 원본 수정 가능

---

## 2. std::ranges 알고리즘

> [!IMPORTANT] 
> 복잡한 iterator 대신 `std::ranges`를 사용하면 더 간결한 코드 작성이 가능합니다.

### 2.1 주요 함수

```cpp
// 정렬
std::ranges::sort(v);

// 최대/최소값
std::ranges::max(v);
std::ranges::min(v);

// 특정 값 개수 세기
std::ranges::count(v, 값);

// 뒤집기
std::ranges::reverse(v);

// 가장 큰/작은 원소의 위치(iterator) 반환
std::ranges::max_element(v);
std::ranges::min_element(v);
```

---

## 3. std::views 파이프라인

### 3.1 파이프라인 문법

데이터를 `|` 기호를 통해 **순차적으로 가공**합니다.

```
원본 | 뷰 어댑터1 | 뷰 어댑터2 | ...
```

**구성 요소:**
- **데이터 제공**: `std::vector`, `std::array`, `std::views::iota` 등
- **뷰 어댑터**: `filter`, `transform`, `take` 등
- **Sink (소비)**: `for`, `ranges::copy`, `to<vector>` 등

### 3.2 주요 뷰 어댑터

| 어댑터 | 기능 | 예시 |
|:-------|:-----|:-----|
| `filter(조건)` | 참인 것만 통과 | 조건 필터링 |
| `transform(함수)` | 값을 변형 | 연산 적용 |
| `take(n)` | 앞에서 n개 가져옴 | 처음 n개 선택 |
| `drop(n)` | 앞에서 n개 버림 | 처음 n개 제외 |
| `reverse` | 순서 거꾸로 | 역순 정렬 |
| `join` | 이중 배열을 1차원으로 합침 | 평탄화 |
| `iota(start, end)` | start부터 end 직전까지 정수 생성 | 반복문 대체 |

### 3.3 filter 문법

```cpp
[외부변수](검사할_숫자) { return 조건; }
```

---

## 4. 유용한 STL 함수

### 4.1 std::fill - 범위 채우기

```cpp
#include <algorithm>

// v의 특정 범위를 값으로 채우기
std::fill(v.begin() + i, v.begin() + j, 값);
```

### 4.2 std::iota - 연속 정수로 채우기

```cpp
#include <numeric>

// v를 1, 2, 3, ... 으로 채우기
std::iota(v.begin(), v.end(), 시작값);
```

### 4.3 std::swap - 값 교환

```cpp
#include <algorithm>

std::swap(a, b);  // a와 b의 값 교환
```

### 4.4 std::distance - 거리 계산

```cpp
#include <iterator>

// 두 iterator 사이의 거리 반환
int idx = std::distance(v.begin(), it);
```

---

## 5. 백준 문제 풀이

### 5.1 #10807 - 개수 세기 (기초)

> 배열에서 특정 값의 개수를 찾는 문제

```cpp
#include <algorithm>
#include <iostream>
#include <vector>

auto main() -> int {
    std::cin.tie(nullptr)->sync_with_stdio(false);

    int n, target;
    if (std::cin >> n) {
        std::vector<int> v(n);
        
        for (auto& x : v)
            std::cin >> x;
        
        if (std::cin >> target) {
            std::cout << std::ranges::count(v, target);
        }
    }
}
```

**핵심 포인트:**
- `std::ranges::count(v, target)` 으로 간단히 개수 세기

---

### 5.2 #10871 - X보다 작은 수

> 배열에서 X보다 작은 값만 필터링하여 출력

```cpp
#include <iostream>
#include <ranges>
#include <vector>

auto main() -> int {
    std::cin.tie(nullptr)->sync_with_stdio(false);
    
    int n, x;
    if (std::cin >> n >> x) {
        std::vector<int> a(n);
        
        for (auto& y : a)
            std::cin >> y;
        
        // 파이프라인으로 x보다 작은 값 필터링
        auto small = a | std::views::filter([x](int i) { return i < x; });
        
        for (int result : small) {
            std::cout << result << " ";
        }
    }
    return 0;
}
```

**핵심 포인트:**
- `std::views::filter`로 조건에 맞는 값만 추출
- 람다식 `[x](int i) { return i < x; }`로 조건 정의

---

### 5.3 #10818 - 최소, 최대

> 배열의 최솟값과 최댓값 출력

```cpp
#include <algorithm>
#include <iostream>
#include <vector>

auto main() -> int {
    std::cin.tie(nullptr)->sync_with_stdio(false);

    int n;
    if (std::cin >> n) {
        std::vector<int> v(n);
        
        for (auto& x : v) {
            std::cin >> x;
        }
        
        std::ranges::sort(v);
        std::cout << std::ranges::min(v) << " " << std::ranges::max(v);
    }
}
```

**핵심 포인트:**
- `std::ranges::min/max`로 간단히 최솟값/최댓값 구하기

---

### 5.4 #2562 - 최댓값과 위치

> 가장 큰 값과 그 인덱스(1-based) 출력

```cpp
#include <algorithm>
#include <iostream>
#include <iterator>
#include <vector>

auto main() -> int {
    std::cin.tie(nullptr)->sync_with_stdio(false);

    std::vector<int> v(9);
    for (auto& x : v) {
        std::cin >> x;
    }
    
    // 최댓값의 위치(iterator) 반환
    auto it = std::ranges::max_element(v);
    
    // 역참조로 값 출력
    std::cout << *it << "\n";
    
    // distance로 인덱스 계산 (+1은 1-based 변환)
    std::cout << std::distance(v.begin(), it) + 1;
}
```

**핵심 포인트:**
- `std::ranges::max_element` → 최댓값의 **iterator** 반환
- `*it` → iterator가 가리키는 **값** 출력
- `std::distance` → 두 iterator 사이의 **거리** 계산

---

### 5.5 #10810 - 공 넣기

> 바구니에 공을 넣고 결과 출력 (덮어쓰기 방식)

```cpp
#include <algorithm>
#include <iostream>
#include <ranges>
#include <vector>

auto main() -> int {
    int n, m;
    if (std::cin >> n >> m) {
        std::vector<int> v(n);
        
        int i, j, k;
        for (auto _ : std::views::iota(0, m)) {
            if (std::cin >> i >> j >> k) {
                // i~j 범위를 k로 채우기
                std::fill(v.begin() + i - 1, v.begin() + j, k);
            }
        }
        
        for (int ball : v) {
            std::cout << ball << " ";
        }
    }
}
```

**핵심 포인트:**
- `std::views::iota(0, m)` → 0부터 m-1까지 반복
- `std::fill` → 특정 범위를 값으로 채우기

---

### 5.6 #10813 - 공 바꾸기
# 제목
> 바구니 두 개의 공을 교환

```cpp
#include <algorithm>
#include <iostream>
#include <numeric>
#include <ranges>
#include <vector>

auto main() -> int {
    std::cin.tie(nullptr)->sync_with_stdio(false);
    
    int n, m;
    if (std::cin >> n >> m) {
        std::vector<int> v(n);
        
        // 1, 2, 3, ... 으로 초기화
        std::iota(v.begin(), v.end(), 1);
        
        int i, j;
        for (auto _ : std::views::iota(0, m)) {
            if (std::cin >> i >> j) {
                // 0-based 인덱스로 변환 후 교환
                std::swap(v[i - 1], v[j - 1]);
            }
        }
        
        for (int ball : v) {
            std::cout << ball << " ";
        }
    }
}
```

**핵심 포인트:**
- `std::iota` → 연속 정수로 배열 초기화
- `std::swap` → 두 값 교환

---

### 5.7 #5597 - 과제 안 낸 동명이

> 제출하지 않은 학생 2명의 번호 찾기

```cpp
#include <iostream>
#include <ranges>
#include <vector>

auto main() -> int {
    std::cin.tie(nullptr)->sync_with_stdio(false);
    
    // 인덱스 0은 사용하지 않음 (1~30번 학생)
    std::vector<bool> submitted(31, false);
    
    // 28명의 제출자 번호 입력
    for (auto _ : std::views::iota(0, 28)) {
        int n;
        std::cin >> n;
        submitted[n] = true;
    }
    
    // 제출하지 않은 학생 번호 출력
    for (int i : std::views::iota(1, 31)) {
        if (!submitted[i]) {
            std::cout << i << "\n";
        }
    }
    return 0;
}
```

**핵심 포인트:**
- `std::vector<bool>` → 체크리스트로 활용
- `std::views::iota(1, 31)` → 1부터 30까지 순회

---

## 6. 고급 기능 - Modern C++ 핵심 개념

> [!TIP] Modern C++ (C++20/23)의 핵심
> **"안전함, 효율성, 그리고 표현력"** - `span`으로 자르고, `ranges`로 조작하고, `views`로 걸러내는 것이 Modern C++ PS의 3박자입니다.

---

### 6.1 std::span (메모리를 보는 안경) 👓

> 연속된 메모리 공간을 **복사 없이** 가리키기만 하는 객체 (C++20)

**내부 구조:**
- `T* ptr` (시작 주소)
- `size_t size` (길이)

**왜 쓰는가?**
- **Zero-Copy:** 함수에 `vector`를 통째로 넘기면 복사 비용이 들지만, `span`은 주소만 넘기므로 비용이 0에 가깝습니다.
- **유연함:** `std::vector`든, C배열(`int arr[]`)이든, `std::array`든 가리지 않고 다 받을 수 있습니다.

```cpp
#include <span>

void print_span(std::span<int> s) { // 벡터든 배열이든 다 와라
    s[0] = 99; // 원본이 수정됨 (참조의 성격)
}
```

---

### 6.2 subspan (부분 잘라내기) 🍰

> `span`의 가장 강력한 기능 - 특정 구간만 잘라서 참조

**문법:**
```cpp
s.subspan(시작인덱스, 개수)
```

**⚠️ 주의할 점:**
1. **두 번째 인자는 '끝 인덱스'가 아니라 '개수(Length)'입니다.**
   - i번부터 j번까지라면 개수는 `j - i + 1`

2. **리턴값을 무시하면 안 됩니다 (`nodiscard`).**
   - `s.subspan(...)`만 쓴다고 `s`가 줄어드는 게 아님
   - 잘린 **새로운 span**을 리턴하므로, 그걸 받아서 함수에 전달

**사용 예시:**
```cpp
// v의 i~j 구간을 잘라서 -> 뒤집기 함수에 바로 전달
std::ranges::reverse(std::span(v).subspan(i, j - i + 1));
```

---

### 6.3 std::ranges 알고리즘 (행동대장) 🛠️

> 과거의 STL 알고리즘을 업그레이드한 버전

**헤더:** `#include <algorithm>`

**차이점:**

| Old Style | Modern Style |
|:----------|:-------------|
| `std::sort(v.begin(), v.end())` | `std::ranges::sort(v)` |

**특징:**
- `span`이나 `subspan`과 결합했을 때 강력한 시너지
- "이 구간만 뒤집어라" 같은 명령이 아주 깔끔해짐

---

### 6.4 std::views와 파이프라인 (계획가) 🌊

> 데이터를 즉시 계산하지 않고, **"어떻게 다룰지 계획(View)"** 만 세우는 기법 (지연 평가, Lazy Evaluation)

**헤더:** `#include <ranges>`

**주요 View:**

| View | 설명 | 주의 |
|:-----|:-----|:-----|
| `views::iota(Start, End)` | Start부터 End **전까지** 숫자 생성 | 끝 숫자 미포함! |
| `views::filter(조건함수)` | 조건이 `true`인 데이터만 통과 | 거름망 역할 |
| `views::transform(함수)` | 각 요소에 함수 적용 | 변형 |

**파이프(`|`) 문법:**
```cpp
// 1~30 숫자 중 -> 짝수만 골라서 -> 제곱한다
auto result = views::iota(1, 31) 
            | views::filter([](int n){ return n % 2 == 0; })
            | views::transform([](int n){ return n * n; });
```

---

### 6.5 유니크(Unique) 처리 전략 🔢

> 중복을 없애거나, 없는 숫자를 찾을 때 사용하는 전략들

**1. `std::set` (집합):**
- 가장 Modern하고 직관적
- 넣기만 하면 알아서 중복 제거

```cpp
#include <set>
std::set<int> s;
for (int x : v) s.insert(x % 42);  // 중복 자동 제거
std::cout << s.size();  // 유니크한 개수
```

**2. `std::vector<bool>` (체크리스트):**
- 가장 빠르고 실무적인 PS 테크닉
- "이 번호가 있었나?" 체크용 출석부

```cpp
std::vector<bool> checked(31, false);
checked[n] = true;  // n번 체크
```

---

### 6.6 반복자와 인덱스 (`begin` vs `end`) 📍

> 메모리 주소를 다룰 때의 기본 규칙

| 반복자 | 의미 |
|:-------|:-----|
| `v.begin()` | 0번 인덱스 (시작점) |
| `v.end()` | **마지막 요소의 다음 칸** (끝난 지점, 절대 접근 금지 🚫) |

**거리 계산:**
- i번째 요소의 위치 = `v.begin() + i`
- i번째부터 j번째까지의 범위 = `v.begin() + i` 부터 `v.begin() + j + 1`
- 또는 `subspan`의 길이로 제어: `subspan(i, j - i + 1)`

---

## 7. 자주 사용되는 코드 패턴

### 7.1 입출력 최적화 (경쟁 프로그래밍)

```cpp
std::cin.tie(nullptr)->sync_with_stdio(false);
```

### 7.2 필수 헤더

```cpp
#include <algorithm>   // sort, fill, swap
#include <iostream>    // cin, cout
#include <iterator>    // distance
#include <numeric>     // iota
#include <ranges>      // views, ranges
#include <set>         // set (중복 제거)
#include <span>        // span (C++20)
#include <vector>      // vector
```

---

## 💡 최종 요약

> **"C 스타일의 인덱스 노가다"** 에서 벗어나, **"데이터의 구간(Span)과 흐름(Ranges/Views)을 제어하는 Modern C++"** 로!

| 단계 | 도구 | 역할 |
|:-----|:-----|:-----|
| 1️⃣ | `span` / `subspan` | 데이터 구간 잘라내기 |
| 2️⃣ | `ranges` 알고리즘 | 구간 조작 (정렬, 뒤집기 등) |
| 3️⃣ | `views` | 데이터 걸러내기 (필터, 변형) |

---

## 참고 자료

- 원본 노트: [[N - Modern C++ baekjoon Array_part]]
- 관련 노트: [[N - Modern C++ baekjoon while_part]]
- [[C - Modern C++ Day 1]]
- [[C - Modern C++ 궁금증 모음]]

