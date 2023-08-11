#!/usr/bin/python3
from models.base_model import BaseModel


class Place(BaseModel):
    """Define Place class.

    Attributes:
    city_id(str):  The city id. set as an empty string.
    user_id(str):   The user id.
    name(str):      The name of the place.
    description:    The description of the place. set as an empty string.
    number_rooms(int):  The number of rooms. Set to zero
    max_guest(int):     The maximum number of guest the place can accomodate.
    price_per_night(float):    The per night rate of the room.
    number_bathrooms(int):      The number of bathrooms in a room. set to zero
    latitude(float):            The latitute set to 0.0
    longitude(float):           The coordinate of the longitude set to 0.0
    amenity_ids(list):          List of amenity id.
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = ""
    max_guest = 0
    price_per_night = 0
    number_bathrooms = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []  # Empty list containing amenity ids
