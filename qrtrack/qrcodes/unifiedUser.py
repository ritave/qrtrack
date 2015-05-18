"""
This class is a unified interface between session user and database user
it allows for collecting qrcode for both of those users
"""
from qrtrack.qrcodes.models import QRTag, CompletedTag


class UnifiedUser:
    def __init__(self, request=None, *, force_db=None, force_session=None):
        """Sets the user based on request and logged in user.
           Developer can force one or other implementation by providing the session or user object
           in force_session / force_db kwargs respectively"""
        if (force_db or force_session) and request is None:
            if force_db and force_session:
                raise ValueError('Can\'t have both forced session and db user')
            elif force_db:
                self.interface = _UnifiedDBUser(force_db)
            else:
                self.interface = _UnifiedSessionUser(force_session)
        elif request is not None:
            if request.user.is_authenticated():
                self.interface = _UnifiedDBUser(request.user)
            else:
                self.interface = _UnifiedSessionUser(request.session)
        else:
            raise ValueError('Request can\'t be None if no force kwarg was provided')

    def is_authenticated(self):
        return self.interface.is_authenticated

    def collect_code(self, qrobj):
        assert qrobj not in self.owned_qrcodes
        self.interface.collect_code(qrobj)

    def has_qrcode(self, qrobj):
        return qrobj in self.owned_qrcodes

    def remove_all_qrcodes(self):
        self.interface.remove_all_qrcodes()

    @property
    def owned_qrcodes(self):
        """Queryset object"""
        return self.interface.owned_qrcodes


class _UnifiedDBUser:
    def __init__(self, user):
        self._user = user

    def is_authenticated(self):
        return True

    def collect_code(self, qrobj):
        completed = CompletedTag(tag=qrobj, user=self._user)
        completed.save()

    def remove_all_qrcodes(self):
        CompletedTag.objects.filter(tag__in=self.owned_qrcodes).delete()

    @property
    def owned_qrcodes(self):
        return QRTag.objects.filter(completedtag__user=self._user)


class _UnifiedSessionUser():
    def __init__(self, session):
        self._session = session

    def is_authenticated(self):
        return False

    def collect_code(self, qrobj):
        if 'collected' not in self._session:
            self._session['collected'] = []
        self._session['collected'].append(qrobj.pk)

    def remove_all_qrcodes(self):
        if 'collected' in self._session:
            del self._session['collected']

    @property
    def owned_qrcodes(self):
        if 'collected' not in self._session:
            return QRTag.objects.none()
        return QRTag.objects.filter(pk__in=self._session['collected'])
