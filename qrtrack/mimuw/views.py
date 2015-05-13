from django.template.response import TemplateResponse
from qrtrack.core.utils.widget_list import widget
from qrtrack.qrcodes.models import QRCollection
from qrtrack.core.views import profile_widgets
from qrtrack.qrcodes.widgets import collection_status_widget
from qrtrack.qrcodes.unifiedUser import UnifiedUser


@widget(profile_widgets)
def profile_collection_widget(request):
    user = UnifiedUser(request)
    first_collection = QRCollection.objects.first()
    return TemplateResponse(request, 'widgets/profile_collection.html', {
        'collection_widget':
            collection_status_widget(request, first_collection).render().rendered_content,
        'qrcodes': user.owned_qrcodes,
    })