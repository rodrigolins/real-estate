# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tenant', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contract',
            name='property',
        ),
        migrations.RemoveField(
            model_name='contract',
            name='tenant',
        ),
        migrations.DeleteModel(
            name='Contract',
        ),
    ]
