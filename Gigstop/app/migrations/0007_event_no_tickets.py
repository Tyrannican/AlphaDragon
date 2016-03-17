# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_event_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='no_tickets',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
