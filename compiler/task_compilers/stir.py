from ir.ir_nodes import IRNode

def compile(action: dict):
    target = action["target"]
    duration = action.get("duration", 1.0)
    style = action.get("style", "normal")

    return [
        IRNode("move_pose", {"target": f"{target}_center"}),
        IRNode(
            "trajectory",
            {
                "shape": "circle" if style == "circular" else "line",
                "target": target,
                "duration": duration,
            },
        ),
    ]
