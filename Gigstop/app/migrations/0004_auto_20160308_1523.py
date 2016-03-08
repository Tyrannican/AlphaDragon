# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0003_auto_20160308_1517'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='performer',
            name='user',
        ),
        migrations.AddField(
            model_name='performer',
            name='performer',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
