"""The scenario
In this example, Python code is used to get details about regions and Availability Zones. 
The code uses the AWS SDK for Python to get the data by using these methods of the EC2 client class:

- describe_regions.
- describe_availability_zones.

https://boto3.amazonaws.com/v1/documentation/api/latest/guide/ec2-example-regions-avail-zones.html
"""

import boto3

ec2 = boto3.client("ec2")


# Describe Regions and Availability Zones
def describe_regions_az():
    """Describe one or more Regions that are currently available to you.
    Describe one or more of the Availability Zones that are available to you
    """

    # Retrieves all regions/endpoints that work with EC2
    print("Retrieves all regions/endpoints that work with EC2")
    response = ec2.describe_regions()
    for region in response["Regions"]:
        print(f"Regions name: {region['RegionName']}")
    print()

    # Retrieves availability zones only for region of the ec2 object
    print("Retrieves availability zones only for region of the ec2 object")
    response = ec2.describe_availability_zones()
    for az in response["AvailabilityZones"]:
        print(f"Availability Zone Region: {az['RegionName']}")
        print(f"Availability Zone Name: {az['ZoneName']}")
        print(f"Availability Zones Id: {az['ZoneId']}")
        print(f"Availability Zones State: {az['State']}")
        print()


if __name__ == "__main__":
    print("Describe Regions and Availability Zones")
    describe_regions_az()
