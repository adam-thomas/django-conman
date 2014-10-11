from django.core.urlresolvers import reverse
from django.test import TestCase

from conman.tests.utils import TEST_SERVER
from .. import views
from ...tests.factories import ChildNodeFactory


class TestIndex(TestCase):
    view_class = views.Index

    def test_get_queryset(self):
        """Instances of Node should be in the queryset of the Index."""
        node = ChildNodeFactory.create()

        qs = self.view_class().get_queryset()

        self.assertCountEqual(qs, [node, node.parent])


class TestIndexIntegration(TestCase):
    view_class = views.Index
    url = reverse('cms:nav_tree:index')

    def test_status(self):
        """Index should return a 200."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_template(self):
        """Index should use the correct template."""
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'nav_tree/cms/node_list.html')


class TestNodeUpdate(TestCase):
    view_class = views.NodeUpdate

    def setUp(self):
        self.node = ChildNodeFactory.create()
        self.url = reverse(
            'cms:nav_tree:node-update',
            kwargs={'pk': self.node.pk},
        )

    def test_get_success_url(self):
        view = self.view_class()
        view.object = self.node

        url = view.get_success_url()

        self.assertEqual(url, self.url)

    def test_get(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'nav_tree/cms/node_form.html')

    def test_post(self):
        data = {
            'slug': 'new-leaf',
            'parent': self.node.parent_id,
        }
        response = self.client.post(self.url, data=data)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], TEST_SERVER + self.url)
