#!/usr/bin/python3

"""
The __init__ method for models package
"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


storage = FileStorage()
storage.reload()
