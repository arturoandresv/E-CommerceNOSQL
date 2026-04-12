import boto3 
from app.config import settings 

endpoint_url = "http://localhost:3000"

dynamodb = boto3.resource(
    "dynamodb",
    region_name=settings.AWS_REGION,
    aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
    endpoint_url=endpoint_url
)

table = dynamodb.Table(settings.DYNAMODB_TABLE)