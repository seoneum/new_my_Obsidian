---
tags:
  - setting
  - Syntax
  - Markdown
---
# Markdown Syntax Guide for Researchers

## Headings
```
# H1 
## H2 
### H3 
#### H4 
##### H5 
###### H6
```
# This is Heading 1 
## This is Heading 2 
### This is Heading 3 
#### This is Heading 4 
##### This is Heading 5 
###### This is Heading 6
 

---

## Basic Formatting

### Bold
`**볼드체 텍스트**` or `__볼드체 텍스트__`
**볼드체 텍스트**
이런 문장에서 **이 단어**만 강조하고 싶다.

### Italic
`*이탤릭체 텍스트*` or `_이탤릭체 텍스트_`
*이탤릭체 텍스트*
이런 문장에서 *이 단어*만 기울이고 싶다.
### Strikethrough
`~~취소선 텍스트~~`
~~취소선 텍스트~~
~~취소선~~



### Bold and Italic
`***볼드체와 이탤릭체 함께***` or `___볼드체와 이탤릭체 함께___`
***볼드체와 이탤릭체 함께***

---

## Lists

### Ordered List
```
1. First item 
2. Second item 
3. Third item
```
1. First item 
2. Second item 
3. Third item


### Unordered List
```
- First item 
- Second item 
- Third item
```
- 순서
	- First item 
	- Second item 
	- Third item
- 내용
- 불렛
	- TAB 들여쓰기
		- INDENT
	- shift+tab
	- 1
	- 2
	- 3


### Task List 
```
- [x] Write the literature review
- [x] Collect data
- [ ] Analyze results
```
- [x] Write the literature review
- [x] Collect data
- [ ] Analyze results

체크박스
논문 읽기
초록 200자 작성하기

- [x] 빵
- [x] 우유
- [x] 계란 ✅ 2025-12-22
- [x] 논문리뷰
- [x] 리비전 교정 표 만들기 ✅ 2025-12-22
- [x] 이거 했어

---

## Code

### Inline Code
```
Use the `print()` function in Python.
```
Use the `print()` function in Python.
기본적인 함수: `y=f(x)`
`Ctrl + y`

`term a` 
`이 용어`는 굉장히 중요합니다. `구요한`은 사람입니다.



