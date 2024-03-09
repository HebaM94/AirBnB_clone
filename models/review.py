#!/usr/bin/python3
"""User module"""
from models import BaseModel


class Review(BaseModel):
    """Review class"""
    place_id = ""
    user_id = ""
    text = ""
