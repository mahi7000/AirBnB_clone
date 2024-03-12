import unittest
from datetime import datetime

from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ This tests Base Model class """
    def SetUp(self):
        """ make an instance of BaseModel """
        self.base_model = BaseModel()

    def test_id_is_string(self):
        """ tests if the id is a string """
        self.assertIsInstance(self.base_model.id, str)

    def test_created_at_is_datetime(self):
        """ tests if created at is a date """
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_to_dict(self):
        """ test to_dict method """
        expected_dict = {
            'id': self.base_model.id,
            'created_at': self.base_model.created_at.isoformat(),
            'updated_at': self.base_model.updated_at.isoformat(),
            '__class__': 'BaseModel'
        }
        self.assertDictEqual(self.base_model.to_dict(), expected_dict)

    def test_str(self):
        """ __str__ checker """
        expected_str = f"[BaseModel] ({self.base_model.id}) {self.base_model.__dict__}"
        self.assertEqual(str(self.base_model), expected_str)


if __name__ == '__main__':
    unittest.main()
