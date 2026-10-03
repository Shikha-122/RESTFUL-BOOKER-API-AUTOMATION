from tests.test_health import client
from utils.api_client import APIClient
from utils.config import BASE_URL

client = APIClient(BASE_URL)

def test_create_auth_token():
    payload = {
        'username': 'admin',
        'password': 'password123'
    }

    response=client.post("/auth", json=payload)

    assert response.status_code == 200
    assert "token" in response.json()
