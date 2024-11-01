import json
import boto3
from datetime import datetime
import os

# Initialize DynamoDB client
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

def handler(event, context):
    # Get current timestamp
    timestamp = datetime.now().isoformat()

    # Create item to store
    item = {
        'id': str(event.get('id', timestamp)),
        'timestamp': timestamp,
        'data': event.get('data', 'No data provided')
    }

    # Store item in DynamoDB
    table.put_item(Item=item)

    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Item stored successfully',
            'item': item
        })
    }