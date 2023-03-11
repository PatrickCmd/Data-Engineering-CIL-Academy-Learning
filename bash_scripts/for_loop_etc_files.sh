#! /bin/bash

# For loop example: files in /etc starting with n

for FILE in /etc/n*
do
  echo $FILE
done
