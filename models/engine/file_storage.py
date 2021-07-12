#!/usr/bin/python3
"""
Module containing the class Filestorage
"""

import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

class_dict = {
    "Amenity": Amenity,
    "BaseModel": BaseModel,
    "City": City,
    "Place": Place,
    "Review": Review,
    "State": State,
    "User": User
    }


class FileStorage:
    """Serializes and deserializes instances to/from JSON"""
    # String - path to the JSON file
    __file_path = "file.json"
    # Dictionary - empty but will store all objects by <class name>.id
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        object_json = {}
        for key in self.__objects:
            object_json[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(object_json, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, "r") as f:
                objson = json.load(f)
            for obj in objson:
                self.__objects[obj] = class_dict[
                    objson[obj]["__class__"]
                    ](**objson[obj])
        except:
            pass
