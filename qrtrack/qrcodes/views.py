from django.template.response import TemplateResponse
from django.shortcuts import redirect
from qrtrack.qrcodes.models import QRTag, QRCollection
from qrtrack.qrcodes.unifiedUser import UnifiedUser
from qrtrack.core.utils import Alerts
from qrtrack.qrcodes.controllers import SuggestionController


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
    qrcode = QRTag.objects.by_show_hashid_or_404(show_id)
    user = UnifiedUser(request)
    alerts = []
    suggest = None
    if 'just_collected' in request.session:
        if request.session['just_collected']:
            alerts = Alerts().success('Congratulations on getting this qrcode!').build()
        else:
            alerts = Alerts().info('You already had this qrcode before').build()
        del request.session['just_collected']
        suggest = SuggestionController().suggest(qrcode, user)

    total_in_collection = QRTag.objects.filter(collection=qrcode.collection).count()
    done_in_collection = QRTag.objects.\
        filter(pk__in=user.owned_qrcodes, collection=qrcode.collection).count()
    percent_done = (done_in_collection / total_in_collection) * 100.0


    context = {
        'qrcode': qrcode,
        'alerts': alerts,
        'suggest': suggest,
        'total': total_in_collection,
        'done': done_in_collection,
        'percent_done': percent_done,
    }
    return TemplateResponse(request, 'show.html', context)
