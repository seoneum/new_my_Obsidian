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
3. Markov Reward Process
	- 보상을 추가할 것임.
	1) MRP의 정의
		- 일종의 가치판단이 추가된 MP.
		- MP(S, P)에 두 가지를 추가.
		1) 보상함수 $R$
			- 어떤 상태$S$에서 시작할 때 그 상태에서 얻는 **즉각적인 보상**을 알려줌
		2) 할인 인자 $\gamma$
			- 미래 보상에 대한 현재 가치 결정
		e.g.) 각 상태에 보상 함수 올림. Markov Chain을 따라 갔을 때 최대 누적 보상을 쟁취
	2) Return과 $\gamma$
		- Markov chain을 따라 얻은 보상의 모든 누적 : Total Rewards = Return($G$)
		- 이 $G$는 무한히 미래의 모든 합산임. $G$를 유한하게 하고 제어하려면 $\gamma$사용
		- $$
		G_t = R_{t+1} + \gamma R_{t+2} + \gamma^2 R_{t+3} + \dots = \sum_{k=0}^{\infty} \gamma^k R_{t+k+1}
$$
		- 매 시간마다 $\gamma$만큼 할인 함. 
		- $\gamma$가 0.9라면 $t+2$시점에서는 0.9를 곱하고 $t+3$시점에서는 $0.9^2$를 곱함.
		- **할인 인자 ($\gamma$)의 역할
			- $\gamma$는 0~1 사이의 값
			- **미래 보상의 현대 가치**임.
			- $\gamma \approx$ 0 : 극도로 근시안적(Maximally Short-sighted). 현재 시간 단계를 제외한 모든 것을 무시하고 첫 번째 보상만을 봄
			- $\gamma \approx$ 1 : 극도로 원시안적(Maximally Far-sighted), 신경 쓸 필요 없는 미래의 보상까지 신경씀.
	3) 왜 할인해야하나?
		- 지연 보상보다 단기 보상을 선호하는 이유
			- 미래 불확실성 :
			  환경에 대한 완벽한 모델을 가지고 있지 않음
			- **수학적 편의성** :
			  가르치기 쉽고 이해하기 쉬움.
			  MP에 cycle이 있고 계속 보상을 받는 경우 평가가 무한대가 되는 무한리턴을 방지.
			- 금융 환경
			 이자율을 할인 함수를 생각할 수 있음.
			 $\gamma$를 이자율의 역수로 생각
			- 인지 모델
			  동물/인간은 즉각적 보상 선호.
			  생물학적 의사 결정 작동 방식에 대한 인지 모델.
		- 모든 것에 $\gamma$를 적용하진 않음. Undiscounted MRPs존재.
			- 편의를 위해 인위적으로 넣은 것임
			- 유한한 리턴 내에서는 $\gamma$필요 없음
			- 또 다른 공식화는 **Average Reward Formulation**
	4) Value Function & Bellman Equation
		- 가치 함수
			- Expectation -> Value Function
			- Value Function ($V(s)$) : 어떤 상태 S부터 얻게 될 장기 가치(Long-term Value)
			$$
V(s) = \mathbb{E}[G_t | S_t = s]
$$
			- MRP에서 가치함수는 얼마나 많은 보상을 얻을지 측정한다.
		- Bellman Equation
			- Value Function이 따르는 Recursive Decomposition를 나타냅니다.
			- $$

V(s) = \mathbb{E}[R_{t+1} + \gamma V(S_{t+1}) | S_t = s]

$$
            - **$R_{t+1}$:** 즉각적인 보상.
			- **$\gamma V(S_{t+1})$:** 다음 상태($S_{t+1}$)의 가치에 할인 인자($\gamma$)를 곱한 값.
## 📝 Notes

### 핵심 1
- 

### 핵심 2
- 

---

## ❓ Questions
- [ ] 무한리턴이 뭐임?
- [ ] 할인 인자의 확실한 정의

## 🔗 Related
- [[ ]]

---

## 📝 FC
#flashcards/general

핵심 개념:: 

