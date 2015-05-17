from django.template.response import TemplateResponse
from django.shortcuts import redirect
from qrtrack.qrcodes.models import QRTag, QRCollection
from qrtrack.qrcodes.unifiedUser import UnifiedUser
from qrtrack.core.utils import Alerts
from qrtrack.qrcodes.controllers import SuggestionController
from qrtrack.qrcodes.widgets import collection_status_widget
from qrtrack.analytics.utils import track_event


def collect(request, collect_id):
    qrcode = QRTag.objects.by_collect_hashid_or_404(collect_id)
    u_user = UnifiedUser(request)
    if not u_user.has_qrcode(qrcode):
        u_user.collect_code(qrcode)
        request.session['just_collected'] = True
        track_event(request, 'collected', qrcode=qrcode.name)
    else:
        request.session['just_collected'] = False
    return redirect('show', permanent=False, show_id=qrcode.show_hashid)


def show(request, show_id):
    qrcode = QRTag.objects.by_show_hashid_or_404(show_id)
    track_event(request, 'shown', qrcode=qrcode.name)
    user = UnifiedUser(request)
    alerts = []

    suggest = None
    if request.user.is_authenticated():
        suggest = SuggestionController().suggest(qrcode, user)

    if 'just_collected' in request.session:
        if request.session['just_collected']:
            alerts = Alerts().success('Congratulations on getting this qrcode!').build()
        else:
            alerts = Alerts().info('You already had this qrcode before').build()
        del request.session['just_collected']

    context = {
        'qrcode': qrcode,
        'alerts': alerts,
        'suggest': suggest,
        'collection_widget':
            collection_status_widget(request, qrcode.collection).render().rendered_content
    }
    return TemplateResponse(request, 'show.html', context)
