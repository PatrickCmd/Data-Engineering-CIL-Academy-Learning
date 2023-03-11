#! /bin/bash

# Write a Shell Script to obtain the user's name and his age from input and print the year when the user would become 50 years of age
read -p "Enter your name: " NAME
echo "Your name is $NAME"

read -p "Enter your age: " AGE
echo "You are $AGE years old."

CURRENT_YEAR=$(date +'%Y')
AGE_DIFF=$[50-AGE]
YEAR_TO_BE_FIFTY="$((CURRENT_YEAR+AGE_DIFF))"
echo "You be 50 years old in $YEAR_TO_BE_FIFTY"
