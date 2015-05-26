from __future__ import absolute_import  # Normally a good idea. It always will import the top level element
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
# from django.utils.translation import ugettext_lazy as _

from .models import Contract

from apps.property.models import Property
from apps.tenant.models import Tenant


class ContractDetailView(DetailView):
    model = Contract
    template_name = 'contract_detail.html'


class ContractListView(ListView):
    model = Contract
    template_name = 'contract_list.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        return Contract.objects.all()


# A property cannot be rented for more than one person.
# When create a new contract, change the property status to occupied.
class ContractCreateView(CreateView):
    model = Contract
    template_name = 'contract_create.html'

    fields = '__all__'

    def get_initial(self):
        try:
            property = Property.objects.get(pk=self.kwargs.get('property_id'))
        except ObjectDoesNotExist:
            property = None

        try:
            tenant = Tenant.objects.get(pk=self.kwargs.get('tenant_id'))
        except ObjectDoesNotExist:
            tenant = None

        return {
            'property': property,
            'tenant': tenant
        }

    def get_success_url(self):
        return reverse_lazy('contract:list')


class ContractDeleteView(DeleteView):
    model = Contract
    success_url = reverse_lazy('contract:list')
    template_name = 'contract_delete.html'


class ContractUpdateView(UpdateView):
    model = Contract
    template_name = 'contract_update.html'
    success_url = reverse_lazy('contract:list')

    fields = '__all__'

    def get_success_url(self):
        return reverse("contract:detail", kwargs={"pk": self.object.pk})
