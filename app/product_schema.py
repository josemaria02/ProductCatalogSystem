from pydantic import BaseModel, Field
from typing import List, Optional

class ProductBase(BaseModel):
    id: int
    name: str #= Field(..., example="Sample Product")
    description: Optional[str] #= Field(None, example="This is a sample product.")
    price: float #= Field(..., gt=0, example=19.99)
    category: str #= Field(..., example=["electronics", "gadgets"])


class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):
    name: Optional[str] #= Field(None, example="Updated Product")
    description: Optional[str] #= Field(None, example="This is an updated product description.")
    price: Optional[float] #= Field(None, gt=0, example=29.99)
    category: Optional[List[str]] #= Field(None, example=["updated", "category"])


class ProductResponse(ProductBase):
    id: int

