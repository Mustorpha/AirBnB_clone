#!/usr/bin/python3
"""Initializes the model module"""

from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
