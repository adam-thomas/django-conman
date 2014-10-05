from django.apps import AppConfig, apps
from django.core.urlresolvers import reverse


class NavTreeConfig(AppConfig):
    name = 'conman.nav_tree'
    cms_urls = 'conman.nav_tree.cms.urls'

    def ready(self):
        apps.get_app_config('cms').manage_app(self)

    def get_cms_url(self):
        return reverse('cms:nav-tree-index')
