from fastapi import HTTPException

class ProductException(HTTPException):
    """
        Base exception for product-related errors.
    """
    pass

class ProductNotFoundException(ProductException):
    """
        Exception raised when a product is not found.
    """
    def __init__(self, product_id: int):
        super().__init__(status_code=404, detail=f"Product with id {product_id} not found.")

class DatabaseException(ProductException):
    """
        Exception raised when database operations fail.
    """
    def __init__(self, operation: str):
        super().__init__(status_code=500, detail=f"Database error during {operation}")