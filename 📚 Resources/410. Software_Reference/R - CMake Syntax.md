---
type: reference
title: R - CMake Syntax
created: 2026-01-05
updated: 2026-01-18T16:42:53
author: [[김선음]]
group: SE
status: [[🌱Seed]]
tags:
  - reference
  - web
  - tagging/needed
aliases: []
source_kind: web
source_url: https://alida.tistory.com/19
source_authors: ALIDA
migrated_from: CMDS/400. Reference/410. Software_Reference/R - CMake Syntax.md
cmds: connect
---

# R - CMake Syntax

## Notes
- CMake는 먼저 CMakeLists.txt를 작성해 CMake 빌드의 틀을 잡아놓는다.
```bash
my_cpp20_project/
├── CMakeLists.txt       # 빌드 설정 파일
├── src/
│   └── main.cpp         # 소스 코드
└── build/               # 빌드 결과물이 저장될 폴더
```
- 간단한 문법과 구조
	- CMake에 사용하는 간단한 문법이 있음.
```CMake
cmake_minimum_required(VERSION 3.20) # 최소 CMake버전 명시

# 프로젝트 이름 및 버전
project(ModernCpp20Start VERSION 1.0 LANGUAGES CXX)

# C++ 표준을 20으로 설정 (필수)
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF) # GNU 확장 등이 아닌 순수 표준 모드 사용

# 컴파일러 경고 옵션 강화 (Modern C++ 학습 시 매우 중요)
add_compile_options(
    -Wall -Wextra -Wpedantic
    # -Werror # (선택사항) 경고를 에러로 처리하고 싶다면 주석 해제
)

# 실행 파일 생성
add_executable(app src/main.cpp)
```
## Next
- [ ] 

