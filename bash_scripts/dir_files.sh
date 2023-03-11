#! /bin/bash

# Write a Shell Script to create a directory called `test00` inside `/tmp` and three blank files `file01`, `file02`, `file03` inside it and list them

mkdir /tmp/test00
touch /tmp/test00/file01 /tmp/test00/file02 /tmp/test00/file03
LIST=`ls -l /tmp/test00`
echo -e "Files in /tmp/test00 are: \n$LIST"
