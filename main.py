import json

from cooking_code.validator import CookingCodeValidator
from compiler.compiler import compile_program

if __name__ == "__main__":
    with open("recipe.json") as f:
        cooking_code = json.load(f)

    # Validate
    validator = CookingCodeValidator(cooking_code)
    validator.validate()

    # Compile to IR
    ir_nodes = compile_program(cooking_code["program"])

    print("=== IR OUTPUT ===")
    for node in ir_nodes:
        print(node)
