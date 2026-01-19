# C++ STL 레퍼런스

> 과제와 시험에서 자주 사용하는 C++ 표준 라이브러리 함수 정리

---

## 1. 문자열 처리 (C 스타일) - `<cstring>`

### 문자열 복사
```cpp
#include <cstring>

char str1[20];
char str2[] = "Hello";

strcpy(str1, str2);        // str2를 str1에 복사
strncpy(str1, str2, 5);    // 최대 5글자만 복사 (안전)
```

### 문자열 연결
```cpp
char str1[20] = "Hello";
char str2[] = " World";

strcat(str1, str2);        // str1 뒤에 str2 추가
strncat(str1, str2, 3);    // 최대 3글자만 추가
```

### 문자열 비교
```cpp
strcmp("abc", "abc");      // 0 (같음)
strcmp("abc", "abd");      // -1 (str1 < str2)
strcmp("abd", "abc");      // 1 (str1 > str2)
strncmp("abc", "abd", 2);  // 처음 2글자만 비교
```

### 문자열 길이/검색
```cpp
strlen("Hello");           // 5 ('\0' 제외)
strchr("Hello", 'l');      // 'l'의 첫 위치 포인터
strrchr("Hello", 'l');     // 'l'의 마지막 위치 포인터
strstr("Hello World", "Wo"); // "World"의 위치 포인터
```

---

## 2. 메모리 처리 - `<cstring>`

```cpp
char arr[10];

memset(arr, 0, sizeof(arr));        // 0으로 채우기
memcpy(dest, src, size);            // 메모리 복사
memmove(dest, src, size);           // 겹쳐도 안전한 복사
memcmp(arr1, arr2, size);           // 메모리 비교
```

---

## 3. 동적 메모리 할당

```cpp
// C++ 스타일 (권장)
int* ptr = new int;              // 단일 변수
int* arr = new int[10];          // 배열

delete ptr;                      // 단일 해제
delete[] arr;                    // 배열 해제

// C 스타일 (사용 지양)
int* ptr = (int*)malloc(sizeof(int) * 10);
free(ptr);
```

---

## 4. 입출력 - `<iostream>`

### 콘솔 입출력
```cpp
#include <iostream>
using namespace std;

// 출력
cout << "Hello" << endl;
cout << 123 << " " << 3.14 << endl;

// 입력
int n;
string str;
cin >> n;                        // 공백 전까지
getline(cin, str);               // 한 줄 전체
```

### 파일 입출력 - `<fstream>`
```cpp
#include <fstream>

// 쓰기
ofstream outFile("data.txt");
outFile << "Hello" << endl;
outFile.close();

// 읽기
ifstream inFile("data.txt");
string line;
getline(inFile, line);
inFile.close();
```

---

## 5. 문자열 (C++ 스타일) - `<string>`

```cpp
#include <string>

string str = "Hello";

// 기본 함수
str.length();                    // 길이
str.size();                      // 길이 (동일)
str.empty();                     // 비어있는지
str.clear();                     // 비우기

// 추가/삭제
str.push_back('!');              // 뒤에 추가
str.pop_back();                  // 뒤에서 제거
str.append(" World");            // 문자열 추가
str.insert(5, "XX");             // 5번 위치에 삽입
str.erase(0, 2);                 // 0번부터 2개 삭제

// 검색/변환
str.find("lo");                  // "lo"의 위치 (없으면 string::npos)
str.substr(0, 3);                // 부분 문자열
str.c_str();                     // C 스타일 문자열로 변환
```

---

## 6. 벡터 (동적 배열) - `<vector>` ⭐

```cpp
#include <vector>

vector<int> v;

// 추가/삭제
v.push_back(10);                 // 뒤에 추가
v.pop_back();                    // 뒤에서 제거
v.insert(v.begin() + 2, 99);     // 2번 위치에 삽입
v.erase(v.begin() + 1);          // 1번 위치 삭제
v.clear();                       // 전체 삭제

// 접근/정보
v[0];                            // 인덱스 접근
v.at(0);                         // 범위 체크하는 접근
v.front();                       // 첫 요소
v.back();                        // 마지막 요소
v.size();                        // 크기
v.empty();                       // 비어있는지
v.capacity();                    // 할당된 용량
```

---

## 7. 스택 - `<stack>` ⭐

```cpp
#include <stack>

stack<int> s;

// 기본 연산
s.push(10);                      // 삽입
s.pop();                         // 삭제 (반환 없음!)
s.top();                         // 최상단 요소 보기
s.size();                        // 크기
s.empty();                       // 비어있는지
```

**⚠️ 주의:** `pop()`은 요소를 반환하지 않음!
```cpp
// ❌ 잘못된 사용
int val = s.pop();  // 에러!

// ✅ 올바른 사용
int val = s.top();  // 먼저 확인
s.pop();            // 그 다음 삭제
```

---

## 8. 큐 - `<queue>`

