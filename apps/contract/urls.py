from django.conf.urls import patterns, url

from . import views as v

urlpatterns = patterns(
    '',
    url(r'^(?P<pk>\d+)/$', v.ContractDetailView.as_view(), name='detail'),
    url(r'^$', v.ContractListView.as_view(), name='list'),
    url(r'^create/$', v.ContractCreateView.as_view(), name='create'),
    url(r'^create/(?P<property_id>\d+)/(?P<tenant_id>\d+)$', v.ContractCreateView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/delete/$', v.ContractDeleteView.as_view(), name='delete'),
    url(r'^(?P<pk>\d+)/update/$', v.ContractUpdateView.as_view(), name='update'),
)
