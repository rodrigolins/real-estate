from django.conf.urls import patterns, url

from . import views as v

urlpatterns = patterns(
    '',
    url(r'^$', v.Index.as_view(), name='index'),
)
