from django.conf.urls import url

from . import views


urlpatterns = [url(r'^$', views.simple_route_view)]
