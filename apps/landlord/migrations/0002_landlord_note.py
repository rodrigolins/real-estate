# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landlord', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='landlord',
            name='note',
            field=models.TextField(default='Default note'),
            preserve_default=False,
        ),
    ]
