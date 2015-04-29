from hashids import Hashids

from django.conf import settings
from qrtrack.core.constants import MINIMUM_HASHID_LENGTH

_hashid = Hashids(salt=settings.SECRET_KEY, min_length=MINIMUM_HASHID_LENGTH)


def get_hashid():
    return _hashid
