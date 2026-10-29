import pytest
from app import app


@pytest.fixture
def client():
    """Fixture to configure and provide the Flask test client."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home_page_loads(client):
    """Test that the application main page loads successfully (GET)."""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Temperature Converter Application (Push 1)" in response.data


def test_push1_celsius_to_fahrenheit_zero(client):
    """Test standard freezing point conversion (0 C to 32 F)."""
    payload = {"val1": "0", "action": "c_to_f"}
    response = client.post("/", data=payload)

    assert response.status_code == 200
    assert "0.0°C = 32.00°F" in response.data.decode("utf-8")


def test_push1_celsius_to_fahrenheit_boiling(client):
    """Test standard boiling point conversion (100 C to 212 F)."""
    payload = {"val1": "100", "action": "c_to_f"}
    response = client.post("/", data=payload)

    assert response.status_code == 200
    assert "100.0°C = 212.00°F" in response.data.decode("utf-8")


def test_invalid_input_handling(client):
    """Test that non-numeric inputs output the safe error string."""
    payload = {"val1": "abc", "action": "c_to_f"}
    response = client.post("/", data=payload)

    assert response.status_code == 200
    assert b"Invalid input" in response.data
