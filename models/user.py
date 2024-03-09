#!/usr/bin/python3
"""User module"""
from models import BaseModel


class User(BaseModel):
    """User class represents a user of the application."""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
