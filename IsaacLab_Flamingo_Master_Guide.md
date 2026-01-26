# 🦩 Isaac Lab Flamingo 강화학습 마스터 가이드

이 문서는 Isaac Sim과 Isaac Lab을 사용하여 **Flamingo (이륜 로봇)**의 강화학습을 처음부터 끝까지(설정, 학습, 분석, 로봇 배포) 진행하며 나눈 모든 대화와 꿀팁을 총정리한 가이드입니다.

---

## 1. ⚙️ 환경 설정 및 기초 (Setup)

### 1.1. 초기 실행 문제 해결
*   **문제**: `isaaclab.sh`가 Flamingo 프로젝트를 인식하지 못함.
*   **해결**: 전용 실행 스크립트(`run_flamingo.sh`)를 제작하여 `PYTHONPATH`와 가상환경(`venv`) 설정을 자동화함.
*   **파일 수정**: `scripts/co_rl/train.py`의 `dump_pickle` 에러 수정 (표준 `pickle` 라이브러리로 대체).
*   **에셋 경로**: 로봇 모델(`usd`) 압축 해제 시 중복 폴더 문제 해결.

### 1.2. 실행 명령어 (Run)
터미널에서 `/home/huro/IsaacLab`으로 이동 후 실행합니다.

```bash
# 기본 학습 (평지)
./run_flamingo.sh
```

---

## 2. 🚀 학습 가속화 및 고급 옵션 (Training)

학습 속도를 높이거나, 중단된 학습을 이어가는 "치트키" 명령어입니다.

### 2.1. 속도 10배 높이기 (Headless + 대량 생성)
화면을 끄고(`--headless`), 로봇 수를 4096마리로 늘려 학습 속도를 극대화합니다.

```bash
./run_flamingo.sh --headless --num_envs 4096
```

### 2.2. 학습 이어하기 (Resume)
중단된 시점(`--load_run`)부터 이어서 학습합니다.

```bash
# 예시: 2026-01-26_16-12-30 폴더의 학습을 이어하기
./run_flamingo.sh --headless --num_envs 4096 --resume --load_run 2026-01-26_16-12-30
```

### 2.3. 학습 횟수 무한대로 늘리기
기본 설정(약 6000번)에서 꺼지지 않게 하려면 `--max_iterations`를 늘립니다.

```bash
# 5만 번 반복 (사실상 무한)
./run_flamingo.sh --headless --num_envs 4096 --resume --load_run [폴더명] --max_iterations 50000
```

### 2.4. 목표 점수 도달 시 자동 종료 (Early Stopping)
"점수가 20점이 되면 그만해!"라고 설정할 수 있습니다. 과적합 방지와 시간 절약에 유용합니다.

```bash
# 평균 보상(Mean Reward)이 20점을 넘으면 자동 저장 후 종료
./run_flamingo.sh --headless --num_envs 4096 --task Isaac-Velocity-Rough-Flamingo-v1-ppo --target_reward 20
```

---

## 3. 🏔️ 험지(Rough) 및 심화 학습 (Curriculum)

### 3.1. 험지 학습 시작하기 (추천)
평지 학습 모델을 험지로 가져가는 것(전이 학습)보다, **험지 태스크를 처음부터 학습시키는 것**이 훨씬 효율적이고 강력합니다. (험지 모델은 평지도 잘 걷습니다)

```bash
# 험지 태스크 처음부터 시작 (New Start)
./run_flamingo.sh --headless --num_envs 4096 \
    --task Isaac-Velocity-Rough-Flamingo-v1-ppo \
    --max_iterations 10000
```

### 3.2. 점프(Jump)와 주행을 동시에?
하나의 뇌로 다 하려 하지 말고, **모드 전환(Mode Switching)** 전략을 사용하세요.
*   **평상시**: 험지 주행 모델 (`rough_walk.onnx`)
*   **특수 상황**: 점프 모델 (`jump.onnx`)
실제 로봇에서 상황에 맞춰 두 파일을 번갈아 로딩하여 사용합니다.

---

## 4. 📊 결과 분석 및 그래프 해석 (Analysis)

### 4.1. 텐서보드(TensorBoard) 실행
```bash
# 가상환경 활성화 상태에서
tensorboard --logdir=/home/huro/IsaacLab/logs/co_rl
```
*   웹 브라우저로 `http://localhost:6006/` 접속.
*   `TensorFlow installation not found` 경고는 정상입니다 (무시).

### 4.2. 핵심 3대 지표 (이것만 보면 됨)
1.  **`Episode_Termination / time_out`** ↗️ (상승): 1.0에 가까워야 함. (안 넘어지고 버팀)
2.  **`Episode_Reward / track_lin_vel_xy_exp`** ↗️ (상승): 시킨 속도대로 잘 감. (가장 중요)
3.  **`Loss / Value`** ↘️ (하락): AI의 예측 오차가 줄어듬.

### 4.3. 문제 해결 (디버깅)
*   **점수는 높은데 로봇이 너무 느리다?**: `error_vel_xy` 확인. 높다면(0.4 등) 험지 훈련으로 '꼼수'를 교정해야 함.
*   **Warning 로그들**: `quat_rotate_inverse deprecated...` 등은 무시해도 되는 단순 경고입니다.

---

## 5. 🤖 실제 로봇 배포 (Sim2Real)

### 5.1. 모델 확인 (Play) 및 ONNX 추출
학습된 모델을 눈으로 확인(`Play`)하면 자동으로 `exported` 폴더에 `policy.onnx`가 생성됩니다.

```bash
# 한 줄 실행 명령어 (경로 문제 해결됨)
source /home/huro/isaac_sim_project/venv/bin/activate && \
export PYTHONPATH=$PYTHONPATH:/home/huro/isaac_sim_project/Isaac-RL-Two-wheel-Legged-Bot && \
cd /home/huro/IsaacLab && \
python /home/huro/isaac_sim_project/Isaac-RL-Two-wheel-Legged-Bot/scripts/co_rl/play.py \
    --task Isaac-Velocity-Rough-Flamingo-Play-v1-ppo \
    --num_envs 1 \
    --load_run [날짜_폴더명]
```

### 5.2. 실제 로봇 코드 (Python)
로봇에는 `onnxruntime`만 설치하면 됩니다.

```python
import onnxruntime as ort
import numpy as np

# 1. 모델 로드 (험지 모델 또는 점프 모델)
session = ort.InferenceSession("policy.onnx")

# 2. 센서 데이터 입력 (시뮬레이션과 순서/단위 일치 필수!)
# [Linear Vel, Angular Vel, Gravity, Joint Pos, Joint Vel, Actions]
obs = get_sensor_data() 

# 3. 추론 및 제어
actions = session.run(None, {"obs": obs})[0]
set_motor_commands(actions)
```

---
**작성일**: 2026-01-26
**작성자**: Antigravity AI Assistant
