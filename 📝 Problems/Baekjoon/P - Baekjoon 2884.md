---
type: problem
title: 백준 2884 알람시계
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

# 백준 2884 알람시계

## Notes
- 설정 시간보다 45분 먼저 알람을 울려주는 알람시계
```cpp
#include <format>
#include <iostream>

auto main() -> int {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);
  int H, M; //시간, 분
  if (std::cin >> H >> M) {
    if (M < 45) {
      M += 15; // 45분보다 적으면 시간을 빌려옴. 60-45=15라 똑같음.
      H--; // 그리고 시간을 하나 빼줌
      if (H < 0) {
        H = 23; // 0이하면 23으로 감.
      }
    } else {
      M -= 45; // 45이상이면 그냥 빼기
    }
    std::cout << std::format("{} {}", H, M);
  }
  return 0;
}
```
- 

## Next
- [ ] 

