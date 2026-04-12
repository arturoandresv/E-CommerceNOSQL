import boto3
from dotenv import load_dotenv
import os

load_dotenv()

dynamodb = boto3.resource(
    "dynamodb",
    region_name=os.getenv("AWS_REGION"),
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    endpoint_url="http://localhost:3000"
)

def create_table():
    table = dynamodb.create_table(
        TableName=os.getenv("DYNAMODB_TABLE"),
        AttributeDefinitions=[
            {"AttributeName": "PK", "AttributeType": "S"},
            {"AttributeName": "SK", "AttributeType": "S"}
        ],
        KeySchema=[
            {"AttributeName": "PK", "KeyType": "HASH"},
            {"AttributeName": "SK", "KeyType": "RANGE"}
        ],
        BillingMode="PAY_PER_REQUEST"
    )
    print(f"Table created: {table.table_name}")

if __name__ == "__main__":
    create_table()