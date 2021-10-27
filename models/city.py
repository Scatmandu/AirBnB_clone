#!/usr/bin/python3
''' Model defines class City'''

from models.base_model import BaseModel

class City(BaseModel):
    '''Defining City inherited from BaseModel'''

    state_id = ""
    name = ""