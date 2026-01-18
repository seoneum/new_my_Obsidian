---
type: project
title: PRJ - Bipedal
created: 2025-12-23
updated: 2026-01-18T16:42:53
author:
  - "[[김선음]]"
  - "[[최수아]]"
  - "[[이승주]]"
  - "[[남경빈]]"
  - "[[윤아현]]"
group: Robotics
status: [[🚜In Progress]]
tags:
  - project
  - build
  - tagging/needed
aliases: []
goal: 여기서는 reference를 모으고 방향성을 정한다
deadline: 2026/10/30
share_link: https://share.note.sx/cuty3o30#h1JPhWFBn37CoqjV+CDUkA/dJT0k5Zwm2OiRUMSau8U
share_updated: 2025-12-29T16:28:37+09:00
migrated_from: CMDS/200. CMDS/280. Project/PRJ - Bipedal.md
domain:
  - robotics
cmds: develop
---
- 1문장 버전:

# PRJ - Bipedal

## Goal
- 여기서는 reference를 모으고 방향성을 정한다
- 독거노인이나 아가 전용 로봇. 감수성을 자극하는 귀염둥이 로봇
- 2족 보행이고 기반은 [Qmini](https://github.com/unitreerobotics/Qmini/?tab=readme-ov-file) 로 하겠습니다
- 제어는 bldc+encoder+board+3d printing한 감속기 + 강화 학습 + llm + SLAM
	- 모터제어, 강화학습, 인지
	- 경빈이 : 
	- 수아 : 
	- 나 : 
	- 제어는 좀 봐야할듯.
- 하드는 원래 것을 변경하는 느낌으로 가야겠죠
	- 아현이 : 안에 들어가는 부품 자리, 위치 설계
	- 승주 : 다리에 모터 새로 들어가는 사이즈, 하중, 생김새 설계

## Reference 
- 
	[감속기, 드라이버도 같이 설명되어있음](https://www.instructables.com/OpenCycloid-3D-printed-Open-Source-Robotic-Actuato/)
	[엔코더](https://ko.aliexpress.com/item/4000081648489.html)
	[motor](https://ko.aliexpress.com/item/1005009181683055.html?spm=a2g0o.productlist.main.4.6bfa162bKxwY7Z&algo_pvid=5fb53778-5212-41ab-adf9-e0d6affc01d1&algo_exp_id=5fb53778-5212-41ab-adf9-e0d6affc01d1-3&pdp_ext_f=%7B%22order%22%3A%2216%22%2C%22eval%22%3A%221%22%2C%22fromPage%22%3A%22search%22%7D&pdp_npi=6%40dis%21KRW%2176844%2177352%21%21%21364.92%21367.33%21%402101529317669912109771990ef121%2112000048218877416%21sea%21KR%210%21ABX%211%210%21n_tag%3A-29910%3Bd%3A8356eda8%3Bm03_new_user%3A-29895%3BpisId%3A5000000194819415&curPageLogUid=q0HeWgUUfrT6&utparam-url=scene%3Asearch%7Cquery_from%3A%7Cx_object_id%3A1005009181683055%7C_p_origin_prod%3A)
	[드라이버](https://ko.aliexpress.com/item/1005009117943590.html)
	논문 찾는 법~
	- alphaaxiv.org에 논문들을 찾는다
	- 퍼플렉시티 쓰는 것이 좋음
	- 찾은 논문 주소에서 arxiv앞에 quick쓰고 generating하면 한글 요약본 나옴
	- alphaxiv아니면 

## Deadline
- 2026/10/30

## Repo
-

## Requirements
- 현재
	90KV motor[^1]
## Constraints
- 

## Plan
- 

## Log
- 2025-12-23 - 만들기
- 2025-12-29 15:57 - 초안 update.
- [[20260113_Bipedal_01]]
- 


## Related Project
- [[PRJ - Hexapod]]
