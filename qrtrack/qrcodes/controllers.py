from qrtrack.qrcodes.models import QRTag


class _CollectionSuggestionController:
    """Suggests another random from collection which the user doesn't have"""
    def __init__(self):
        pass

    def suggest(self, last_collected, user):
        """Accepts last_collected qrcode and UnifiedUser"""
        owned = user.owned_qrcodes
        return QRTag.objects.exclude(pk__in=owned).filter(collection=last_collected.collection)\
            .order_by('?').first()


class SuggestionController:
    _interface_class = _CollectionSuggestionController

    def __init__(self):
        self._interface = SuggestionController._interface_class()

    def suggest(self, last_collected, user):
        if user.is_authenticated() or user.owned_qrcodes.count() <= 3:
            return self._interface.suggest(last_collected, user)
        return None
