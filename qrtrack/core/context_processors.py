from django.conf import settings
from django.core.urlresolvers import reverse

def core_processor(request):
    return {
        'contact_email': settings.CONTACT_EMAIL,
        'show_profile_link': request.path_info != reverse('profile'),
    }
