#!/usr/bin/env python3
"""
Web cache and tracker module
"""

import redis
import requests
from functools import wraps

# Initialize Redis client
redis_client = redis.Redis()


def url_access_count(method):
    """Decorator to track URL access count and cache result"""
    @wraps(method)
    def wrapper(url):
        """Wrapper function"""
        # Increment the access count
        count_key = f"count:{url}"
        redis_client.incr(count_key)

        # Check if we have cached content
        cache_key = f"result:{url}"
        cached_result = redis_client.get(cache_key)

        if cached_result:
            return cached_result.decode('utf-8')

        # Get fresh content
        result = method(url)

        # Cache the result for 10 seconds
        redis_client.setex(cache_key, 10, result)

        return result
    return wrapper


@url_access_count
def get_page(url: str) -> str:
    """
    Get a web page and cache the result
    with an expiration time of 10 seconds
    """
    response = requests.get(url)
    return response.text


if __name__ == "__main__":
    get_page('http://slowwly.robertomurray.co.uk')
