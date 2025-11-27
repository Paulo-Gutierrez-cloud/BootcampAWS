import boto3
from pprint import pprint

ec2 = boto3.client("ec2")
response = ec2.describe_instances()

instance_id = response["Reservations"][0]["Instances"][0]["InstanceId"]

pprint(instance_id)

ec2.terminate_instances(InstanceIds=[instance_id])
pprint(f"Terminated instance {instance_id}")
