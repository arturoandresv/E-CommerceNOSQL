import json
import uuid
from fastapi import BackgroundTasks
from app.repositories.user_repository import UserRepository
from app.database.redis import redis_client
from app.database.dynamo import DecimalEncoder

class UserService:

    def __init__(self):
        self.repo = UserRepository()
        self.redis = redis_client

    def get_user(self, user_id: str):
        cache_key = f"user:{user_id}"
        cached = self.redis.get(cache_key)
        if cached:
            return {
            "source": "Redis (cache)",
            "user": json.loads(cached)
        }
        item = self.repo.get_user(user_id)
        if item:
            self.redis.setex(cache_key, 300, json.dumps(item))
        return item

    def get_orders_by_user(self, user_id):
        cache_key = f"user:{user_id}:orders"
        cached = self.redis.get(cache_key)
        if cached:
            return {
            "source": "Redis (cache)",
            "user": json.loads(cached)
        }
        item = self.repo.get_orders_by_user(user_id)
        if item:
            self.redis.setex(cache_key, 300, json.dumps(item, cls=DecimalEncoder))
        return item

    def get_payment_methods(self, user_id):
        cache_key = f"user:{user_id}:payments"
        cached = self.redis.get(cache_key)
        if cached:
            return {
            "source": "Redis (cache)",
            "user": json.loads(cached)
        }
        item = self.repo.get_payment_methods(user_id)
        if item:
            self.redis.setex(cache_key, 300, json.dumps(item))
        return item

    def get_addresses(self, user_id):
        cache_key = f"user:{user_id}:addresses"
        cached = self.redis.get(cache_key)
        if cached:
            return {
            "source": "Redis (cache)",
            "user": json.loads(cached)
        }
        item = self.repo.get_addresses(user_id)
        if item:
            self.redis.setex(cache_key, 300, json.dumps(item))
        return item
    
    def create_user(self, data: dict, background_tasks: BackgroundTasks):
        user_id = str(uuid.uuid4())
        data["user_id"] = user_id

        cache_key = f"user:{user_id}"
        self.redis.setex(cache_key, 300, json.dumps(data, cls=DecimalEncoder))

        background_tasks.add_task(self.repo.create_user, user_id, data)

        return data
    