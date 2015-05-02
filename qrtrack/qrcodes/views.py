from django.template.response import TemplateResponse
from django.shortcuts import redirect
from qrtrack.qrcodes.models import QRTag
from qrtrack.qrcodes.unifiedUser import UnifiedUser
from qrtrack.core.utils import Alerts


def collect(request, collect_id):
    qrcode = QRTag.objects.by_collect_hashid_or_404(collect_id)
    u_user = UnifiedUser(request)
    if not u_user.has_qrcode(qrcode):
        u_user.collect_code(qrcode)
        request.session['just_collected'] = True
    else:
        request.session['just_collected'] = False
    return redirect('show', permanent=False, show_id=qrcode.show_hashid)


def show(request, show_id):
    alerts = []
    if 'just_collected' in request.session:
        if request.session['just_collected']:
            alerts = Alerts().info('Got it now').build()
        else:
            alerts = Alerts().info('Already got it').build()
        del request.session['just_collected']

    context = {
        'qrcode': QRTag.objects.by_show_hashid_or_404(show_id),
        'alerts': alerts
    }
    return TemplateResponse(request, 'show.html', context)
