---
type: inbox
title: N - Modern C++ Day 1
created: 2026-01-05
updated: 2026-01-05T09:13:44
author: "[[김선음]]"
group: SE
status: "[[🌱Seed]]"
tags:
  - "#inbox"
  - "#note"
  - "#tagging/needed"
  - baekjoon
aliases: []
---

# N - Modern C++ baekjoon #2588

## Notes
- C++할거야. modern형식 사용 할거고. CMake로 빌드 할거임.
- 기본적인 [[R - CMake Syntax]]를 알아보자!
- 뭘 보고 시작해야할지 모르겠네. 

## Baekjoon
- 2588 - 곱셈
	- 모던 스타일로 함. for 문법 바꿈. 
	- `#include <ranges> 를 통해 python처럼 range사용 가능
	- **int main() ➡️auto main() -> int**
		-> auto == return type 뒤에서 반환해 줄 것임. Placeholder역할
		- main() -> int == main뒤에 return type 명시해줌
		- 가독성을 위해 이렇게 적는 것. 형태가 통일되어 깔끔해짐
	- Pipeline
		- 데이터를 조작하지 않음. 참조, 복사처럼. 어떻게 처리할지 흐름만 처리
		- 어떻게가 아닌 무엇을 할 지 명시하는 것.
		- Lazy Evaluation = 나중에 for 문 안에서 데이터 꺼낼 때만 계산.
		- `데이터_원본 | 뷰1 | 뷰2`
		- `auto my_view = b | std::views::reverse | std::view::transform`(변환함수);
	- Range-based For문
		- 배열, 문자열, 벡터, **뷰**까지 순회 가능한 모든 것을 처리함.
		`for (데이터타입 변수명 : 컨테이너 or 뷰) {}
		- Container 내 모든 element를 꺼내서 반복.
	- Format
		- 파이썬 타입의 print를 가능하게!
		`std::format("문자열 틀..{}..{}..{}", 값1, 값2, 값3);`
	- Lambda Expression
		- 일회용 미니 함수.
		`[캡처] (매개변수) -> 반환타입{본문} `
		- \[캡쳐] = 외부 변수 훔치기. 
			1) [] : 아무것도 안 가져오기
			2) \[&] : 외부변수 참조
			3) \[=] : 외부 변수 복사. 
		- (Parameter) == 입력값
			- 일반 함수와 같음
		- -> (return type) : 출력 타입
			- 생략하면 컴파일러가 알아서 추론하긴 해~ 근데 복잡하면 가독성 위해 명시
		- {Body} : 함수 내용 코드 들어가는 곳
	- \<ranges> header
		- 파이프라인과 뷰를 가진 헤더
			1) view : 지연 평가. Lazy Evaluation. 
			   성능 저하 없는 가벼운 객체를 만들어서 계산 시점에만 사용
			2) Adaptors : 파이프 연산자
			   | 를 사용한 직관적 코드 작성 가능
			3) Concepts기반 알고리즘
			   container를 그대로 던져도 알아먹는 알고리즘!!
	- 
```c++
//baekjoon #2588
#include <iostream>
#include <string>
#include <ranges>    // 파이프라인 로직
#include <algorithm> 
#include <format>    // 출력의 핵심

auto main() -> int {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int A;
    std::string B;

    if (std::cin >> A >> B) {
        // 1. [Logic] 뷰 파이프라인: 뒤집고 -> 숫자로 변환
        auto digit_view = B 
            | std::views::reverse 
            | std::views::transform([](char c) { return c - '0'; });

        // 2. [Output] 포맷팅을 사용한 출력
        for (int digit : digit_view) {
            // std::format: "{}" 안에 값을 넣는 파이썬 스타일
            std::cout << std::format("{}\n", A * digit);
        }

        // 3. 전체 결과 출력
        std::cout << std::format("{}\n", A * std::stoi(B));
    }

    return 0;
}
```


## Link
- [[C - Modern C++ Array]]
- [[C - Modern C++ 궁금증 모음]]

## Next
- [ ] 
# Clang을 쓰되, GCC 13의 라이브러리 경로를 힌트로 줌
```shell
cmake -DCMAKE_CXX_COMPILER=clang++ -DCMAKE_CXX_FLAGS="--gcc-toolchain=/usr/lib/gcc/x86_64-linux-gnu/13" ..
```

```shell
CXX=/home/linuxbrew/.linuxbrew/bin/g++-15 cmake ..
```