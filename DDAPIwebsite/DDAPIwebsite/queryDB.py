from django.db import connections


def get_from_DB(query):
    cursor = connections['apiDB'].cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    return rows


def get_json_from_backend(query):

    # here is where we'd check if the query exists in the cache
    # if in cache, return json
    # if not in cache, then query database

    rows = get_from_DB(query)

    # convert to json here

    return rows



