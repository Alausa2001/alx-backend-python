#!/usr/bin/env python3
"""
contains tests for utils.py
"""
import unittest
from utils import access_nested_map
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
