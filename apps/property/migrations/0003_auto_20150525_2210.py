# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from decimal import Decimal


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0002_property_landlord'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='rooms',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='property',
            name='size',
            field=models.DecimalField(default=Decimal('0.00'), null=True, max_digits=6, decimal_places=2, blank=True),
        ),
    ]
