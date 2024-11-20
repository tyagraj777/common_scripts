#Use AWS CLI or Python (Boto3 library) to start/stop instances based on a schedule.
#python
import boto3

ec2 = boto3.client('ec2')

def stop_instances():
    ec2.stop_instances(InstanceIds=['i-xxxxxxxx'])
    print("Stopped instances: ['i-xxxxxxxx']")

stop_instances()

