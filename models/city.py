#!/usr/bin/python3
"""Cities of airbnb"""

from models.base_model import BaseModel


class City(BaseModel):
    """Class city with attributes state_id and name"""
    state_id = ""
    name = ""
