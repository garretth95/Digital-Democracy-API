# Caching functionality
# created by Conor Murphy

from django.core.cache import cache

TIMEOUT = 60 * 60 * 6


def generate_key(query):
    s = query
    s = s.replace(" ","")
    s = s.replace(".","")
    return s


def cache_has(query):
    key = generate_key(query)
    return cache.get(key) is not None


def get_from_cache(query):
    key = generate_key(query)
    return cache.get(key)


def set_cache(query, data):
    key = generate_key(query)
    if cache.get(key) is None:
        cache.set(key, data, TIMEOUT)
