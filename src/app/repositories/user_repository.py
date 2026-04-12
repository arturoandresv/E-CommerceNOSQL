from boto3.dynamodb.conditions import Key
from app.database.dynamo import table

class UserRepository:

    def get_user(self, user_id: str):
        response = table.get_item(Key={
            "PK": f"USER#{user_id}",
            "SK": f"PROFILE#{user_id}"
        })
        return response.get("Item")

    def get_orders_by_user(self, user_id: str):
        response = table.query(
            KeyConditionExpression=
                Key("PK").eq(f"USER#{user_id}") &
                Key("SK").begins_with("ORDER#")
        )
        return response.get("Items", [])

    def get_payment_methods(self, user_id: str):
        response = table.query(
            KeyConditionExpression=
                Key("PK").eq(f"USER#{user_id}") &
                Key("SK").begins_with("PAYMENT_METHOD#")
        )
        return response.get("Items", [])

    def get_addresses(self, user_id: str):
        response = table.query(
            KeyConditionExpression=
                Key("PK").eq(f"USER#{user_id}") &
                Key("SK").begins_with("ADDRESS#")
        )
        return response.get("Items", [])

    def create_user(self, user_id: str, data: dict):
        item = {
            "PK": f"USER#{user_id}",
            "SK": f"PROFILE#{user_id}",
            **data
        }
        table.put_item(Item=item)
        return item