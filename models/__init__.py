#!/usr/bin/python3
"""
Loads the objects stored in a JSON file on the disk
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
