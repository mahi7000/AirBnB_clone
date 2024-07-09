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

    def test_file_path(self):
        """Test file path is the same"""
        path = self.fstorage._FileStorage__file_path
        self.assertEqual(path, "file.json")

    def test_all(self):
        obj = BaseModel()
        self.fstorage.new(obj)
        all_objs = self.fstorage.all()
        self.assertIsInstance(all_objs, dict)
        self.assertIn(obj.__class__.__name__ + "." + obj.id,
                all_objs)

    def test_new(self):
        """Test adding new instance to basemodel"""
        obj = BaseModel()
        self.fstorage.new(obj)
        self.assertIn('BaseModel.{}'.format(obj.id),
                      self.fstorage._FileStorage__objects)

    def test_save_reload(self):
        """Test save and reload"""
        obj1 = BaseModel()
        self.fstorage.new(obj1)
        self.fstorage.save()

        new_storage = FileStorage()
        new_storage.reload()

        all_objs = new_storage.all()
        self.assertIn(obj1.__class__.__name__ + '.' + obj1.id, all_objs)


if __name__ == '__main__':
    unittest.main()
