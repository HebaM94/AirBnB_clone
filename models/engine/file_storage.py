#!/usr/bin/python3
"""storage module"""
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
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id"""
        FileStorage.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file."""
        if len(FileStorage.__objects) > 0:
            new_dict = {}
            for key, obj in FileStorage.__objects.items():
                new_dict[key] = obj.to_dict().copy()

        with open(FileStorage.__file_path, 'w', encoding="utf-8") as file:
            file.write(json.dumps(new_dict, indent=4))

    def reload(self):
        """Deserialize the JSON file to __objects."""
        try:
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as file:
                new = file.read()
                loaded_objects = json.loads(new)
                for key, value in loaded_objects.items():
                    class_name = value.get('__class__')
                    obj =BaseModel(**value)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
