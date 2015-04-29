from django.db import models
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from qrtrack.core.utils import get_hashid
from qrtrack.core.validators import RatingValidator


class QRTagManager(models.Manager):
    """Custom manager that allows getting QRTags by it's hashid"""
    def by_hashid(self, hashid):
        return self.get(pk=get_hashid().decode(hashid))

    def by_hashid_or_404(self, hashid):
        return get_object_or_404(self, pk=get_hashid().decode(hashid))


class QRCollection(models.Model):
    """A category for tags, in the future it might be curated"""
    name = models.CharField(max_length=300, null=False, blank=False, unique=True)
    description = models.TextField()


class QRCollectionType(models.Model):
    name = models.CharField(max_length=300, null=False, blank=False, unique=True)


class QRTag(models.Model):
    collection = models.ForeignKey(QRCollection, null=False, blank=False, on_delete=models.PROTECT)
    name = models.CharField(max_length=300, null=False, blank=False, unique=True)
    description = models.TextField()

    objects = QRTagManager()

    @property
    def hashid(self):
        return get_hashid().encode(self.pk)


class CompletedTags(models.Model):
    tag = models.ForeignKey(QRTag, null=False, blank=False)
    user = models.ForeignKey(User, null=False, blank=False)
    rating = models.IntegerField(null=True, blank=True, validators=[RatingValidator])

    class Meta:
        unique_together = ('tag', 'user')