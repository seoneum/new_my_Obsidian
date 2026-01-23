---
type: problem
title: 나머지
created: 2026-01-19
updated: 2026-01-19T07:15:24
author:
  - "[[김선음]]"
problem_type: coding
source: baekjoon
difficulty: easy
language: cpp
status:
  - "[[🚜In Progress]]"
tags:
  - problem
  - problem/coding
  - difficulty/easy
  - source/baekjoon
solved: true
time_spent: 0
---

# 나머지

> **coding** | 난이도: **easy** | 출처: baekjoon 3052

---

## 📋 문제

### 입력
```
10개 숫자 입력
```

### 출력
```
나머지가 다른 것의 개수 출력
```

### 제한
- 시간: 
- 메모리: 

---

## 🧠 접근

### 첫 생각
- 일단 vector로 10개 받자.
- 그리고 10개 모두 나머지를 구한 후 같은 것의 개수를 세고 10개에서 빼면 되잖아

### 핵심 아이디어
- 근데 그게 아니었음.
- set이라는 중복을 거부하는 배열이 있다.
- 그 배열에 몽땅 집어넣고 그 배열 개수를 세면 중복 제외한 것의 개수가 나옴.

### 필요 개념
- [[C - Modern C++ Array]]
- [[P - 백준 Array part]]

---

## ✏️ 풀이

### C++
```cpp
#include <iostream>
#include <ranges>
#include <set>
#include <vector>

auto main() -> int {
  std::cin.tie(nullptr)->sync_with_stdio(false);

  std::vector<int> v(10);
  for (auto &x : v) {
    std::cin >> x;
  }
  std::set<int> s;
  for (int i : std::views::iota(0, 10)) {
    v[i] = v[i] % 42;
    s.insert(v[i]);
  }
  std::cout << s.size();
}
    

```

### 복잡도
- 시간: O()
- 공간: O()

---

## 🔍 복기

### 맞았으면
- 핵심:
- 더 좋은 방법: 이거 배열을 그냥 바로 set으로 만들어도 됐을 것 같아. 어차피 동일한 수는 나머지도 같으니. 

### 틀렸으면
- 실수: 반복을 0~9까지 함. 이러면 10번 아니냐? 근데 왜 0~10까지 해야하는거냐
- 정답: 마지막 숫자는 포함을 안 해서 그런 것 같은데. 아마도?

---

## 📝 FC

#flashcards/coding

나머지 핵심:: 



