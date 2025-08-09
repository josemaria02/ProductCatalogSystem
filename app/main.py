from fastapi import FastAPI
from app.database import init_db
from app.logging import configure_logging, LogLevels
from app.products import controller

app = FastAPI()

init_db()

configure_logging(LogLevels.debug)

app.include_router(controller.router, prefix="/api/v1/products", tags=["products"])

@app.get("/")
async def read_root():
    print("Root received")
    return {"message": "Welcome to the Product Catalog API"}

@app.get("/health")
async def health_check():
    return {"status": "ok"}




