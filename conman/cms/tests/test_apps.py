from unittest import mock

from django.apps import apps
from django.test import TestCase


class CMSAppRegistrationTest(TestCase):
    """Test the app registration process"""
    def setUp(self):
        # Get the AppConfig for this app (by label).
        self.config = apps.get_app_config('cms')
        # Copy original value so test does not taint the global state.
        self._original_registry = self.config.managed_apps

    def tearDown(self):
        # Restore original value to its rightful place.
        self.config._managed_apps = self._original_registry

    def test_apps_can_register(self):
        mock_app = mock.Mock()

        self.config.manage_app(mock_app)

        self.assertIn(mock_app, self.config._managed_apps)
