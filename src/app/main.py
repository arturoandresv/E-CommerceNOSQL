from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import users, orders

app = FastAPI(
    title="E-Commerce NoSQL",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # URL de Vite
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(orders.router)

@app.get("/")
def healt_check():
    return {
        "status": "ok",
        "message": "E-Commerce API running"
    }