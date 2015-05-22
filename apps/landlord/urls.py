from django.conf.urls import patterns, url

from . import views as v

urlpatterns = patterns(
    '',
    url(r'^(?P<pk>\d+)/$', v.LandlordDetailView.as_view(), name='detail'),
    url(r'^$', v.LandlordListView.as_view(), name='list'),
    url(r'^create/$', v.LandlordCreateView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/delete/$', v.LandlordDeleteView.as_view(), name='delete'),
    url(r'^(?P<pk>\d+)/update/$', v.LandlordUpdateView.as_view(), name='update'),
)
