from django.template.response import TemplateResponse
from qrtrack.qrcodes.models import QRTag
from qrtrack.qrcodes.unifiedUser import UnifiedUser


def collection_status_widget(request, collection):
    user = UnifiedUser(request)
    total_in_collection = QRTag.objects.filter(collection=collection, hidden=False).count()
    hidden_done_in_collection = user.owned_qrcodes.filter(collection=collection, hidden=True).count()
    done_in_collection = user.owned_qrcodes.filter(collection=collection, hidden=False).count()
    percent_done = (done_in_collection / total_in_collection) * 100.0

    return TemplateResponse(request, 'collection_widget.html', {
        'collection': collection,
        'total': total_in_collection,
        'done_hidden': hidden_done_in_collection,
        'done': done_in_collection,
        'percent_done': percent_done,
    })
