from pydantic import BaseModel, Field
from typing import List, Optional

class ProductBase(BaseModel):
    name: str #= Field(..., example="Sample Product")
    description: Optional[str] #= Field(None, example="This is a sample product.")
    price: float #= Field(..., gt=0, example=19.99)
    category: str #= Field(..., example=["electronics", "gadgets"])


class Product(ProductBase):
    id: int


class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):
    name: Optional[str] = None#= Field(None, example="Updated Product")
    description: Optional[str] = None #= Field(None, example="This is an updated product description.")
    price: Optional[float] = None #= Field(None, gt=0, example=29.99)
    category: Optional[List[str]] = None #= Field(None, example=["updated", "category"])


class PaginatedProducts(BaseModel):
    total: int
    limit: int
    offset: int
    products: List[Product]