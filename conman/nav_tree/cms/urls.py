from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.NodeUpdate.as_view(), name='node-update'),
]
