#!/usr/bin/python3
"""
Defines the BaeModel class
Parent to all classes
"""

from datetime import datetime
from models import storage
import uuid


class BaseModel:
    """
    Defines BaseModel class
    Methods:
        __init__()
        __str__()
        save()
        to_dict()
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a BaseModel instance object
        If it is a new instance (not from a dictionary representation),
        add a call to the method new(self) on storage.

        Args:
            args - variable arguments
            kwargs - key word arguments
        Returns:
            BaseModel instance
        """
        if kwargs:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    v = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                if k != "__class__":
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        Generate a string representation of the object

        Returns:
            Str: string representation of the object
        """

        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        Update the attribute updated_time.
        """

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Dictionary representation of the class

        Returns:
            dict: Dictionary representation of the class
        """
        class_dict = {
            "__class__": self.__class__.__name__
        }
        for k, v in self.__dict__.items():
            if k == "created_at":
                class_dict[k] = v.isoformat()
            elif k == "updated_at":
                class_dict[k] = v.isoformat()
            else:
                class_dict[k] = v
        return class_dict
