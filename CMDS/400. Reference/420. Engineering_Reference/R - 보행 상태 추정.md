---
type: reference
title: R - 보행 상태 추정
created: 2025-12-23
updated: 2025-12-23T17:48:59
author: "[[김선음]]"
group: EE
status: "[[🌱Seed]]"
tags:
  - reference
  - doc
  - tagging/needed
aliases: []
source_kind: doc
---

# R - 보행 상태 추정

## Notes
  

목차

[State Estimation for Legged Robots](https://lilys.ai/digest/7366348/7972880#a5e32238-4875-4244-969b-d58da69a4766)

[1. 저자 및 학술지 정보](https://lilys.ai/digest/7366348/7972880#7da061c2-5962-4b89-be8d-5e41d61d50db)

[2. 초록 (IMRaD 요약)](https://lilys.ai/digest/7366348/7972880#3ecd9c11-5e04-4bda-8926-259f3cae2298)

[2.1. 🎯 연구 목적 (Purpose)](https://lilys.ai/digest/7366348/7972880#67d9389b-7c78-4f6c-aff3-82027e2330d5)

[2.2. 🛠️ 연구 방법 (Methods)](https://lilys.ai/digest/7366348/7972880#aa1e9ad9-e6b6-4552-bb2d-c2a6b1e31679)

[2.3. 💡 주요 결과 (Results)](https://lilys.ai/digest/7366348/7972880#0c6dbadc-d414-498e-bcbf-972218f1a26a)

[2.4. 💬 결론 및 논의 (Discussion/Conclusion)](https://lilys.ai/digest/7366348/7972880#7198590c-9d1a-447c-ac07-125a6ea24ba6)

[3. 핵심 용어 및 개념](https://lilys.ai/digest/7366348/7972880#b721a200-e732-4d6d-91a2-e03ca9170da3)

[4. 연구 방법](https://lilys.ai/digest/7366348/7972880#4c7c372d-cdab-4ca4-8d85-315c1e6ce78c)

[4.1. 🧭 연구 설계 및 목표](https://lilys.ai/digest/7366348/7972880#3a863f68-c66c-44f4-9fcf-5525bc752b6c)

[4.2. ⚙️ 센서 장비 (Proprioceptive Sensors)](https://lilys.ai/digest/7366348/7972880#1122af78-960d-4f63-81ee-8c148036a5b6)

[4.3. 🎛️ Two Stage Estimation (TS) 프레임워크](https://lilys.ai/digest/7366348/7972880#b6cd1ded-5600-48f1-8171-58d1f78acf21)

[4.4. 📐 자세 (Orientation) 필터 구현](https://lilys.ai/digest/7366348/7972880#3816eaaf-ecd1-48bb-a373-c1812028067e)

[4.5. 🏃 위치 및 속도 (Position and Velocity) 필터 구현 (Classical KF)](https://lilys.ai/digest/7366348/7972880#d61c9fd4-68e3-4964-88bf-caca74c58086)

[4.6. 🧪 테스트 시나리오 및 평가 지표](https://lilys.ai/digest/7366348/7972880#f3b066a5-d14f-4788-a54c-cede0263bacf)

[5. 결과](https://lilys.ai/digest/7366348/7972880#4352de8f-d8fc-47a6-bee7-a17b4367a8ca)

[5.1. 🧭 자세 추정 결과 (Orientation Estimation)](https://lilys.ai/digest/7366348/7972880#cec6fa04-5e28-449f-a97d-1268b9cf3565)

[5.2. 🏃 위치 및 속도 추정 결과 (Position and Velocity Estimation)](https://lilys.ai/digest/7366348/7972880#4a1b9344-ea7c-474b-badd-0a090804bf7c)

[6. 결론 및 논의](https://lilys.ai/digest/7366348/7972880#82d033d2-2f77-40f5-8522-82dcccd43681)

[6.1. 🏆 최적의 추정 접근 방식](https://lilys.ai/digest/7366348/7972880#b863581f-4e3e-4bed-8259-fed3f5d2deae)

[6.2. 🔍 주요 학문적 의의 및 차별점](https://lilys.ai/digest/7366348/7972880#3d96baa2-0502-4ff2-ac04-866101918688)

[6.3. 🚧 연구의 한계 및 향후 연구](https://lilys.ai/digest/7366348/7972880#75a1c998-ad1b-4041-af31-ca3284174ad2)

[7. 인용](https://lilys.ai/digest/7366348/7972880#53a243f1-49b8-4c32-ba24-401845a2ffdb)

## State Estimation for Legged Robots

  

## 1. 저자 및 학술지 정보

- **저자:** Benjamin Hoffman  
    
- **소속:** ETH Zurich (스위스 연방 공과대학교), Robotics Lab  
    
- **학위 논문 정보:** 학사 학위 논문 (Bachelor Thesis) | 2021년 7월 발행  
    
- **감독:** Dongho Kang, Dr. Stelian Coros  
    

  

## 2. 초록 (IMRaD 요약)

  

## 2.1. 🎯 연구 목적 (Purpose)

- 본 논문은 네발로 걷는 로봇의 **정확하고 견고한 상태 추정**을 위한 다양한 접근 방식을 구현, 조합 및 비교하는 것을 목표로 함 .
    
- 특히, 복잡도 증가가 항상 정확도 증가로 이어지지 않는 현 상황에서, **단순하고 정확한** 새로운 상태 추정 접근 방식을 제시하고자 함 .
    

  

## 2.2. 🛠️ 연구 방법 (Methods)

- **Two Stage Estimation (TS)** 프레임워크를 기반으로 선형 및 비선형 추정 단계를 분리하여 사용함 .
    
- 비선형인 **자세(Orientation) 추정**을 위해 Complementary Filter (CF), Unscented Kalman Filter (UKF), Angular Velocity 추정을 포함한 UKF (UKF AV)를 구현하고, 기존의 Extended Kalman Filter (EKF)와 비교함 .
    
- 선형인 **위치/속도(Position/Velocity) 추정**을 위해 Classical Kalman Filter (KF)를 사용했으며, 로봇의 상대 발 위치 및 속도 정보를 측정값에 통합하는 증강(Augmentation) 방법을 비교함 .
    

  

## 2.3. 💡 주요 결과 (Results)

- 자세 추정에서 CF, UKF, UKF AV, EKF 모두 **유사한 범위의 높은 정확도**를 보였으나, UKF는 EKF보다 더 낮은 구현 복잡도를 제공함 .
    
- 위치/속도 추정에서 **TS (Classical KF + 상대 발 위치)** 는 EKF와 거의 **동일한 수준의 정확도**를 달성했으나, 상대 발 속도를 추가한 **TS FV**는 오히려 성능이 저하됨 .
    

  

## 2.4. 💬 결론 및 논의 (Discussion/Conclusion)

- **UKF 기반의 Two Stage Estimation** 프레임워크는 높은 정확도를 유지하면서도 기존 EKF 방식의 복잡한 선형화 과정을 회피하여, **낮은 복잡도와 높은 성능**을 결합한 최적의 상태 추정 접근 방식으로 확인됨 .
    
- 이 결과는 복잡한 EKF 구현 없이도 네발로 걷는 로봇의 상태 추정에 효과적임을 입증함 .
    

  

## 3. 핵심 용어 및 개념

|   |   |   |   |
|---|---|---|---|
|**용어**|**약어**|**정의**|**출처**|
|상태 추정|State Estimation|로봇의 현재 상태(자세, 위치, 속도 등)를 확률적으로 결정하는 기술||
|IMRAD 구조|Two Stage Estimation (TS)|비선형 자세 추정과 선형 위치/속도 추정을 분리하는 프레임워크||
|관성 측정 장치|Inertial Measurement Unit (IMU)|자이로스코프(각속도) 및 가속도계(가속도) 측정을 제공하는 센서||
|확장 칼만 필터|Extended Kalman Filter (EKF)|비선형 시스템을 추정하기 위해 모델을 선형화하여 적용하는 칼만 필터 확장 기법||
|무취 칼만 필터|Unscented Kalman Filter (UKF)|선형화 대신 시그마 벡터 샘플링을 사용하여 비선형성을 우회하는 칼만 필터 확장 기법||
|상보 필터|Complementary Filter (CF)|자이로스코프(고주파)와 가속도계(저주파) 측정을 결합하여 효율적인 자세 추정을 제공하는 알고리즘||
|고유 감각 센서|Proprioceptive Sensors|로봇 내부의 정보(IMU, 관절 엔코더)를 측정하여 환경에 덜 민감하고 견고한 추정을 가능하게 하는 센서||

  

## 4. 연구 방법

  

## 4.1. 🧭 연구 설계 및 목표

- **목표:** Two Stage Estimation (TS) 프레임워크 내에서 다양한 자세 필터(CF, UKF, UKF AV)와 위치/속도 필터(TS, TS FV)의 성능을 **EKF**와 비교 평가하여, **정확도와 구현 복잡도**를 모두 만족하는 최적의 조합을 도출 .
    

  

## 4.2. ⚙️ 센서 장비 (Proprioceptive Sensors)

- **IMU:** 가속도 및 각속도 측정 제공  
    
- **Joint Encoders:** 모든 관절의 각 위치 측정 제공. 이를 이용해 **순방향 운동학**을 통해 로봇의 특정 강체 링크 위치를 계산 가능  
    
- **센서 선택의 이유:**
    
    - **단순성 및 다양성:** IMU는 독립적이고, 엔코더 데이터는 쉽게 사용 가능  
        
    - **견고성:** 환경에 크게 의존하는 외부 센서(Visual, Lidar 등)와 달리, 내부 값을 측정하여 견고함  
        
    

  

## 4.3. 🎛️ Two Stage Estimation (TS) 프레임워크

- **핵심 원리:** 비선형인 자세 추정(qq$\mathbf{q}$)과 선형인 위치 및 속도 추정(r,vr,v$\mathbf{r, v}$)을 분리하여 각 단계에 최적화된 필터를 적용  
    
- **장점:**
    
    - 선형 상태(위치, 속도)에 **Classical Kalman Filter (KF)**를 적용하여 최적의 추정 결과를 활용  
        
    - 구현 복잡도 감소 및 선형화 필요성 제거  
        
    - 다양한 비선형 필터 조합 및 비교가 가능한 **모듈성** 제공  
        
    

  

## 4.4. 📐 자세 (Orientation) 필터 구현

|   |   |   |   |
|---|---|---|---|
|**필터**|**상태 벡터 xx$\mathbf{x}$**|**추정 특징**|**비교 기준**|
|**Complementary Filter (CF)**|qq$\mathbf{q}$ (쿼터니언)|Madgwick의 IMU 필터 기반; 단순성 및 낮은 계산 비용|단순성 및 성능 **벤치마크**|
|**Unscented Kalman Filter (UKF)**|qq$\mathbf{q}$ (쿼터니언)|각속도 추정 제외, 자세 qq$\mathbf{q}$만 추정 (3 DOF)|EKF를 대체하는 간단한 비선형 추정 대안 탐색|
|**Unscented Kalman Filter AV (UKF AV)**|x=[q,ω]x=[q,ω]$\mathbf{x} = [\mathbf{q}, \mathbf{\omega}]$|각속도 ωω$\mathbf{\omega}$를 포함하여 자세와 함께 추정|각속도 추정 추가가 성능에 미치는 영향 분석|
|**Extended Kalman Filter (EKF)**|x=[r,v,q,...]x=[r,v,q,...]$\mathbf{x} = [\mathbf{r}, \mathbf{v}, \mathbf{q}, ...]$|Bloesch et al. [10]의 상태 추정 구현을 비교 목적으로 사용|최신 연구의 복잡한 프레임워크와의 성능 비교|

  

## 4.5. 🏃 위치 및 속도 (Position and Velocity) 필터 구현 (Classical KF)

- **기본 틀:** Bledt et al. [6] 및 Bloesch et al. [10]의 증강된 Classical KF 기반  
    
- **상태 벡터 xx$\mathbf{x}$:** x=[r,v,p1,…,pM]x=[r,v,p1​,…,pM​]$\mathbf{x} = [\mathbf{r}, \mathbf{v}, \mathbf{p}_1, \dots, \mathbf{p}_M]$ (위치, 속도, MM$M$개 발의 접촉 위치)  
    

  

|   |   |   |
|---|---|---|
|**필터**|**업데이트 증강 (Augmentation)**|**특징**|
|**TS**|**상대 발 위치** (Relative Foot Position)|접지 중인 발의 위치는 월드 좌표계에서 일정하다고 가정하고, 순방향 운동학으로 계산된 발 위치를 측정값에 통합|
|**TS FV**|**상대 발 위치 및 속도** (Relative Foot Velocity)|TS의 측정값에 더해, 접지 중인 발의 속도는 0이라는 가정을 측정값에 추가하여 통합|

  

## 4.6. 🧪 테스트 시나리오 및 평가 지표

- **시뮬레이션 환경:** Unitree A1 사족보행 로봇, 트로팅(trotting) 보행 사용  
    
- **노이즈 모델:** InvenSense MPU9150 IMU 파라미터를 기반으로 가속도계 및 자이로스코프 노이즈(백색 노이즈, 바이어스 확산)를 현실적으로 시뮬레이션에 적용  
    
- **평가 지표:**
    
    - **RMSE (Root-Mean-Square Error):** 추정 정확도의 평균 편차를 정량화 (낮을수록 좋음)  
        
    - **MaAR (Maximum Absolute Error):** 최악의 경우 성능(안정성)을 정량화 (낮을수록 좋음)  
        
    - **FEFD (Final Position Error vs Final Distance Travelled):** 이동 거리 대비 최종 위치 오차 비율 (낮을수록 좋음, 이동 시나리오에만 사용)  
        
    

  

## 5. 결과

  

## 5.1. 🧭 자세 추정 결과 (Orientation Estimation)

- **시나리오:** Stance (30s 정지), CCW Rotation (60s 회전)  
    
- **정지 (Stance):** 모든 필터가 롤, 피치, 요 각도에서 RMSE 0.000 rad (반올림)의 매우 높은 정확도를 보임  
    
- **회전 (CCW Rotation):**
    
    - **요 각도 (Yaw) RMSE:** CF (0.098 rad) < UKF (0.105 rad) < UKF AV (0.105 rad) < EKF (0.427 rad)  
        
    - **핵심:** CF와 UKF가 EKF보다 요 각도 추정에서 더 나은 성능을 보였으며, UKF와 UKF AV 간에는 성능 차이가 미미함 (UKF AV는 각속도 추정에서만 이점)  
        
    

  

## 5.2. 🏃 위치 및 속도 추정 결과 (Position and Velocity Estimation)

- **비교 필터:** EKF, TS, TS FV (단, TS/TS FV에는 Ground Truth 자세 데이터를 입력으로 제공)  
    
- **정지 및 높이 변화 (Stance & Variation in y):**
    
    - 모든 필터가 매우 낮은 RMSE 값을 달성하며 높은 정확도를 보임  
        
    - TS FV는 xx$\mathbf{x}$ 위치 추정에서 EKF 및 TS보다 약간 우수했으나, **전반적으로 필터 간 성능 차이는 미미**  
        
    
- **전진 및 측면 이동 (Forward in z/x & Sideways in x):**
    
    - **TS와 EKF는 유사한 성능**을 보였으며, TS FV는 두 필터보다 일관되게 성능이 저하됨  
        
    - **Forward in z (z축 전진) FEFD (목표 방향 최종 위치 오차):**
        
        - TS (8.40%)와 EKF (8.41%)는 거의 동일  
            
        - TS FV (9.87%)는 오차가 가장 큼  
            
        
    - **Sideways in x (x축 측면 이동) FEFD:**
        
        - EKF (6.27%)와 TS (6.61%)는 유사  
            
        - TS FV (9.02%)는 오차가 가장 큼  
            
        
    - **결론:** 상대 발 속도 정보를 추가한 **TS FV가 TS보다 성능이 저하**되어, 추가적인 증강이 오히려 추정의 정확도를 떨어뜨릴 수 있음을 시사  
        
    

  

## 6. 결론 및 논의

  

## 6.1. 🏆 최적의 추정 접근 방식

|   |   |   |   |
|---|---|---|---|
|**요소**|**최적의 필터**|**이유**|**출처**|
|**자세 추정**|**Unscented Kalman Filter (UKF)**|EKF와 유사하거나 더 나은 정확도를 달성하며, 복잡한 비선형 선형화 및 자코비안 계산을 회피하여 구현 복잡도가 낮음||
|**위치/속도 추정**|**Classical Kalman Filter (TS)**|EKF와 동일한 수준의 정확도를 제공하지만, 선형 시스템에 최적인 KF를 사용하므로 구현이 단순하고 모듈성이 높음||

  

- **최종 결론:** **UKF + TS (Classical KF)**의 조합은 높은 정확도를 유지하면서도 EKF보다 구현이 훨씬 단순하고 모듈성이 뛰어난 상태 추정 프레임워크를 제공함 .
    

  

## 6.2. 🔍 주요 학문적 의의 및 차별점

- **EKF 복잡성 해소:** 기존 최신 연구(Bloesch et al. [10])가 EKF를 사용하는 반면, 본 연구는 Two Stage 접근법이 복잡한 EKF와 동등한 성능을 제공함을 입증 .
    
- **UKF의 유효성 검증:** 자세 추정에서 UKF가 EKF의 대안으로 매우 유효함을 보였으며, 각속도 ωω$\mathbf{\omega}$를 상태 변수에서 제외한 단순화된 UKF가 충분함을 확인 (UKF ≈≈$\approx$ UKF AV) .
    
- **증강 기법 분석:** 상대 발 위치 정보(TS)는 유효하지만, 상대 발 속도 정보(TS FV)는 시뮬레이션 조건에서 성능을 저하시킴을 발견하여 증강 기법 선택의 중요성을 강조 .
    

  

## 6.3. 🚧 연구의 한계 및 향후 연구

- **시뮬레이션 기반:** 모든 평가는 현실적인 노이즈 모델을 사용한 시뮬레이션에서 수행되었으며, **실제 하드웨어 실험을 통한 검증이 필요** .
    
- **단순한 환경:** 시뮬레이션 환경은 평평하고 발 미끄러짐(foot slippage)이 없었으며, 동적인 보행 속도가 낮았음. 향후 불규칙한 지형과 고속 보행 환경에서의 평가가 필요 .
    
- **Ground Truth 사용:** 위치/속도 추정 평가 시, TS 및 TS FV에 **Ground Truth 자세 데이터**를 입력으로 사용한 점은 실제 시나리오를 완전히 반영하지 못하는 한계가 있음. 향후 비선형 필터의 출력 자세를 입력으로 사용하여 전체 프레임워크를 검증해야 함 .
    

  

## 7. 인용

- [6] Bledt, G. et al. (2018). MIT Cheetah 3: Design and Control of a Robust, Dynamic Quadruped Robot. IEEE International Conference on Intelligent Robots and Systems.  
    
- [10] Bloesch, M. et al. (2013). State estimation for legged robots: Consistent fusion of leg kinematics and IMU. Robotics: Science and Systems.  
    
- [31] Madgwick, S. O. H. et al. (2011). Estimation of IMU and MARG orientation using a gradient descent algorithm. IEEE International Conference on Rehabilitation Robotics.  
    
- [30] Kraft, E. (2003). A quaternion-based unscented Kalman filter for orientation tracking. Proceedings of the 6th International Conference on Information Fusion, FUSION 2003.  
    

  

**(원문 DOI 링크는 PDF 원문에 포함되어 있지 않으므로 생략)**

## Next
- [ ] 

