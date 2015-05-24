# -*- coding: utf-8 -*-
from django.db import models
from django.forms import ModelForm
from apps.core.utils import STATES
from decimal import Decimal


# Create your models here.
class Property(models.Model):
    code = models.CharField(max_length=12)
    address = models.CharField(max_length=255)
    number = models.CharField(max_length=20)
    zip_code = models.CharField(max_length=8)
    neighborhood = models.CharField(max_length=80)
    city = models.CharField(max_length=40)
    state = models.CharField(max_length=2, choices=STATES)
    status = models.CharField(max_length=2)
    rent = models.DecimalField(max_digits=8, decimal_places=2, default=Decimal('0.00'))
    note = models.TextField()


class PropertyForm(ModelForm):
    class Meta:
        model = Property
        fields = '__all__'
