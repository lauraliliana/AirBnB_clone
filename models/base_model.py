#!/usr/bin/python3
"""
Module containing the class BaseModel
"""

import uuid
from datetime import datetime, time
import models

timeformat = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """This is the base class for many other classes in this project"""

    def __init__(self, *args, **kwargs):
        """Constructor function of the class BaseModel"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if hasattr(self, "created_at") and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], timeformat)
            if hasattr(self, "updated_at") and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], timeformat)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
            models.storage.save()

    def __str__(self):
        """Returns the string representation of the class"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the public attribute updated_at"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing the values of the instance"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].strftime(timeformat)
        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].strftime(timeformat)
        return new_dict
