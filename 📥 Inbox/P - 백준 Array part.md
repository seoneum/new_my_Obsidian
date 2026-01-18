---
tags:
  - inbox
  - note
  - tagging/needed
aliases: []
index:
  - "[[🏷️Software]]"
type:
  - basic
title: N - Modern C++ baekjoon Array_part
created: 2026-01-13
cover_url: {}
updated: 2026-01-18T16:42:53
my_rate: {}
authors:
  - "[[김선음]]"
CMDS: []
started: 2026-01-13
status:
  - "[[🌱Seed]]"
group:
  - SE
publishDate: {}
start_read_date: {}
finish_read_date: {}
migrated_from: CMDS/200. CMDS/220. Merge/224. Problem/Coding/P - 백준 Array part.md
domain:
  - math
cmds: inbox
---
# N - Modern C++ baekjoon Array_part

## Notes
- 배열에 대해 알아보아요
- C++표준 배열인 vector를 사용하자! 동적 배열임
- 길이 정보가 내장되어있어 `v.size()` 로 길이정보를 알 수 있음
```cpp
//크기를 n으로 두면 알아서 자동으로 조절!!
std::vector<자료형 타입> 이름(n);
//특정 값 넣어서 만들기
std::vector<int> v(크기,특정 값);
// 직접 값 넣기
std::vector<int> v = {1,2,3,4};
//다른 벡터 복사하기
std::vector<int> v(다른 벡터);

push_back(값) = 맨 뒤에 값 추가
emplace_back(값) = push_back과 같은데 더 빠름
pop_back() = 맨 뒷 값 삭제. 리턴 없음
clear() = 싹 다 지우기
resize(n) = 크기를 n으로 변경
사용할 때 벡터이름.함수()로 사용

//입력. 범위기반 for문 + 참조 연산자 &를 사용.
for (auto& x : v){
	std::cin>>x;
}

//복잡한 iterator대신 std::range사용!
//sort에 배열 전체를 던지면 알아서 정렬
std::ranges::sort(v);
//최대 최소
std::ranges::max(v);
std::ranges::min(v);
//특정 값 개수 세기
std::ranges::count(v,값);
//뒤집기
std::ranges::reverse(v);

//고급
std::span
//메모리 복사 없이 특정 부분만 쳐다보는 안경.
```

- #10807
	- 배열 기초 문제. 배열 안에서 특정 값 개수 찾는 문제임
	- vector로 받을 때는 for문을 사용해서 받음
	- vector는 연속된 공간인 heap으로 공간 구성.
	- 참조로 받는다 = 별명 설정하는 것 = 주소 값을 가짐 = 복사 없음.
```cpp
#include <algorithm>
#include <iostream>
#include <vector>

auto main() -> int {
  std::cin.tie(nullptr)->sync_with_stdio(false);

  int n, i;
//배열의 크기인 n입력받음.
  if (std::cin >> n) {
    std::vector<int> v(n);
	// 정확히 x를 어떻게 받는건지는 모르겠네. 참조로 받는 것 같긴 한데
	// x는 v[0],[1]..의 주소를 가지고 있는 포인터임. 가리키는 곳에 대입!
    for (auto &x : v)
      std::cin >> x;
    if (std::cin >> i) {
	// 찾을 값인 i입력 받음. 그리고 찾아서 바로 출력.
      std::cout << std::ranges::count(v, i);
    }
  }
}
```

#10871
- 원하는 값만 취해야함. 어떻게? 그것은 말이죠
- std::views::filter를 쓴다!!
- 이게 무슨 기능이에요?
	- 이건 말이죵~~ 파이프 연산자를 사용해서 데이터가 걸러지는 그런 역할이에요~~
	- 아하~~ 그럼 일정 값보다 작은 값을 걸러내야하는 이 문제에 정말 적합하겠네요!
	- 근데 어떻게 해야 걸러낼 수 있는건가요? pivot처럼 기준값으로 하고 정렬하고 버리나요?
	- 아니요아뇨, 하나씩 꺼내서 필터를 통과시키는거예요. 기준값을 잡고. 그리고 그것만 출력하면 되겠죠??
```cpp
#include <iostream>
#include <ranges>
#include <vector>

auto main() -> int {
  std::cin.tie(nullptr)->sync_with_stdio(false);
  int n, x;
  if (std::cin >> n >> x) {
    std::vector<int> a(n);
    // 입력받은 x보다 작은 배열 내 값을 순서대로 없애서 출력.
    // 어떻게 해야할까. sort한 벡터를 따로 만들어서 없애고 같은 값만 출력?
    // for문을 돌려봐야하나?
    //이 for문은 그냥 값 받기 용. 이 안에 아무것도 드가면 안됨
    for (auto &y : a)
      std::cin >> y;
	  //파이프라인 문법.
    auto small = a | std::views::filter([x](int i) { return i < x; });
    for (int result : small) {
      std::cout << result << " ";
    }
  }
  return 0;
}

```
- 파이프라인 문법이 뭘까\~~요
- 이 | 기호를 통과하며 데이터를 가공한다!!
- 기본적으로는 `원본 | 뷰 어댑터 1 | 뷰 어댑터 2 | ...`이런 식으로 가공을 해요
- 데이터 제공 : `std::vector, std::array, std::views::iota`등등
- 뷰 어댑터 : `filter, transform, take`등등
- Sink : 데이터 사용하는 곳 : `for, ranges::copy, to<vector>`

