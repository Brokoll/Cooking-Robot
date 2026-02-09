from typing import List
from ir.ir_nodes import IRNode

class IRProgram:#명령어들을 담는 리스트
    def __init__(self):
        self.nodes: List[IRNode] = [] #IRNode 객체들을 담는 리스트

    def add(self, node: IRNode):#명령어를 하나씩 추가
        self.nodes.append(node)

    def extend(self, nodes: List[IRNode]):#명령어들을 리스트로 추가
        self.nodes.extend(nodes)

    def __iter__(self):#리스트처럼 반복가능하게 함
        return iter(self.nodes)
#IRnode들을 관리하는 프로그램