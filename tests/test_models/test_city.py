#!/usr/bin/python3
"""unittest City"""

import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """class to Test City"""
    def setUp(self):
        c = City()

    def testStateId(self):
        self.assertEqual(c.state_id, "")

    def testName(self):
        self.assertEqual(c.name, "")
