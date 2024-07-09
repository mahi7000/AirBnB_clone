#!/usr/bin/python3
"""Unittest for class BaseModel"""

from models.base_model import BaseModel
import unittest
from datetime import datetime, timedelta


class TestBaseModel(unittest.TestCase):
    def test_id_creation(self):
        """Test that a unique ID is created for each instance"""
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model1.id, model2.id)

    def test_to_dict(self):
        """Test the to_dict() method"""
        model = BaseModel()
        model_dict = model.to_dict()

        self.assertIsInstance(model_dict, dict)
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')


if __name__ == '__main__':
    unittest.main()
