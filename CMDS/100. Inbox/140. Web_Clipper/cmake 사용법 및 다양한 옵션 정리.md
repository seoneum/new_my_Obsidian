---
title: "cmake 사용법 및 다양한 옵션 정리"
source_url: "https://alida.tistory.com/19"
author:
  - "[[alida]]"
published: 2022-01-06
created: 2026-01-05
description: "1 소개 본 포스트에서는 cmake의 사용법 및 다양한 옵션들에 대해 설명한다. cmake는 리눅스, 윈도우, 맥 등 운영체제에 관계없이 하나의 코드만으로 실행 파일을 생성해주는 크로스 컴파일러 프로그램이다. 본 포스트에서는 리눅스 터미널에서 cmake를 사용하는 방법에 한정하여 설명한다. 포스트에서 설명하는 모든 내용들은 우분투 18.04 LTS 환경에서 테스트하였다. 2 환경 설정 터미널에서 아래 명령어를 입력하여 cmake를 설치한다 # Install cmake. $ sudo apt install cmake # Check cmake is installed successfully. $ cmake --help 3 CMakeLists.txt 사용법 해당 섹션에서는 cmake의 명령어와 변수의 의미에 대해.."
tags:
  - "clippings"
---
> [!summary]+ 3줄 요약
> - CMake는 운영체제에 독립적으로 실행 파일을 생성할 수 있게 해주는 크로스 컴파일러 프로그램입니다.
> - CMakeLists.txt 파일에 프로젝트 설정 및 빌드 명령어를 작성하며, `cmake_minimum_required`, `project`, `find_package`, `add_executable`, `target_link_libraries` 등이 주요 명령어입니다.
> - `CMAKE_CXX_FLAGS`, `CMAKE_BUILD_TYPE` 등 다양한 변수를 사용하여 컴파일 옵션이나 빌드 타입을 설정할 수 있습니다.


---

Software

## 1 소개

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdna%2Fk4JWU%2FbtrpUIgy206%2FAAAAAAAAAAAAAAAAAAAAAKd85RDa5aD1yGSWa9twBG0ptBQBP9RsKI6bLJ-1LJHF%2Fimg.png%3Fcredential%3DyqXZFxpELC7KVnFOS48ylbz2pIh7yKj8%26expires%3D1769871599%26allow_ip%3D%26allow_referer%3D%26signature%3DdSI8%252BtGBADkK7yiNuR5KJgUHsxo%253D)

본 포스트에서는 cmake의 사용법 및 다양한 옵션들에 대해 설명한다. cmake는 리눅스, 윈도우, 맥 등 운영체제에 관계없이 하나의 코드만으로 실행 파일을 생성해주는 크로스 컴파일러 프로그램이다. 본 포스트에서는 리눅스 터미널에서 cmake를 사용하는 방법에 한정하여 설명한다. 포스트에서 설명하는 모든 내용들은 우분투 18.04 LTS 환경에서 테스트하였다.

## 2 환경 설정

터미널에서 아래 명령어를 입력하여 cmake를 설치한다

```shell
# Install cmake.
$ sudo apt install cmake

# Check cmake is installed successfully.
$ cmake --help
```

## 3 CMakeLists.txt 사용법

해당 섹션에서는 cmake의 명령어와 변수의 의미에 대해 설명한다. 일반적으로 cmake는CMakeLists.txt라는 파일에 코드를 작성한 후 터미널에서cmake명령을 통해 인식하는 방법으로 주로 사용한다. 간단한 프로젝트의 경우, 프로젝트 최상단 디렉토리에CMakeLists.txt파일 하나를 작성하는 방법이 있고 큰 프로젝트의 경우 디렉토리 별로 각각의CMakeLists.txt파일을 작성하는 방법이 있다. 예를 들어, ROS의 catkin\_ws는 src 디렉토리에CMakeLists.txt파일이 존재하고 각각 ROS 패키지별로CMakeLists.txt파일이 존재하는 큰 프로젝트의 예시 중 하나이다.

cmake의 명령어는 대소문자를 구분하지 않는다. 따라서MESSAGE(), message()모두 동일한 명령어를 의미한다. 본 포스트에서는 모든 명령어를 소문자로 표기하였다. cmake에서는 전용으로 사용할 수 있는 변수들이 있는데 일반적으로${...}과 같이 표기한다. 변수는 일반적으로 미리 예약된 변수들이 있으며${CMAKE\_...}로 시작한다. 또한 유저가 직접 변수를 설정할 수 있다.

자세한 설명에 앞서서 실제로 사용 중인 간단한CMakeLists.txt파일의 예시를 소개한다. 다음 섹션을 보고 난 후 다시 해당 파일을 보면 해석할 수 있을 것이다.

```cmake
cmake_minimum_required(VERSION 3.0)
project(opencv_test)

set(CMAKE_CXX_FLAGS ${CMAKE_CXX_FLAGS} "-std=c++11 -O3")

find_package(OpenCV 3.4 REQUIRED)
find_package(Eigen3 REQUIRED)

include_directories(
    ${OpenCV_INCLUDE_DIRS}
    ${EIGEN3_INCLUDE_DIRS}
)

# Make binary.
add_executable(output
               src/stereo_rectify.cpp
              )
target_link_libraries(output
                      ${OpenCV_LIBS}
                      ${EIGEN3_LIBS}
                     )
```

### 3.1 cmake 코드 설명

해당 섹션에서는CMakeLists.txt에서 사용하는 명령어들에 대해 설명한다.

#### 3.1.1 cmake\_minimum\_required()

빌드에 필요한 cmake의 최소 버전 명시

#### 3.1.2 project()

현재 프로젝트의 이름 설정

#### 3.1.3 message()

