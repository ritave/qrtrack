from django.template.response import TemplateResponse
from django.shortcuts import redirect
from django.utils.translation import ugettext as _
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
        track_event(request, 'qrcode_collected', collection=qrcode.collection.name, qrcode=qrcode.name)
    else:
        request.session['just_collected'] = False
    return redirect('show', permanent=False, show_id=qrcode.show_hashid)


def show(request, show_id):
    qrcode = QRTag.objects.by_show_hashid_or_404(show_id)
    track_event(request, 'qrcode_shown', collection=qrcode.collection.name, qrcode=qrcode.name)
    user = UnifiedUser(request)
    alerts = Alerts()

    suggest = SuggestionController().suggest(qrcode, user)

    if 'just_collected' in request.session:
        if request.session['just_collected']:
            if user.owned_qrcodes.count() == 1:
                alerts.success(_("I see you got your first qrcode, throughout the building we have"
                                 " hidden a lot more, can you find the all and complete your"
                                 " collection?"))
            else:
                alerts.info(_("This qrcode has been added to your collection."))
        else:
            alerts.warning(_("You already collected qrcode before"))
        del request.session['just_collected']

    context = {
        'qrcode': qrcode,
        'alerts': alerts.build(),
        'suggest': suggest,
        'collection_widget':
            collection_status_widget(request, qrcode.collection).render().rendered_content
    }
    return TemplateResponse(request, 'show.html', context)
