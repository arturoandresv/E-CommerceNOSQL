from fastapi import FastAPI
from app.routers import users, orders

app = FastAPI(
    title="E-Commerce NoSQL",
    version="1.0.0"
)

app.include_router(users.router)
app.include_router(orders.router)

@app.get("/")
def healt_check():
    return {
        "status": "ok",
        "message": "E-Commerce API running"
    }