from fastapi import APIRouter
from app.repositories.user_repository import UserRepository
from app.models.schemas import UserProfile

router = APIRouter(prefix="/users", tags=["Users"])
repo = UserRepository()

@router.get("/{user_id}")
def get_user(user_id: str):
    return repo.get_user(user_id)

@router.get("/{user_id}/orders")
def get_orders_by_user(user_id: str):
    return repo.get_orders_by_user(user_id)
    
@router.get("/{user_id}/payment-methods")
def get_payment_methods(user_id: str):
    return repo.get_payment_methods(user_id)

@router.get("/{user_id}/addresses")
def get_addresses(user_id: str):
    return repo.get_addresses(user_id)

@router.post("")
def create_user(user: UserProfile):
    return repo.create_user(user.name, user.model_dump())