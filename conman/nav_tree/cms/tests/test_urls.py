from incuna_test_utils.testcases.urls import URLTestCase

from .. import views


class TestNodeIndexURL(URLTestCase):
    """Make sure that the Node Index view has a URL."""
    def test_url(self):
        self.assert_url_matches_view(
            views.Index,
            '/cms/nav_tree/',
            'cms:nav_tree:index',
        )


class TestNodeDetailURL(URLTestCase):
    """Make sure that the NodeUpdate view has a URL."""
    def test_url(self):
        self.assert_url_matches_view(
            views.NodeUpdate,
            '/cms/nav_tree/42/',
            'cms:nav_tree:node-update',
            url_kwargs={'pk': 42},
        )
