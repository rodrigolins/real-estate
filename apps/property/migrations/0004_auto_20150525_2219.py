# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_auto_20150525_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='note',
            field=models.TextField(null=True, blank=True),
        ),
    ]
