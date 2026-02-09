from enum import Enum

class IROp(Enum):
    MOVE_POSE = "move_pose"
    MOVE_JOINTS = "move_joints"
    GRIPPER = "gripper"
    WAIT = "wait"
    TRAJECTORY = "trajectory"
#로봇 제어 명령어를 묶어서 Enum형태로 정의