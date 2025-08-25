# app/main.py
from fastapi import FastAPI
from app.api import endpoints

app = FastAPI(
    title="Python Service API",
    description="A sample FastAPI service",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.include_router(endpoints.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Python Service API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)