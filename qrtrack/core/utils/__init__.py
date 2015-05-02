from hashids import Hashids

from django.conf import settings
from qrtrack.core.constants import MINIMUM_HASHID_LENGTH

_collect_hashid = Hashids(salt=settings.COLLECT_ID_SALT, min_length=MINIMUM_HASHID_LENGTH)
_show_hashid = Hashids(salt=settings.SHOW_ID_SALT, min_length=MINIMUM_HASHID_LENGTH)


def get_collect_hashid():
    return _collect_hashid


def get_show_hashid():
    return _show_hashid


class Alerts:
    def __init__(self, before=None):
        if before is None:
            self._alerts = []
        else:
            self._alerts = before[:]  # Will be modified, we don't wanna modify what user gave us

    def info(self, msg):
        self._alert('info', msg)
        return self

    def warning(self, msg):
        self._alert('warn', msg)
        return self

    def build(self):
        return self._alerts

    def _alert(self, alert_type, msg):
        self._alerts += [{'type': alert_type, 'msg': msg}]
