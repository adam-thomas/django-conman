from django.conf.urls import url


def dummy_view():
    """A stub view that is always mocked."""


view_path = 'conman.routes.tests.urls.dummy_view'


urlpatterns = [
    url(r'^$', view_path),
    url(r'^(?P<slug>[a-zA-Z0-9_-]+)/$', view_path),
]
