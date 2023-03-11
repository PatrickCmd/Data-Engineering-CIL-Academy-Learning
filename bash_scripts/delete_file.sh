#! /bin/bash

# Write a Shell Script to delete the file `file03` in the question 2 above and also print the time after the deletion of the file

echo "Delete file file03 from /tmp/test00"
read -p "Enter file03 as filename: " FILE
echo "Type 'y' to remove it, 'n' to change your mind..."
rm -i /tmp/test00/${FILE}

LIST=`ls -l /tmp/test00`
echo -e "Files in /tmp/test00 are: \n$LIST"
CURRENT_TIME=`date +"%T"`
echo "Current time is: $CURRENT_TIME"
