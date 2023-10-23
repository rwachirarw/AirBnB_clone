#!/usr/bin/python3
"""
module that defines the Amenity class
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class that inherits from BaseModel.
    Public class attributes:
        name: string - empty string
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Method to initialize the Amenity class instance

        Args:
            args - variable arguments
            kwargs - key word arguments
        """
        super().__init__(*args, **kwargs)
