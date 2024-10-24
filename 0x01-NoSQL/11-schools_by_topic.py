#!/usr/bin/env python3
'''
A schools_by_topic function module.
'''


def schools_by_topic(mongo_collection, topic):
    '''
    Returns a list of documents with the specified topic
    '''
    match = mongo_collection.find({"topics": topic})
    return match
