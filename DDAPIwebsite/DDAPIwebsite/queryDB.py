from django.db import connections
import json
import datetime
from .cache import *


def get_from_DB(query):

    # This will get the SQL data as a dictionary
    cursor = connections['apiDB'].cursor()
    cursor.execute(query)

    # Returns all rows from a cursor as a dict
    desc = cursor.description
    dic = [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]

    return dic


def get_json_from_backend(query):

    # here is where we'd check if the query exists in the cache
    # if in cache, return json
    # if not in cache, then query database
    if cache_has(query):
        rows = get_from_cache(query)
    else:
        rows = get_from_DB(query)

    # def clean_output(o):
    #     # Checked for single quote strings
    #     if isinstance(o, str):
    #         return o.__str__()
    #     if isinstance(o, datetime.datetime):
    #         # set time to Epoch PST
    #         return o.strftime('%s')
    #
    # # convert to json here
    # rows = json.dumps(rows, default=clean_output)

    return rows



