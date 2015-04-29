#!/usr/bin/env python
import argparse
import os
import sys
import shutil

SKEL_DIR = 'skeleton/'


def generate(directory, file, replacements):
    skeleton_file = os.path.join(SKEL_DIR, file)
    output_file = os.path.join(directory, file)
    with open(skeleton_file, 'r') as file:
        contents = file.read()
    for old, new in replacements.items():
        contents = contents.replace(old, new)
    with open(output_file, 'w') as file:
        file.write(contents)


def generate_all(directory):
    generate(directory, 'settings.py',
        {
            '__SECRET_KEY__': 'asd'
        })


def main():
    parser = argparse.ArgumentParser(description="Creates a Django deployment of qrtrack")
    parser.add_argument('dir', help="Non-existent directory where deployment will be created")
    args = parser.parse_args()

    if os.path.exists(args.dir):
        print("The existing folder already exists, choose another location", file=sys.stderr)

    try:
        os.mkdir(args.dir)
        generate_all(args.dir)
    except BaseException:
        shutil.rmtree(args.dir, ignore_errors=True)
        raise

if __name__ == "__main__":
    main()