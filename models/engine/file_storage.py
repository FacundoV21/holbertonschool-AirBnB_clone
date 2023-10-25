#!/usr/bin/python3
import json
import sys

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        json_dictionary = {}
        for k, obj in self.__objects.items:
            json_dictionary[k] = obj.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(json_dictionary, file)

    def reload(self):
        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                for k, v in json.load(file).items:
                    clsobj = v.get(__class__)
                      
        except FileNotFoundError:
            pass
 