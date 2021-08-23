#!/usr/bin/env python3
""" getting started write test using methoology TDD,
it has 3 steps fail, pass, refactor"""
import unittest
from unittest import mock
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """ unit test is the first step in TDD
    it has 3 steps fail, pass, refactor"""

    @parameterized.expand([
        ({"a": 1}, ("a",), (1)),
        ({"a": {"b": 2}}, ("a",), {'b': 2},),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """test a function using pattern parameterized"""
        self.assertEqual(access_nested_map(nested_map, path), expected)
