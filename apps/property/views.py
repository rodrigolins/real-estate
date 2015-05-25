from __future__ import absolute_import  # Normally a good idea. It always will import the top level element
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist

from .models import Property


class PropertyDetailView(DetailView):
    model = Property
    template_name = 'property_detail.html'


class PropertyListView(ListView):
    model = Property
    template_name = 'property_list.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        return Property.objects.all()


class PropertyCreateView(CreateView):
    model = Property
    template_name = 'property_create.html'

    fields = '__all__'

    def get_initial(self):
        try:
            landlord = Property.objects.get(pk=self.kwargs.get('landlord_id'))
        except ObjectDoesNotExist:
            landlord = None

        return {
            'landlord': landlord,
        }

    def get_success_url(self):
        return reverse_lazy('property:list')


class PropertyDeleteView(DeleteView):
    model = Property
    success_url = reverse_lazy('property:list')
    template_name = 'property_delete.html'


class PropertyUpdateView(UpdateView):
    model = Property
    template_name = 'property_update.html'
    success_url = reverse_lazy('property:list')

    fields = '__all__'

    def get_success_url(self):
        return reverse("property:detail", kwargs={"pk": self.object.pk})
