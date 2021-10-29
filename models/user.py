#!/usr/bin/python3
''' Model defines class User'''


from models.base_model import BaseModel


class User(BaseModel):
    '''Defining Review inherited from BaseModel'''

    email = ""
    password = ""
    first_name = ""
    last_name = ""
