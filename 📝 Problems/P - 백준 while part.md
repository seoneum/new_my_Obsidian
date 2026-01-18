---
migrated_from: CMDS/200. CMDS/220. Merge/224. Problem/Coding/P - 백준 while part.md
updated: 2026-01-18T16:42:53
cmds: inbox
---
# N - Modern C++ baekjoon while_part

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
