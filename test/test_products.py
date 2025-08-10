import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_products():
    response = client.get("/api/v1/products/")
    assert response.status_code == 200
    assert "products" in response.json()

def test_get_product_not_found():
    response = client.get("/api/v1/products/99999")
    assert response.status_code == 404
