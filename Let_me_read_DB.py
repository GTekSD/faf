"""
The script reads the contents of the input file in binary mode to ensure that all characters are included, then decodes the bytes using the utf-8 encoding with errors='replace' to replace any invalid characters with the ? character. It then writes the decoded text to the output file in text mode.

To use the script, save it as script.py and run it in the terminal with the following command:

python script.py <file_to_convert> -o <result.txt>

"""


import sys

def convert_to_text(input_file, output_file):
    try:
        with open(input_file, 'rb') as f:
            content = f.read().decode('utf-8', errors='replace')
        with open(output_file, 'w') as f:
            f.write(content)
        print(f"{input_file} successfully converted to {output_file}")
    except Exception as e:
        print(f"Error converting {input_file} to {output_file}: {str(e)}")

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: script.py <file_to_convert> -o <result.txt>')
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[3]
        convert_to_text(input_file, output_file)
