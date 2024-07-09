#!/usr/bin/python3
"""Test reviews of places"""

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Test the class Review"""
    def setUp(self):
        self.r = Review()

    def testAttributes(self):
        self.assertEqual(self.r.place_id, "")
        self.assertEqual(self.r.user_id, "")
        self.assertEqual(self.r.text, "")
