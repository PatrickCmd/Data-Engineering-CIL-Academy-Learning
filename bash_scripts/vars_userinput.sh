#!/bin/sh
touch file1 file2
echo -n "Enter name of file to delete: "
read file
echo "Type 'y' to remove it, 'n' to change your mind..."
rm -i $file
echo "That was YOUR decision"
