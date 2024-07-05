#!/usr/bin/python3
"""Create a unique Filestorage instance"""

from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
