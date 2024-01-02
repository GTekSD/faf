
#!/usr/bin/env python

import sys
from collections import defaultdict
import pyperclip

def display_help():
    print("Usage: python merge_ports_domains.py input_file [-cp]")
    print("Example: python NessusPortMerger.py input.txt")
    print("         python NessusPortMerger.py input.txt -cp")
    sys.exit(1)

def print_logo():
    logo = """

 _____            _    _____                          
|  _  |NESSUS___ | |_ |     | ___  ___  ___  ___  ___ 
|   __|| . ||  _||  _|| | | || -_||  _|| . || -_||  _|
|__|   |___||_|  |_|  |_|_|_||___||_|  |_  ||___||_|  
             Created by Team GTekSD    |___|             
            https://gteksd.github.io/
"""


    print(logo)

if __name__ == "__main__":
    print_logo()
    
    if len(sys.argv) < 2 or len(sys.argv) > 3 or ("-cp" in sys.argv and len(sys.argv) != 3):
        print("Error: Please provide an input file and optionally use the -cp flag to copy the result to clipboard.")
        display_help()
    else:
        input_file = sys.argv[1]
        copy_to_clipboard = "-cp" in sys.argv

    # Read input file and process data
    if copy_to_clipboard:
        arguments = sys.argv[1:]
        arguments.remove("-cp")
        input_file = arguments[0]

    domain_ports = defaultdict(list)
    with open(input_file, 'r') as file:
        for line in file:
            line = line.strip()
            parts = line.split(':')
            if len(parts) == 2:
                domain, port = parts[0].strip(), parts[1].strip()
                domain_ports[domain].append(port)

    # Merge ports, remove duplicates, and sort in ascending order
    output = ""
    for domain, ports in sorted(domain_ports.items()):
        ports = sorted(set(ports), key=int)
        output += f"{domain}: {', '.join(ports)}\n"

    # Check if the -cp flag is used and copy the output to the clipboard
    if copy_to_clipboard:
        pyperclip.copy(output)
        print("BOOM!!!")
        print("Result copied to clipboard.")
    else:
        print(output)
        print("BOOM!!!")
