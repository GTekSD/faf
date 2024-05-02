#!/bin/bash

# Function to display usage information
usage() {
    echo "Usage: $0 <command> <filename>"
    echo "  -h, --help    Display this help message."
    echo ""
    echo "Developed by Сухас Дхолз | GtekSD."
    echo "Website: https://gteksd.github.io"
    exit 1
}

# Check if the help argument is provided
if [ "$#" -eq 1 ] && { [ "$1" = "-h" ] || [ "$1" = "--help" ]; }; then
    usage
elif [ "$#" -ne 2 ]; then
    echo "Error: Invalid number of arguments."
    usage
fi

command="$1"
filename="$2"

if [ ! -f "$filename" ]; then
    echo "Error: File '$filename' not found."
    exit 1
fi

while IFS= read -r line; do
    full_command="$command $line"
    echo "Executing: $full_command"
    eval "$full_command"
done < "$filename"
