# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20160308_1523'),
    ]

    operations = [
        migrations.AddField(
            model_name='performer',
            name='bandname',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
    ]
