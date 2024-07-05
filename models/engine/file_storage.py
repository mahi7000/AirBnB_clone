#!/usr/bin/python3
"""Serializes instances to JSON file and back"""

import json


class FileStorage:
    """Serializes and deserializes instances and JSON"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj"""
        cls = obj.__class__.__name__
        key = "{}.{}".format(cls, str(obj.id))
        self.__objects[key] = obj

    def save(self):
        """serialize __objects to JSON"""
        with open(self.__file_path, 'w') as file:
            for key, value in self.__objects.items():
                json.dump({key: value.to_dict()}, file)

    def reload(self):
        """Deserialize the JSON file to instances """
        try:
            from models.base_model import BaseModel
            classes = {'BaseModel': BaseModel}

            with open(self.__file_path, 'r') as file:
                content = file.read().strip()
                if content:
                    serialized = json.loads(content)
                    for key, value in serialized.items():
                        cls, objid = key.split('.')
                        self.__objects[key] = classes[cls](**value)
        except FileNotFoundError:
            pass
