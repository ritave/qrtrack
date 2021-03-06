#!/usr/bin/env python3
import argparse
import os
import sys
import shutil
from subprocess import check_call
import uuid
from qrtrack.deployment.init import init_env
from qrtrack.deployment.core_settings import DEVELOPMENT_SETTINGS_VERSION

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
SKEL_DIR = 'skeleton/'


def generate(directory, input_file, replacements={}, mode=None):
    skeleton_file_path = os.path.join(BASE_DIR, SKEL_DIR, input_file)
    output_file_path = os.path.join(directory, input_file)
    with open(skeleton_file_path, 'r') as input_file:
        contents = input_file.read()
    for old, new in replacements.items():
        contents = contents.replace(old, new)
    with open(output_file_path, 'w') as output_file:
        output_file.write(contents)
    if mode is not None:
        os.chmod(output_file_path, mode)


def generate_all(directory, production):
    generate(directory, 'settings.py',
        {
            '__SECRET_KEY__': str(uuid.uuid4()),
            '__COLLECT_SALT__': str(uuid.uuid4()),
            '__SHOW_SALT__': str(uuid.uuid4()),
            '__SETTINGS_VERSION__': DEVELOPMENT_SETTINGS_VERSION,
            '__STATIC_ROOT__': os.path.join(directory, 'static'),
            '__MEDIA_ROOT__': os.path.join(directory, 'media'),
        })
    generate(directory, 'manage.py',
        {
            '__DIR__': directory,
        },
        mode=0o0755)
    generate(directory, 'wsgi.py',
        {
            '__DIR__': directory,
        })

    init_env(directory)

    collect_static = [
        os.path.join(directory, 'manage.py'),
        'collectstatic', '--verbosity', '0', '--noinput'
    ]
    print('Collecting static files...')
    check_call(collect_static)


def main():
    parser = argparse.ArgumentParser(description="Creates a Django deployment of qrtrack")
    parser.add_argument('dir', help="Non-existent directory where deployment will be created")
    parser.add_argument(
        '--production',
        help='Does stuff a bit differently, for safer production',
        action='store_true',
        default=False
    )
    args = parser.parse_args()

    args.dir = os.path.abspath(args.dir)

    if os.path.exists(args.dir):
        print("The existing folder already exists, choose another location", file=sys.stderr)
        sys.exit(1)

    try:
        os.mkdir(args.dir)
        generate_all(args.dir, args.production)
    except BaseException:
        shutil.rmtree(args.dir, ignore_errors=True)
        raise

if __name__ == "__main__":
    main()