### Code Block
````
```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
```
````

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
```
\[\[Markdown for Prompt Engineering 예시]]

```text
구요한은 커맨드스페이스 소속입니다.
- 정보 1
- 정보 2
```



---

## Links and References

### External Link
```
[Markdown Guide](https://www.markdownguide.org)
```
\[Markdown Guide](https://www.markdownguide.org)
\[네이버 주소](https://www.naver.com)
\[커맨드스페이스 유튜브](https://www.youtube.com/@cmdspace)
\[더배러 뉴스레터 아티클](https://stibee.com/api/v1.0/emails/share/RE-vXyUeRwta62Y40iRhUtKkFzqMNSQ)
![뉴스레터 이미지|300](https://img2.stibee.com/93641_2237554_1718685222867507626.jpeg)

![유튜브 영상](https://youtu.be/LxvbzoCfdw0?si=6aMkxTgci-P4IQIp)
![영상](https://youtu.be/LxvbzoCfdw0?si=6aMkxTgci-P4IQIp)


### Internal Link (for tools that support it)
```
[[Research Methods]]
```
[[Research Methods]]
[[🔖 Knowledge Connectivity]]
[[📜 The Power of Niklas Luhmann's Social Systems Theory in a Postmodern World]]

[[새로운 지식]]을 마주하는 일[^knowledge]은 지금 [[우리가 살고 있는 사회에서 필요조건]]으로 자리하였다. [[우리가 기존]]에 쌓아온 가치체계와 [[지식 시스템]]을 통해 이 "새로움"을[[ 어떻게 수용하고 이해할 수 있을지 고민]]해 보자.

[^knowledge]: 지식이란 말이다. 이런거야.
### Footnote
```
Here's a sentence with a footnote.[^1]

[^1]: This is the footnote content.
```
Here's a sentence with a footnote.[^1]

[^1]: This is the footnote content.



내가 밥을 먹었는데 치킨이 먹고싶더라. [^2]

[^2]: 나의 감정을 표현한 글



---

## Quotes and Callouts

### Blockquote
```
> This is a blockquote.
> It can span multiple lines.
```
> This is a blockquote.
> It can span multiple lines.

> 밥을 많이 먹으면 살이 찌더라.
> —구요한


> 이런 사람이 이렇게 말했다.
> —책 제목, 저자

> [!NOTE]
> 이런 사람이 이렇게 말했다.
> —책 제목, 저자

> [!Quote]
> 이런 사람이 이렇게 말했다.
> —책 제목, 저자
> > 그 다음 내용
> > 두 번째 줄
> > >
> > > 내용
### Nested Blockquotes
```
> This is the first level of quoting.
>
> > This is nested blockquote.
>
> Back to the first level.
```
> This is the first level of quoting.
>
> > This is nested blockquote.
>
> Back to the first level.

---

## Images

```
![Alt text](image-url.jpg "Optional title")
```

![text|400](https://i.ytimg.com/vi/4WZ-6EomEzE/hqdefault.jpg?sqp=-oaymwEcCNACELwBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLAD0hVGWBzhVGY0UpjMWIKYWx-Rdg)
![[Pasted image 20240627022953.png|400]]


---

## Tables

```
| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Row 1, Col 1 | Row 1, Col 2 | Row 1, Col 3 |
| Row 2, Col 1 | Row 2, Col 2 | Row 2, Col 3 |
```

| number | name |     |
| ------ | ---- | --- |
| 내용     | 내용2  |     |
|        |      |     |
 ## 표: Arrival vs. Contact - 제목과 관점의 차이

| **항목**        | **Arrival** (서양)                               | **Contact** (한국)                         |
| ------------- | ---------------------------------------------- | ---------------------------------------- |
| **영화 제목의 의미** | 외계인의 도착이라는 구체적이고 사건 중심적인 의미를 강조                | 인간과 외계인 간의 접촉과 상호작용을 강조                  |
| **문화적 사고방식**  | 서양: 분류적 사고방식 - 개별 사건이나 객체를 독립적으로 이해하려는 경향      | 한국: 관계론적 사고방식 - 사물 간의 관계와 상호작용을 중시       |
| **주제 강조점**    | 사건 중심: 외계인의 "도착"이라는 물리적, 시간적 개념에 집중            | 관계 중심: 인간과 외계인의 "접촉"과 상호작용에 초점           |
| **관련 시사점**    | - 구체적 사건과 객체를 분석하고 독립적으로 이해- 지식을 개별적으로 분류하고 평가 | - 상호작용과 관계를 통해 맥락을 이해- 지식을 통합적으로 파악하고 적용 |
|               |                                                |                                          |

| A   | B   |
| --- | --- |
| 1   | 2   |

| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Row 1, Col 1 | Row 1, Col 2 | Row 1, Col 3 |
| Row 2, Col 1 | Row 2, Col 2 | Row 2, Col 3 |

---

## Horizontal Rule

```
---
```

---

## Mathematical Equations (LaTeX)

Many Markdown processors support LaTeX for mathematical equations.

### Inline Math
```
This is an inline equation: $E = mc^2$
```
This is an inline equation: $E = mc^2$
$y=f(x)$는 함수입니다.
### Display Math
```
This is a display equation:

$$
\frac{\partial f}{\partial x} = 2\sqrt{a}x
$$
```
This is a display equation:

$$
\frac{\partial f}{\partial x} = 2\sqrt{a}x
$$

근의공식:
$$
x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
$$



---

## Citations (for academic writing)

Some Markdown flavors (like Pandoc) support citations:

```
According to recent studies [@smith2023; @johnson2022], ...
```

---

## Abbreviations

```
The HTML specification is maintained by the W3C.

*[HTML]: Hyper Text Markup Language
*[W3C]: World Wide Web Consortium
```

The HTML specification is maintained by the W3C.

*[HTML]: Hyper Text Markup Language
*[W3C]: World Wide Web Consortium

---

## Highlighting (supported in some flavors)

```
Here's some ==highlighted text==.
```
Here's some ==highlighted text==.

---

Remember that support for some of these features (especially LaTeX equations, citations, and certain extensions) may vary depending on the Markdown processor or platform you're using. Always check your specific environment's capabilities and syntax requirements.

