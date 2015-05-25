from django.conf.urls import patterns, url

from . import views as v

urlpatterns = patterns(
    '',
    url(r'^(?P<pk>\d+)/$', v.PropertyDetailView.as_view(), name='detail'),
    url(r'^$', v.PropertyListView.as_view(), name='list'),
    url(r'^create/$', v.PropertyCreateView.as_view(), name='create'),
    url(r'^create/(?P<landlord_id>\d+)$', v.PropertyCreateView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/delete/$', v.PropertyDeleteView.as_view(), name='delete'),
    url(r'^(?P<pk>\d+)/update/$', v.PropertyUpdateView.as_view(), name='update'),
)
