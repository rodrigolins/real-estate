# -*- coding: utf-8 -*-
from django.db import models
from django.forms import ModelForm


class Tenant(models.Model):
    name = models.CharField(max_length=255, help_text='Name')
    phone = models.CharField(max_length=12)
    email = models.EmailField(null=True)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return("%s" % (self.name))


class TenantForm(ModelForm):
    class Meta:
        model = Tenant
        fields = '__all__'
