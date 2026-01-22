---
type: problem
title: P - 10811
created: 2026-01-22
updated: 2026-01-22T16:29:48
problem_type: coding
source: baekjoon
difficulty: easy
language: cpp
status: "[[🚜In Progress]]"
solved: false
tags:
  - problem
  - problem/coding
  - difficulty/easy
  - source/baekjoon
---
# 10811

> **coding** | 난이도: **easy** | 출처: baekjoon 10811

---

## 📋 문제

### 입력
```
n개의 바구니 개수, m번의 변환. i - j까지의 변환범위.
```

### 출력
```
m번 i - j까지 변환해서 출력
```

### 제한
- 시간: 
- 메모리: 

---

## 🧠 접근

### 첫 생각
- 부분 부분 짤라야겠네? 그럼 span의 개념을 쓰는게 좋을지도?
- 흠... 어떻게 해야할까? 

### 핵심 아이디어
- 그럼 vector를 쓰고 그걸 span으로 바꾸자.
- 그리고 subspan으로 자르기.
- 전체를 뒤집에서 span에 넣고 자르면 되겠다!!
- 그리고 나머지를 잘라서 출력하자~

### 필요 개념
- [[C - Modern C++ Array]]

---

## ✏️ 풀이

### C++
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
  int n, m;
  if (std::cin >> n >> m) {
    int i, j;
    std::vector<int> v(n);
    std::iota(v.begin(), v.end(), 1);
    std::span<int> s = v;
    for (auto _ : std::views::iota(0, m)) {
      if (std::cin >> i >> j) {
        std::ranges::reverse(s.subspan(i - 1, j - i + 1));
      }
    }
    for (int num : s) {
      std::cout << num << " ";
    }
  }
  return 0;
}
```

### 복잡도
- 시간: O()
- 공간: O()

---

## 🔍 복기

### 맞았으면
- 핵심:
- 더 좋은 방법:

### 틀렸으면
- 실수: 돌려서 span에 집어넣으면 안되던데요. 왜일까?
- 정답: 전체를 출력해야하는데 변하지 않아야하는 부분도 변하기 때문에 그렇단다. 그리고 중복 변화가 있을 때도 문제가 생기겠지. 
- 근데 span은 참조 매커니즘이라 그냥 보고 돌리고 출력하면 돼서 상관이 없어. 

---

## 📝 FC
#flashcards/coding

10811 핵심:: 

