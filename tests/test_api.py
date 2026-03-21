from fastapi.testclient import TestClient

from app.main import app
from app.core.database import Base, engine

# Create tables for test DB
Base.metadata.create_all(bind=engine)

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_create_item():
    response = client.post(
        "/api/v1/items/",
        json={"title": "Test Item", "description": "A test item"},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Test Item"
    assert data["is_active"] is True


def test_list_items():
    response = client.get("/api/v1/items/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_item_not_found():
    response = client.get("/api/v1/items/99999")
    assert response.status_code == 404
