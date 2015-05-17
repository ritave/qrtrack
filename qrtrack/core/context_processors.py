from django.conf import settings

def contact_email(request):
    return {'contact_email': settings.CONTACT_EMAIL}
