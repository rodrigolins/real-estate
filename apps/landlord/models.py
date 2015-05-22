# -*- coding: utf-8 -*-
from django.db import models
from django.forms import ModelForm


# Create your models here.
class Landlord(models.Model):
    STATES = (
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins'),
    )
    name = models.CharField(max_length=255, help_text='Name')
    street = models.CharField(max_length=255, help_text='Street')
    number = models.CharField(max_length=30, help_text='Number')
    neighborhood = models.CharField(max_length=80, help_text='Neighborhood')
    state = models.CharField(max_length=2, help_text='State', choices=STATES)
    city = models.CharField(max_length=40, help_text='City')


class LandlordForm(ModelForm):
    class Meta:
        model = Landlord
        fields = '__all__'
