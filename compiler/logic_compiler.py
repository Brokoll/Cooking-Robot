

def compile_logic(action: dict):
    action_type = action["action"]

    if action_type == "sequence":
        return compile_sequence(action)

    if action_type == "repeat":
        return compile_repeat(action)

    raise ValueError(f"Unknown logic action: {action_type}")


def compile_sequence(action: dict):
    steps = action.get("steps", [])
    return compile_program(steps)


def compile_repeat(action: dict):
    times = action.get("times")
    body = action.get("body", [])

    if times is None:
        raise ValueError("repeat requires 'times'")

    compiled_body = compile_program(body)
    ir_nodes = []

    for _ in range(times):
        ir_nodes.extend(compiled_body)

    return ir_nodes
