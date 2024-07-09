#!/usr/bin/python3
"""Test reviews of places"""

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Test the class Review"""
    def setUp(self):
        r = Review()

    def testAttributes(self):
        self.assertEqual(r.place_id, "")
        self.assertEqual(r.user_id, "")
        self.assertEqual(r.text, "")
