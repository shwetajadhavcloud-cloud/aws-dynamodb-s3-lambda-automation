import json
import boto3
from uuid import uuid4

def lambda_handler(event, context):
    try:
        print("Received event:", json.dumps(event))
        
        # Initialize AWS clients
        s3 = boto3.client("s3")
        dynamodb = boto3.resource('dynamodb')
        
        # Check if this is an S3 event
        if 'Records' in event:
            for record in event['Records']:
                bucket_name = record['s3']['bucket']['name']
                object_key = record['s3']['object']['key']
                size = record['s3']['object'].get('size', -1)
                event_name = record['eventName']
                event_time = record['eventTime']
                
                # Connect to DynamoDB table
                dynamo_table = dynamodb.Table('newtable')
                
                # Insert S3 event details into DynamoDB
                dynamo_table.put_item(
                    Item={
                        'unique': str(uuid4()),
                        'Bucket': bucket_name,
                        'Object': object_key,
                        'Size': size,
                        'Event': event_name,
                        'EventTime': event_time
                    }
                )
            
            return {
                'statusCode': 200,
                'headers': {'Content-Type': 'application/json'},
                'body': json.dumps({'message': 'S3 event processed successfully'})
            }
        
        else:
            # For direct Function URL or test invocation
            return {
                'statusCode': 200,
                'headers': {'Content-Type': 'application/json'},
                'body': json.dumps({'message': 'Lambda is alive. Send an S3 event to trigger processing.'})
            }
    
    except Exception as e:
        print(f"Error: {e}")
        return {
            'statusCode': 500,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({'error': str(e)})
        }
