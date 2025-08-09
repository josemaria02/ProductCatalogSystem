from fastapi import FastAPI
import uvicorn


from app.database import init_db
# from app.routes.v1 import product_routes
from app.routes.v1 import product_routes

app = FastAPI()

init_db()

app.include_router(product_routes.router, prefix="/api/v1/products", tags=["products"])

@app.get("/")
async def read_root():
    print("Root received")
    return {"message": "Hello World"}
    # return {"message": "Welcome to the Product Catalog API"}

@app.get("/health")
async def health_check():
    return {"status": "ok"}




