#!/bin/bash -ex
sudo apt-get update -y && sudo apt-get upgrade -y
wget https://aws-tc-largeobjects.s3-us-west-2.amazonaws.com/DEV-AWS-MO-GCNv2/FlaskApp.zip
sudo apt-get install zip -y
unzip FlaskApp.zip
cd FlaskApp/
apt-get -y install python3 mysql
apt install python3-pip -y
pip3 install -r requirements.txt
apt -y install stress
export PHOTOS_BUCKET=employee-photo-bucket-cmd-2023
export AWS_DEFAULT_REGION=us-east-1
export DYNAMO_MODE=on
FLASK_APP=application.py flask run --host=0.0.0.0 --port=80
