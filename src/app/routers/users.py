from fastapi import APIRouter
from app.services.user_service import UserService
from app.models.schemas import UserProfile

router = APIRouter(prefix="/users", tags=["Users"])
service = UserService()

@router.get("/{user_id}")
def get_user(user_id: str):
        return service.get_user(user_id)

@router.get("/{user_id}/orders")
def get_orders_by_user(user_id: str):
        return service.get_orders_by_user(user_id)
        
@router.get("/{user_id}/payment-methods")
def get_payment_methods(user_id: str):
        return service.get_payment_methods(user_id)

@router.get("/{user_id}/addresses")
def get_addresses(user_id: str):
        return service.get_addresses(user_id)

@router.post("")
def create_user(user: UserProfile):
       return service.create_user(user.user_id, user.model_dump())