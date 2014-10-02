from django.apps import apps, AppConfig


class NavTreeConfig(AppConfig):
    name = 'conman.nav_tree'

    def ready(self):
        apps.get_app_config('cms').manage_app(self)
