from jsonschema import validate
from jsonschema.exceptions import ValidationError

def validate_response(data, schema):
    """
    Validação inteligente:
    - Se 'data' é um dict → valida como um único objeto
    - Se 'data' é uma lista → valida cada item separadamente
    """

    # Caso 1: retorno único
    if isinstance(data, dict):
        return validate(instance=data, schema=schema)

    # Caso 2: lista de objetos
    if isinstance(data, list):
        for item in data:
            if not isinstance(item, dict):
                raise ValidationError(f"Item inválido: {item}")
            validate(instance=item, schema=schema)
        return

    # Caso 3: inesperado
    raise ValidationError(f"Tipo inesperado: {type(data)}")
