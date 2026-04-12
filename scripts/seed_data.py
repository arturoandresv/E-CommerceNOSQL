# scripts/seed_data.py
import boto3
from dotenv import load_dotenv
import os
from decimal import Decimal

load_dotenv()

dynamodb = boto3.resource(
    "dynamodb",
    region_name=os.getenv("AWS_REGION"),
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    endpoint_url="http://localhost:3000"
)

table = dynamodb.Table(os.getenv("DYNAMODB_TABLE"))

def seed():
    # Usuario Luisa
    table.put_item(Item={
        "PK": "USER#1",
        "SK": "PROFILE#1",
        "user_id": "1",
        "name": "Luisa",
        "email": "l@x.com"
    })

    # Direcciones de Luisa
    table.put_item(Item={
        "PK": "USER#1",
        "SK": "ADDRESS#1",
        "address_id": "1",
        "user_id": "1",
        "street": "Calle 10",
        "city": "Bogotá"
    })
    table.put_item(Item={
        "PK": "USER#1",
        "SK": "ADDRESS#2",
        "address_id": "2",
        "user_id": "1",
        "street": "Ave. 5",
        "city": "Medellín"
    })

    # Métodos de pago de Luisa
    table.put_item(Item={
        "PK": "USER#1",
        "SK": "PAYMENT_METHOD#1",
        "payment_id": "1",
        "user_id": "1",
        "type": "Visa",
        "last_four": "1234"
    })
    table.put_item(Item={
        "PK": "USER#1",
        "SK": "PAYMENT_METHOD#2",
        "payment_id": "2",
        "user_id": "1",
        "type": "PayPal",
        "last_four": None
    })

    # Orden ORD#555 relacionada al usuario
    table.put_item(Item={
        "PK": "USER#1",
        "SK": "ORDER#555",
        "order_id": "555",
        "user_id": "1",
        "status": "Pago exitoso",
        "total": Decimal(1250.0),
        "created_at": "2023-10-27T08:00Z",
        "shipping_address": "Calle 10, Bogotá"
    })

    # Detalle de la orden
    table.put_item(Item={
        "PK": "ORDER#555",
        "SK": "DATA#555",
        "order_id": "555",
        "user_id": "1",
        "status": "Pago exitoso",
        "total": Decimal(1250.0),
        "created_at": "2023-10-27T08:00Z",
        "shipping_address": "Calle 10, Bogotá"
    })

    # Items de la orden
    table.put_item(Item={
        "PK": "ORDER#555",
        "SK": "ITEM#1",
        "item_id": "1",
        "order_id": "555",
        "product_name": "Laptop XPS",
        "quantity": 1,
        "unit_price": Decimal(1200.0),
        "subtotal": Decimal(1200.0)
    })
    table.put_item(Item={
        "PK": "ORDER#555",
        "SK": "ITEM#2",
        "item_id": "2",
        "order_id": "555",
        "product_name": "Libro: El Capital",
        "quantity": 2,
        "unit_price": Decimal(25.0),
        "subtotal": Decimal(50.0)
    })

    print("Test data succesfully inserted")

if __name__ == "__main__":
    seed()