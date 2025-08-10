"""
    Data Models
"""
from pydantic import BaseModel, Field
from typing import List, Optional

class ProductBase(BaseModel):
    """
        Base product model product with validation rules
    """
    name: str = Field(..., min_length=3, max_length=50, description="Product name must be between 3 and 50 characters")
    description: Optional[str] = Field(None, max_length=200, description="Optional product description up to 200 characters")
    price: float = Field(..., gt=0, description="Price value should be greater than 0")
    category: str = Field(..., min_length=3, max_length=50, description="Product category should be between 1 and 50 characters")


class ProductResponse(ProductBase):
    """
        Product response model returned by API endpoints.
    """
    id: int


class ProductCreate(ProductBase):
    """
        Product model for create endpoint.
    """
    pass


class ProductUpdate(BaseModel):
    """
        Product model for update endpoint.
    """
    name: Optional[str] = Field(None, min_length=3, max_length=50, description="Product name must be between 3 and 50 characters")
    description: Optional[str] = Field(None, max_length=200,
                                       description="Optional product description up to 200 characters")
    price: Optional[float] = Field(None, gt=0, description="Price value should be greater than 0")
    category: Optional[str] = Field(None, min_length=3, max_length=50,
                          description="Product category should be between 1 and 50 characters")


class PaginatedProducts(BaseModel):
    """
        Product model for paginated response.
    """
    total: int
    limit: int
    offset: int
    products: List[ProductResponse]

class DeleteResponse(BaseModel):
    """
        Product response model for delete endpoint.
    """
    message: str = "Delete product successful"
    product_id: int
