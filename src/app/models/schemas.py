from pydantic import BaseModel, EmailStr
from typing import Optional

class UserProfile(BaseModel):
    user_id: str
    name: str
    email: EmailStr

class Address(BaseModel):
    address_id: str
    user_id: str
    street: str
    city: str

class PaymentMethod(BaseModel):
    payment_id: str
    user_id: str
    type: str                        
    last_four: Optional[str] = None  

class Order(BaseModel):
    order_id: str
    user_id: str
    status: str                   
    total: float
    created_at: str
    shipping_address: str

class OrderItem(BaseModel):
    item_id: str
    order_id: str
    product_name: str
    quantity: int
    unit_price: float
    subtotal: float

class UserPost(BaseModel):
    name: str
    email:str

class OrderPost(BaseModel):
    user_id: str
    status: str                   
    total: float
    created_at: str
    shipping_address: str