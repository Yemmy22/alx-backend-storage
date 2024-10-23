#!/usr/bin/env python3
'''
An update_topics function module.
'''


def update_topics(mongo_collection, name, topics):
    '''
    Updates the school documents with the match
    '''
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
