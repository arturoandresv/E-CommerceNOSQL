from aws_cdk import (
    Stack,
    Duration,
    aws_lambda as _lambda,
    aws_apigateway as apigw,
)
from constructs import Construct

class EcommerceStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        api = apigw.RestApi(
            self, "EcommerceApiGateway",
            rest_api_name="Ecommerce API",
            description="API Gateway for Serverless E-commerce"
        )

        common_lambda_args = {
            "runtime": _lambda.Runtime.PYTHON_3_9,
            "code": _lambda.Code.from_asset("../src"),
            "timeout": Duration.seconds(30),
            "environment": {"ENV": "prod"}
        }

        get_user_lambda = _lambda.Function(self, "GetUserLambda", handler="lambdas.users_handler.get_user", **common_lambda_args)
        get_user_orders_lambda = _lambda.Function(self, "GetUserOrdersLambda", handler="lambdas.users_handler.get_orders_by_user", **common_lambda_args)
        get_user_payments_lambda = _lambda.Function(self, "GetUserPaymentsLambda", handler="lambdas.users_handler.get_payment_methods", **common_lambda_args)
        get_user_addresses_lambda = _lambda.Function(self, "GetUserAddressesLambda", handler="lambdas.users_handler.get_addresses", **common_lambda_args)
        create_user_lambda = _lambda.Function(self, "CreateUserLambda", handler="lambdas.users_handler.create_user", **common_lambda_args)

        users_resource = api.root.add_resource("users")
        users_resource.add_method("POST", apigw.LambdaIntegration(create_user_lambda))

        user_id_resource = users_resource.add_resource("{user_id}")
        user_id_resource.add_method("GET", apigw.LambdaIntegration(get_user_lambda))

        user_id_resource.add_resource("orders").add_method("GET", apigw.LambdaIntegration(get_user_orders_lambda))
        user_id_resource.add_resource("payment-methods").add_method("GET", apigw.LambdaIntegration(get_user_payments_lambda))
        user_id_resource.add_resource("addresses").add_method("GET", apigw.LambdaIntegration(get_user_addresses_lambda))

        get_order_lambda = _lambda.Function(self, "GetOrderLambda", handler="lambdas.orders_handler.get_order_detail", **common_lambda_args)
        get_order_items_lambda = _lambda.Function(self, "GetOrderItemsLambda", handler="lambdas.orders_handler.get_items_by_order", **common_lambda_args)
        create_order_lambda = _lambda.Function(self, "CreateOrderLambda", handler="lambdas.orders_handler.create_order", **common_lambda_args)

        orders_resource = api.root.add_resource("orders")
        orders_resource.add_method("POST", apigw.LambdaIntegration(create_order_lambda))

        order_id_resource = orders_resource.add_resource("{order_id}")
        order_id_resource.add_method("GET", apigw.LambdaIntegration(get_order_lambda))

        order_id_resource.add_resource("items").add_method("GET", apigw.LambdaIntegration(get_order_items_lambda))

