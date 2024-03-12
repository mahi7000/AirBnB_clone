import unittest
from datetime import datetime

from models.base_model import BaseModel


class TestBaseModel(unnittest.TestCase):
    """ This tests Base Model class """
    bm = BaseModel()
    def test_id_is_string(self):
        """ tests if the id is a string """
        self.assertIsInstance(bm.id, str)

    def test_created_at_is_datetime(self):
        """ tests if created at is a date """
        self.assertIsInstance(bm.created_at, datetime)

    def test_to_dict(self):
        """ test to_dict method """
        expected_dict = {
            'id': bm.id,
            'created_at': bm.created_at.isoformat(),
            'updated_at': bm.updated_at.isoformat(),
            '__class__': 'BaseModel'
        }
        self.assertDictEqual(self.base_model.to_dict(), expected_dict)

    def test_str(self):
        """ __str__ checker """
        expected_str = f"[BaseModel] ({bm.id}) {bm.__dict__}"
        self.assertEqual(str(bm), expected_str)


if __name__ == '__main__':
    unittest.main()
