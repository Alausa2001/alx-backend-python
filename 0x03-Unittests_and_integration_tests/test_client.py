#!/usr/bin/env python3
"""
contain tests for class/methods in client.py
"""
import unittest
from unittest.mock import MagicMock, patch, PropertyMock
from parameterized import parameterized
# from utils import get_json, access_nested_map, memoize
from client import GithubOrgClient
import client


class TestGithubOrgClient(unittest.TestCase):
    """
    test class for client.py
    """

    @parameterized.expand([
        ('google'),
        ('abc')
        ])
    @patch('client.get_json')
    def test_org(self, org_name, get_json_mock):
        """
        tests the org method in client.GithubOrgClient
        """
        endpoint = 'https://api.github.com/orgs/{}'.format(org_name)
        test = GithubOrgClient(org_name)
        test.org()
        test.org()
        get_json_mock.assert_called_once_with(endpoint)

    # @patch('GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self):
        """
        test _public_repos_url method in client.GithubOrgClient
        """
        return_dict = {
                "url": "https://api.github.com/orgs/google",
                "repos_url": "https://api.github.com/orgs/google/repos"
                }
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock:
            test = GithubOrgClient('google')
            mock.return_value = return_dict
            _public_repos_url = test._public_repos_url
            repos_url = "https://api.github.com/orgs/google/repos"
            self.assertEqual(_public_repos_url, repos_url)
