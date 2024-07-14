#!/usr/bin/python3
"""
Parent class that will inherit
"""
import uuid
from datetime import datetime
from models import storage

class BaseModel:
    def __init__(self, *args, **kwargs):
        date_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, date_format))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
        models.storage.new(self)

    def save(self):
        """
        updates the last update time
        """
        self.updated_at = datetime.utcnow()
        models.storage.save(self)

    def to_dict(self):
        """
        creates a new dictionary, adding a key and returning
        datemtimes converted to strings
        """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()

        return new_dict

    def __str__(self):
        """returns class name, id and attribute dictionary
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) ({})".format(class_name, self.id, self.__dict__)
