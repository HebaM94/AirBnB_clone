#!/usr/bin/python3
"""storage module"""
import datetime
import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """File Storage class to handle file operations."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id"""
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file."""
        if len(self.__objects) > 0:
            new_dict = {}
            for key, obj in self.__objects.items():
                new_dict[key] = obj.to_dict()

        with open(self.__file_path, 'w', encoding="utf-8") as file:
            file.write(json.dumps(new_dict, indent=4))

    def reload(self):
        """Deserialize the JSON file to __objects."""
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as file:
                loaded_objects = json.load(file)
                for key, value in loaded_objects.items():
                    class_name, obj_id = key.split('.')
                    obj = eval(class_name)(**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
