from django.dispatch import receiver
from qrtrack.core.views import registration_successful
from qrtrack.qrcodes.unifiedUser import UnifiedUser

@receiver(registration_successful)
def copy_qrcodes_on_register(sender, request, user, **kwargs):
    """The user might have gotten many qrcodes before registering, we should copy them to his new
       account
    """
    session_user = UnifiedUser(force_session=request.session)
    db_user = UnifiedUser(force_db=user)

    for qrcode in session_user.owned_qrcodes.all():
        db_user.collect_code(qrcode)
