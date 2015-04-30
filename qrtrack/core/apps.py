from django.apps import AppConfig
from django.conf import settings
import sys


# Checking settings version
class MyCoreAppConfig(AppConfig):
    name = 'qrtrack.core'

    def ready(self):
        if settings.DEVELOPMENT_SETTINGS_VERSION != settings.DEPLOYED_SETTINGS_VERSION:
            print('Your settings.py is outdated, refusing to start.\n'
                  'Check qrtrack.deployment.skeleton.settings.py file for differences and then '
                  'update your settings.py and change DEPLOYED_SETTINGS_VERSION', file=sys.stderr)
            sys.exit(1)
