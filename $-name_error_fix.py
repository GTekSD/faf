#script to remove "$" from file name which gives an error while rebuild an apk with an apktool.

import os
import argparse

def remove_dollar_signs(path):
    for root, dirs, files in os.walk(path):
        for filename in files:
            if "$" in filename:
                new_filename = filename.replace("$", "")
                os.rename(os.path.join(root, filename), os.path.join(root, new_filename))
                print(f"Renamed {filename} to {new_filename}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--directory", help="Directory to remove $ character from filenames")
    args = parser.parse_args()

    if args.directory:
        remove_dollar_signs(args.directory)
    else:
        print("Please provide a directory path with -d option")
