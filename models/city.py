#!/usr/bin/python3
"""Extends the base models for cities"""

from models.base_model import BaseModel


class City(BaseModel):
    """Class for managing city objects"""

    state_id = ""
    name = ""