| Adapter name  | Function        | E.G.) |
| ------------- | --------------- | ----- |
| filter(조건)    | 참인 것만 통과        |       |
| transform(함수) | 값을 변형           |       |
| take(n)       | 앞에서부터 n개 가져옴    |       |
| drop(n)       | 앞에서부터 n개 버림     |       |
| reverse       | 순서 거꾸로          |       |
| join          | 이중 배열을 1차원으로 합침 |       |
- filter문법
	`[외부변수](검사할_숫자){return 조건;}`

- #10818
	- vector를 sorting하고 min, max출력하면 되는 쉬운 문제!!
```cpp
#include <algorithm>
#include <iostream>
#include <vector>

auto main() -> int {
  std::cin.tie(nullptr)->sync_with_stdio(false);

  int n;
  if (std::cin >> n) {
    std::vector<int> v(n);
    for (auto &x : v) {
      std::cin >> x;
    }
    std::ranges::sort(v);
    std::cout << std::ranges::min(v) << " " << std::ranges::max(v);
  }
}
```
- #2562
	- 가장 높은 값 출력하고 그 값의 인덱스 번호 따기.
	- Modern한 방법론
	1) `std::ranges::max_element(배열이름)`사용하기
		가장 큰 원소의 주소 반환
	2) it으로 받아서 \*it으로 안의 값 출력
		위 두 가지는 iterator STL에 포함되어있음. 반복자인데 나중에 또 다룰게.
	3) distance로 자동 거리 계산. 
		`distance(시작, 끝)+1`하면 숫자 나옴. 1은 0부터 시작이라 더해주는 것
```cpp
#include <algorithm>
#include <iostream>
#include <iterator>
#include <vector>

auto main() -> int {
  std::cin.tie(nullptr)->sync_with_stdio(false);

  std::vector<int> v(9);
  for (auto &x : v) {
    std::cin >> x;
  }
  // max_element : 가장 높은 값의 주소.
  auto it = std::ranges::max_element(v);
  // *를 사용해 그 주소에 있는 것의 값 꺼냄
  std::cout << *it << "\n";

  // int index = it - v.begin() == std::distance(v.begin(), it);
  // distance쓰면 자동으로 뺄셈 연산 해줌.
  std::cout << distance(v.begin(), it) + 1;
}
```
- 10810 공 넣기
	- 바구니 n개 존재. 한 바구니 당 공은 무조건 한 개.
	- 이미 들어있다면 없애고 그 수를 다시 넣음.
	1) cin으로 n,m입력 받기
	2) 벡터 n짜리 만들기. m번 반복문 만들기
	3) i,j,k 입력 받기.
	4) 벡터에서 i~j까지에 숫자 k대입.
	- key syntax : std::fill(시작, 끝, 값)
```cpp
#include <algorithm>
#include <iostream>
#include <ranges>
#include <vector>

auto main() -> int {
  int n, m;
  if (std::cin >> n >> m) {
    std::vector<int> v(n);
    int i, j, k;
    for (auto _ : std::views::iota(0, m)) {
      if (std::cin >> i >> j >> k) {
        std::fill(v.begin() + i - 1, v.begin() + j, k);
      }
    }
    for (int ball : v) {
      std::cout << ball << " ";
    }
  }
}
```
- 공 바꾸기
	- 위와 같은 조건에서 바구니에 넣는 것이 아닌 바꾸는 것
	- 벡터 내 값 한 번에 채우는 법
		- numeric헤더 -> std::iota(시작, 끝, 시작 숫자)
	- swap을 구현하지 않아도! algorithm에 들어있는 swap을 쓰면 된다는 사실!
```cpp
#include <algorithm>
#include <iostream>
#include <numeric>
#include <ranges>
#include <vector>

auto main() -> int {
  std::cin.tie(nullptr)->sync_with_stdio(false);
  int n, m;
  if (std::cin >> n >> m) {
    std::vector<int> v(n);
    std::iota(v.begin(), v.end(), 1);
    int i, j;
    for (auto _ : std::views::iota(0, m)) {
      if (std::cin >> i >> j) {
	  //하나 전의 인덱스를 하는 이유는 0부터 시작하기 때문~
        std::swap(v[i - 1], v[j - 1]);
      }
    }
    for (int ball : v) {
      std::cout << ball << " ";
    }
  }
}
```
- #5597
	- 학생 30명 존재. 번호 다 붙어있음.
	- 입력 28줄로 안 한 2명 제외하고 다 있음.
	- 출력은 없는 번호 2개 낮은 순으로 정렬해서 출력
```cpp
#include <iostream>
#include <ranges>
#include <vector>

auto main() -> int {
  std::cin.tie(nullptr)->sync_with_stdio(false);
  //문자열을 bool로 만들어서 31개 만들기. 0은 안 씀
  std::vector<bool> check(31, false);
  //0~27까지 28번 반복
  for (auto _ : std::views::iota(0, 28)) {
    int n;
    std::cin >> n;
	//같은 것 있으면 true 표시
    check[n] = true;
  }
  //1~30까지 false인 것 체크해서 출력
  for (int i : std::views::iota(1, 31)) {
    if (!check[i]) {
      std::cout << i << "\n";
    }
  }
  return 0;
}
```
## Next
- [ ] 
