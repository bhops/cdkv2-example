from aws_cdk import (
    Duration,
    Stack,
    aws_sqs as sqs,
    aws_lambda as _lambda,  # must not conflict with python's builtin lambda
    aws_apigateway as apigateway,
)
from constructs import Construct


class Cdkv2ExamplesStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        queue = sqs.Queue(
            self, "Cdkv2ExamplesQueue",
            retention_period=Duration.days(1),
            visibility_timeout=Duration.seconds(300),
        )

        home_page = _lambda.Function(
            self,
            "HomePage",
            runtime=_lambda.Runtime.PYTHON_3_8,
            handler='app.lambda_handler',
            environment={
                'SQS_QUEUE_URL': queue.queue_url,
            },
            code=_lambda.Code.from_asset('home_page')
        )

        queue.grant_send_messages(home_page)
        queue.grant_consume_messages(home_page)

        api = apigateway.RestApi(self, "cdkv2-example-api",
                                 rest_api_name="cdkv2-example",
                                 description="An example api gateway with cdk")

        home_page_integration = apigateway.LambdaIntegration(home_page,
                                                             request_templates={"application/json": '{ "statusCode": "200" }'})

        api.root.add_method("GET", home_page_integration)   # GET /
        api.root.add_method("POST", home_page_integration)  # POST /
