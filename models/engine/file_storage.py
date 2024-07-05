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
            for key,value in self.__objects.items():
                json.dump({key: value.to_dict()}, file)

        def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        if (os.path.isfile(self.__file_path)
                and os.path.getsize(self.__file_path) > 0):
            with open(self.__file_path, 'r') as f:
                self.__objects = {k: self.get_class(k.split(".")[0])(**v)
                                  for k, v in json.load(f).items()}

    def get_class(self, name):
        """ returns a class from models module using its name"""
        sub_module = re.sub('(?!^)([A-Z]+)', r'_\1', name).lower()
        module = importlib.import_module(f"models.{sub_module}")
        return getattr(module, name)
