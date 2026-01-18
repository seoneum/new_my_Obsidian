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
title: L - Part 1_Chapter 1-2
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
start_read_date: 2025-12-21T04:21:00
finish_read_date: 2025-12-21T04:21:00
migrated_from: CMDS/200. CMDS/201. Connect/Fastcampus_SLAM/L - Part 1_Chapter 1-2.md
domain:
  - robotics
cmds: connect
---
# L - Part 1_Chapter 1-2

## Meta
- Course: SLAM/SLAM_BIBLE
- Session: 2025-12-21/01/02
- Instructor: SLAMSLAM
- URL: https://fastcampus.co.kr/me/course

## Outline
- 

## Raw Notes
- 모바일 로보틱스
1. 로보틱스
	- 산업 로봇(다관절 로봇 팔, scara 로봇, Delta 로봇)	
	- 로봇 3요소 : 인지(물체를 인지)-판단-제어
	- 레일, caterpillar[^1], 바퀴, 다리 활용으로 workspace 확장할 수 있음
2. 모바일 로보틱스
	- mobile : 움직이는
	- robotics : 로봇
	- 공간의 제약이 사라짐
	- Perception : 이동 가능한 공간을 인지.(벽/장애물, 빈 공간)
		- 센서를 통해 인지를 함.
		- Exteroceptive sensor(외부/카메라, 라이다 등), Proprioceptive sensor(내부/imu, encoder 등). 
		- 기본 제어 루프 : sensor값 받기 -> 이동
			- 문제점 발생 : exteroceptive와 proprioceptive값이 다를 수 있고 센서 값이 불안정할 경우 전체 시스템 불안정해짐.
			- 센서에 따라 noise가 낀다! -> 누적 오차 짱 커짐. -> 평균 구해서 오차 줄임.
			- Exteroceptive는 평균 구해서 줄일 수 있음. 하지만 수집 중 이동 불가능.
			- Proprioceptive는 한 이동에 하나의 데이터만 수집 가능함.
			- **모든 센서는 특정 확률 분포를 따름** -> 모든 센서가 따르는 확률 분포를 통한 최적의 이동치/지도가 존재할 수도 있다!! -> Optimal pose/map

## Questions
-  여기까지는 무난한듯 ?

## Merge Candidates
- [[ ]] 

## Priori Lecture
- [[L - Part 1_Chapter 1-1]]


[^1]: caterpillar : 무한궤도임
