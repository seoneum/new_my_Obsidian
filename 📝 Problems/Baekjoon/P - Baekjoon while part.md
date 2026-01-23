---
type: problem
title: 백준 while 파트 (10950, 10951)
created: 2026-01-13
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
# 백준 while 파트 (10950, 10951)

## Notes
- 10950, 10951
```cpp
//10950
#include <iostream>

auto main() -> int {
  std::cin.tie(nullptr)->sync_with_stdio(false);

  int a, b;
  while (std::cin >> a >> b && (a != 0 || b != 0)) {
    std::cout << a + b << "\n";
  }
  return 0;
}

``` 

## Next
- [ ] 
