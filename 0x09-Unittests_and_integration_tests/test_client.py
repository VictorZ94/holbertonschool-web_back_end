#!/usr/bin/env python3
""" Parameterize and patch as decorators
    his method should test that GithubOrgClient.org
    returns the correct value.
"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """ Test a resources without external called

    Args:
        unittest ([type]): [description]
    """
    @parameterized.expand([
        ('google'),
        ('abc'),
    ])
    @patch('requests.get')
    def test_org(self, param, mock_get):
        """ mock request HTTP without external called

        Args:
            param ([type]): [description]
            mock_get ([type]): [description]
        """
        json_test = {
            'type': 'OK'
        }
        mock_get.return_value.json.return_value = json_test
        response = GithubOrgClient(param)
        response.org
        mock_get.assert_called_once()
