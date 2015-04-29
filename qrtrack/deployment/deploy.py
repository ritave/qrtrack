#!/usr/bin/env python
import argparse
import os
import sys
import shutil

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
SKEL_DIR = 'skeleton/'


def generate(directory, input_file, replacements={}):
    skeleton_file = os.path.join(BASE_DIR, SKEL_DIR, input_file)
    output_file = os.path.join(directory, input_file)
    with open(skeleton_file, 'r') as input_file:
        contents = input_file.read()
    for old, new in replacements.items():
        contents = contents.replace(old, new)
    with open(output_file, 'w') as output_file:
        output_file.write(contents)


def generate_all(directory):
    generate(directory, 'settings.py',
        {
            '__SECRET_KEY__': 'asd'
        })
    generate(directory, 'manage.py',
        {
            '__DIR__': directory,
        })
    generate(directory, 'wsgi.py',
        {
            '__DIR__': directory,
        })


def main():
    parser = argparse.ArgumentParser(description="Creates a Django deployment of qrtrack")
    parser.add_argument('dir', help="Non-existent directory where deployment will be created")
    args = parser.parse_args()

    args.dir = os.path.abspath(args.dir)

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