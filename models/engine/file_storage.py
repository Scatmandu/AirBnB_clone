#!/usr/bin/python3
'''
Module to serializes instance to Json file and deserializes
Json file to a instance
'''
from models.base_model import BaseModel


import os.path
import json

class FileStorage:
    '''Class to Serializes and deserializes'''

    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''Returns Dict __objects'''

        return __objects

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


