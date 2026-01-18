---
type: concept
title: Modern C++ 궁금증 모음
created: 2026-01-16
updated: 2026-01-18T16:42:53
author: "[[김선음]]"
status: in_progress
tags:
  - concept
  - domain/cs
  - cpp
  - modern-cpp
domain:
  - cs
---

# Modern C++ 궁금증 모음

## notes
- 왜 std::cin으로 그냥 받지 않고 `if (cin)으로 받을까?`
	1) 여러가지 이유로 입력이 실패(타입 불일치)가 발생하면 버그 발생.
	   하지만 if문에 넣으면? 잘못 입력된다면 실행되지 않음
	2) 변수의 수명을 제한할 수 있음
	   `if (int n; cin>>n)`으로 scope통제해버림
	3) EOF처리하기 편하다
	   `cin>>n; if (cin.fail() == false)` 로 실패여부 확인 후 ㄱㄱ.
- 


## Link
- [[C - Modern C++ Day 1]]
- [[C - Modern C++ Array]]

## Next
- [ ] 
