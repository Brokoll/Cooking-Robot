class ValidationError(Exception):
    pass


class CookingCodeValidator:
    def __init__(self, cooking_code: dict):
        self.code = cooking_code

    def validate(self):
        self._validate_structure()
        self._validate_program()

    def _validate_structure(self):
        if "robot" not in self.code:
            raise ValidationError("Missing robot section")

        if "program" not in self.code or not self.code["program"]:
            raise ValidationError("Program is empty")

        robot = self.code["robot"]
        if "dof" not in robot:
            raise ValidationError("Robot DOF not defined")

    def _validate_program(self):
        dof = self.code["robot"]["dof"]

        for action in self.code["program"]:
            if "action" not in action:
                raise ValidationError("Action field missing")

            if action["action"] == "move_joints":
                positions = action.get("positions", [])
                if len(positions) != dof:
                    raise ValidationError(
                        f"move_joints length {len(positions)} != dof {dof}"
                    )
