#!/usr/bin/python3
"""Serializes instances to JSON file and back"""

import json
from models.base_model import BaseModel


class FileStorage:
    """Serializes and deserializes instances and JSON"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj"""
        cls = obj.__class__.__name__
        key = "{}.{}".format(cls, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serialize __objects to JSON"""
        objs = FileStorage.__objects
        serialized = {}

        for obj in objs.keys():
            serialized[obj] = objs[obj].to_dict()

        with open(FileStorage.__file_path, 'w', encoding="utf-8") as file:
            json.dump(serialized, file)

    def reload(self):
        """Deserialize the JSON file to instances """
        try:
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as file:
                deserialized = json.load(file)
                for key, value in deserialized.items():
                    cls_name, obj_id = key.split('.')
                    cls = eval(cls_name)
                    new = cls(**value)
                    FileStorage.__objects[key] = new
                
        except FileNotFoundError:
            pass
