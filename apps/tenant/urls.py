from django.conf.urls import patterns, url

from . import views as v

urlpatterns = patterns(
    '',
    url(r'^(?P<pk>\d+)/$', v.TenantDetailView.as_view(), name='detail'),
    url(r'^$', v.TenantListView.as_view(), name='list'),
    url(r'^create/$', v.TenantCreateView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/delete/$', v.TenantDeleteView.as_view(), name='delete'),
    url(r'^(?P<pk>\d+)/update/$', v.TenantUpdateView.as_view(), name='update'),
)
