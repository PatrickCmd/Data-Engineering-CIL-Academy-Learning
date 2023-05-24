"""The scenario
Amazon EC2 uses public–key cryptography to encrypt and decrypt login information. Public–key cryptography uses a public key to encrypt data, 
then the recipient uses the private key to decrypt the data. The public and private keys are known as a key pair.

In this example, Python code is used to perform several Amazon EC2 key pair management operations. 
The code uses the AWS SDK for Python to manage IAM access keys using these methods of the EC2 client class:
- describe_key_pairs.
- create_key_pair.
- delete_key_pair.

https://boto3.amazonaws.com/v1/documentation/api/latest/guide/ec2-example-key-pairs.html
"""

import os
import boto3

ec2 = boto3.client("ec2")


# Describe key pairs
def describe_key_pairs():
    """Describe one or more of your key pairs."""
    response = ec2.describe_key_pairs()
    # print(response)

    for key_pair in response["KeyPairs"]:
        print(f"Key Pair Id: {key_pair['KeyPairId']}")
        print(f"Key Name: {key_pair['KeyName']}")
        print(f"Key Tags: {key_pair['Tags']}")
        print()

    return response


# Create a key pair
def create_key_pair(key_pair_name):
    """Create a 2048-bit RSA key pair with a specified name using create_key_pair."""
    response = ec2.create_key_pair(KeyName=key_pair_name)
    # print(response)
    key_material = response["KeyMaterial"]

    # write 2048-bit RSA key to file
    key_file = f"{key_pair_name}.pem"
    with open(key_file, "w") as f:
        f.write(key_material)

    return response


# Delete a key pair
def delete_key_pair(key_pair_name):
    """Delete a key pair by removing the public key from Amazon EC2 using delete_key_pair."""
    response = ec2.delete_key_pair(KeyName=key_pair_name)
    print(response)

    # Remove key pair file
    filename = f"{key_pair_name}.pem"
    if os.path.exists(filename):
        os.remove(filename)


if __name__ == "__main__":
    print("""Describe one or more of your key pairs.""")
    describe_key_pairs()

    print(
        """Create a 2048-bit RSA key pair with a specified name using create_key_pair."""
    )
    key_pair_name = "boto3-key-pair"
    # uncomment line below to execute it
    # create_key_pair(key_pair_name)

    print(
        "Delete a key pair by removing the public key from Amazon EC2 using delete_key_pair."
    )
    delete_key_pair(key_pair_name)
