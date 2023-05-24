"""The scenario
In this example, Python code is used perform several basic instance management operations. The code uses the AWS SDK for Python to manage the instances by using these methods of the EC2 client class:

- describe_instances.
- monitor_instances.
- unmonitor_instances.
- start_instances.
- stop_instances.
- reboot_instances.

https://boto3.amazonaws.com/v1/documentation/api/latest/guide/ec2-example-managing-instances.html
"""

import sys
import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client("ec2")


# Describe instances
def describe_instances():
    """Describe one or more EC2 instances using describe_instances."""
    response = ec2.describe_instances()
    # print(response)
    for res in response["Reservations"]:
        for instance in res["Instances"]:
            print(f"Instance ID: {instance['InstanceId']}")
            print(f"Instance Type: {instance['InstanceType']}")
            print(f"Instance Name: {instance['KeyName']}")
            print(f"Instance Tags: {instance['Tags']}")
        print()


# Monitor and unmonitor instances
def monitor_unmonitor_instances(INSTANCE_ID):
    """Enable detailed monitoring for a running instance using monitor_instances.
    Disable detailed monitoring for a running instance using unmonitor_instances.
    """
    if action == "ON":
        response = ec2.monitor_instances(InstanceIds=[INSTANCE_ID])
    else:
        response = ec2.unmonitor_instances(InstanceIds=[INSTANCE_ID])
    print(response)

    return response


# Start and stop instances
def start_stop_instances(instance_id):
    """Start an Amazon EBS-backed AMI that you’ve previously stopped using start_instances.
    Stop an Amazon EBS-backed instance using stop_instances.
    """
    if action == "ON":
        # Do a dryrun first to verify permissions
        try:
            ec2.start_instances(InstanceIds=[instance_id], DryRun=True)
        except ClientError as e:
            if "DryRunOperation" not in str(e):
                raise

        # Dry run succeeded, run start_instances without dryrun
        try:
            response = ec2.start_instances(InstanceIds=[instance_id], DryRun=False)
            print(response)
        except ClientError as e:
            print(e)
    else:
        # Do a dryrun first to verify permissions
        try:
            ec2.stop_instances(InstanceIds=[instance_id], DryRun=True)
        except ClientError as e:
            if "DryRunOperation" not in str(e):
                raise

        # Dry run succeeded, call stop_instances without dryrun
        try:
            response = ec2.stop_instances(InstanceIds=[instance_id], DryRun=False)
            print(response)
        except ClientError as e:
            print(e)


# Reboot instances
def reboot_instances(instance_id):
    """Request a reboot of one or more instances using reboot_instances"""
    try:
        ec2.reboot_instances(InstanceIds=[instance_id], DryRun=True)
    except ClientError as e:
        if "DryRunOperation" not in str(e):
            print("You don't have permission to reboot instances.")
            raise

    try:
        response = ec2.reboot_instances(InstanceIds=[instance_id], DryRun=False)
        print("Success", response)
    except ClientError as e:
        print("Error", e)


if __name__ == "__main__":
    instance_id = sys.argv[2]
    action = sys.argv[1].upper()

    print("Describe one or more EC2 instances using describe_instances.")
    describe_instances()

    print("Monitor and unmonitor instances")
    monitor_unmonitor_instances(instance_id)

    print("Start and stop instances")
    start_stop_instances(instance_id)

    print("Reboot instance")
    reboot_instances(instance_id)
