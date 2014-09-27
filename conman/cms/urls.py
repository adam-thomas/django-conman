from django.conf.urls import include, url

from . import views


urlpatterns = [
    url(r'^$', views.CMSIndex.as_view(), name='cms-index'),
]
