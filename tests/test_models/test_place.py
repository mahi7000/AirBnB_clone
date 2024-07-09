#!/usr/bin/python3
"""Test Place"""

import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test the class Place"""
    def setUp(self):
        p = Place()

    def TestId(self):
        self.assertEqual(p.city_id, "")
        self.assertEqual(p.user_id, "")
    
    def TestNameDescription(self):
        self.assertEqual(p.name, "")
        self.assertEqual(p.description, "")

    def TestNumber(self):
        self.assertEqual(p.number_rooms, 0)
        self.assertEqual(p.number_bathrooms, 0)
        self.assertEqual(p.max_guest, 0)
        self.assertEqual(p.price_by_night, 0)

    def TestLatitudeLongitude(self):
        self.assertEqual(p.latitude, 0.0)
        self.assertEqual(p.longitude, 0.0)

    def TestAmenityIds(self):
        self.assertEqual(p.amenity_ids, [])
