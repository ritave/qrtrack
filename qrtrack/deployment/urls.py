from django.conf.urls import include, url
from django.conf import settings
from importlib import import_module

urlpatterns = []

for app in settings.INSTALLED_APPS:
    if app.startswith('qrtrack.'):
        try:
            imported = import_module(app + '.urls')
            urlpatterns += imported.urlpatterns
        except ImportError:
            pass
