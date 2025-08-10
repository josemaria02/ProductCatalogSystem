from fastapi import FastAPI
from app.database import init_db
from app.logging import configure_logging, LogLevels
from app.products import controller
from app.database import get_connection

#Initialize FastAPI application
app = FastAPI( title="Product Catalog API",
               description="A comprehensive product catalog system with CRUD operations",
               version="1.0.0",)

# Initialize database schema on startup
# Creates tables if they don't exist
init_db()

# Configure application logging
configure_logging(LogLevels.info)

# Register product routes with API prefix and tags
app.include_router(controller.router, prefix="/api/v1/products", tags=["products"])

@app.get("/")
def read_root():
    print("Root received")
    return {"message": "Welcome to the Product Catalog API"}

@app.get("/health")
def health_check():
    try:
        # Test database connection
        with get_connection() as conn:
            conn.execute("SELECT 1")
            return {
                "status": "healthy"
            }
    except Exception as e:
        return {
            "status": "unhealthy",
            "error": str(e)
        }




