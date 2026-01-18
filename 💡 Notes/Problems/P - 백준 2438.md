---
type: problem
title: 백준 2438, 2439 별찍기
created: 2026-01-12
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
# 백준 2438, 2439 별찍기

## Notes
- 고전인 별찍기. 벌써 3번째 인데도 왜 어렵게 느껴질까'
- for문을 두 번 써서 풀어야겠지
- 한번은 전체 줄 갯수 만큼 도는 n.
- 두 번째는 별을 출력해야겠지.
```cpp
#include <iostream>
#include <ranges>

auto main() -> int {
  std::cin.tie(nullptr)->sync_with_stdio(false);
  // i의 개수에 따라 별을 여러개 한 줄에 출력
  int n;
  if (std::cin >> n) {
    // 어떻게 한 줄에 출력할 수 있을까?
    for (int i : std::views::iota(1, n + 1)) {
	//[[maybe_unused]] -> 안 쓸 수 있음을 명시하기.
      for ([[maybe_unused]] int j : std::views::iota(1, i + 1)) {
        std::cout << "*";
      }
      std::cout << "\n";
    }
  }
  return 0;
}
```
- 하지만 string을 사용한 for 한 번의 더 modern한 풀이가 있다면?
```cpp
#include <iostream>
#include <string> 
#include <ranges>

auto main() -> int {
  std::cin.tie(nullptr)->sync_with_stdio(false);

  int n;
  if (std::cin >> n) {
    for (int i : std::views::iota(1, n + 1)) {
      // [핵심] 안쪽 for문을 이 한 줄로 대체!
      // "별(*)을 i개만큼 반복해서 문자열로 만들어라"
      std::cout << std::string(i, '*') << "\n";
    }
  }
  return 0;
}
```
- 별찍기 2번
	- 별 있던 자리에 공백 넣고 반대에 별 세우기
	- 
## Next
- [ ] 
