from fastapi import APIRouter
from app.product_model import Product
from app.product_service import ProductService

router = APIRouter()
service = ProductService()

@router.post("/", response_model=Product)
async def create_product(product: Product):
    return service.create_product(product)

@router.get("/")
async def list_products():
    return [{"id": 1, "name": "Sample Product", "description": "This is a sample product."}]    

