#!/usr/bin/python3
"""unittest user"""

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Test user"""
    def setUp(self):
        """Make a user object"""
        self.first = User()

    def test_email(self):
        self.assertEqual(self.first.email, "")

    def test_password(self):
        self.assertEqual(self.first.password, "")

    def test_first_name(self):
        self.assertEqual(self.first.first_name, "")

    def test_last_name(self):
        self.assertEqual(self.first.last_name, "")
