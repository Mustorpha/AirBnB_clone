#!/usr/bin/python3
"""Extending the base class for amenties"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Class for managing amenity objects"""

    name = ""
