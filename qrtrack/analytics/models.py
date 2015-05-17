from django.db import models


class EventType(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, unique=True)


class Event(models.Model):
    type = models.ForeignKey(EventType)
    occurred = models.DateTimeField(null=False, blank=False, auto_now_add=True)


class EventParameters(models.Model):
    event_occurrence = models.ForeignKey(Event)
    parameter = models.CharField(max_length=100, null=False, blank=False)
    value = models.TextField()

    class Meta:
        unique_together = ('event_occurrence', 'parameter')
