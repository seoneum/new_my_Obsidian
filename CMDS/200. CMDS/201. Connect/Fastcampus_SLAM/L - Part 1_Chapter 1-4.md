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
title: L - Part 1_Chapter 1-4
created: 2025-12-21
cover_url: ""
updated: 2025-12-21T05:02:58
my_rate: ""
authors:
  - "[[장형기|SLAMSLAM]]"
CMDS:
  - Connect
started: 2025-12-21
status:
  - "[[🌱Seed]]"
group:
  - SE
  - ROBOTICS
publishDate: ""
start_read_date: 2025-12-21T22:47:00
finish_read_date: ""
---
# L - Part 1_Chapter 1-4

## Meta
- Course: SLAM/SLAM BIBLE
- Session: 2025-12-21/01/04
- Instructor: SLAMSLAM
- URL: https://fastcampus.co.kr/me/course

## Outline
- 

## Raw Notes
- .
1. Sensors
	1) Proprioceptive sensor
		- 내부 인지 센서.
		- Wheel encoder
			- 이동량[^1]  측정 센서
			- 장점 : 자동차/최신 로봇 모터에 탑재
			- 단점 : Drift[^2] 취약. 헛돌거나 둘레 변형 시 오차 ⬆️
			![[Pasted image 20251221144414.png|300]]
		- IMU
			- Linear accelerator, Angular accelerator 측정.
			- 가속도계와 자이로를 통한 측정. (+ 자기장도 요즘 있음), 각 3축.
			- 가속도를 적분 할 경우 noise 줄이고 적분 함.
			- 장점 : 일반적으로 싸다! 성능 일반적으로 괜찮다!
			- 단점 : Drift 누적 개빠름
			- ![[Pasted image 20251221145306.png|300]]
		- Forward kinematics (alias FK)
			- 인코더를 통해 다중 관절 움직임 계산 + end-effecter[^3]의 위치 계산
			- 장점 : 최신은 인코더 있음.
			- Leg odometry : 다리의 모션 계산 가능. 하지만 몸 전체 기우는 것 인지 불가능.
	2) Exteroceptive sensor
		- 외부 환경 인지 센서. 
		- GNSS
			- 위성 비콘 기반 위치 추정. 삼각측량 사용함. (국어 비콘 지문 생각하면 빠를듯)
			- 범위가 지구임. 4개의 위성은 있어야함.
			- 나라마다 이름, 서비스 수준의 차이가 있긴 함.
			![[Pasted image 20251221180301.png|400]]
			- 방식
				- GNSS - SPS (Standard Positioning System)
					- 가장 기본. 10~20m 정도의 오차 존재. 위성 신호를 직접 받음.
					- 직접 신호를 받기 때문에 Canopy[^4]현상이 나타나 오차가 커짐
					-> 싸다! 하지만 정밀하진 않다
					![[Pasted image 20251221180523.png|300]]
				- GNSS - DGPS (Differential GPS)
					-  기지국 위치를 기반으로 보정. 1~3m오차.
					- 인공위성에서도 받고 기지국(Ground truth[^5])에서도 받아 보정하는 것.
					- sps보다 훨씬 정확하지만 비싸다. 또 기지국 반경 200km내에 있어야함.
					![[Pasted image 20251221180732.png|400]]
				- GNSS - PTK - GPS (Real time GPS)
					- 근거리 기지국 기반 보정.  ~10cm 오차
					- 가정 정확(Ground truth 수준)하지만 개비쌈. 기지국 20km이내.
					![[Pasted image 20251221181950.png|400]]
		- LiDAR
			- 장애물에 적외선 레이저가 반사되어 오는 시간 기반 추정. (찍은 점을 Point cloud라 함)
			- 주변 환경의 3D geometry 추정. 2D, 3D라이다 있음
			- 장점 : 3D geometry 추론 가장 잘함. ~200, 300m 까지. 주변광 영향⬇️
			- 단점 : 존나 비쌈. 레이저기에 기상상황에 영향⭕️. 해상도 sparse[^6]함.
			- 레이저 발사 방식
				- Time-of-Flight
				- Phase shift
				- Frequency modulation
			- 스캐닝 방식
				- Mechanical scanner
				- Solid-state scanne
				- Flash LiDAR
			- FMCW LiDAR - 4D LiDAR
				- 기존 : x,y,z만 가능 -> 이건 Doppler를 통한 velocity 측정 가능
		- RADAR
			- 반사되는 전파로 radial거리 측정. Doppler로 속도 추정.
			- 전파의 종류에 따라 near~far range 변화 가능
			- 장점 : 날씨 영향❌, 속도도 가능하다!(4D라이다도 되는데?)
			- 단점 : 작은 물체는 힘듦. Multi-path[^7] 문제
			- Imaging RADAR - 4D RADAR
				- 높은 해상도를 가짐. Point cloud도 있음. 속도 정보도 제공
				- 하지만 파장의 영역이 RADAR에 속한다!
		- Camera
			- 빛 신호를 받아 RGB image 재구성. (빛을 RGB로 측량)
			- 장점 : 저렴띠. 성능 굿(Dense data, Texture, Color, High-FPS), 시야각 변경 easy(렌즈), 사람과 시야 비슷
			- 단점 : Depth 정보❌, 조명 영향⬆️
		- Ultrasound
			- 근거리 장애물 검출. E.G.) 주차 보조, 장애물 감지
			- 장점 : 저렴띠
			- 단점 : 형태 추정 힘듦. 노이즈⬆️

## Questions
- 

## Merge Candidates
- [[ ]] 

## Priori Lecture
- [[L - Part 1_Chapter 1-3]]
-  참고 링크 [슬램슬램 블로그](https://www.cv-learn.com/20210228-AD-sensors/)

[^1]: 바퀴 회전량(RPM) * 바퀴 둘레

[^2]: 실제 회전과 측정 회전 간의 오차 발생.
	noise에 의한 오차가 시간에 따라 누적됨. 

[^3]: 관절의 끝 부분

[^4]: 신호가 벽에 튕겨서 거리가 더 길다고 판단.

[^5]: 정답 정보.

[^6]: 부족하다.

[^7]: 유리나 물 같은 것에 반사되는 문제
