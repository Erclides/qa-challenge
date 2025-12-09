import pytest
from core.api_client import APIClient

@pytest.fixture(scope="session")
def api_client():
    client = APIClient(base_url="http://localhost", username="user", password="pass123")
    return client

@pytest.fixture(scope="session")
def post_state():
    """Dicionário para compartilhar dados do post criado entre testes."""
    return {}

@pytest.fixture(scope="session")
def user_state():
    """Dicionário para compartilhar dados do usuário criado entre testes."""
    return {}
