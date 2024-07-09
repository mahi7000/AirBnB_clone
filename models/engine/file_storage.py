#!/usr/bin/python3
"""Serializes instances to JSON file and back"""

import json
import re
import importlib


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
        key = "{}.{}".format(cls, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serialize __objects to JSON"""
        serialized = {}
        for key, value in self.__objects.items():
            serialized[key] = value.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump({key: value.to_dict for key,
                       value in self.__objects.items()}, file)

    def reload(self):
        """Deserialize the JSON file to instances """
        try:
            with open(self.__file_path, 'r') as file:
                self.__objects = {key: self.get_class(
                        key.split('.')[0])(**value)
                        for key, value in json.load(file).items()}
        except FileNotFoundError:
            pass

    def get_class(self, name):
        """ returns a class from models module using its name"""
        sub_module = re.sub('(?!^)([A-Z]+)', r'_\1', name).lower()
        module = importlib.import_module(f"models.{sub_module}")
        return getattr(module, name)
