---
type: lecture
title: L - David Silver's RL 2주차
created: 2026-01-27
updated: 2026-01-27T13:55:26
course: David Silver's RL
session: 2
group: General
tags:
  - lecture
  - course/David Silver's RL
---
# David Silver's RL 2주차

> **David Silver's RL** | 2주차

---

## 📋 Outline
### Markov Process
-  Reward를 추가해 Markov Reward Process를 만들 것.
-  Action을 추가해 Markov Decision Process를 만들 것
1. MDP의 기본
	- 개발 목표, Formalism(형식론) : Markov Decision Process임.
	- Agent와 세계는 상호작용 함.
	- Agent와 상호작용하는 환경, 그 환경을 설명하는 것이 MDP가 될 것.
	1) 완전 관측 가능성 (Fully observability)
		- 상태가 주어짐
		- 환경에 대한 모든 정보가 Agent에게 제공됨.
		- Agent에게 주어진 현재 상태가 이 과정을 완전히 특징지음.
		- 환경이 전개되는 방식은 어떤 상태에 의존하고 그 상태도 알고있음.
		- 완전히 관측 가능.
	2) MDP의 보편성
		- 거의 모든 강화학습 문제를 MDP로 공식화 할 수 있음.
	3) Markov Properties
		- 현재 상태(S)라는 확률 변수 : 환경의 어디에 있는지를 알 수 있는 특징.
		- S가 Markov propertie를 갖는다면 *미래는 현재가 주어졌을 때 과거와 독립적이다.*
		- 환경에서 다음에 일어날 일은 이전 상태에만 의존, 이전의 이전에 일어났던 모든 것에 의존하지 않음.
	4) State Transition Probability
		- Markov process의 경우 어떤 S에서 -> 후속 S'로 전이할 확률을 정의할 수 있음.
		- 현 상태 S에서 다음에 일어날 모든 일을 특징지으려면 S라는 전제하에 S'로 가는 확률을 알려주는 Transition Probability가 있어야함.
		- 상태 전이 확률 : State Transition Probability
		$$P_{ss'} = P[S_{t+1} = s'|S_{t} = s]$$
		- S에서 S'로 전이할 확률임.
	5) Transition Probability Matrix
		- 전이 확률의 아이디어를 갖게 되면 완전한 행렬로 구성할 수 있다.
		- 상태 1-> 상태 2-> ... 상태 N으로 끝날 확률을 알려줌
		- 각 행은 MP에서 가능한 하나의 시작점부터의 전이를 완전히 특징지음
		- 단일행렬 P는 어떤 S에서 다른 S'로의 끝날 가능성을 알려줌.
2. MP의 정의와 예시
	1) MP의 정의
		- 반복적으로 sampling하는 Random Process임.
		- Markov Properties를 가진 무작위 상태의 순서 $S_{1}, S_{2}, S_{3}\dots$
		- 필요 요소
			- 상태 공간(S) : 우리가 있을 수 있는 상태들의 집합
			- 전이 확률(P) : 한 상태에서 다음 상태로 어떻게 전이하는지의 확률
		- 이 것으로 전체 system의 Dynamics를 정의할 수 있음.
		- Action, Reward없이 환경, 규칙, 진화와 같은 역학은 S와 P matrix로 정의 가능
	2) Markov Chain
		- 하나의 S에서 S', S''로 넘어갈 확률을 선으로 이어서 각 확률을 적음.
## 📝 Notes

### 핵심 1
- 

### 핵심 2
- 

---

## ❓ Questions
- [ ] 

## 🔗 Related
- [[ ]]

---

## 📝 FC
#flashcards/general

핵심 개념:: 

