import boto3
import json
import os

SQS = boto3.client('sqs')

SQS_URL = os.environ.get('SQS_QUEUE_URL')


def lambda_handler(event, _context):
    if event.get('httpMethod', 'GET') == 'POST':
        # We got a POST request
        request_id = event.get('requestContext', {}).get(
            'requestId', 'UNKNOWN')

        response = SQS.send_message(
            QueueUrl=SQS_URL,
            MessageBody=request_id,

        )
        response_body = {
            'response': response
        }
    else:
        response = SQS.receive_message(
            QueueUrl=SQS_URL,
        )
        response_body = {
            'response': response
        }

    return {
        'statusCode': 200,
        'headers': {},
        'body': json.dumps(response_body)
    }
