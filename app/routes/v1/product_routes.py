from fastapi import APIRouter
from app.product_schema import ProductCreate, ProductResponse
from app.product_service import ProductService
from typing import List

router = APIRouter()
service = ProductService()

@router.get("/", response_model=List[ProductResponse])
def list_products():
    return service.list_products()

@router.get("/{product_id}", response_model=ProductResponse)
def get_product(product_id: int):
    return service.get_product(product_id)

@router.post("/", response_model=ProductResponse)
async def create_product(product: ProductCreate):
    return service.create_product(product)

@router.get("/")
async def list_products():
    print("list_products")
    return [{"id": 1, "name": "Sample Product", "description": "This is a sample product."}]    

