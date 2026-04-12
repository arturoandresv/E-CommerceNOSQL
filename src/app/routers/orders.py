from fastapi import APIRouter
from app.services.order_service import OrderService
from app.models.schemas import Order

router = APIRouter(prefix="/orders", tags=["Orders"])
service = OrderService()

@router.get("/{order_id}")
def get_order_detail(order_id: str):
    return service.get_order_detail(order_id)

@router.get("/{order_id}/items")
def get_items_by_order(order_id: str):
    return service.get_items_by_order(order_id)

@router.post("")
def create_order(order: Order):
    return service.create_order(order.user_id , order.order_id, order.model_dump())