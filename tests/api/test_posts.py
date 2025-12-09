import pytest
from utils.schema_loader import validate_schema

@pytest.mark.crud
def test_create_post(api_client, post_state={}):
    payload = {
        "title": "Primeiro Post",
        "content": "Conteúdo do post",
        "public": True
    }

    status, data = api_client.post("/posts", payload)
    assert status in (200, 201)

    validate_schema(data, "post_schema.json")

    post_state["id"] = data["id"]


@pytest.mark.crud
def test_read_post(api_client, post_state):
    post_id = post_state.get("id")
    if not post_id:
        pytest.skip("Post não criado")

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
        "public": True
    }

    status, data = api_client.put(f"/posts/{post_id}", payload)
    assert status in (200, 201)
    assert data["title"] == "Post Atualizado"


@pytest.mark.crud
def test_delete_post(api_client, post_state):
    post_id = post_state.get("id")
    if not post_id:
        pytest.skip("Post não criado")

    status, _ = api_client.delete(f"/posts/{post_id}")
    assert status in (200, 204)
