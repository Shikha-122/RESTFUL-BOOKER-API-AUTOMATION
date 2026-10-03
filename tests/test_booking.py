from urllib import response

from test_data.booking_data import booking_data

def test_create_booking(api_client):
    response= api_client.post(
        '/booking',
        json=booking_data,
    )

    assert response.status_code == 200

    response_data = response.json()
    assert "bookingid" in response_data
    assert "booking" in response_data
    assert response_data["booking"]["firstname"] == booking_data["firstname"]
    assert response_data["booking"]["lastname"] == booking_data["lastname"]
    assert response_data["booking"]["totalprice"] == booking_data["totalprice"]
    assert response_data["booking"]["depositpaid"] == booking_data["depositpaid"]


def test_get_booking(api_client,booking_id):
    response = api_client.get(
        f"/booking/{booking_id}"
    )
    assert response.status_code == 200
    response_data = response.json()
    assert response_data['firstname'] == booking_data['firstname']
    assert response_data['lastname'] == booking_data['lastname']

def test_get_booking_invalid_id(api_client):
    response = api_client.get(
        "/booking/999999"
    )
    assert response.status_code == 404


def test_update_booking(api_client, booking_id, auth_token):
    updated_data = {
        "firstname": "ShikhaUpdated",
        "lastname": "RaiUpdated",
        "totalprice": 1500,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2026-11-01",
            "checkout": "2026-11-05"
        },
        "additionalneeds": "Lunch"
    }

    response = api_client.put(
        f"/booking/{booking_id}",
        json=updated_data,
        headers={
            "Cookie": f"token={auth_token}"
        }
    )

    assert response.status_code == 200

    response_data = response.json()

    assert response_data["firstname"] == updated_data["firstname"]
    assert response_data["lastname"] == updated_data["lastname"]
    assert response_data["totalprice"] == updated_data["totalprice"]

def test_update_booking_invalid_token(api_client, booking_id):
    updated_data = {
        "firstname": "Invalid",
        "lastname": "Token"
    }

    response = api_client.put(
        f"/booking/{booking_id}",
        json=updated_data,
        headers={
            "Cookie": "token=invalid_token"
        }
    )

    assert response.status_code == 403

def test_delete_booking(api_client, booking_id, auth_token):
    delete_response = api_client.delete(
        f"/booking/{booking_id}",
        headers={
            "Cookie": f"token={auth_token}"
        }
    )

    assert delete_response.status_code == 201

    get_response = api_client.get(
        f"/booking/{booking_id}"
    )

    assert get_response.status_code == 404