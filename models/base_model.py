#!/usr/bin/python3
""" defines all common attributes """
import uuid
from datetime import datetime


class BaseModel:
    """ defines common attributes/methods for other classes """
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """ updates update_at with current datetime """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ returns dict containing all values of __dict__ """
        data = self.__dict__.copy()
        data['__class__'] = self.__class__.__name__
        data['created_at'] = self.created_at.isoformat()
        data['updated_at'] = self.updated_at.isoformat()
        return data

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
