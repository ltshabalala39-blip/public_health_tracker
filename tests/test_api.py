from fastapi.testclient import TestClient
from src.api import app

client = TestClient(app)

def test_docs_available():
    """Verify OpenAPI documentation is reachable."""
    response = client.get("/docs")
    assert response.status_code == 200

def test_invalid_route_returns_404():
    """Verify hitting an unconfigured root route returns 404."""
    response = client.get("/")
    assert response.status_code == 404

def test_get_cases_valid_province():
    """Verify that querying a valid province returns 200 and a list."""
    response = client.get("/api/v1/cases/western_cape")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
