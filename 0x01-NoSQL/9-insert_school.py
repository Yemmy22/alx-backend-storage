#!/usr/bin/env python3
"""
An insert_school function module.
"""


def insert_school(mongo_collection, **kwargs):
    '''
    Returns an updated list following a new document insertion.
    '''
    doc = {}
    for key, value in kwargs.items():
        doc[key] = value
    mongo_collection.insert_one(doc)
    return mongo_collection
