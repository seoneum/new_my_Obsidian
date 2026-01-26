# 🦩 Isaac Lab Flamingo 강화학습 통합 가이드

이 문서는 Isaac Sim과 Isaac Lab을 사용하여 **Flamingo (이륜 로봇)**의 강화학습을 실행하고, **결과를 확인**하며, 최종적으로 **실제 로봇에 배포(Sim2Real)**하는 방법까지 정리한 통합 가이드입니다.

---

## 1. 🚀 학습 실행 (Training)

### 기본 학습 시작
터미널을 열고 다음 명령어로 학습을 시작합니다.

```bash
cd /home/huro/IsaacLab
./run_flamingo.sh
```

### 다양한 태스크 실행
`--task` 옵션으로 학습 목표를 변경할 수 있습니다.
*   **평지 주행**: `Isaac-Velocity-Flat-Flamingo-v1-ppo` (기본값)
*   **험지 주행**: `Isaac-Velocity-Rough-Flamingo-v1-ppo`
*   **점프**: `Isaac-TrackJUMP-Flat-Flamingo-v1-ppo`

---

## 2. 📊 학습 결과 확인 (Evaluation)

학습이 진행되는 동안, 또는 완료된 후에 결과를 확인하는 방법입니다.

### 2.1. 로그 및 모델 파일 위치
학습 데이터는 다음 경로에 자동 저장됩니다.
*   **경로**: `/home/huro/IsaacLab/logs/co_rl/[태스크명]/ppo/[날짜_시간]`
*   **주요 파일**:
    *   `model_*.pt`: 학습된 모델의 체크포인트 파일
    *   `events.out.tfevents.*`: Tensorboard 로그 파일 (학습 그래프)
    *   `params/`: 학습 설정 파일들

### 2.2. 텐서보드(TensorBoard)로 그래프 확인하기
학습 진행 상황(보상 증가, 손실 감소 등)을 그래프로 확인할 수 있습니다.

1.  터미널에서 가상환경 활성화 후 실행:
    ```bash
    source /home/huro/isaac_sim_project/venv/bin/activate
    tensorboard --logdir=/home/huro/IsaacLab/logs/co_rl
    ```
2.  실행 후 `TensorFlow installation not found` 경고가 나올 수 있으나, **정상입니다** (PyTorch 환경이라서 뜨는 메시지).
3.  인터넷 브라우저를 열고 `http://localhost:6006/` 주소로 접속하세요.

### 2.3. 학습된 모델 눈으로 확인하기 (Play)
학습된 정책(Policy)이 실제로 로봇을 잘 조종하는지 시뮬레이션으로 확인합니다.
**Play 모드를 실행하면 자동으로 ONNX 변환(Export)도 수행됩니다.**

터미널 복사가 안 될 경우를 대비해, **아래 긴 명령어를 한 줄에 모두 입력**해야 합니다. (중간에 끊지 마세요)

```bash
# 한 줄로 실행하는 명령어 (가상환경 + 경로설정 + 폴더이동 + 실행)
source /home/huro/isaac_sim_project/venv/bin/activate && export PYTHONPATH=$PYTHONPATH:/home/huro/isaac_sim_project/Isaac-RL-Two-wheel-Legged-Bot && cd /home/huro/IsaacLab && python /home/huro/isaac_sim_project/Isaac-RL-Two-wheel-Legged-Bot/scripts/co_rl/play.py --task Isaac-Velocity-Flat-Flamingo-Play-v1-ppo --num_envs 1 --load_run 2026-01-26_16-12-30
```
*(위 명령어에서 `2026...` 부분만 본인의 폴더명으로 바꾸면 됩니다)*

---

## 3. 🤖 실제 로봇 적용 (Sim2Real)

학습된 인공지능 모델을 실제 로봇(Jetson, Raspberry Pi 등)에 넣어서 작동시키는 과정입니다.

### 3.1. 모델 추출 (Export)
위의 **2.2 Play 모드**를 한 번이라도 실행하면, 로그 폴더 안에 `exported` 폴더가 생성됩니다.
*   **생성 위치**: `logs/co_rl/[태스크명]/ppo/[날짜_시간]/exported/`
*   **필요한 파일**: `policy.onnx`

> **참고**: 이 `policy.onnx` 파일 내부에는 **관측값 정규화(Normalization)** 과정이 이미 포함되어 있습니다. 따라서 실제 로봇에서는 센서 원본 값을 그대로 넣어도 됩니다.

### 3.2. 실제 로봇에서의 실행 코드 (Python 예시)
실제 로봇에는 `onnxruntime` 라이브러리만 설치하면 됩니다. (`pip install onnxruntime`)
아래는 로봇에서 실행할 추론 코드의 예시입니다.

```python
import onnxruntime as ort
import numpy as np

# 1. 모델 로드
session = ort.InferenceSession("policy.onnx")

# 2. 로봇 센서 데이터 읽기 (예시 함수)
# Isaac Lab에서 정의된 순서대로 48개의 관측값(Observation)을 채워야 합니다.
# (예: 관절 위치, 속도, IMU 값 등 - tasks/.../mdp/observations.py 참고)
def get_robot_observation():
    # 실제로는 센서 값을 읽어와야 함
    obs = np.zeros((1, 48), dtype=np.float32) 
    return obs

# 3. 제어 루프
while True:
    # 관측값 가져오기
    obs = get_robot_observation()
    
    # 추론 실행 (Inference)
    # 입력 이름 "obs"는 모델에 따라 다를 수 있으나 보통 "obs" 또는 "input"입니다.
    inputs = {session.get_inputs()[0].name: obs}
    actions = session.run(None, inputs)[0]
    
    # 결과: actions (모터 제어 명령)
    print(f"Motor Command: {actions}")
    
    # 로봇 모터 제어 함수 호출
    # set_motor_targets(actions)
```

