#!/usr/bin/python3
"""Contains class BaseModel that defines
    all common attributes/methods for other classes"""

import uuid
from datetime import datetime


class BaseModel:
    """Contains common attributes/methods"""

    def __init__(self):
        """Creates public instance attributes"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """Prints string representaion of object"""
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates 'updated_at' with current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary with values of __dict__"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
