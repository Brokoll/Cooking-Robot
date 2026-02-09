from ir.ir_nodes import IRNode

def compile(action: dict):
    target = action["target"]

    return [
        IRNode("move_pose", {"target": f"{target}_above"}),
        IRNode("move_pose", {"target": f"{target}_place"}),
        IRNode("gripper", {"state": "open"}),
        IRNode("move_pose", {"target": f"{target}_above"}),
    ]
