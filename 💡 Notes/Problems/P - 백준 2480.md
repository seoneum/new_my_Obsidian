---
type: problem
title: 백준 2480 주사위
created: 2026-01-08
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

# 백준 2480 주사위

## Notes
- 주사위 문제. 
- 처음에는 if문을 사용해서 분기를 하려고 함.
- 코드가 길고 불편함.
- ai를 사용해서 vector화 시킬 수 있는 방법 생각.
- vector에 넣고 돌리기. 샌드위치 생각. sort알고리즘도 사용 가능.
```cpp
#include <algorithm>
#include <iostream>
#include <vector>

auto main() -> int {
  int a, b, c;
  if (std::cin >> a >> b >> c) {
    std::vector<int> v = {a, b, c}; //벡터에 다 넣음
    sort(v.begin(), v.end()); //sort STL사용
    if (v[0] == v[2]) { //sort했기 때문에 양 끝 값만 비교
      std::cout << 10000 + v[0] * 1000;
    } else if (v[0] == v[1] || v[1] == v[2]) { //가운데 기준으로 비교
      std::cout << 1000 + v[1] * 100;
    } else {
      std::cout << 100 * v[2]; //제일 큰 값
    }
  }
}
```

## Next
- [ ] 

