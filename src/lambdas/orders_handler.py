import json
from pydantic import ValidationError
from app.services.order_service import OrderService
from app.models.schemas import Order

service = OrderService()

def _respond(status_code, body):
    return {
        "statusCode": status_code,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(body)
    }

def get_order_detail(event, context):
    try:
        order_id = event.get("pathParameters", {}).get("order_id")
        result = service.get_order_detail(order_id)
        if not result:
             return _respond(404, {"error": "Order not found"})
        return _respond(200, result)
    except Exception as e:
        return _respond(500, {"error": str(e)})

def get_items_by_order(event, context):
    try:
        order_id = event.get("pathParameters", {}).get("order_id")
        result = service.get_items_by_order(order_id)
        return _respond(200, result)
    except Exception as e:
        return _respond(500, {"error": str(e)})

def create_order(event, context):
    try:
        body = json.loads(event.get("body", "{}"))
        # Validar payload usando Pydantic
        order = Order(**body)
        result = service.create_order(order.user_id, order.order_id, order.model_dump())
        return _respond(201, result)
    except ValidationError as e:
        return _respond(400, {"error": e.errors()})
    except Exception as e:
        return _respond(500, {"error": str(e)})
