#!/usr/bin/python3

from models.base_model import BaseModel


class Review(BaseModel):
    """Define Review class.

    Attributes:
    place_id(str):  The id of the place. set as an empty string
    user_id(str):   The id of the user. set as an empty string.
    text(str):      The text containing the reviews from the user.
    """
    place_id = ""
    user_id = ""
    text = ""
