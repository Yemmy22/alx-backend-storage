#!/usr/bin/env python3
"""
Web page caching module using Redis
"""

import redis
import requests
from functools import wraps
from typing import Callable

# Initialize Redis client
r = redis.Redis()


def url_access_count(method: Callable) -> Callable:
    """
    Decorator for tracking URL access counts
    and caching responses
    """
    @wraps(method)
    def wrapper(url: str) -> str:
        """
        Wrapper function implementing caching logic
        """
        # Keys for cache and count
        cache_key = f"cached:{url}"
        count_key = f"count:{url}"

        # Increment the access count before checking cache
        r.incr(count_key)

        # Check if content is cached
        cached_content = r.get(cache_key)
        if cached_content:
            return cached_content.decode('utf-8')

        # Get new content if not cached
        html_content = method(url)

        # Cache the new content with expiration
        r.setex(cache_key, 10, html_content)

        return html_content

    return wrapper


@url_access_count
def get_page(url: str) -> str:
    """Get HTML content of a web page"""
    response = requests.get(url)
    return response.text


if __name__ == "__main__":
    get_page('http://slowwly.robertomurray.co.uk')
