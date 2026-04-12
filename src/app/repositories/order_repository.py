from boto3.dynamodb.conditions import Key
from app.database.dynamo import table

class OrderRepository:

    def get_order_detail(self, order_id: str):
        response = table.get_item(Key={
            "PK": f"ORDER#{order_id}",
            "SK": f"DATA#{order_id}"
        })
        return response.get("Item")

    def get_items_by_order(self, order_id: str):
        response = table.query(
            KeyConditionExpression=
                Key("PK").eq(f"ORDER#{order_id}") &
                Key("SK").begins_with("ITEM#")
        )
        return response.get("Items", [])

    def create_order(self, user_id: str, order_id: str, data: dict):
        table.put_item(Item={
            "PK": f"USER#{user_id}",
            "SK": f"ORDER#{order_id}",
            **data
        })
        table.put_item(Item={
            "PK": f"ORDER#{order_id}",
            "SK": f"DATA#{order_id}",
            **data
        })
        return data