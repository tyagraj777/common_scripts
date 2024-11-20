#Purpose: Automate creating IAM users and attaching policies.

import boto3

iam = boto3.client('iam')

def create_user(username):
    iam.create_user(UserName=username)
    iam.attach_user_policy(
        UserName=username,
        PolicyArn='arn:aws:iam::aws:policy/AmazonS3FullAccess'
    )
    print(f"User {username} created with S3 access.")

create_user('new-user')
