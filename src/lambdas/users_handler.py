import json
from pydantic import ValidationError
from app.services.user_service import UserService
from app.models.schemas import UserProfile

service = UserService()

def _respond(status_code, body):
    # Asegurar que el body sea un dict/list para serializarlo
    return {
        "statusCode": status_code,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(body)
    }

def get_user(event, context):
    try:
        user_id = event.get("pathParameters", {}).get("user_id")
        result = service.get_user(user_id)
        if not result:
            return _respond(404, {"error": "User not found"})
        return _respond(200, result)
    except Exception as e:
        return _respond(500, {"error": str(e)})

def get_orders_by_user(event, context):
    try:
        user_id = event.get("pathParameters", {}).get("user_id")
        result = service.get_orders_by_user(user_id)
        return _respond(200, result)
    except Exception as e:
        return _respond(500, {"error": str(e)})

def get_payment_methods(event, context):
    try:
        user_id = event.get("pathParameters", {}).get("user_id")
        result = service.get_payment_methods(user_id)
        return _respond(200, result)
    except Exception as e:
        return _respond(500, {"error": str(e)})

def get_addresses(event, context):
    try:
        user_id = event.get("pathParameters", {}).get("user_id")
        result = service.get_addresses(user_id)
        return _respond(200, result)
    except Exception as e:
        return _respond(500, {"error": str(e)})

def create_user(event, context):
    try:
        body = json.loads(event.get("body", "{}"))
        # Validar payload usando Pydantic
        user = UserProfile(**body)
        result = service.create_user(user.user_id, user.model_dump())
        return _respond(201, result)
    except ValidationError as e:
        return _respond(400, {"error": e.errors()})
    except Exception as e:
        return _respond(500, {"error": str(e)})
