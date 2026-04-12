import json
from app.repositories.order_repository import OrderRepository
from app.database.redis import redis_client
from app.database.dynamo import DecimalEncoder

class OrderService:

    def __init__ (self):
        self.repo = OrderRepository()
        self.redis = redis_client

    def get_order_detail(self, order_id: str):
        cache_key = f"order:{order_id}"
        cached = self.redis.get(cache_key)
        if cached:
            return json.loads(cached)
        item = self.repo.get_order_detail(order_id)
        if item:
            self.redis.setex(cache_key, 300, json.dumps(item, cls=DecimalEncoder))
        return item

    def get_items_by_order(self, order_id: str):
        cache_key = f"order:{order_id}:items"
        cached = self.redis.get(cache_key)
        if cached:
            return json.loads(cached)
        item = self.repo.get_items_by_order(order_id)
        if item:
            self.redis.setex(cache_key, 300, json.dumps(item, cls=DecimalEncoder))
        return item

    def create_order(self, user_id: str, order_id: str, data: dict):
        self.repo.create_order(user_id, order_id, data)
        self.redis.delete(f"user:{user_id}:orders")
        return data