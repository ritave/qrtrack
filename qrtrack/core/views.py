from django.template.response import TemplateResponse
from qrtrack.core.forms import RegistrationForm


def index(request):
    return TemplateResponse(request, 'index.html')


def register(request):
    if request.method == 'POST':
        pass
    else:
        form = RegistrationForm()
    return TemplateResponse(request, 'registration/register.html',
        {'form': form}
    )