#!/usr/bin/env python3
"""
A Cache class module.
"""

import redis
import uuid
from typing import Union


class Cache():
    """
    A cache class
    """
    def __init__(self):
        """
        Instantiates a redis client cache and flushes it.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Saves input data as a key value pair in
        the database and returns the value.
        """
        randNum = str(uuid.uuid4())
        self._redis.set(randNum, data)
        return randNum
