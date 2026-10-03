from utils.api_client import APIClient
from utils.config import BASE_URL

client= APIClient(BASE_URL)

def test_health_check():
    response=client.get("/ping")

    assert response.status_code == 201
