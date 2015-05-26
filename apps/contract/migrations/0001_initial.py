# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0004_auto_20150525_2219'),
        ('tenant', '0002_auto_20150526_1841'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('duration', models.IntegerField(help_text=b'In months')),
                ('start_date', models.DateField()),
                ('finished_date', models.DateField()),
                ('status', models.CharField(max_length=2, choices=[(b'EN', b'Ended'), (b'OP', b'Operative'), (b'CN', b'Canceled')])),
                ('property', models.ForeignKey(to='property.Property')),
                ('tenant', models.ForeignKey(to='tenant.Tenant')),
            ],
        ),
    ]
