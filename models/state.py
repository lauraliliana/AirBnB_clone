#!/usr/bin/python3
"""
Module containing the class State
"""

from models.base_model import BaseModel


class State(BaseModel):
    """State class
        Public class attributes:
            - name: string - empty string
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """Constructor of the class state"""
        super().__init__(*args, **kwargs)
