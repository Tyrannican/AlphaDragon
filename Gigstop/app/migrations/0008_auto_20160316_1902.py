# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0007_event_no_tickets'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='sold',
        ),
        migrations.AddField(
            model_name='event',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ticket',
            name='quantity',
            field=models.IntegerField(default=1, max_length=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ticket',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='venue',
            name='name',
            field=models.CharField(max_length=128),
        ),
    ]
