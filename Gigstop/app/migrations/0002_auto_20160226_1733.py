# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='performer',
            field=models.ForeignKey(default=1, to='app.Performer'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='performer',
            name='genre',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.DateTimeField(),
        ),
    ]
