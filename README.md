# RESTFUL BOOKER API AUTOMATION

API automation testing framework for the RESTful Booker API using Python, Pytest, and Requests.

## Tech Stack

- Python
- Pytest
- Requests
- REST API
- Git & GitHub
- GitHub Actions

## Project Structure

```text
RESTFUL-BOOKER-API-AUTOMATION/
│
├── .github/
│   └── workflows/
│       └── tests.yml
│
├── api/
│   ├── auth_api.py
│   └── booking_api.py
│
├── tests/
│   ├── conftest.py
│   ├── test_auth.py
│   ├── test_booking.py
│   ├── test_health.py
│   └── __init__.py
│
├── test_data/
│   └── booking_data.py
│
├── utils/
│   ├── api_client.py
│   ├── config.py
│   └── logger.py
│
├── pytest.ini
├── requirements.txt
└── README.md

API Scenarios Covered

- Health check
- Authentication / token generation
- Create booking
- Get booking
- Get booking with invalid ID
- Update booking
- Update booking with invalid token
- Delete booking
- Verify deleted booking

Setup

Install the project dependencies:
python -m pip install -r requirements.txt

Run Tests

Run the complete test suite:
pytest -v

CI/CD

GitHub Actions is configured to automatically run the API automation tests when code is pushed to the main branch or a pull request is created.

Test Result
Current test suite contains 8 automated API tests.

All tests are passing successfully.

Framework Highlights
- Reusable API client using Requests
- Pytest fixtures for reusable test setup
- Centralized base URL configuration
- External test data
- Basic request/response logging
- Positive and negative API test scenarios
- GitHub Actions CI pipeline