#!/usr/bin/python3
"""FileStorage class module"""

import os.path
import json


class FileStorage:
    """storing and retrieving objects
    """
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """initializing instance
        """
        pass

    def all(self):
        """returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id
        """
        key = obj.__class__.__name__ + ".{}".format(obj.id)
        FileStorage.__objects[key] = obj

    @staticmethod
    def to_json_string(objects):
        final_dec = {}
        for key in objects.keys():
            val = objects[key].to_dict()
            final_dec[key] = val
        return final_dec

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path)
        """
        jsn_format = FileStorage.to_json_string(FileStorage.__objects)
        with open(FileStorage.__file_path, mode="w", encoding="utf-8") as fily:
            fily.write(json.dumps(jsn_format))

    @staticmethod
    def from_json_string(string):
        if string:
            return json.loads(string)
        else:
            return {}

    def reload(self):
        """ deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists
        """
        from models.base_model import BaseModel

        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as fily:
                var = fily.read()
            if var is None or var == "":
                return

            objects = FileStorage.from_json_string(var)
            for key, value in objects.items():
                FileStorage.__objects[key] = BaseModel(**value)
        else:
            return
