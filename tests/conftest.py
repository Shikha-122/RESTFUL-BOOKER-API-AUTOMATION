import pytest

from test_data.booking_data import booking_data
from utils.api_client import APIClient
from utils.config import BASE_URL


@pytest.fixture
def api_client():
    return APIClient(BASE_URL)

@pytest.fixture
def booking_id(api_client):
    response = api_client.post(
        "/booking",
        json=booking_data
    )
    assert response.status_code == 200
    return response.json()['bookingid']

@pytest.fixture

def auth_token(api_client):
    payload = {
        'username':'admin',
        'password': 'password123'
    }

    response = api_client.post(
        '/auth',
        json=payload
    )
    assert response.status_code == 200
    return response.json()['token']

