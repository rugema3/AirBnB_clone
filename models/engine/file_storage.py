#!/usr/bin/python3
from base_model import BaseModel
import Json
class FileStorage(BaseModel):
    def __init__(self, __file_path, __objects):
        super().__init(args, kwargs)
        self.__file_path = 'file.json'
        self.__objects = {}
    def all(self):
        return FileStorage.self.__objects

