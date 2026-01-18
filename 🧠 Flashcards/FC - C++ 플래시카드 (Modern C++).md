---
type: flashcard
title: FC - C++ 플래시카드 (Modern C++)
created: 2026-01-17
updated: 2026-01-18T16:42:53
group: SE
status: [[🌿Sprout]]
tags:
  - flashcards
  - cpp
  - modern-cpp
  - algorithm
migrated_from: CMDS/200. CMDS/220. Merge/222. FlashCard/FC - C++ 플래시카드 (Modern C++).md
domain:
  - cs
cmds: inbox
---

# C++ 플래시카드 (Modern C++)

#flashcards/cpp

## 1. Modern C++ 기본 문법

Modern C++ 스타일 main 함수 선언 형식?
?
```cpp
auto main() -> int { return 0; }
```
auto: placeholder, -> int: trailing return type

범위 기반 for문(Range-based For Loop) 문법?
?
```cpp
for (데이터타입 변수명 : 컨테이너or뷰) { }
```
배열, 벡터, **뷰**까지 순회 가능

람다 표현식(Lambda Expression) 문법?
?
```cpp
[캡처](매개변수) -> 반환타입 { 본문 }
```
캡처: `[]` 안함, `[&]` 참조, `[=]` 복사

std format 사용법?
?
```cpp
std::format("문자열..{}..{}", 값1, 값2)
```
파이썬 스타일 포맷팅

C++ 입출력 최적화 코드?
?
```cpp
std::cin.tie(nullptr)->sync_with_stdio(false);
```

if문으로 cin 입력받는 이유?
?
```cpp
if (std::cin >> n) { }
```
1. 입력 실패 처리 2. 변수 수명 제한 3. EOF 처리 편리

## 2. vector 사용법

vector 선언 방법 4가지?
?
```cpp
vector<int> v(n);           // 크기만
vector<int> v(크기, 값);     // 초기화
vector<int> v = {1,2,3};    // 직접
vector<int> v(다른벡터);     // 복사
```

vector 주요 멤버 함수 6가지?
?
```cpp
push_back, emplace_back(더 빠름), pop_back, clear, resize, size()
```

벡터에 범위 기반 for문으로 입력 받는 방법?
?
```cpp
for (auto& x : v) { std::cin >> x; }
```
**참조 &** 필수!

참조(Reference)란?
?
변수의 **별명**, 주소 값 가짐, 복사 없이 원본 수정 가능

vector의 메모리 특성?
?
동적 배열, 연속된 메모리(Heap), `v.size()`로 길이 확인
<!--SR:!2026-01-22,4,270-->

## 3. ranges 알고리즘

ranges 주요 함수들?
?
```cpp
std::ranges::sort(v)
std::ranges::max(v)
std::ranges::min(v)
std::ranges::count(v, 값)
std::ranges::reverse(v)
std::ranges::max_element(v)
std::ranges::min_element(v)
```

ranges max_element 사용법?
?
```cpp
auto it = std::ranges::max_element(v);
// *it 로 값
// std::distance(v.begin(), it) 로 인덱스
```

## 4. views 파이프라인

파이프라인 문법 기본 구조?
?
```cpp
원본 | 뷰어댑터1 | 뷰어댑터2 | ...
```

주요 뷰 어댑터 6가지?
?
```cpp
filter(조건)   // 필터
transform(함수) // 변환
take(n)        // 앞 n개
drop(n)        // 앞 n개 버림
reverse        // 역순
join           // 평탄화
```

views filter 사용 예시?
?
```cpp
auto small = a | std::views::filter([x](int i) { 
    return i < x; 
});
```

views iota 사용법?
?
```cpp
for (auto _ : std::views::iota(0, m)) { }
```
0부터 m-1까지 반복

Lazy Evaluation이란?
?
지연 평가 - 데이터를 미리 계산하지 않고 for문에서 꺼낼 때만 계산. 성능 저하 없음!
<!--SR:!2026-01-22,4,270-->

## 5. ranges 헤더 기능

ranges 헤더의 핵심 기능 3가지?
?
1. View (지연 평가)
2. Adaptors (파이프 |)
3. Concepts 기반 알고리즘

## 6. 유용한 STL 함수

fill 사용법?
?
```cpp
std::fill(v.begin()+i, v.begin()+j, 값);
```
범위를 값으로 채움
<!--SR:!2026-01-22,4,270-->

iota 사용법?
?
```cpp
std::iota(v.begin(), v.end(), 시작값);
```
연속 정수로 채움 {시작, 시작+1, ...}

swap 사용법?
?
```cpp
std::swap(a, b);
```
두 값 교환

distance 사용법?
?
```cpp
int idx = std::distance(v.begin(), it);
```
두 iterator 사이 거리

## 7. 필수 헤더

Modern C++ 필수 헤더들?
?
```cpp
#include <algorithm>  // sort/fill/swap
#include <iostream>   // cin/cout
#include <iterator>   // distance
#include <numeric>    // iota
#include <ranges>     // views
#include <vector>
#include <format>
```

## 8. 백준 문제 패턴

특정 값 개수 세기 패턴?
?
```cpp
std::cout << std::ranges::count(v, target);
```

최대값과 인덱스 동시 구하기 패턴?
?
```cpp
auto it = std::ranges::max_element(v);
// *it → 값
// distance(v.begin(), it)+1 → 1-based 인덱스
```

범위 채우기 + 반복 패턴?
?
```cpp
for (auto _ : std::views::iota(0, m)) { 
    std::fill(v.begin()+i-1, v.begin()+j, k); 
}
```

체크리스트 패턴(bool 벡터)?
?
```cpp
std::vector<bool> check(31, false);
check[n] = true;
if (!check[i]) { /* 미체크 */ }
```

## 9. 고급 기능

span이란?
?
```cpp
std::span<int> partial(v.data()+1, 3);
```
메모리 복사 없이 배열 특정 부분만 참조하는 뷰

while문 종료 조건 처리 패턴?
?
```cpp
while (std::cin >> a >> b && (a != 0 || b != 0)) { }
```
EOF와 종료 조건 동시 처리
