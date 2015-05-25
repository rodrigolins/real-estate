from __future__ import absolute_import  # Normally a good idea. It always will import the top level element
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
# from django.utils.translation import ugettext_lazy as _

from .models import Landlord


class LandlordDetailView(DetailView):
    model = Landlord
    template_name = 'landlord_detail.html'


class LandlordListView(ListView):
    model = Landlord
    template_name = 'landlord_list.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        return Landlord.objects.all()


class LandlordCreateView(CreateView):
    model = Landlord
    template_name = 'landlord_create.html'

    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('landlord:list')


class LandlordDeleteView(DeleteView):
    model = Landlord
    success_url = reverse_lazy('landlord:list')
    template_name = 'landlord_delete.html'


class LandlordUpdateView(UpdateView):
    model = Landlord
    template_name = 'landlord_update.html'
    success_url = reverse_lazy('landlord:list')

    fields = '__all__'

    def get_success_url(self):
        return reverse("landlord:detail", kwargs={"pk": self.object.pk})
