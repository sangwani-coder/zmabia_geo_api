from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_main():
    """Test if the landing page loads"""
    response = client.get("/")
    assert response.status_code == 200

def test_get_provinces():
    """Test the provinces endpoint"""
    response = client.get("/api/v1/provinces")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_search_city():
    """Test city search validation"""
    response = client.get("/api/v1/cities/search?q=Lusaka")
    assert response.status_code == 200