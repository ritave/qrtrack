from django.db import transaction
from django.dispatch import Signal, receiver
from qrtrack.analytics.models import Event, EventParameters, EventType

event_tracked = Signal(providing_args=['sender', 'event'])


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
    if request.session.session_key:
        return 'ANON:' + request.session.session_key
    # No qrcodes collected, we haven't set anything in the session cookie
    return 'NONE'


def _add_param(event, param, value):
    new_param = EventParameters(event_occurrence=event, parameter=param, value=value)
    new_param.save()


def log_to_file(file):
    """Prints ALL analytic events to file"""
    with open(file, 'w+') as f:
        for event in Event.objects.order_by('occurred').all():
            f.write('[' + str(event.occurred) + '] ' + event.type.name + '\n')
            for param in event.eventparameters_set.all():
                f.write('\t' + param.parameter + ' :: ' + param.value + '\n')
