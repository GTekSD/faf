#!/bin/bash

# loop through a list of IP addresses and ping them one by one
#usage: ping_ips.sh <ip_list_file>

if [ $# -eq 0 ]; then
    echo "Usage: $0 <ip_list_file>"
    exit 1
fi

while read -r ip; do
    if ping -c 1 "$ip" >/dev/null; then
        echo "$ip is up"
    else
        echo "$ip is down"
    fi
done < "$1"
