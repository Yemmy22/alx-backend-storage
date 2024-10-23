#!/usr/bin/env python3


'''
A  lis_all function module.
'''


def list_all(mongo_collection):
    '''
    Returns a list of all documents in the collection 'school'.
    '''
    return mongo_collection.find()
