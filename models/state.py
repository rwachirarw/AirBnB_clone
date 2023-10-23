#!/usr/bin/python3
"""
module that defines the State class
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    State class that inherits from BaseModel.
    Public class attributes:
        name: string - empty string
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Method to initialize the State class instance

        Args:
            args - variable arguments
            kwargs - key word arguments
        """
        super().__init__(*args, **kwargs)
