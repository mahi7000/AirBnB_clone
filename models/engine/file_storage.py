#!/usr/bin/python3
"""Serializes instances to JSON file and
Deserializes JSON file to instances"""

import json


class FileStorage:
    """Serialize and deserialize"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return dictionary objects"""
        return self.__objects

    def new(self, obj):
        """Sets obj with key <obj classname.id>"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)        self.__object[key] = obj

    def save(self):
        """Serializes objects to JSON file"""
        serialized = {}
        for key, obj in self.__objects.items():
            serialized[key] = obj.to_dict()

        with open(self.__file_path, "w") as file:                       json.dump(serialized, file)

    def reload(self):
        """Deserializes JSON file to objects"""
        try:
            with open(self.__file_path, "r") as file:
                serialized = json.load(file)

                for key, value in serialized.items():
                    class_name, obj_id = key.split('.')
                    cls = eval(class_name)
                    obj = cls(**value)
                    self.__objects[key] = obj

        except FileNotFoundError:
            pass
