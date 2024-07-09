#!/usr/bin/python3
"""Review of airbnb"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review with attr place_id, user_id and text"""
    place_id = ""
    user_id = ""
    text = ""
