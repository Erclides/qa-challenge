import random
import pytest
from utils.schema_loader import validate_schema

@pytest.mark.crud
def test_create_user(api_client, user_state):
    """Cria um usuário único e armazena no user_state."""
    unique_id = random.randint(1000, 9999)
    payload = {
        "username": f"novo_user_{unique_id}",
        "email": f"novo_{unique_id}@qa.com",
        "full_name": "Novo Usuário",
        "password": "senha123",
        "disabled": False
    }

    status, data = api_client.post("/users/", payload)  # note a barra final
    assert status in (200, 201)

    validate_schema(data, "user_schema.json")

    # Armazena informações do usuário criado
    user_state["id"] = data["id"]
    user_state["username"] = data["username"]
    user_state["email"] = data["email"]
    user_state["full_name"] = data["full_name"]
    print("user_state após criação:", user_state)


@pytest.mark.crud
def test_read_user(api_client, user_state):
    """Valida leitura do usuário criado."""
    print("user_state durante leitura:", user_state)
    user_id = user_state.get("id")
    if not user_id:
        pytest.skip("Usuário não criado")

    status, data = api_client.get(f"/users/{user_id}")
    assert status == 200

    validate_schema(data, "user_schema.json")


@pytest.mark.crud
def test_update_user(api_client, user_state):
    """Atualiza usuário criado."""
    user_id = user_state.get("id")
    if not user_id:
        pytest.skip("Usuário não criado")

    payload = {
        "full_name": "Usuário Atualizado",
        "username": f"{user_state['username']}_upd",
        "email": f"upd_{user_state['email']}"
    }

    status, data = api_client.put(f"/users/{user_id}", payload)
    assert status in (200, 201)
    assert data["full_name"] == "Usuário Atualizado"


@pytest.mark.crud
def test_delete_user(api_client, user_state):
    """Exclui usuário criado."""
    user_id = user_state.get("id")
    if not user_id:
        pytest.skip("Usuário não criado")

    status, _ = api_client.delete(f"/users/{user_id}")
    assert status in (200, 204)
