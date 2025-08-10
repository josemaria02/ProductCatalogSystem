import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# def test_create_product():
#     response = client.post("/api/v1/products/", json={
#         "name": "Test Product",
#         "description": "Test Description",
#         "price": 99.99,
#         "category": "Test Category"
#     })
#     assert response.status_code == 200
#     assert response.json()["name"] == "Test Product"

def test_get_products():
    response = client.get("/api/v1/products/")
    assert response.status_code == 200
    assert "products" in response.json()

def test_get_product_not_found():
    response = client.get("/api/v1/products/99999")
    assert response.status_code == 404

# def test_search_products():
#     response = client.get("/api/v1/products/?name=Test")
#     assert response.status_code == 200