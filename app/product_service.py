from app.product_schema import ProductCreate, ProductUpdate, ProductResponse
from app.product_repo import ProductRepo
from typing import List

class ProductService:
    def __init__(self):
        self.repo = ProductRepo()

    def create_product(self, product: ProductCreate) -> ProductResponse:
        return self.repo.create(product)

    def list_products(self) -> List[ProductResponse]:
        return self.repo.get_all()

    def get_product(self, product_id: int) -> ProductResponse:
        product = self.repo.get_by_id(product_id)
        if not product:
            raise Exception(f"Product with ID {product_id} not found")
        return product