### 3.3. 관측값(Observation) 구성 주의사항
실제 로봇에 적용할 때 가장 중요한 것은 **시뮬레이션과 똑같은 순서와 단위**로 데이터를 넣어주는 것입니다.
`Isaac-RL-Two-wheel-Legged-Bot/lab/flamingo/tasks/.../mdp/observations.py` 파일을 참고하여 다음 순서를 맞춰야 합니다. (일반적인 순서 예시)

1.  Base Linear Velocity (x, y, z)
2.  Base Angular Velocity (x, y, z)
3.  Projected Gravity (x, y, z)
4.  Joint Positions (관절 각도)
5.  Joint Velocities (관절 속도)
6.  Last Actions (이전 스텝의 행동)

---

## 4. 📈 텐서보드 그래프 해석 가이드

학습이 잘 되고 있는지 판단하기 위한 **핵심 3대 지표**와 상세 분석법입니다.

### 4.1. 핵심 3대 지표 (이것만 보면 됨)
다음 세 가지 그래프가 모두 목표 방향으로 가고 있다면 학습은 **대성공**입니다.

1.  **`Episode_Termination / time_out`** (생존율)
    *   **목표**: **1.0 (100%)** 근처로 상승
    *   **해석**: 로봇이 넘어지지 않고 끝까지 버티는 비율입니다. 1.0이면 "이제 안 넘어진다"는 뜻입니다.
2.  **`Episode_Reward / track_lin_vel_xy_exp`** (속도 추종)
    *   **목표**: **우상향 (계속 상승)**
    *   **해석**: 사용자가 시킨 속도대로 정확하게 가고 있는지 나타냅니다. 점수가 높을수록 말을 잘 듣는 것입니다. (텐서보드 검색창에 `track` 검색 시 나옴)
3.  **`Loss / Value`** (예측 오차)
    *   **목표**: **하락 (감소)**
    *   **해석**: AI의 예측 능력입니다. 이 값이 떨어져야 "자신의 행동 결과를 정확히 알고 움직인다"는 뜻입니다.

### 4.2. 보조 지표 (상세 분석용)
*   **`Mean_Episode_Length`**: 한 번 시도 시 버틴 시간. 최대치(1000)를 찍고 유지해야 합니다.
*   **`lin_vel_z_l2` (수직 진동)**: 0에 가까워야 함. (통통 튀면 감점)
*   **`ang_vel_xy_l2` (기울기 진동)**: 0에 가까워야 함. (좌우로 흔들리면 감점)
*   **`dof_torques_l2` (에너지)**: 낮을수록 좋음. (힘을 적게 쓰고 효율적으로 움직임)
*   **`undesired_contacts`**: 0이어야 함. (무릎이나 몸체가 땅에 닿으면 안 됨)

---

## 5. ⚡️ 고급 실행 옵션 (Power User)

학습 효율을 높이거나 중단된 학습을 이어할 때 사용하는 "치트키" 같은 명령어 조합입니다.

### 4.1. 학습 속도 10배 높이기 (Headless + 대량 생성)
화면 렌더링을 끄고(`--headless`), 로봇 개수를 대폭 늘려서(`--num_envs 4096`) 학습 속도를 극대화합니다.

```bash
./run_flamingo.sh --headless --num_envs 4096
```

### 4.2. 학습 중단 및 이어하기 (Resume)
*   **중단**: 터미널에서 `Ctrl + C`를 누르면 안전하게 종료됩니다. (체크포인트는 자동 저장됨)
*   **같은 태스크 이어하기**: `--resume --load_run [폴더명]`
*   **다른 태스크로 전이 학습 (예: 평지 → 험지)**: `--resume --checkpoint [파일절대경로]`

```bash
# 험지(Rough) 학습 시작 예시 (평지에서 배운 모델을 불러와서 시작)
# --checkpoint 뒤의 경로는 본인의 실제 파일 위치로 바꿔주세요!
./run_flamingo.sh --headless --num_envs 4096 --task Isaac-Velocity-Rough-Flamingo-v1-ppo --resume --checkpoint /home/huro/IsaacLab/logs/co_rl/Flamingo_Flat_Stand_Drive/ppo/2026-01-26_16-12-30/model_4600.pt
```

---

## 5. 문제 해결 (Troubleshooting)

*   **Play 실행 시 에러**: `ImportError: cannot import name 'dump_pickle'` 에러가 나면 제가 수정한 코드가 적용되지 않은 것입니다. `train.py` 뿐만 아니라 관련 파일들이 최신 상태인지 확인하세요.
*   **ONNX 모델이 안 생겨요**: `play.py`가 끝까지(또는 에러 없이) 실행되어야 저장됩니다.
*   **Resume 실행 시 에러**: `expected one argument` 에러가 난다면, 코드가 `--resume True` 형식을 요구하는 구버전일 수 있습니다. (현재 가이드에 따라 코드를 수정했다면 발생하지 않습니다)

---
**최종 업데이트**: 2026-01-26
**작성자**: Antigravity AI Assistant
