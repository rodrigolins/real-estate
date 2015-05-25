# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landlord', '0003_auto_20150525_1542'),
        ('property', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='landlord',
            field=models.ForeignKey(default='1', to='landlord.Landlord'),
            preserve_default=False,
        ),
    ]
