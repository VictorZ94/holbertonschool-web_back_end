#!/usr/bin/env python3
"""test utils module"""

import unittest
from unittest import mock
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """class to test access
    nested map method"""

    @parameterized.expand([
        ({"a": 1}, ("a",), (1)),
        ({"a": {"b": 2}}, ("a",), {'b': 2},),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """test access nested map method"""
        self.assertEqual(access_nested_map(nested_map, path), expected)
