from __future__ import absolute_import  # Normally a good idea. It always will import the top level element
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
# from django.utils.translation import ugettext_lazy as _

from .models import Tenant


class TenantDetailView(DetailView):
    model = Tenant
    template_name = 'tenant_detail.html'


class TenantListView(ListView):
    model = Tenant
    template_name = 'tenant_list.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        return Tenant.objects.all()


class TenantCreateView(CreateView):
    model = Tenant
    template_name = 'tenant_create.html'

    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('tenant:list')


class TenantDeleteView(DeleteView):
    model = Tenant
    success_url = reverse_lazy('tenant:list')
    template_name = 'tenant_delete.html'


class TenantUpdateView(UpdateView):
    model = Tenant
    template_name = 'tenant_update.html'
    success_url = reverse_lazy('tenant:list')

    fields = '__all__'

    def get_success_url(self):
        return reverse("tenant:detail", kwargs={"pk": self.object.pk})
