#!/bin/bash

# This is a Bash script that takes a filename as input and creates a directory with the name specified in each line of the file

if [ -z "$1" ]; then
    echo "Error: No filename provided"
    exit 1
fi

while IFS= read -r line; do
    mkdir "$line"
done < "$1"
