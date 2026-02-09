from compiler.task_compilers import pick, place, stir, pour

TASK_COMPILERS = {
    "pick": pick,
    "place": place,
    "stir": stir,
    "pour": pour,
}

def compile_action(action: dict):
    action_type = action["action"]

    if action_type in TASK_COMPILERS:
        return TASK_COMPILERS[action_type](action)

    from compiler.logic_compiler import compile_logic
    return compile_logic(action)


def compile_program(program: list):
    ir_nodes = []
    for action in program:
        ir_nodes.extend(compile_action(action))
    return ir_nodes
