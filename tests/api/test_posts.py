import pytest
from utils.schema_loader import validate_schema

@pytest.mark.crud
def test_create_post(api_client, post_state):
    payload = {
        "title": "Primeiro Post",
        "content": "Conteúdo do post",
        "public": True  # Ajustado para o nome correto do campo
    }

    status, data = api_client.post("/posts", payload)
    assert status in (200, 201)

    # Valida usando o schema atualizado
    validate_schema(data, "post_schema.json")

    # Armazena informações do post criado
    post_state["id"] = data["id"]
    post_state["title"] = data["title"]
    post_state["content"] = data["content"]
    post_state["public"] = data["public"]
    print("post_state após criação:", post_state)



@pytest.mark.crud
def test_read_post(api_client, post_state):
    print("post_state após criação:", post_state)
    post_id = post_state.get("id")
    if not post_id:
        pytest.skip("Post ainda não criado")

    status, data = api_client.get(f"/posts/{post_id}")
    assert status == 200

    validate_schema(data, "post_schema.json")


@pytest.mark.crud
def test_update_post(api_client, post_state):
    post_id = post_state.get("id")
    if not post_id:
        pytest.skip("Post não criado")

    payload = {
        "title": "Post Atualizado",
        "content": "Conteúdo atualizado",
        "public": False
    }

    status, data = api_client.put(f"/posts/{post_id}", payload)
    assert status in (200, 201)
    assert data["title"] == "Post Atualizado"
    assert data["content"] == "Conteúdo atualizado"
    assert data["public"] is False


@pytest.mark.crud
def test_delete_post(api_client, post_state):
    post_id = post_state.get("id")
    if not post_id:
        pytest.skip("Post não criado")

    status, _ = api_client.delete(f"/posts/{post_id}")
    assert status in (200, 204)
