#!/usr/bin/python3

from models.base_model import BaseModel


class City(BaseModel):
    """Define City class.

    Attribute:
    state_id(str):  The state id
    name(str):      The name of the city
    """
    name = ""   # the name of the city is set as an empty string
    state_id = ""   # The state id is set as an empty string
