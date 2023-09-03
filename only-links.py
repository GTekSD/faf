# This script reads the content of the specified input_file, extracts all the links using regular expressions, and then processes the links based on the provided options. The extracted links are written to the output_file. You can use the options -d and -s to customize the behavior of the script.
# python only-links.py input_file output_file [-d] [-s]


import re
import argparse

# Define a regular expression pattern to match URLs
url_pattern = r'https?://\S+|www\.\S+'

# Function to extract links from a text
def extract_links(text):
    return re.findall(url_pattern, text)

# Function to remove everything from a text file except links
def remove_text_except_links(input_file, output_file, remove_duplicates, add_serial_numbers):
    with open(input_file, 'r', encoding='utf-8') as infile:
        text = infile.read()

    # Extract links from the text using the regex pattern
    links = extract_links(text)

    # Optionally remove duplicate links
    if remove_duplicates:
        links = list(set(links))

    # Optionally add serial numbers to the links
    if add_serial_numbers:
        links = [f"{i+1}. {link}" for i, link in enumerate(links)]

    # Join the links into a single string
    links_text = '\n'.join(links)

    # Write the extracted links to the output file
    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write(links_text)

def main():
    parser = argparse.ArgumentParser(description='Remove everything from a text file except links')
    parser.add_argument('input_file', help='Input text file')
    parser.add_argument('output_file', help='Output text file')
    parser.add_argument('-d', '--remove-duplicates', action='store_true', help='Remove duplicate links')
    parser.add_argument('-s', '--add-serial-numbers', action='store_true', help='Add serial numbers to links')

    args = parser.parse_args()
    input_file = args.input_file
    output_file = args.output_file
    remove_duplicates = args.remove_duplicates
    add_serial_numbers = args.add_serial_numbers

    remove_text_except_links(input_file, output_file, remove_duplicates, add_serial_numbers)

    print(f"Links extracted and saved to {output_file}")

if __name__ == "__main__":
    main()
