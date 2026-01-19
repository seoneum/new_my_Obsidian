# 입출력 시스템

## 1. 스트림 (Stream) 개념

### 정의
- 데이터의 **흐름**을 추상화한 소프트웨어 모듈
- 장치와 프로그램 사이의 데이터 전송 통로

```
[장치] ←→ [스트림] ←→ [프로그램]
```

### 스트림 종류
| 스트림 | 역할 | 예시 |
|--------|------|------|
| **입력 스트림** | 장치 → 프로그램 | `cin`, `ifstream` |
| **출력 스트림** | 프로그램 → 장치 | `cout`, `ofstream` |

---

## 2. 스트림 버퍼

### 키 입력 스트림 버퍼
- 입력 장치로부터 받은 데이터를 **임시 저장**
- **Enter** 키가 입력의 끝을 알림
- Enter를 누르면 버퍼에서 프로그램으로 읽어감
- 버퍼에서 수정 가능 (백스페이스 등)

### 스크린 출력 스트림 버퍼
- 출력 데이터를 송출 전에 **임시 저장**
- 출력 장치의 효율성 개선
- 버퍼 비우기(flush) 조건:
  - 버퍼가 꽉 참
  - `\n` 또는 `endl` 만남
  - `cout.flush()` 호출

---

## 3. 기본 입출력 (iostream)

### cout (출력)
```cpp
#include <iostream>
using namespace std;

cout << "Hello" << endl;
cout << 123 << " " << 3.14 << endl;
```

### cin (입력)
```cpp
int n;
string str;

cin >> n;           // 공백 전까지 읽음
cin >> str;         // 공백 전까지 읽음
```

> **주의**: `cin >>`은 공백, 탭, 엔터를 구분자로 사용

---

## 4. 문자/문자열 입력

### cin.get()
- **한 문자**씩 읽음
- 공백, 탭, 엔터도 읽음

```cpp
char ch;
ch = cin.get();      // 한 문자 읽기
cin.get(ch);         // 같은 동작

// 여러 문자 읽기
char buf[100];
cin.get(buf, 100);   // 최대 99자 + '\0'
```

### cin.getline()
- **한 줄** 전체를 읽음
- 구분자(기본: `\n`)를 만나면 종료
- **구분자를 버퍼에서 제거**함

```cpp
char buf[100];
cin.getline(buf, 100);         // '\n' 전까지 읽고 '\n' 제거
cin.getline(buf, 100, ';');    // ';' 전까지 읽고 ';' 제거
```

### getline() - string용
```cpp
#include <string>

string str;
getline(cin, str);             // 한 줄 전체 읽기
getline(cin, str, ';');        // ';' 전까지 읽기
```

### cin >> 와 getline 혼용 문제
```cpp
int age;
string name;

cin >> age;          // 숫자 입력 후 Enter
// 버퍼에 '\n'이 남아있음!
getline(cin, name);  // '\n'만 읽고 끝남

// 해결: ignore() 사용
cin >> age;
cin.ignore();        // '\n' 제거
getline(cin, name);  // 정상 동작
```

---

## 5. 포맷 플래그

### 주요 포맷 플래그

| 플래그 | 설명 |
|--------|------|
| `ios::left` | 왼쪽 정렬 |
| `ios::right` | 오른쪽 정렬 |
| `ios::dec` | 10진수 출력 |
| `ios::hex` | 16진수 출력 |
| `ios::oct` | 8진수 출력 |
| `ios::showbase` | 진법 접두어 표시 (0x, 0) |
| `ios::showpoint` | 소수점 항상 표시 |
| `ios::fixed` | 고정 소수점 표기 |
| `ios::scientific` | 과학적 표기법 |

### 사용법
```cpp
// setf()로 설정
cout.setf(ios::hex);
cout << 255 << endl;  // ff

// unsetf()로 해제
cout.unsetf(ios::hex);

// 조작자(manipulator) 사용
cout << hex << 255 << endl;
cout << dec << 255 << endl;
```

---

## 6. 조작자 (Manipulator)

