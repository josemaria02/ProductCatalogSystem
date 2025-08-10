"""
    Service Layer for business logic for product operations.
"""

from app.products.model import ProductCreate, ProductUpdate, ProductResponse, PaginatedProducts, DeleteResponse
from app.products.repo import ProductRepo
from app.exceptions import ProductNotFoundException
from typing import Optional
import logging

class ProductService:
    def __init__(self):
        """
            Initialize service with repository dependency.
        """
        self.repo = ProductRepo()

    def list_products(self,
                      limit: int = 10,
                      offset: int = 0,
                      name: Optional[str] = None,
                      category: Optional[str] = None) -> PaginatedProducts:
        """
            Retrieve a paginated list of products with optional filtering.
        """
        logging.info("Listing products")
        total = self.repo.count_products(name=name, category=category)
        products = self.repo.list(limit=limit, offset=offset, name=name, category=category)
        logging.info(f"Total products: {total}")
        logging.info(f"Products: {products}")
        return PaginatedProducts(total=total, limit=limit, offset=offset, products=products)


    def get_product(self, product_id: int) -> ProductResponse:
        """
            Retrieve a specific product by its ID.
        """
        product = self.repo.get(product_id)
        if not product:
            logging.error(f"Product {product_id} not found")
            raise ProductNotFoundException(product_id)
        return product

    def create_product(self, product: ProductCreate) -> ProductResponse:
        """
            Create a new product.
        """
        return self.repo.create(product)

    def update_product(self, product_id: int, product: ProductUpdate) -> ProductResponse:
        """
            Update an existing product.
        """
        updated = self.repo.update(product_id, product)
        if not updated:
            logging.error(f"Product {product_id} not found")
            raise ProductNotFoundException(product_id)
        return updated

    def delete_product(self, product_id: int) -> DeleteResponse:
        """
            Delete an existing product.
        """
        deleted = self.repo.delete(product_id)
        if not deleted:
            logging.error(f"Product {product_id} not found")
            raise ProductNotFoundException(product_id)
        return deleted


