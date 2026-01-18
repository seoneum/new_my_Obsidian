---
type: problem
title: 백준 14681 사분면 고르기
created: 2026-01-06
updated: 2026-01-18T16:42:53
author: "[[김선음]]"
status: sprout
problem_type: coding
solved: true
tags:
  - problem
  - problem/coding
  - baekjoon
  - cpp
domain:
  - cs
---

# 백준 14681 사분면 고르기

## Notes
- 좌표 받아서 사분면 반환하기.
- 첫 번째 답
```cpp
#include <iostream>

auto main() -> int {
  int a, b;
  if (std::cin >> a >> b) {
    if (0 < a && 0 < b) //a,b둘 다 0이상
      std::cout << "1";
    else if (0 < a && 0 > b) //a는 양수, b는 음수
      std::cout << "2";
    else if (0 > a && 0 > b) //a,b 둘 다 음수
      std::cout << "3";
    else if (0 < a && 0 > b) //a음수, b양수
      std::cout << "4";
  }
}
```
- 두 번째 답
```cpp
#include <iostream>

auto main() -> int {
  int a, b;
  if (std::cin >> a >> b) {
    if (a > 0) {
      if (b > 0) {
        std::cout << "1";
      } else {
        std::cout << "4";
      }
    } else {
      if (b > 0) {
        std::cout << "2";
      } else {
        std::cout << "3";
      }
    }
  }
  return 0;
}
```

## Next
- [ ] 