```cpp
#include <queue>

queue<int> q;

// 기본 연산
q.push(10);                      // 삽입
q.pop();                         // 삭제 (반환 없음!)
q.front();                       // 앞 요소
q.back();                        // 뒤 요소
q.size();                        // 크기
q.empty();                       // 비어있는지
```

---

## 9. 정렬/알고리즘 - `<algorithm>` ⭐

```cpp
#include <algorithm>

int arr[] = {5, 2, 8, 1, 9};
vector<int> v = {5, 2, 8, 1, 9};

// 정렬
sort(arr, arr + 5);                  // 배열 정렬
sort(v.begin(), v.end());            // 벡터 정렬
sort(v.begin(), v.end(), greater<int>());  // 내림차순

// 검색
find(v.begin(), v.end(), 8);         // 8 찾기
binary_search(v.begin(), v.end(), 5);  // 이진 탐색 (정렬 필요)

// 최대/최소
max(10, 20);                     // 20
min(10, 20);                     // 10
max_element(v.begin(), v.end()); // 최댓값 위치 (반복자)
min_element(v.begin(), v.end()); // 최솟값 위치

// 역순/채우기
reverse(v.begin(), v.end());     // 역순 정렬
fill(v.begin(), v.end(), 0);     // 0으로 채우기
```

---

## 10. 수학 함수 - `<cmath>`

```cpp
#include <cmath>

// 기본 연산
abs(-5);                         // 절댓값 (정수)
fabs(-3.14);                     // 절댓값 (실수)
pow(2, 3);                       // 2^3 = 8
sqrt(16);                        // 제곱근 = 4
ceil(3.2);                       // 올림 = 4
floor(3.8);                      // 내림 = 3
round(3.5);                      // 반올림 = 4

// 삼각함수
sin(3.14);
cos(3.14);
tan(3.14);
```

---

## 11. 시간/난수 - `<ctime>`, `<cstdlib>`

```cpp
#include <ctime>
#include <cstdlib>

// 시간 측정
clock_t start = clock();
// ... 코드 실행 ...
clock_t end = clock();
double time = (double)(end - start) / CLOCKS_PER_SEC;

// 난수 생성
srand(time(NULL));               // 시드 설정 (한 번만)
int random = rand();             // 0 ~ RAND_MAX
int dice = rand() % 6 + 1;       // 1 ~ 6
```

---

## 12. 유틸리티 - `<utility>`

```cpp
#include <utility>

// pair (두 개 묶음)
pair<int, string> p = {1, "Hello"};
p.first;                         // 1
p.second;                        // "Hello"
pair<int, int> p2 = make_pair(10, 20);

// swap
int a = 10, b = 20;
swap(a, b);                      // a=20, b=10
```

---

## 13. 입출력 조작 - `<iomanip>`

```cpp
#include <iomanip>

// 출력 형식 조정
cout << setw(10) << 123;                      // 너비 10으로 출력
cout << setfill('0') << setw(5) << 42;        // 00042
cout << fixed << setprecision(2) << 3.14159;  // 3.14
cout << left << setw(10) << "Hi";             // 왼쪽 정렬
```

---

## 14. 문자 판별 - `<cctype>`

```cpp
#include <cctype>

isalpha('A');        // 알파벳인지
isdigit('5');        // 숫자인지
isspace(' ');        // 공백인지
isalnum('a');        // 알파벳 또는 숫자인지
isupper('A');        // 대문자인지
islower('a');        // 소문자인지
toupper('a');        // 대문자로 변환 → 'A'
tolower('A');        // 소문자로 변환 → 'a'
```

---

## 15. 자주 쓰는 헤더 요약

| 헤더 | 용도 | 주요 함수/클래스 |
|------|------|-----------------|
| `<iostream>` | 입출력 | `cout`, `cin`, `endl` |
| `<string>` | 문자열 | `string`, `getline` |
| `<vector>` | 동적 배열 | `vector<T>`, `push_back`, `pop_back` |
| `<stack>` | 스택 | `stack<T>`, `push`, `pop`, `top` |
| `<queue>` | 큐 | `queue<T>`, `push`, `pop`, `front` |
| `<algorithm>` | 알고리즘 | `sort`, `find`, `reverse` |
| `<cmath>` | 수학 | `abs`, `pow`, `sqrt` |
| `<cstring>` | C 문자열 | `strcpy`, `strlen`, `strcmp` |
| `<iomanip>` | 출력 형식 | `setw`, `setprecision`, `fixed` |
| `<cctype>` | 문자 판별 | `isalpha`, `isdigit`, `toupper` |

---

## 16. 종합 예제

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <stack>
#include <algorithm>
using namespace std;

int main() {
    // string
    string str = "Hello";
    str.push_back('!');
    cout << str << endl;  // Hello!
    
    // vector
    vector<int> v = {3, 1, 4, 1, 5};
    sort(v.begin(), v.end());
    v.push_back(9);
    
    // stack
    stack<int> s;
    s.push(10);
    s.push(20);
    cout << s.top() << endl;  // 20
    s.pop();
    
    return 0;
}
```
