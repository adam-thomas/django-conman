from unittest import mock

from django.apps import apps
from django.test import TestCase


class TestAppRegistration(TestCase):
    def setUp(self):
        self.tree_app = apps.get_app_config('nav_tree')

    def test_app_registered(self):
        """
        Has this app been registered with the CMS app?

        This should be the case because it is in INSTALLED_APPS in the tests.
        """
        cms_app = apps.get_app_config('cms')
        self.assertIn(self.tree_app, cms_app.managed_apps)

    def test_app_ready(self):
        """Does the `ready` method act as expected?"""
        with mock.patch('conman.cms.apps.CMSConfig.manage_app') as manage_app:
            self.tree_app.ready()

        manage_app.assert_called_with(self.tree_app)
