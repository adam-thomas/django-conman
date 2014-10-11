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
