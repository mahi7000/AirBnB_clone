#!/usr/bin/python3
""" unittest file storage """

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """ Test file storage """
    def setUp(self):
        """ Create new FileStorage instance """
        self.fstorage = FileStorage()

    def test_new(self):
        """Test adding new instance to basemodel"""
        obj = BaseModel()
        self.fstorage.new(obj)
        self.assertIn('BaseModel.{}'.format(obj.id),
                      self.fstorage._FileStorage__objects)

    def test_save_reload(self):
        """Test save and reload"""
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.fstorage.new(obj1)
        self.fstorage.new(obj2)
        self.fstorage.save()
        self.fstorage.reload()
        self.assertIn('BaseModel.{}'.format(obj1.id),
                      self.fstorage._FileStorage__objects)
        self.assertIn('BaseModel.{}'.format(obj2.id),
                      self.fstorage._FileStorage__objects)


if __name__ == '__main__':
    unittest.main()
