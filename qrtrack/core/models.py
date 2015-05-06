from django.db import models
from django.contrib.auth.models import User


class UserWantsBeta(models.Model):
    user = models.OneToOneField(User, null=False, blank=False)
    wants_beta = models.BooleanField(null=False, blank=False, default=False)