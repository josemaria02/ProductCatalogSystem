"""
    Data access Layer for all database operations.
"""

import logging
from mailcap import lookup

from app.database import get_connection
from app.exceptions import DatabaseException, ProductNotFoundException
from app.products.model import *
from typing import Optional


class ProductRepo:

    def list(self,
             limit: int = 10,
             offset: int = 0,
             name: Optional[str] = None,
             category: Optional[str] = None) -> List[ProductResponse]:
        """
            Retrieve a list of products based on given parameters.
        """

        query = "SELECT * FROM products WHERE 1=1"
        params = []
        if name:
            query += " AND name LIKE ?"
            params.append(f"%{name}%")
        if category:
            query += " AND category LIKE ?"
            params.append(f"%{category}%")
        query += " LIMIT ? OFFSET ?"
        params.extend([limit, offset])

        try:
            with get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(query, params)
                rows = cursor.fetchall()
                products = [ProductResponse(**dict(row)) for row in rows]
                return products
        except Exception as e:
            logging.error(f"Getting product list failed: {str(e)}")
            raise DatabaseException(f"Getting product list failed: {str(e)}")

    def get(self, product_id: int) -> ProductResponse:
        """
            Retrieve a specific product by its ID.
        """
        try:
            with get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM products WHERE id = ?", (product_id,))
                row = cursor.fetchone()
                return ProductResponse(**dict(row)) if row else None
        except Exception as e:
            logging.error(f"Getting product by id failed: {str(e)}")
            raise DatabaseException(f"Getting product by id failed: {str(e)}")

    def create(self, product: ProductCreate) -> ProductResponse:
        """
            Create a new product.
        """
        try:
            with get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO products (name, description, price, category) VALUES (?, ?, ?, ?)",
                    (product.name, product.description, product.price, product.category)
                )
                conn.commit()
                new_id = cursor.lastrowid
                return self.get(new_id)
        except Exception as e:
            logging.error(f"Creating product failed: {str(e)}")
            raise DatabaseException(f"Creating product failed: {str(e)}")

    def update(self, product_id: int, product: ProductUpdate) -> ProductResponse:
        """
            Update an existing product.
        """
        existing = self.get(product_id)
        if not existing:
            raise ProductNotFoundException(product_id)

        existing_data = existing.model_dump()
        new_data = product.model_dump(exclude_unset=True)
        updated_data = {**existing_data, **new_data}
        logging.info(updated_data)
        try:
            with get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "UPDATE products SET name=?, description=?, price=?, category=? WHERE id=?",
                    (updated_data["name"], updated_data["description"], updated_data["price"], updated_data["category"],
                     product_id)
                )
                conn.commit()
                return self.get(product_id)
        except Exception as e:
            logging.error(f"Updating product failed: {str(e)}")
            raise DatabaseException(f"Updating product failed: {str(e)}")

    def delete(self, product_id: int) -> DeleteResponse:
        """
            Delete an existing product with given id.
        """
        logging.info("in delete method")
        try:
            with get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM products WHERE id=?", (product_id,))
                conn.commit()
                affected = cursor.rowcount
                return DeleteResponse(product_id=product_id) if affected else None

        except Exception as e:
            logging.error(f"Deleting product failed: {str(e)}")
            raise DatabaseException(f"Deleting product failed: {str(e)}")

    def count_products(self,
                       name: Optional[str] = None,
                       category: Optional[str] = None) -> int:
        """
            Get the number of products matching the given parameters.
        """
        query = "SELECT COUNT(*) FROM products WHERE 1=1"
        params = []

        if name:
            query += " AND name LIKE ?"
            params.append(f"%{name}%")
        if category:
            query += " AND category LIKE ?"
            params.append(f"%{category}%")

        try:
            with get_connection() as conn:
                result = conn.execute(query, params).fetchone()
                return result[0] if result else 0
        except Exception as e:
            logging.error(f"Getting product count failed: {str(e)}")
            raise DatabaseException(f"Getting product count failed: {str(e)}")



