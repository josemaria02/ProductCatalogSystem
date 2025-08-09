from fastapi import FastAPI
# from app.routes.v1 import product_routes
from app.routes.v1 import product_routes

app = FastAPI()

app.include_router(product_routes.router, prefix="/api/v1/products", tags=["products"])

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Product Catalog API"} 

@app.get("/health")
async def health_check():
    return {"status": "ok"}
