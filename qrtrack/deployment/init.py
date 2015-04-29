import os
import sys


def init_env(deploy_dir):
    os.chdir(deploy_dir)
    sys.path.insert(0, deploy_dir)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
