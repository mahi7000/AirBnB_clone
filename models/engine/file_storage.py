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
        serialized = {}
        for key, value in self.__objects.items():
            serialized[key] = value.to_dict()
        with open(self.__file_path, 'w') as file:
            for key in serialized.keys():
                json.dump(serialized, file)
                file.write("\n")

    def reload(self):
        try:
            with open(self.__file_path, 'r') as file:
                for line in f:
                    data = json.load(line)

                    for key, value in data.items():
                        cls, obj_id = key.split('.')
                        obj = eval(cls)(**value)
                        self.__objects[key] = obj

        except FileNotFoundError:
            pass
