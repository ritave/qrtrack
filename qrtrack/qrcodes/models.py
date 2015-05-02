from django.db import models
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from qrtrack.core.utils import get_collect_hashid, get_show_hashid
from qrtrack.core.validators import RatingValidator


class QRTagManager(models.Manager):
    """Custom manager that allows getting QRTags by it's hashid"""
    def by_collect_hashid(self, hashid):
        return self._by_some_hashid(hashid, get_collect_hashid)

    def by_collect_hashid_or_404(self, hashid):
        return self._by_some_hashid_or_404(hashid, get_collect_hashid)

    def by_show_hashid(self, hashid):
        return self._by_some_hashid(hashid, get_show_hashid)

    def by_show_hashid_or_404(self, hashid):
        return self._by_some_hashid_or_404(hashid, get_show_hashid)

    # PRIVATES

    def _by_some_hashid(self, hashid, factory):
        qrcode = factory().decode(hashid)
        if qrcode is not None and len(qrcode) == 1:
            return self.get(pk=qrcode[0])
        return None

    def _by_some_hashid_or_404(self, hashid, factory):
        qrcode = factory().decode(hashid)
        if qrcode is not None and len(qrcode) == 1:
            return get_object_or_404(self, pk=qrcode[0])
        raise Http404


class QRCollection(models.Model):
    """A category for tags, in the future it might be curated"""
    name = models.CharField(max_length=300, null=False, blank=False, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class QRTag(models.Model):
    collection = models.ForeignKey(QRCollection, null=False, blank=False, on_delete=models.PROTECT)
    name = models.CharField(max_length=300, null=False, blank=False, unique=True)
    description = models.TextField()

    objects = QRTagManager()

    def __str__(self):
        return self.name + ' (collect: ' + self.collect_hashid + ' / show: ' + self.show_hashid + ')'

    @property
    def collect_hashid(self):
        return get_collect_hashid().encode(self.pk)

    @property
    def show_hashid(self):
        return get_show_hashid().encode(self.pk)


class CompletedTag(models.Model):
    tag = models.ForeignKey(QRTag, null=False, blank=False)
    user = models.ForeignKey(User, null=False, blank=False)
    rating = models.IntegerField(null=True, blank=True, validators=[RatingValidator])

    def __str__(self):
        return self.tag.name + ' : ' + self.user.username

    class Meta:
        unique_together = ('tag', 'user')
