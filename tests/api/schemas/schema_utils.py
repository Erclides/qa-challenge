import json
from jsonschema import validate, ValidationError
from pathlib import Path

def validate_schema(data, schema_name):
    """
    Valida resposta JSON contra schema.
    Funciona para objeto único ou array.
    """
    schema_path = Path(__file__).parent / schema_name
    with open(schema_path, "r", encoding="utf-8") as f:
        schema = json.load(f)

    # Se schema espera array mas veio objeto, transforma
    if schema.get("type") == "array" and not isinstance(data, list):
        data = [data]

    try:
        validate(instance=data, schema=schema)
    except ValidationError as e:
        raise AssertionError(f"Schema inválido: {e.message}")
