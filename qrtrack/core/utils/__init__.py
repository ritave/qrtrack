from hashids import Hashids

from qrtrack.settings import SECRET_KEY
from core.constants import MINIMUM_HASHID_LENGTH

_hashid = Hashids(salt=SECRET_KEY, min_length=MINIMUM_HASHID_LENGTH)

def get_hashid():
    return _hashid