from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from qrtrack.core.forms import RegistrationForm
from qrtrack.core.utils.widget_list import WidgetList
from qrtrack.analytics.utils import track_event

profile_widgets = WidgetList()


def index(request):
    track_event(request, 'index_page_visitted')
    return profile(request)


def profile(request):
    track_event(request, 'profile_page_visitted')
    return TemplateResponse(request, 'registration/profile.html', {
        'widgets': profile_widgets(request)
    })


def register(request):
    if request.user.is_authenticated():
        return redirect(reverse('index'))

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        track_event(request, 'register_attempt')
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

            track_event(request, 'register_success', username=username, email=email)

            if 'next' in request.GET:
                next = request.GET['next']
            else:
                next = reverse('index')
            return redirect(next)

    else:
        track_event(request, 'register_page_visitted')
        form = RegistrationForm()
    return TemplateResponse(request, 'registration/register.html',
        {'form': form}
    )
