#!/usr/bin/python3
"""Models package.

~~~~~~~~~~~~~~

This package contains the data models for the AirBnB Clone project.

Subpackages:
- engine: Contains FileStorage classes for data persistence.


Modules:
- base_model: Defines the BaseModel class, which is the parent class for
  all other data models.
- user: Defines the User class for user-related data.
- state: Defines the State class for state-related data.
- ...

"""
from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
