from django.db import models
from django.forms import ModelForm

from apps.property.models import Property
from apps.tenant.models import Tenant


# Create your models here.
class Contract(models.Model):
    STATUS = (
        ('EN', 'Ended'),
        ('OP', 'Operative'),
        ('CN', 'Canceled'),
    )


    def __str__(self):
        return("%s %s" % (self.tenant.name, self.property.address))


class ContractForm(ModelForm):
    class Meta:
        model = Contract
        fields = '__all__'
