#!/usr/bin/python3
"""
Defines class FileStorage
Serializes instances to a JSON file and deserializes JSON file to instances
"""

import json
from datetime import datetime


class FileStorage:
    """
    Class to perform Serialization and Deserialization to JSON files

    Attributes:
        __file_path
        __objects
    Methods:
        all()
        new()
        save()
        reload()
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Method to ectract the stored objects

        Returns:
            Attribute __objects; the dictionary of all stored objects
        """
        return self.__objects

    def new(self, obj):
        """
        Store created objects into the sictioanry

        Args:
            obj: object class type to be stored
        """

        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serialize the __objects to the JSON file in path __file_path

        __objects dictionary contains instances of custom classes.
        We cannot use directly json.dump().
        We have to call the to_dict() method on each object to
        convert it into a dictionary representation
        before serializing it using json.dump().
        """

        serial_objects = {}

        for k, v in self.__objects.items():
            serial_objects[k] = v.to_dict()

        with open(self.__file_path, mode='w', encoding="utf-8") as f:
            json.dump(serial_objects, f)

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ; otherwise,
        do nothing. If the file doesn’t exist, no exception should be raised)
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
        }

        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                obj_dict = json.load(f)
            for k, v in obj_dict.items():
                obj = classes[v["__class__"]](**v)
                self.__objects[k] = obj
        except FileNotFoundError:
            pass
