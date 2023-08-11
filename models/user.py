#!/usr/bin/python3
from models.base_model import BaseModel
"""define user class"""


class User(BaseModel):
    """define user description"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
