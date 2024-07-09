#!/usr/bin/python3
"""Test Place"""

import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test the class Place"""
    def setUp(self):
        self.p = Place()

    def testId(self):
        self.assertEqual(self.p.city_id, "")
        self.assertEqual(self.p.user_id, "")
    
    def testNameDescription(self):
        self.assertEqual(self.p.name, "")
        self.assertEqual(self.p.description, "")

    def testNumber(self):
        self.assertEqual(self.p.number_rooms, 0)
        self.assertEqual(self.p.number_bathrooms, 0)
        self.assertEqual(self.p.max_guest, 0)
        self.assertEqual(self.p.price_by_night, 0)

    def testLatitudeLongitude(self):
        self.assertEqual(self.p.latitude, 0.0)
        self.assertEqual(self.p.longitude, 0.0)

    def testAmenityIds(self):
        self.assertEqual(self.p.amenity_ids, [])
