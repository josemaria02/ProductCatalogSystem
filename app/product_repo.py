from app.database import get_connection
from app.product_schema import *


class ProductRepo:
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

    def get_by_id(self, product_id: int) -> Optional[dict]:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products WHERE id = ?", (product_id,))
        row = cursor.fetchone()
        conn.close()
        return dict(row) if row else None

    def get_all(self) -> List[ProductResponse]:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products")
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows]

