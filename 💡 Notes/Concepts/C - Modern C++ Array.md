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

## 6. 고급 기능

### 6.1 std::span

> 메모리 복사 없이 배열의 **특정 부분만 참조**하는 뷰

```cpp
#include <span>

std::vector<int> v = {1, 2, 3, 4, 5};
std::span<int> partial(v.data() + 1, 3);  // {2, 3, 4} 참조
```

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
#include <vector>      // vector
```

---

## 참고 자료

- 원본 노트: [[N - Modern C++ baekjoon Array_part]]
- 관련 노트: [[N - Modern C++ baekjoon while_part]]
- [[C - Modern C++ Day 1]]
- [[C - Modern C++ 궁금증 모음]]
