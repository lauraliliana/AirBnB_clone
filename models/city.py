#!/usr/bin/python3
"""
Module containing the class City
"""

from models.base_model import BaseModel


class City(BaseModel):
    """City class
        Public class attributes:
            - state_id: string - empty string: it will be the State.id
            - name: string - empty string
    """

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Constructor of the class city"""
        super().__init__(*args, **kwargs)
