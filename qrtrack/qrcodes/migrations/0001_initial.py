# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings
import qrtrack.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CompletedTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating', models.IntegerField(blank=True, null=True, validators=[qrtrack.core.validators.RatingValidator])),
            ],
        ),
        migrations.CreateModel(
            name='QRCollection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=300)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='QRTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=300)),
                ('description', models.TextField()),
                ('collection', models.ForeignKey(to='qrcodes.QRCollection', on_delete=django.db.models.deletion.PROTECT)),
            ],
        ),
        migrations.AddField(
            model_name='completedtag',
            name='tag',
            field=models.ForeignKey(to='qrcodes.QRTag'),
        ),
        migrations.AddField(
            model_name='completedtag',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='completedtag',
            unique_together=set([('tag', 'user')]),
        ),
    ]