터미널에 특정 메세지를 출력한다.message(STATUS ${CMAKE\_PROJECT\_NAME})과 같이 사용할 수 있다. STATUS 외에도 WARNING, AUTHOR\_WARNING, SEND\_ERROR, FATAL\_ERROR와 같은 키워드들이 존재한다.

#### 3.1.4 find\_package()

특정 라이브러리의 경로를 찾는다. 일반적으로find\_package({package\_name})과 같이 사용한다.

```bash
find_package({package_name} 3.4)                    # 특정 라이브러리의 특정 버전을 찾는다.
find_package({package_name} REQUIRED)               # 해당 라이브러리를 찾지 못하면 에러를 출력하며 cmake를 종료한다.
find_package({package_name} COMPONENTS {aaa} {bbb}) # 해당 라이브러리의 모든 기능들을 불러오지 않고 특정 컴포넌트들만 불러온다.
```

정상적으로 라이브러리를 찾는 경우 특정 CMAKE 변수에 특정 라이브러리의 경로가 저장된다.

예를 들어, OpenCV 라이브러리를 찾고자 하는 경우find\_package(OpenCV)를 사용하면${OpenCV\_INCLUDE\_DIRS}에는 OpenCV의 헤더파일의 경로가 저장되며${OpenCV\_LIBS}에는 라이브러리의 파일 경로가 저장된다.

#### 3.1.5 include\_directories()

헤더 파일의 경로를 입력한다.

아래와 같이 프로젝트 최상단 디렉토리 기준으로 경로를 입력할 수도 있고 특정 라이브러리의 헤더 파일 경로를 입력할 수도 있다.

```cmake
include_directories(
    include/
    src/
    ${OpenCV_INCLUDE_DIRS}
)
```

#### 3.1.6 add\_executable()

빌드 최종 결과물로 바이너리를 생성한다.

아래와 같이 괄호 옆에 실행파일의 이름을 설정하고 다음 라인부터는 코드 파일의 경로를 입력하면 된다.

```bash
add_executable (output
                src/main.cpp
                src/foo.cpp
                src/bar.cpp
               )
```

#### 3.1.7 add\_library()

빌드 최종 결과물로 라이브러리를 생성한다.

아래와 같이 괄호 옆에 라이브러리의 이름을 설정하고 그 옆에 정적/동적 라이브러리 여부를 설정한다. STATIC의 경우 정적 라이브러리(.a)이고 SHARED의 경우 동적 라이브러리(.so)를 의미한다. 그리고 다음 라인부터는 코드 파일의 경로를 입력하면 된다.

```armasm
add_library (outputlib STATIC
             src/foo.cpp
             src/bar.cpp
            )
```

#### 3.1.8 target\_link\_libraries()

add\_executable(), add\_library()를 통해 바이너리(또는 라이브러리)를 생성할 때 해당 바이너리(또는 라이브러리)가 요구하는 라이브러리를 추가한다.

예를 들면, 아래와 같이 output 바이너리가 내부적으로 OpenCV와 Eigen 라이브러리를 사용하는 경우target\_link\_libraries()의 괄호 옆에는 바이너리의 이름을 적은 후 다음 라인부터 해당 라이브러리가 요구하는 라이브러리의 경로를 입력한다. 일반적으로find\_package()를 통해 XXXX\_INCLUDE\_DIRS, XXXX\_LIBS 변수가 생성되므로 이를 사용한다.

```cmake
add_executable(output
                src/main.cpp
                src/foo.cpp
                src/bar.cpp
               )
target_link_libraries(output
                      ${OpenCV_LIBS}
                      ${EIGEN3_LIBS}
                     )
```

#### 3.1.9 install()

make install명령을 실행했을 때 실행할 동작을 지정한다. 아래 명령은 output을 /usr/local/bin에, liboutputlib.a는 /usr/local/lib에 설치하는 install target을 추가한다.

```crystal
install (TARGETS output outputlib
         RUNTIME_DESTINATION /usr/local/bin
         ARCHIVE_DESTINATION /usr/local/lib
        )
```

### 3.2 cmake 변수 설명

해당 섹션에서는CMakeLists.txt에서 사용하는 변수들에 대해 설명한다. 변수를 설정하는 방법은set($VARIABLE value)로 설정할 수 있다. 변수를 확인하는 방법은message(${VARIABLE})로 확인할 수 있다.

#### 3.2.1 ${CMAKE\_PROJECT\_NAME}

현재 프로젝트의 이름

#### 3.2.2 ${CMAKE\_BUILD\_TYPE}

현재 프로젝트의 빌드 타입. 빌드 타입에는 Release, RelWithDebInfo, Debug, MinSizeRel이 있다.

#### 3.2.3 ${CMAKE\_CXX\_FLAGS}

g++에서 사용하는 컴파일 옵션을 설정할 수 있다. 일반적으로 다음과 같이 사용한다.

```bash
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11 -O3")
```

#### 3.2.4 ${CMAKE\_VERBOSE\_MAKEFILE}

Verbose Makefile 작성 여부. 다음과 같이 값을 true(또는 1)로 지정하면 빌드 상세 과정을 모두 출력하는 Makefile을 생성한다.

```swift
set(CMAKE_VERBOSE_MAKEFILE true)
```

#### 3.2.5 ${CMAKE\_INSTALL\_PREFIX}

설치 매크로(make install)에서 실행 바이너리와 라이브러리 등의 최종 생성물을 복사할 설치 디렉토리를 지정한다. install() 명령에서 상대 경로를 사용한 경우, 이 변수에 지정한 디렉토리가 Base 디렉토리가 된다. 이 변수를 별도로 지정하지 않으면 기본값은/usr/local이다.

```python
set(CMAKE_INSTALL_PREFIX /usr/bin)
```
