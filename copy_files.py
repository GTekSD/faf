"""
Python script is designed to find files in the current directory and its subdirectories that are greater than or equal to 13 MB in size, 
sort them by size in descending order, write the sorted files and their sizes to a text file, 
and copy them to a new directory structure based on their original paths. 
The script achieves this through three functions: get_file_sizes, format_file_size, and copy_sorted_files, 
as well as a main function that orchestrates the execution of the other functions.
"""


import os
import shutil

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

def copy_sorted_files(sorted_files):
    """Copies the files in sorted_files to a new directory structure based on their original paths"""
    base_dir = os.path.abspath(os.path.dirname(__file__))
    output_dir = os.path.join(base_dir, 'Sorted')
    for file_path, file_size in sorted_files:
        formatted_size = format_file_size(file_size)
        output_path = os.path.join(output_dir, os.path.relpath(file_path, os.getcwd()))
        output_dirname = os.path.dirname(output_path)
        if not os.path.exists(output_dirname):
            os.makedirs(output_dirname)
        shutil.copy2(file_path, output_path)
        print(f'Copied {file_path} to {output_path}')
    print(f'Finished copying files to {output_dir}')

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
    
    # copy sorted files to new directory structure
    copy_sorted_files(sorted_files)
    
if __name__ == '__main__':
    main()
