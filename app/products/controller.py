from fastapi import APIRouter, Query
from app.products.model import ProductCreate, Product, ProductUpdate, PaginatedProducts
from app.products.service import ProductService

router = APIRouter()
service = ProductService()

@router.get("/", response_model=PaginatedProducts)
async def list_products(
        limit: int = Query(10, ge=1, le=100, description="Max number of products to return"),
        offset: int = Query(0, ge=0, description="Number of products to skip"),
        name: str = Query(None, description="Search based on name"),
        category: str = Query(None, description="Search based on category"),
):
    return service.list_products(limit=limit, offset=offset, name=name, category=category)

@router.get("/{product_id}", response_model=Product)
async def get_product(product_id: int):
    return service.get_product(product_id)

@router.post("/", response_model=Product)
async def create_product(product: ProductCreate):
    return service.create_product(product)

@router.put("/{product_id}", response_model=Product)
async def update_product(product_id: int, product: ProductUpdate):
    return service.update_product(product_id, product)

@router.delete("/{product_id}", response_model=Product)
async def delete_product(product_id: int):
    return service.delete_product(product_id)


