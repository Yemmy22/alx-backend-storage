#!/usr/bin/env python3
"""
An insert_school function module.
"""


def insert_school(mongo_collection, **kwargs):
    '''
    Returns the document insertion ID.
    '''
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
