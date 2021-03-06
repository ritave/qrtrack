"""
WSGI config for qrtrack project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from qrtrack.deployment.init import init_env

init_env('__DIR__')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "qrtrack.settings")

application = get_wsgi_application()
