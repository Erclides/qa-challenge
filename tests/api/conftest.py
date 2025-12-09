import pytest
from core.api_client import APIClient

BASE_URL = "http://localhost:80"

@pytest.fixture(scope="session")
def api_client():
    client = APIClient(BASE_URL)
    client.authenticate(username="user", password="pass123")
    return client
