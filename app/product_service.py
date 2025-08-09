from app.product_model import Product
from app.product_schema import ProductCreate, ProductUpdate, ProductResponse

class ProductService:
    def __init__(self):
        self.db = []

    def create_product(self, product: ProductCreate) -> ProductResponse:
        self.db.append(product)
        return product
    
    def get_product(self, product_id: int) -> ProductResponse:
        for product in self.db:
            if product.id == product_id:
                return product