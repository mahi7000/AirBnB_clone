#!/usr/bin/python3
""" Test amentiies"""

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test Amenities"""
    def setUp(self):
        a = Amenity()

    def testName(self):
        self.assertEqual(a.name, "")
