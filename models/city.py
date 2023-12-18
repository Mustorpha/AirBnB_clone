#!/usr/bin/python3
"""Extending the base models for cities"""

from models.base_model import BaseModel


class City(BaseModel):
    """Class to manage city objects"""

    state_id = ""
    name = ""
