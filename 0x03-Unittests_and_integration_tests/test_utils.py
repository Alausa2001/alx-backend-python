#!/usr/bin/env python3
"""
contains tests for utils.py
"""
import utils
import unittest
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """
    test class for access_nested_map in utils.py
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self, paramA, paramB, out):
        """tests the function in utils.py"""
        self.assertEqual(access_nested_map(paramA, paramB), out)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
        ])
    def test_access_nested_map_exception(self, paramA, paramB):
        """test for if an exception is raised"""
        with self.assertRaises(KeyError):
            access_nested_map(paramA, paramB)


class TestGetJson(unittest.TestCase):
    """
    test class of get_json in utils.py
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
        ])
    def test_get_json(self, url, expected):
        """
        tests external http calls
        """

        with patch('utils.requests') as mock_requests:
            response = Mock()
            mock_requests.get.return_value = response
            response.json.return_value = expected
            self.assertEqual(get_json(url), response.json.return_value)
