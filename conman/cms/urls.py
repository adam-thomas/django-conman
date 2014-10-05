from django.apps import apps
from django.conf.urls import include, url

from . import views


def _app_url(app):
    return url(r'^{}/'.format(app.label), include(app.cms_urls))


def _build_urls(managed_apps):
    return list(map(_app_url, managed_apps))

_managed_apps = apps.get_app_config('cms').managed_apps
_cms_urls = _build_urls(_managed_apps)

urlpatterns = [
    url(
        '',
        include(
            [
                url(r'^$', views.CMSIndex.as_view(), name='index'),
            ] + _cms_urls,
            namespace='cms',
        )
    ),
]
