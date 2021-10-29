#!/usr/bin/python3
'''
Module to serializes instance to Json file and deserializes
Json file to a instance
'''

import models
import os.path
import json
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.user import User

class FileStorage:
    '''Class to Serializes and deserializes'''

    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''Returns Dict __objects'''

        return self.__objects

    def new(self, obj):
        '''Set __objects with obj as value and obj class name + .id as key
        '''

        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        ''' Serializes __objects to Json file'''

        newDict = {}
        for key, value in self.__objects.items():
            newDict[key] = value.to_dict()

        with open(self.__file_path, "w") as fd:
            json.dump(newDict, fd)

    def reload(self):
        '''load objs from json file'''

        from models.city import City
        from models.place import Place
        from models.state import State
        from models.review import Review
        from models.amenity import Amenity
        from models.user import User

        if os.path.isfile(self.__file_path):
            from models.base_model import BaseModel

            with open(self.__file_path, "r", encoding='UTF-8') as thefile:
                objectfromjson = json.load(thefile)

            for key, value in objectfromjson.items():
                cls = value["__class__"]
                obj = eval(cls + "(**value)")
                self.__objects[key] = obj
        else:
            return
