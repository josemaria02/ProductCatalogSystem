"""
Controller Layer containing route handlers for product operations.
Endpoints:
    - GET /: List products with pagination and search
    - GET /{product_id}: Get specific product by ID
    - POST /: Create new product
    - PUT /{product_id}: Update existing product
    - DELETE /{product_id}: Delete product
"""

import logging

from fastapi import APIRouter, Query
from app.products.model import ProductCreate, ProductResponse, ProductUpdate, PaginatedProducts, DeleteResponse
from app.products.service import ProductService

router = APIRouter()
service = ProductService()


@router.get("/", response_model=PaginatedProducts)
def list_products(
        limit: int = Query(10, ge=1, le=100, description="Max number of products to return"),
        offset: int = Query(0, ge=0, description="Number of products to skip"),
        name: str = Query(None, description="Search based on name"),
        category: str = Query(None, description="Search based on category"),
):
    """
        List products with pagination and search capabilities.
        Query Parameters:
            - limit: Number of products per page (1-100)
            - offset: Number of products to skip
            - name: Filter by product name (partial match)
            - category: Filter by product category (partial match)
        Returns:
            PaginatedProducts with products list and pagination info
    """
    logging.info("Listing products")
    return service.list_products(limit=limit, offset=offset, name=name, category=category)

@router.get("/{product_id}", response_model=ProductResponse)
def get_product(product_id: int):
    """
        Get product by id.
        Path Parameter: product id
        Returns:Product details of product with given id.
    """
    logging.info("Getting product by id")
    return service.get_product(product_id)

@router.post("/", response_model=ProductResponse)
def create_product(product: ProductCreate):
    """
        Create a new product in the system.
        Returns:Product response with generated id.
    """
    logging.info("Creating new product")
    return service.create_product(product)

@router.put("/{product_id}", response_model=ProductResponse)
def update_product(product_id: int, product: ProductUpdate):
    """
        Update an existing product in the system.
        Returns:Product response with updated data.
    """
    logging.info("Updating product by id")
    return service.update_product(product_id, product)

@router.delete("/{product_id}", response_model=DeleteResponse)
def delete_product(product_id: int):
    """
        Delete an existing product in the system.
        Returns:Success message with product id deleted.
    """
    logging.info("Deleting product by id")
    return service.delete_product(product_id)


