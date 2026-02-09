##JSON_Schema를 파이썬에 다루기 쉽게하기 위한 코드

from dataclasses import dataclass
from typing import List, Dict, Any

@dataclass
class Meta:
    name: str = ""
    version: str = "1.0"

@dataclass
class RobotSpec:
    type: str
    dof: int
    capabilities: List[str] = None

@dataclass
class Action:
    action: str
    params: Dict[str, Any]

@dataclass
class CookingCode:
    meta: Meta
    robot: RobotSpec
    program: List[Dict[str, Any]]
