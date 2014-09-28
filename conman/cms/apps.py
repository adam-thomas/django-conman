from django.apps import AppConfig


class CMSConfig(AppConfig):
    name = 'conman.cms'

    def __init__(self, *args, **kwargs):
        self._registry = set()
        return super().__init__(*args, **kwargs)

    def register(self, app):
        self._registry.add(app)
