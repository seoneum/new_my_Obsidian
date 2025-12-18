## Philosophy tag를 이용한 연결
```dataview
List
FROM #Philosophy 
```
dataview로 모여있는 그래프는 실제 그래프와 상관 없음
```dataview
TABLE 
	link,
	author as "사람"
FROM #Philosophy 
WHERE CMDS = "Connet"
```

- List : 리스트로 보여줌
- TABLE : 표로 보여줌

## 나만의 도서관 만들기
```dataview
TABLE without id
	author as Author,
	"![|50]("+cover_url+")" as Cover,
	link(file.link, title) as Title
FROM #📚Book 
```

## Reference
- [데이터뷰 티스토리](https://kaminik.tistory.com/entry/Dataview-%ED%94%8C%EB%9F%AC%EA%B7%B8%EC%9D%B8-%EC%86%8C%EA%B0%9C)
- [Dataview Official](https://blacksmithgu.github.io/obsidian-dataview/)
- [Dataview query builder](https://s-blu.github.io/basic-dataview-query-builder/) : 쓰고 싶은 것 쓰면 문법 보여줌