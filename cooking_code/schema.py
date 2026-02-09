# JSON Schema 정의 (Phase 2 기반, 최소 형태)

COOKING_CODE_SCHEMA = {
    "type": "object",
    "required": ["meta", "robot", "program"],
    "properties": {
        "meta": {"type": "object"},
        "robot": {
            "type": "object",
            "required": ["type", "dof"],
            "properties": {
                "type": {"type": "string"},
                "dof": {"type": "integer", "minimum": 1},
                "capabilities": {
                    "type": "array",
                    "items": {"type": "string"}
                }
            }
        },
        "program": {
            "type": "array",
            "minItems": 1,
            "items": {"type": "object"}
        }
    }
}
