#!/usr/bin/python3
"""



"""
from uuid import uuid4
import json



class BaseModel:
    def __init__(self):
        self.id = str(uuid4())
        """Buscar como usar datetime"""
        self.created_at = "datetime"
        self.updated_at = "datetime"
    
    def __str__(self):
        """
            Deberia imprimir [<class name>] (<self.id>) <self.__dict__>
        """
        return f"[{__name__}] ({self.id}) {self.__dict__}"
    def save(self):
        """
            updates the public instance attribute updated_at with the current datetime
        """

    def to_dict(self):
        """
            returns a dictionary containing all keys/values of __dict__ of the instance
        """
    