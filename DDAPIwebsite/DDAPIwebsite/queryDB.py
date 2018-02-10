from django.db import connections
from . import API_settings


def test_get_bill_text():
    cursor = connections['apiDB'].cursor()
    cursor.execute('select text from BillVersion where bid = "CA_201520160AB1";')  # sample SQL query
    row = cursor.fetchall()
    return row


def hearing_transcript(hid):

    query = API_settings.HEARING_ID_STRING % str(hid)

    # result = check_cache(query)  # get json object from cache, or null
    result = None

    if result is None:  # if the query was not in the cache

        # database stuff
        cursor = connections['apiDB'].cursor()
        cursor.execute(query)
        rows = cursor.fetchall()

        # convert to json here
        # result = convert to json (rows)

        # add_to_cache(query, result)  # add SQL string and json to cache
        result = rows  # remove this after we convert to json

    return result

