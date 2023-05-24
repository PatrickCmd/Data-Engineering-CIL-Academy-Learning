"""A Sample Tutorial
This tutorial will show you how to use Boto3 with an AWS service. In this sample tutorial, 
you will learn how to use Boto3 with [Amazon Simple Queue Service (SQS)](http://aws.amazon.com/documentation/sqs/)

https://boto3.amazonaws.com/v1/documentation/api/latest/guide/sqs.html
"""

import boto3

# Get the service resource
sqs = boto3.resource("sqs")


# Creating a queue
def create_queue():
    # Create the queue. This returns an SQS.Queue instance
    queue = sqs.create_queue(
        QueueName="data-test-queue", Attributes={"DelaySeconds": "5"}
    )

    # You can now access identifiers and attributes
    print(queue.url)
    print(queue.attributes.get("DelaySeconds"))

    return queue


# Using an existing queue
def get_queue(name):
    # Get the queue. This returns an SQS.Queue instance
    queue = sqs.get_queue_by_name(QueueName=name)

    # You can now access identifiers and attributes
    print(queue.url)
    print(queue.attributes.get("DelaySeconds"))


# list all of your existing queues:
def list_queues():
    # Print out each queue name, which is part of its ARN
    # To get the name from a queue, you must use its ARN,
    # which is available in the queue’s attributes attribute.
    # Using queue.attributes['QueueArn'].split(':')[-1] will return its name.
    for queue in sqs.queues.all():
        name = queue.attributes["QueueArn"].split(":")[-1]
        print(f"Queue name: {name}")
        print(f"Queue URL: {queue.url}")


# Sending messages
# Sending a message adds it to the end of the queue:
def send_messages(queue_name):
    # Get the queue
    queue = sqs.get_queue_by_name(QueueName=queue_name)

    # Create a new message
    response = queue.send_message(MessageBody="Data streaming test message")

    # The response is NOT a resource, but gives you a message ID and MD5
    print(response.get("MessageId"))
    print(response.get("MD5OfMessageBody"))

    # create messages with custom attributes:
    body = "Boto3 Data streaming test message"
    response = queue.send_message(
        MessageBody=body,
        MessageAttributes={
            "Author": {"StringValue": "PatrickCmd", "DataType": "String"}
        },
    )

    print(response.get("MessageId"))
    print(response.get("MD5OfMessageBody"))


# Messages can also be sent in batches. For example, sending the
# two messages described above in a single request would look like the following:
def send_batch_messages(queue_name):
    # Get the queue
    queue = sqs.get_queue_by_name(QueueName=queue_name)

    response = queue.send_messages(
        Entries=[
            {"Id": "1", "MessageBody": "world"},
            {
                "Id": "2",
                "MessageBody": "boto3",
                "MessageAttributes": {
                    "Author": {"StringValue": "Daniel", "DataType": "String"}
                },
            },
        ]
    )

    # Print out any failures
    print(response.get("Failed"))


# Processing messages
# Messages are processed in batches:
def process_queue_messages(queue_name):
    # Get the queue
    queue = sqs.get_queue_by_name(QueueName=queue_name)

    # Process messages by printing out body and optional author name
    for message in queue.receive_messages(MessageAttributeNames=["Author"]):
        # Get the custom author message attribute if it was set
        author_text = ""
        if message.message_attributes is not None:
            author_name = message.message_attributes.get("Author").get("StringValue")
            if author_name:
                author_text = " ({0})".format(author_name)

        # Print out the body and author (if set)
        print("Hello, {0}!{1}".format(message.body, author_text))

        # Let the queue know that the message is processed
        message.delete()


if __name__ == "__main__":
    queue = create_queue()
    queue_name = name = queue.attributes["QueueArn"].split(":")[-1]
    get_queue(queue_name)

    print()
    print("Print out each queue name, which is part of its ARN")
    list_queues()

    print()
    print("Sending messages to queue")
    send_messages(queue_name)

    print()
    print("Processing messages in queue")
    process_queue_messages(queue_name)
