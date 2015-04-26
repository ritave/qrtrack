import argparse
import os.path
import sys
import shutil


def generate(directory):
    pass


def main():
    parser = argparse.ArgumentParser(description="Creates a Django deployment of qrtrack")
    parser.add_argument('dir', help="Non-existent directory where deployment will be created")
    args = parser.parse_args()

    if os.path.exists(args.dir):
        print("The existing folder already exists, choose another location", file=sys.stderr)

    try:
        generate(args.dir)
    except BaseException:
        shutil.rmtree(args.dir)
        raise

if __name__ == "__main__":
    main()