# -*- coding: utf-8 -*-
from django.db import models
from django.forms import ModelForm
from apps.core.utils import STATES


class Landlord(models.Model):
    name = models.CharField(max_length=255, help_text='Name')
    street = models.CharField(max_length=255, help_text='Street')
    number = models.CharField(max_length=30, help_text='Number')
    neighborhood = models.CharField(max_length=80, help_text='Neighborhood')
    state = models.CharField(max_length=2, help_text='State', choices=STATES)
    city = models.CharField(max_length=40, help_text='City')
    phone = models.CharField(max_length=12)
    email = models.EmailField(null=True)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return("%s" % (self.name))


class LandlordForm(ModelForm):
    class Meta:
        model = Landlord
        fields = '__all__'
