from ir.ir_nodes import IRNode

def compile(action: dict):
    source = action["from"]
    target = action["to"]

    return [
        IRNode("move_pose", {"target": f"{source}_pour"}),
        IRNode("move_pose", {"target": f"{target}_center"}),
        IRNode("wait", {"duration": 1.0}),
    ]
