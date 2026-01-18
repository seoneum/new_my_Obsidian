---
tags:
  - lecture
  - lecture/SE
  - tagging/needed
aliases: []
index:
  - "[[🏷 Lecture Notes]]"
type:
  - lecture
title: L - Part 1_Chapter 1-3
created: 2025-12-21
cover_url: {}
updated: 2026-01-18T16:42:53
my_rate: {}
authors:
  - "[[장형기|SLAMSLAM]]"
CMDS:
  - Connect
started: 2025-12-21
status:
  - "[[🌱Seed]]"
group:
  - SE
publishDate: {}
start_read_date: 2025-12-21T05:04:00
finish_read_date: 2025-12-21T05:04:00
migrated_from: CMDS/200. CMDS/201. Connect/Fastcampus_SLAM/L - Part 1_Chapter 1-3.md
domain:
  - robotics
cmds: connect
---
# L - Part 1_Chapter 1-3

## Meta
- Course: SLAM/SLAM BIBLE
- Session: 2025-12-21/01/03
- Instructor: SLAMSLAM
- URL: https://fastcampus.co.kr/me/course

## Outline
- 

## Raw Notes
### Localization, Mapping, SLAM
1. Navigation
	- Map-less navigation
		- 지도 없이 공간 탐색
		- 종료 지점 선택 불가
	- Map-based navigation
		- A ->B지점 까지 정확한 경로 탐색 가능
		- 모든 obstacle 위지 앎
2. Localization, Mapping
	- Localization
		- 지도가 있을 때, 내 위치는?
		- 정확한 Exteroceptive로 부정확한 Proprioceptive 개선
		- 즉 정확한 지도 + 외부 센서 데이터 = 내 위치 추정
	- Mapping
		- Exteroceptive + Proprioceptive -> 지도 제작
		- 정확한 Proprioceptive로 부정확한 Exteroceptive 개선
		- 즉 내 움직임 + 외부 센서 데이터 = 지도 완성!
	- 자율주행 시나리오
		- Mapping : 정확한 위치 정보 -> HD-Map 생성
		- Localization : HD-Map기반으로 자동차의 위치 추정
		-> 존나 자세한 navigation가능 - path plannig가능하는 것
	- 사용처 : 차, VR, drone등등
	- 공간 + 위치
3. SLAM
	- Localization, Mapping의 한계
		- 정확한 지도, 정확한 위치 정보 필요함. 언뜻 보면 상호 보완 가능하다고 느껴지지만 
		다시 생각해보면 정확하게 만들기 힘들다는 순환 오류 발생함.
		- 기본 패러다임 운용
		  1) 비싼 센서로 위치 추정
		  2) 위치 정보로 지도 제작
		  3) 비싼 센서 떼고 부착 센서로 위치 추정. 
		  -> 돈 없으면? 공간 너무 크면? 자주 변하는 환경이면? -> SLAM 출현
	- SLAM
		- Simultaneous Localization and Mapping
			- Simultaneous : 동시적
			- Localization : 위치추정
			- Mapping : 지도 작성
				-> 사전 정보 없이 Optimal pose[^1]/map simultaneous으로 추정
			- Deep learning 결합 -> 위치뿐 아닌 의미까지 포함하는 Semantic Map
			- 공간 + 위치 + 상태
![[Pasted image 20251221050835.png]]
## Questions
- 

## Merge Candidates
- [[ ]] 

## Priori Lecture
- [[L - Part 1_Chapter 1-2]]

[^1]: 이동치
