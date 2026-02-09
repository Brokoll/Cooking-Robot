from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class IRNode:#명령어를 객체로 관리할 수있는 노드
    op: str #어떤 명령어인지
    params: Dict[str, Any]#키는 문자열, 값은 어떤 타입이든 가능 (Any)

#- IRNode → "명령어 하나"를 표현하는 데이터 구조
