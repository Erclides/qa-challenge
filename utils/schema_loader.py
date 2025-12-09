import json
from pathlib import Path
from jsonschema import validate

SCHEMAS_DIR = Path(__file__).resolve().parent.parent / "tests" / "api" / "schemas"

def load_schema(schema_name: str):
    path = SCHEMAS_DIR / schema_name
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def validate_schema(instance: dict | list, schema_name: str):
    schema = load_schema(schema_name)
    validate(instance=instance, schema=schema)
