#!/usr/bin/python3
from models.engine.file_storage import FileStorage

print("Initializing storage...")
storage = FileStorage()
print("Reloading data...")
storage.reload()
print("Storage initialization and data reload complete.")
