from django.core.urlresolvers import reverse
from django.test import TestCase

from .. import views
from ...tests.factories import ChildNodeFactory


class TestIndex(TestCase):
    view_class = views.Index

    def test_get_queryset(self):
        """Instances of Node should be in the queryset of the Index."""
        node = ChildNodeFactory.create()

        qs = self.view_class().get_queryset()

        self.assertCountEqual(qs, [node, node.parent])

    def test_integration(self):
        response = self.client.get(reverse('cms:nav-tree-index'))

        self.assertEqual(response.status_code, 200)
