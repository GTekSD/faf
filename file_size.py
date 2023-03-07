"""
Python script that searches a directory and its subdirectories for files larger than 13MB 
and outputs a sorted list of the file paths and their sizes to a text file. 
It also prints the list to the console and displays the total number of files found.
"""


import os

def get_file_sizes(path):
    """Returns a dictionary containing the sizes of all files in the given path and its subdirectories"""
    file_sizes = {}
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            file_size = os.path.getsize(file_path)
            if file_size >= 13000000: # check if file size is greater than 13MB
                file_sizes[file_path] = file_size
    return file_sizes

def format_file_size(size):
    """Formats the given file size in megabytes (MB)"""
    mb_size = size / (1024 * 1024)
    return f'{mb_size:.2f} MB'

def main():
    # get file sizes in current directory and subdirectories
    file_sizes = get_file_sizes('.')
    
    # sort files by size in descending order
    sorted_files = sorted(file_sizes.items(), key=lambda x: x[1], reverse=True)
    
    # write sorted files and their sizes to a text file
    with open('file_sizes.txt', 'w', encoding='utf-8') as f:
        count = 0
        for file_path, file_size in sorted_files:
            formatted_size = format_file_size(file_size)
            f.write(f'{file_path}: {formatted_size}\n')
            print(f'{file_path}: {formatted_size}')
            count += 1
        
        print(f'Total files found: {count}')
    
if __name__ == '__main__':
    main()
