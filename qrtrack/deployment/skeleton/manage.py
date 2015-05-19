#!/usr/bin/env python3
import os
import sys
from qrtrack.deployment.init import init_env

if __name__ == "__main__":
    init_env('__DIR__')

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
