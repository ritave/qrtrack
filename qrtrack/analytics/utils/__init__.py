from django.db import transaction
import django.dispatch
from qrtrack.analytics.models import Event, EventParameters, EventType

event_tracked = django.dispatch.Signal(providing_args=['event'])

@transaction.atomic()
def track_event(request, name, **kwargs):
    event_type, _ = EventType.objects.get_or_create(name=name)

    event = Event(type=event_type)
    event.save()

    _add_param(event, 'user', _user_to_event_param(request))

    for param, value in kwargs.items():
        _add_param(event, param, value)

    event_tracked.send(track_event, event=event)

def _user_to_event_param(request):
    if request.user.is_authenticated():
        return 'AUTH:' + request.user.username
    return 'ANON:' + request.session.session_key

def _add_param(event, param, value):
    new_param = EventParameters(event_occurrence=event, paramater=param, value=value)
    new_param.save()
