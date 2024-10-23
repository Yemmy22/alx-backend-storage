#!/usr/bin/env python3
'''
A top_students function module.
'''


def top_students(mongo_collection):
    """
    Returns all students sorted by average score.
    """
    pipeline = [
            {
                "$unwind": "$topics"
                },
            {
                "$group": {
                    "_id": "$_id",
                    "name": {"$first": "$name"},
                    "averageScore": {"$avg": "$topics.score"}
                    }
                },
            {
                "$sort": {"averageScore": -1}
                }
            ]
    result = list(mongo_collection.aggregate(pipeline))
    return result
