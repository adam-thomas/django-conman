from django.test import TestCase

from .. import utils


class TestSplitPath(TestCase):
    """Test the split_path util function."""
    def test_split_path(self):
        """split_path returns a list of all sub-paths of a url path."""
        paths = utils.split_path('/a/path/with/many/parts/')
        expected = [
            '/',
            '/a/',
            '/a/path/',
            '/a/path/with/',
            '/a/path/with/many/',
            '/a/path/with/many/parts/',
        ]
        self.assertCountEqual(paths, expected)  # Order does not matter

    def test_split_empty_path(self):
        """An empty path has sub-path '/'."""
        paths = utils.split_path('')
        expected = ['/']
        self.assertCountEqual(paths, expected)

    def test_split_root_path(self):
        """The root path '/' has sub-path '/'."""
        paths = utils.split_path('/')
        expected = ['/']
        self.assertCountEqual(paths, expected)

    def test_split_path_with_dots(self):
        """split_path does no special processing on a path containing dots."""
        paths = utils.split_path('/path/../')
        expected = [
            '/',
            '/path/',
            '/path/../',
        ]
        self.assertCountEqual(paths, expected)


class TestImportFromDottedPath(TestCase):
    """Test the import_from_dotted_path util function."""
    def assert_error_message(self, exception):
        """Check the exception's message is correct."""
        message = 'An import path with two or more components is required.'
        self.assertEqual(exception.args[0], message)

    def test_empty(self):
        """An empty path cannot be imported."""
        with self.assertRaises(ValueError) as cm:
            utils.import_from_dotted_path('')
        self.assert_error_message(cm.exception)

    def test_too_short(self):
        """A path with only one component cannot be imported."""
        with self.assertRaises(ValueError) as cm:
            utils.import_from_dotted_path('antigravity')
        self.assert_error_message(cm.exception)

    def test_import_module(self):
        """A module can be imported by dotted path."""
        result = utils.import_from_dotted_path('conman.routes.utils')
        self.assertEqual(result, utils)

    def test_import_class(self):
        """A class can be imported by dotted path."""
        this_test = 'conman.routes.tests.test_utils.TestImportFromDottedPath'
        result = utils.import_from_dotted_path(this_test)
        self.assertEqual(result, self.__class__)
