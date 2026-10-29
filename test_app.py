import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home_page_loads(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Temperature Converter Application (Push 2)" in response.data


def test_push1_celsius_to_fahrenheit(client):
    payload = {"val1": "0", "action": "c_to_f"}
    response = client.post("/", data=payload)

    assert response.status_code == 200
    assert "0.0°C = 32.00°F" in response.data.decode("utf-8")


def test_push2_fahrenheit_to_celsius_boiling(client):
    payload = {"val1": "212", "action": "f_to_c"}
    response = client.post("/", data=payload)

    assert response.status_code == 200
    assert "212.0°F = 100.00°C" in response.data.decode("utf-8")


def test_push2_fahrenheit_to_celsius_negative(client):
    payload = {"val1": "-40", "action": "f_to_c"}
    response = client.post("/", data=payload)

    assert response.status_code == 200
    assert "-40.0°F = -40.00°C" in response.data.decode("utf-8")


def test_invalid_input_handling(client):
    payload = {"val1": "xyz", "action": "f_to_c"}
    response = client.post("/", data=payload)

    assert response.status_code == 200
    assert b"Invalid input" in response.data
