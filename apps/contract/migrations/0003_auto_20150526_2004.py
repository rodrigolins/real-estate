# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0002_auto_20150526_1850'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='due_date',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contract',
            name='finished_reason',
            field=models.TextField(null=True, blank=True),
        ),
    ]
