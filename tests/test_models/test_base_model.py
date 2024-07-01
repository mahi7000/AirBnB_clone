#!/usr/bin/python3
"""Unittest for class BaseModel"""

from models.base_model import BaseModel
import unittest
from datetime import datetime, timedelta


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.model = BaseModel()

    def test_attributes(self):
        self.assertTrue(hasattr(self.model, 'id'))
        self.assertTrue(hasattr(self.model, 'created_at'))
        self.assertTrue(hasattr(self.model, 'updated_at'))

    def test_id_generation(self):
        self.assertIsInstance(self.model.id, str)

    def test_created_at(self):
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at_initial(self):
        self.assertIsInstance(self.model.updated_at, datetime)
        self.assertEqual(self.model.created_at, self.model.updated_at)

    def test_updated_at_save(self):
        initial = self.model.updated_at
        self.model.save()
        self.assertNotEqual(initial, self.model.updated_at)

    def test_to_dict(self):
        obj_dict = self.model.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict['id'], self.model.id)

        created_at = datetime.strptime(
                obj_dict['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
        updated_at = datetime.strptime(
                obj_dict['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')

        self.assertEqual(created_at, self.model.created_at)
        self.assertEqual(updated_at, self.model.updated_at)

    def test_str(self):
        m = BaseModel()
        m.id = "123"
        m.created_at = "2022-01-01 12:00:00"
        m.updated_at = "2022-01-02 12:00:00"

        result = str(m)
        expected = "[BaseModel] (123) {'id': '123', \
'created_at': '2022-01-01 12:00:00', 'updated_at': '2022-01-02 12:00:00'}"
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
