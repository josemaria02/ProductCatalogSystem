from app.products.model import ProductCreate, ProductUpdate, Product, PaginatedProducts
from app.products.repo import ProductRepo
from app.exceptions import ProductNotFoundException
from typing import Optional
import logging

class ProductService:
    def __init__(self):
        self.repo = ProductRepo()

    def list_products(self, limit: int = 10, offset: int = 0, name: Optional[str] = None, category: Optional[str] = None) -> PaginatedProducts:
        logging.info("Listing products")
        total = self.repo.count_products(name=name, category=category)
        products = self.repo.list(limit=limit, offset=offset, name=name, category=category)
        logging.info(f"Total products: {total}")
        logging.info(f"Products: {products}")
        return PaginatedProducts(total=total, limit=limit, offset=offset, products=products)


    def get_product(self, product_id: int) -> Product:
        product = self.repo.get(product_id)
        if not product:
            raise Exception(f"Product with ID {product_id} not found")
        return product

    def create_product(self, product: ProductCreate) -> Product:
        return self.repo.create(product)

    def update_product(self, product_id: int, product: ProductUpdate) -> Product:
        updated = self.repo.update(product_id, product)
        if not updated:
            raise ProductNotFoundException(product_id)
        return updated

    def delete_product(self, product_id: int) -> int:
        if not self.repo.delete(product_id):
            raise ProductNotFoundException(product_id)
        return product_id


