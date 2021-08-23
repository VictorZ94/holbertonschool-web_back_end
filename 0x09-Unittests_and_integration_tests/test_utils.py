#!/usr/bin/env python3
""" getting started write test using methoology TDD,
    it has 3 steps fail, pass, refactor
"""
import unittest
from unittest.mock import patch
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """ unit test is the first step in TDD
        it has 3 steps fail, pass, refactor
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ test a function using pattern parameterized
        """
        from utils import access_nested_map
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, expected):
        """ test assertion raises from exceptions
        """
        from utils import access_nested_map
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, expected)


class TestGetJson(unittest.TestCase):
    """ getting started working with mock testing
        mock some class or object is important to save resources
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """ mock testing to test http GET requests
        """
        from utils import get_json
        with patch("requests.get") as mock_get:
            mock_get.return_value.json.return_value = test_payload
            mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """ Test Memoize class
    Args:
        unittest ([type]): [description]
    """
    def test_memoize():
        """ test class memoization
        """
        from utils import memoize

        class TestClass:
            """ test class memoization
            """
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch("TestClass()") as mock:
            mock.a_method()
            mock.assert_called_once()
            mock.a_method()
            mock.assert_called_once()
