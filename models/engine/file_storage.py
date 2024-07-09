#!/usr/bin/python3

import os
import json
from models.base_model import BaseModel


class FileStorage:
    """
    serializes instances to a JSON file and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        obj_cls_name = obj.__class__.__name__
        key = "{}.{}".format(obj_cls_name, obj.id)
        FileStorage.__objects[key] = obj

    def all(self):
        """
        returns the dictionary __objects
        """
        return FileStorage.__objects

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        all_obj = FileStorage.__objects
        obj_dict = {}
        for obj in all_obj.key():
            obj_dict[obj] = all_obj[obj].to_dict()

        with open(FileStorage.__file_path, "w") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as file:
                try:
                    obj_dict = json.load(file)

                    for key, value in obj_dict.items():
                        class_name, obj_id = key.split('.')
                        cls = eval(class_name)
                        instance = cls(**value)
                        filestorage.__objects[key] = instance
                except Exception:
                    pass
