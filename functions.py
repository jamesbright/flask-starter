#!/usr/bin/python3
"""A module that contains functions for operations"""

import json
from models import storage
from datetime import timedelta

def get_all_users():
    """A function that retrieves all users from storage"""
    all_users = storage.all(User)
    all = [user for user in all_users.values()]
    return all

