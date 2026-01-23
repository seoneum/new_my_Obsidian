---
type: problem
title: 백준 11382 꼬마 정민
created: 2026-01-05
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

# 백준 11382 꼬마 정민

## Notes

### 꼬마 정민
- A+B+C 계산하기
- 조건 
	- 자료형 크기는 $$1\leq a,b,c\leq 10^{12}$$
```cpp
#include <format>
#include <iostream>

auto main() -> int {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);

  long long a, b, c;

  if (std::cin >> a >> b >> c) {
    std::cout << std::format("{}", a + b + c);
  }
}

```

- 풀이
	- modern함을 위해 format을 이용함.
	- 자료형의 type 크기 오류로 계속 통과를 못함.
	- 주의할 것!!
- 다른 풀이
	1) `std::stringstream`
	- 문자열을 마치 입력창인 양 다루는 도구. 백준 치트키라는데?
	- **데이터를 버퍼에 넣고 복사**
```cpp
//1. Parsing. 문자열에서 데이터를 추출
std::string input = "UserA 100 95.5"; // 이름, 점수, 평균
std::stringstream ss(input); // 문자열을 스트림으로 포장

std::string name;
int score;
double avg;

// cin >> name >> score >> avg; 하듯이 똑같이 사용!
ss >> name >> score >> avg;

// 결과: name="UserA", score=100, avg=95.5 (자동 타입 변환됨)
//2. Serialization. 직렬화 = 데이터를 문자열로 합침
std::stringstream ss;
ss << "Name: " << name << ", Score: " << score;
std::string result = ss.str(); // .str()로 포장된 문자열을 꺼냄
```
- 다른 2
	2) `std::views::split
	- 원본은 건드리지 않고 그냥 자르는 위치만 기억.
	- 단어를 구분하는 포인터 쌍을 만듦.
```cpp
#include <iostream>
#include <string>
#include <ranges>
#include <vector>

auto main() -> int {
    std::string data = "10 20 30 40";

    // ' ' (공백)을 기준으로 쪼갠 뷰 생성
    auto split_view = data | std::views::split(' ');

    for (auto sub_range : split_view) {
        // sub_range는 string이 아님! (메모리 주소 범위일 뿐)
        // 사용하려면 string이나 string_view로 변환해야 함
        
        // 방법 1: string으로 변환 (복사 발생)
        // std::string token(sub_range.begin(), sub_range.end());
        
        // 방법 2: string_view로 변환 (복사 없음, 추천)
        // sub_range가 연속된 메모리(contiguous)라면 string_view로 볼 수 있음
        std::string_view token(sub_range.begin(), sub_range.end());

        std::cout << token << "\n";
    }

    return 0;
}
```


## Next
- [ ] 

