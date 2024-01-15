from fastapi.testclient import TestClient
from application.main import app
from application.tests.utils import create_invalid_test_jwt, create_test_jwt
# Setup the TestClient
client = TestClient(app)


def test_historic_weather_valid():
    jwt = create_test_jwt()
    headers = {"Authorization": f"Bearer {jwt}"}
    response = client.get(
        "/api/v1/mapmycrop/historic-weather",headers=headers, params={"latitude": 1.0, "longitude": 2.0, "number_of_days": 7}
    )
    assert response.status_code == 200


def test_historic_weather_invalid_token():
    jwt = create_invalid_test_jwt()
    headers = {"Authorization": f"Bearer {jwt}"}
    response = client.get(
        "/api/v1/mapmycrop/historic-weather",headers=headers, params={"latitude": 1.0, "longitude": 2.0, "number_of_days": 7}
    )
    assert response.status_code == 401
