#!/usr/bin/python3
"""Define the file_storage module."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """Define FileStorage class.

    This class is responsible for serializing and
    deserializing objects to/from JSON files.
    """

    def __init__(self):
        """Define the Class constructor."""
        self.__file_path = 'file.json'
        self.__objects = {}

    def all(self, cls=None):
        """Retrieve a dictionary of objects filtered by class name."""
        if cls is None:
            return self.__objects
        else:
            filtered_objects = {}
            for key, obj in self.__objects.items():
                if isinstance(obj, cls):
                    filtered_objects[key] = obj
            return filtered_objects

    def new(self, obj):
        """Add a new object to the __objects dictionary."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serialize the objects to JSON and save them to the file."""
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Deserialize the JSON file and reload objects into __objects."""
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, obj_data in data.items():
                    class_name, obj_id = key.split('.')
                    class_ = eval(class_name)
                    obj = class_(**obj_data)
                    self.__objects[key] = obj  # Keep the key format consistent
        except FileNotFoundError:
            pass
