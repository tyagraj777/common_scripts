#Automate scanning logs for errors and sending notifications.

import boto3

cloudwatch = boto3.client('logs')

def monitor_logs():
    response = cloudwatch.filter_log_events(
        logGroupName='my-log-group',
        filterPattern='ERROR'
    )
    for event in response['events']:
        print(event['message'])

monitor_logs()
