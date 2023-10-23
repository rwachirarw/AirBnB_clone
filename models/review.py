#!/usr/bin/python3
"""
module that defines the Review class
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class that inherits from BaseModel.
    Public class attributes:
        place_id: string - empty string (Place.id)
        user_id: string - empty string (User.id)
        text: string - empty string
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """
        Method to initialize the Review class instance

        Args:
            args - variable arguments
            kwargs - key word arguments
        """
        super().__init__(*args, **kwargs)
