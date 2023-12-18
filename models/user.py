#!/usr/bin/python3
"""Extends the base model for Users"""

from models.base_model import BaseModel


class User(BaseModel):
    """Class to manage user objects"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
