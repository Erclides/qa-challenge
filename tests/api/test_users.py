import pytest
from utils.schema_loader import validate_schema

@pytest.mark.crud
def test_create_user(api_client, user_state={}):
    payload = {
        "name": "Novo Usuário",
        "username": "novo_user",
        "email": "novo@qa.com"
    }

    status, data = api_client.post("/users", payload)
    assert status in (200, 201)

    validate_schema(data, "user_schema.json")

    user_state["id"] = data["id"]


@pytest.mark.crud
def test_read_user(api_client, user_state):
    user_id = user_state.get("id")
    if not user_id:
        pytest.skip("Usuário não criado")

    status, data = api_client.get(f"/users/{user_id}")
    assert status == 200

    validate_schema(data, "user_schema.json")


@pytest.mark.crud
def test_update_user(api_client, user_state):
    user_id = user_state.get("id")
    if not user_id:
        pytest.skip("Usuário não criado")

    payload = {
        "name": "Usuário Atualizado",
        "username": "novo_user",
        "email": "atualizado@qa.com"
    }

    status, data = api_client.put(f"/users/{user_id}", payload)
    assert status in (200, 201)
    assert data["name"] == "Usuário Atualizado"


@pytest.mark.crud
def test_delete_user(api_client, user_state):
    user_id = user_state.get("id")
    if not user_id:
        pytest.skip("Usuário não criado")

    status, _ = api_client.delete(f"/users/{user_id}")
    assert status in (200, 204)
