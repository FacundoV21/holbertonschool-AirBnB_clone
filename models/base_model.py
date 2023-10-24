#!/usr/bin/python3
"""
    Define a class

    [BaseModel]: class that define all attributes and methods for other class
        Public Instances:
            Id: This instance save a unique id when the an instance is created
            Created_at: assign with the current datetime when an instance
                        is created.
            Update_at: assign with the current datetime when an instance is
            created and it will be updated every time you change your object

"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """BaseModel class: define all attributes and methods"""
    def __init__(self, *args, **kwargs):
        tpyefrmt = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for k, v in kwargs.items():
                if "created_at" == k or "updated_at" == k:
                    self.__dict__[k] = datetime.strptime(v, tpyefrmt)
                else:
                    self.__dict__[k] = v


    def __str__(self):
        """Method __str__ that print a string"""
        return f"[{__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the public instance attribute updated_at with the
        current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """ returns a dictionary containing all keys/values
        of __dict__ of the instance:"""
        dictionary = self.__dict__
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary
