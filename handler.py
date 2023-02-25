import json


def hello(event, context):
    body = {
        "message": "Your function executed successfully!",
        "input": event,
    }

    response = {"statusCode": 200, "body": len(event['body'])}

    return response
