# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landlord', '0002_landlord_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='landlord',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='landlord',
            name='phone',
            field=models.CharField(default='default', max_length=12),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='landlord',
            name='note',
            field=models.TextField(null=True, blank=True),
        ),
    ]
