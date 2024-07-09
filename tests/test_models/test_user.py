#!/usr/bin/python3
"""unittest user"""

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Test user"""
    def setUp(self):
        """Make a user object"""
        first = User()

    def test_email(self):
        self.assertEqual(first.email, "")

    def test_password(self):
        self.assertEqual(first.password, "")

    def test_first_name(self):
        self.assertEqual(first.first_name, "")

    def test_last_name(self):
        self.assertEqual(first.last_name, "")
