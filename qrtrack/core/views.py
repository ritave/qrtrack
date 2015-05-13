from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from qrtrack.core.forms import RegistrationForm
from qrtrack.core.utils.widget_list import WidgetList

index_widgets = WidgetList()


def index(request):
    return TemplateResponse(request, 'index.html', {
        'widgets': index_widgets(request)
    })


def register(request):
    if request.user.is_authenticated():
        return redirect(reverse('index'))

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username,
                                            email,
                                            password)
            user.save()

            user = authenticate(username=username, password=password)
            login(request, user)

            if 'next' in request.GET:
                next = request.GET['next']
            else:
                next = reverse('index')
            return redirect(next)

    else:
        form = RegistrationForm()
    return TemplateResponse(request, 'registration/register.html',
        {'form': form}
    )