### `<iomanip>` 헤더 필요

```cpp
#include <iomanip>
```

### 주요 조작자

| 조작자 | 설명 |
|--------|------|
| `setw(n)` | 출력 너비 n 설정 |
| `setfill(c)` | 빈 공간을 c로 채움 |
| `setprecision(n)` | 유효 자릿수 n |
| `fixed` | 고정 소수점 |
| `left`, `right` | 정렬 방향 |
| `endl` | 줄바꿈 + 버퍼 비우기 |
| `hex`, `dec`, `oct` | 진법 변환 |

### 사용 예제
```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    // 너비와 채우기
    cout << setw(10) << 123 << endl;          // "       123"
    cout << setfill('0') << setw(5) << 42;    // "00042"
    
    // 소수점
    double pi = 3.14159265;
    cout << fixed << setprecision(2) << pi;   // "3.14"
    
    // 정렬
    cout << left << setw(10) << "Hi" << "|";  // "Hi        |"
    cout << right << setw(10) << "Hi" << "|"; // "        Hi|"
    
    // 진법
    cout << hex << 255 << endl;  // ff
    cout << oct << 255 << endl;  // 377
    cout << dec << 255 << endl;  // 255
    
    return 0;
}
```

---

## 7. 파일 입출력

### 헤더
```cpp
#include <fstream>
```

### 파일 쓰기 (ofstream)
```cpp
ofstream fout("data.txt");   // 파일 열기
if (!fout) {
    cout << "파일 열기 실패" << endl;
    return 1;
}

fout << "Hello, File!" << endl;
fout << 123 << " " << 3.14 << endl;

fout.close();  // 파일 닫기
```

### 파일 읽기 (ifstream)
```cpp
ifstream fin("data.txt");
if (!fin) {
    cout << "파일 열기 실패" << endl;
    return 1;
}

string line;
while (getline(fin, line)) {
    cout << line << endl;
}

fin.close();
```

### 파일 열기 모드

| 모드 | 설명 |
|------|------|
| `ios::in` | 읽기 모드 |
| `ios::out` | 쓰기 모드 |
| `ios::app` | 파일 끝에 추가 |
| `ios::trunc` | 기존 내용 삭제 |
| `ios::binary` | 바이너리 모드 |

```cpp
ofstream fout("data.txt", ios::app);  // 추가 모드
```

---

## 8. 바이너리 파일 입출력

### write()와 read()
```cpp
// 쓰기
ofstream fout("data.bin", ios::binary);
int arr[] = {1, 2, 3, 4, 5};
fout.write((char*)arr, sizeof(arr));
fout.close();

// 읽기
ifstream fin("data.bin", ios::binary);
int arr2[5];
fin.read((char*)arr2, sizeof(arr2));
fin.close();
```

---

## 9. 스트림 상태 확인

### 상태 함수

| 함수 | 설명 |
|------|------|
| `good()` | 모든 상태 정상 |
| `eof()` | 파일 끝 도달 |
| `fail()` | 입출력 실패 |
| `bad()` | 심각한 오류 |
| `clear()` | 상태 플래그 초기화 |

```cpp
ifstream fin("data.txt");

while (!fin.eof()) {
    string line;
    getline(fin, line);
    if (fin.good())
        cout << line << endl;
}

if (fin.eof())
    cout << "파일 끝에 도달" << endl;
```

---

## 10. 요약 비교표

### 입력 함수 비교

| 함수 | 대상 | 공백 처리 | 구분자 처리 |
|------|------|----------|------------|
| `cin >>` | 단어 | 공백에서 멈춤 | 버퍼에 남김 |
| `cin.get()` | 한 문자 | 읽음 | 버퍼에 남김 |
| `cin.getline()` | char[] | 읽음 | 버퍼에서 제거 |
| `getline()` | string | 읽음 | 버퍼에서 제거 |

### 파일 스트림

| 클래스 | 용도 |
|--------|------|
| `ifstream` | 파일 읽기 |
| `ofstream` | 파일 쓰기 |
| `fstream` | 읽기/쓰기 |
