#!/usr/bin/python3
"""
Module containing the class User
"""

from models.base_model import BaseModel


class User(BaseModel):
    """User class
        Public class attributes:
            - email: string - empty string
            - password: string - empty string
            - first_name: string - empty string
            - last_name: string - empty string
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Constructor of the calss user"""
        super().__init__(*args, **kwargs)
