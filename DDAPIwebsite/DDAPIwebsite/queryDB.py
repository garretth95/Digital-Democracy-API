from django.db import connections
import json
import datetime

def get_from_DB(query):
    # cursor = connections['apiDB'].cursor()
    # cursor.execute(query)
    # rows = cursor.fetchall()
    # This will get the
    cur2 = connections['apiDB'].cursor(MySQLdb.cursors.DictCursor)
    cur2.execute(query)
    rows2 = cur2.fetchall()
    return rows2


def get_json_from_backend(query):

    # here is where we'd check if the query exists in the cache
    # if in cache, return json
    # if not in cache, then query database

    rows = get_from_DB(query)

    def clean_output(o):
        # Checked for single quote strings
        if isinstance(o, str):
            return o.__str__()
        if isinstance(o, datetime.datetime):
            # set time to Epoch PST
            return o.strftime('%s')

    rows = json.dumps(rows, default=clean_output)

    # convert to json here

    return rows



