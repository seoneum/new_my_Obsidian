---
type: problem
title: P - 27866
created: 2026-01-23
updated: 2026-01-23T11:19:49
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
# 문자와 문자열

> **coding** | 난이도: **easy** | 출처: baekjoon 27866

---

## 📋 문제

### 입력
```
단어 s, 정수 i. 
```

### 출력
```
단어 내에서 i번째 글자 출력
```

### 제한
- 시간: 
- 메모리: 

---

## 🧠 접근

### 첫 생각
- vector에 넣어도 되나?
- 문자열은 string 써야지.
- string 만들고 cin으로 받고 \[i]로 출력
- 근데 0부터 인덱스가 있기 때문에 \[i-1]로.

### 핵심 아이디어
- string만드는 법만 알면 될듯.

### 필요 개념
- [[ ]]

---

## ✏️ 풀이

### C++
```cpp
#include <iostream>
#include <string>

auto main() -> int {
  std::string ch;
  int n;
  if (std::cin >> ch) {
    if (std::cin >> n) {
      std::cout << ch[n - 1];
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
- 실수:
- 정답:

---

## 📝 FC
#flashcards/coding

27866 핵심:: 

