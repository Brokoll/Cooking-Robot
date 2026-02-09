from ir.ir_nodes import IRNode

def compile(action: dict):
    obj = action["object"]

    return [
        IRNode("move_pose", {"target": f"{obj}_above"}),
        IRNode("move_pose", {"target": f"{obj}_grasp"}),
        IRNode("gripper", {"state": "close"}),
        IRNode("move_pose", {"target": f"{obj}_above"}),
    ]
