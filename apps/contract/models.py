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
    property = models.ForeignKey(Property)
    tenant = models.ForeignKey(Tenant)
    duration = models.IntegerField(help_text='In months')
    start_date = models.DateField()  # when contract start
    finished_date = models.DateField(blank=True, null=True)  # when contract actually ended
    status = models.CharField(max_length=2, choices=STATUS)
    finished_reason = models.TextField(blank=True, null=True)
    due_date = models.IntegerField()

    def __str__(self):
        return("%s %s" % (self.tenant.name, self.property.address))


class ContractForm(ModelForm):
    class Meta:
        model = Contract
        fields = '__all__'
