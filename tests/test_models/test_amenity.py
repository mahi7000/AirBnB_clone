#!/usr/bin/python3
""" Test amentiies"""

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test Amenities"""
    def setUp(self):
        self.a = Amenity()

    def testName(self):
        self.assertEqual(self.a.name, "")
