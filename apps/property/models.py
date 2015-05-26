# -*- coding: utf-8 -*-
from django.db import models
from django.forms import ModelForm
from apps.core.utils import STATES
from decimal import Decimal

from apps.landlord.models import Landlord


# Create your models here.
# if a property is deleted we should remove it because the payment slips
# and accountancy.
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
    note = models.TextField(null=True, blank=True)
    landlord = models.ForeignKey(Landlord)
    rooms = models.IntegerField(null=True, blank=True)
    size = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2, default=Decimal('0.00'))

    def __str__(self):
        return("%s %s" % (self.address, self.number))


class PropertyForm(ModelForm):
    class Meta:
        model = Property
        fields = '__all__'
