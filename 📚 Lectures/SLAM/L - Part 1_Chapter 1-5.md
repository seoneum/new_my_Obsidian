---
tags:
  - lecture
  - lecture/SE
  - tagging/needed
aliases: []
type: lecture
created: 2025-12-22
updated: 2026-01-18T16:42:53
group: SE
status:
  - "[[🌱Seed]]"
course: SLAM/SLAM BIBLE
session: 2025-12-22/01/05
instructor: SLAMSLAM
author: [[장형기|SLAMSLAM]]
migrated_from: CMDS/200. CMDS/201. Connect/Fastcampus_SLAM/L - Part 1_Chapter 1-5.md
domain:
  - robotics
cmds: connect
---

# Part 1_Chapter 1-5

## Meta
- Course: SLAM/SLAM BIBLE
- Session: 2025-12-22/01/05
- Instructor: SLAMSLAM
- URL: 

## Outline
- 

## Raw Notes
- SLAM이란
1. Part 1 : SLAM표기 방법
	1) Visual SLAM : 카메라를 사용
	2) LiDAR SLAM : LiDAR를 사용
	3) RADAR SLAM : RADAR 사용
	4) Sensor Fusion SLAM : 다수의 이종 센서 함께 사용
	5) 다른 것들
	   wheel encoder -> wheel, IMU -> Inertial, GPS -> GNSS
2. Visual SLAM
	- 장점 : 저렴이 센서, 성능 조정/딥러닝/시각화 쉬움, 센서 빠름(algorithm도 빨라야함).
	- 단점 : 갑작스러운 변화 대응 불가능, 어두운 곳 사용 불가능
	- 종류
		- Monocular : 카메라 1개
			- 장 : setup비용 저렴, 구성 단순해짐
			- 단 : **Scale ambiguity**[^1] , Metric-Scale❌[^2], 3차원 공간을 실제 비율로 추정 불가능 <- 실제 비율의 motion을 가진 proprioceptive 센서 필요.
			- Algorithm : DSO, ORB-SLAM, LSD-SLAM 등등
		- Stereo/Multi : 2개 이상
		  인접 카메라들간의 baseline[^3] 거리로 삼각 측량 -> 거리/깊이 추정.
			- 장 : 실제 세상 비율에 맞춘 3D 복원 가능(Metric-Scale path-plannig가능)
			- 단 : baseline이 정확해야함. 즉 정교한 설정, 캘리브레이션 잘 해야함
			  Synchronized Camera설정[^4] 해야함. 정확한 캘리 어려움.
			  모든 픽셀에 disparity, depth 계산하려면 연산량 지림.
		- RGB-D : Depth카메라 사용
			- 장 : Dense mapping하기 좋다!
			- 단 : 10~15m 수준만 depth가 정확. 실외 사용 힘듦. 
		- Visual-inertial/-wheel : 카메라+IMU 사용
			- 장 : 실제 비율/위치/지도 알 수 있음, 카메라 실패 지점에서 IMU, wheel 대체됨
			- 단 : 센서들의 캘리 정말 힘들다. 
3. LiDAR SLAM
	- Point cloud 정합해 위치변화 추정하고 지도 생성
	- 장 : 데이터 자체가 3D geometry포함. range 넓음(~300). 정확. 밤에도 가능
	- 단 : 비쌈. 센서 속도 느림(10Hz 정도) <- **deskew**[^5] , RGB color매핑 불가능
	- 종류
		- 2D LiDAR
			- 한 줄로 스캔 됨(Line scanne)
			- 장 : 2D Occupancy 지도를 얻기 쉬움
			- 단 : 주어진 높이에 대한 2D지도. ~50m로 짧음.
			- 대표 algorithm : [Google Cartographer](https://google-cartographer-ros.readthedocs.io/en/latest/)
		- 3D LiDAR
			- 채널 = 높이 각. 즉 2d는 1채널이다.
			- 장 : 넓은 3D공간 정확하게 mapping가능
			- 단 : 비쌈. 속도 느림. 색상 정보 불가능.
			- 대표 algorithm : [LiTAMIN2](https://www.alphaxiv.org/ko/overview/2103.00784) 연산 빠름. 
		- LiDAR-inertial/-wheel SLAM
			- 장 : 더 정확한 Point cloud 정합/de-skew. LiDAR실패 지점에서 다른 센서의 정확한 추정.
			- 단 : 캘리 어려움
			- 대표 algorithm : LIO-SAM
		- Sensor Fusion SLAM
			- 다양한 센서 퓨전해서 장점만 냠냠. 실시간 데이터 -> 서버에서 Offline Reconstruction
			- 장 : 가장 정확한 map 생성
			- 단 : 캘리 개빡셈. 센서/ 플랫폼 단가 높음.
			- 흰 벽같은 변하지 않는 장소의 경우 움직여도 라이다, 카메라가 받아들이지 못함. 하지만 이런 경우 IMU가 잡아내준다!

## Questions
- 

## Merge Candidates
- [[ ]] 

## Priori Lecture
- [[L - Part 1_Chapter 1-4]] 

[^1]: 거리 모호성, 3D차원에서 거리값(depth) 알 수 없음.

[^2]: m단위로 인지. 

[^3]: 카메라 간의 거리. 약간 미간 길이 이런 느낌, 미간 길이 알고 물체와 카메라 각도 알면 직선거리를 알 수 있다.

[^4]: 코드로 할 경우 sequential하기 때문에 하드웨어적 회로 설계 필요.
	CLK -> GPIO signal -> 동시에 따닥 찍히기

[^5]: LiDAR가 도는동안 움직이기에 원이 틀어짐. 그것을 바로잡는 역할
