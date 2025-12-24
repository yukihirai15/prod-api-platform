from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_root():

    response = client.get("/")

    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert data["message"] == "Hello"

    assert "served_by" in data
    assert isinstance(data["served_by"], str)


def test_health():

    response = client.get("/health")

    assert response.status_code == 200

    assert "status" in response.json()


def test_ready():

    response = client.get("/ready")

    assert response.status_code in [200, 503]
