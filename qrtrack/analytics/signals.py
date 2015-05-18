from django.dispatch import receiver
from qrtrack.analytics.utils import event_tracked

@receiver(event_tracked)
def echo_event(sender, event, **kwargs):
    print('Event ' + event.type.name + ' tracked at ' + str(event.occurred))
    for param in event.eventparameters_set.all():
        print('\t' + param.parameter + ' :: ' + param.value)
