import logging

from app.database import get_connection
from app.products.model import *
from typing import Optional


class ProductRepo:

    def list(self, limit: int = 10, offset: int = 0, name: Optional[str] = None, category: Optional[str] = None) -> List[Product]:
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
        logging.info("Params: " + str(params))
        logging.info("Query:" + str(query))

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(query, params)
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows]

    def get(self, product_id: int) -> Optional[dict]:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products WHERE id = ?", (product_id,))
        row = cursor.fetchone()
        conn.close()
        return dict(row) if row else None


    def create(self, product: ProductCreate) -> dict:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO products (name, description, price, category) VALUES (?, ?, ?, ?)",
            (product.name, product.description, product.price, product.category)
        )
        conn.commit()
        new_id = cursor.lastrowid
        conn.close()
        return self.get_by_id(new_id)

    def update(self, product_id: int, product: ProductUpdate) -> Optional[dict]:
        existing = self.get_by_id(product_id)
        if not existing:
            return None

        updated_data = {**existing, **product.dict(exclude_unset=True)}

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE products SET name=?, description=?, price=?, category=? WHERE id=?",
            (updated_data["name"], updated_data["description"], updated_data["price"], updated_data["category"],
             product_id)
        )
        conn.commit()
        conn.close()
        return self.get_by_id(product_id)

    def delete(self, product_id: int) -> bool:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM products WHERE id=?", (product_id,))
        conn.commit()
        affected = cursor.rowcount
        conn.close()
        return affected > 0

    def count_products(self,
                       name: Optional[str] = None,
                       category: Optional[str] = None) -> int:
        query = "SELECT COUNT(*) FROM products WHERE 1=1"
        params = []

        if name:
            query += " AND name LIKE ?"
            params.append(f"%{name}%")
        if category:
            query += " AND category LIKE ?"
            params.append(f"%{category}%")

        conn = get_connection()
        result = conn.execute(query, params).fetchone()
        return result[0] if result else 0



