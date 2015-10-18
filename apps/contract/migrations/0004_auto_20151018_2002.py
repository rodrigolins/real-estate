# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0003_auto_20150526_2004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contract',
            name='due_date',
        ),
        migrations.RemoveField(
            model_name='contract',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='contract',
            name='finished_date',
        ),
        migrations.RemoveField(
            model_name='contract',
            name='finished_reason',
        ),
        migrations.RemoveField(
            model_name='contract',
            name='property',
        ),
        migrations.RemoveField(
            model_name='contract',
            name='start_date',
        ),
        migrations.RemoveField(
            model_name='contract',
            name='status',
        ),
        migrations.RemoveField(
            model_name='contract',
            name='tenant',
        ),
    ]
