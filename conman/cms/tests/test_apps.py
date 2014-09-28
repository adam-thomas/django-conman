from unittest import mock

from django.test import TestCase
from django.apps import apps


class CMSAppRegistrationTest(TestCase):
    """Test the app registration process"""
    def setUp(self):
        # Get the AppConfig for this app (by label).
        self.config = apps.get_app_config('cms')
        # Copy original value so test does not taint the global state.
        self._original_registry = self.config._registry

    def tearDown(self):
        # Restore original value to its rightful place.
        self.config._registry = self._original_registry

    def test_apps_can_register(self):
        mock_app = mock.Mock()

        self.config.register(mock_app)

        self.assertIn(mock_app, self.config._registry)
