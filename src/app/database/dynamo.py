import boto3
import json
from decimal import Decimal
from app.config import settings

# Custom encoder to handle Decimal types from DynamoDB
class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return super().default(obj)

endpoint_url = "http://localhost:3000"

dynamodb = boto3.resource(
    "dynamodb",
    region_name=settings.AWS_REGION,
    aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
    endpoint_url=endpoint_url
)

table = dynamodb.Table(settings.DYNAMODB_TABLE)