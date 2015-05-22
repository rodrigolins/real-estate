# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Landlord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'Name', max_length=255)),
                ('street', models.CharField(help_text=b'Street', max_length=255)),
                ('number', models.CharField(help_text=b'Number', max_length=30)),
                ('neighborhood', models.CharField(help_text=b'Neighborhood', max_length=80)),
                ('state', models.CharField(help_text=b'State', max_length=2, choices=[(b'AC', b'Acre'), (b'AL', b'Alagoas'), (b'AP', b'Amap\xc3\xa1'), (b'AM', b'Amazonas'), (b'BA', b'Bahia'), (b'CE', b'Cear\xc3\xa1'), (b'DF', b'Distrito Federal'), (b'ES', b'Esp\xc3\xadrito Santo'), (b'GO', b'Goi\xc3\xa1s'), (b'MA', b'Maranh\xc3\xa3o'), (b'MT', b'Mato Grosso'), (b'MS', b'Mato Grosso do Sul'), (b'MG', b'Minas Gerais'), (b'PA', b'Par\xc3\xa1'), (b'PB', b'Para\xc3\xadba'), (b'PR', b'Paran\xc3\xa1'), (b'PE', b'Pernambuco'), (b'PI', b'Piau\xc3\xad'), (b'RJ', b'Rio de Janeiro'), (b'RN', b'Rio Grande do Norte'), (b'RS', b'Rio Grande do Sul'), (b'RO', b'Rond\xc3\xb4nia'), (b'RR', b'Roraima'), (b'SC', b'Santa Catarina'), (b'SP', b'S\xc3\xa3o Paulo'), (b'SE', b'Sergipe'), (b'TO', b'Tocantins')])),
                ('city', models.CharField(help_text=b'City', max_length=40)),
            ],
        ),
    ]
