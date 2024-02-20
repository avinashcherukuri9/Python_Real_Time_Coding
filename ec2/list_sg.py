import boto3
client = boto3.client('ec2')

def list_security_groups() -> list:
    groups = ec2.security_groups.all()
    return  list(groups)
    