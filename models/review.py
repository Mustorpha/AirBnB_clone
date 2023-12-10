#!/usr/bin/python3
"""Extends base model for reviews"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Class to manage review objects"""

    place_id = ""
    user_id = ""
    text = ""
