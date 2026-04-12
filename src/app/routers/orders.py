from fastapi import APIRouter
from app.repositories.order_repository import OrderRepository
from app.models.schemas import Order, OrderItem

router = APIRouter(prefix="/orders", tags=["Orders"])
repo = OrderRepository()

@router.get("/{order_id}")
def get_order_detail(order_id: str):
    return repo.get_order_detail(order_id)

@router.get("/{order_id}/items")
def get_items_by_order(order_id: str):
    return repo.get_items_by_order(order_id)

@router.post("")
def create_order(order: Order):
    return repo.create_order(order.user_id , order.order_id, order.model_dump())