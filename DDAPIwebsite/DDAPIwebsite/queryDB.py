from django.db import connections


def test_get_bill_text():
    cursor = connections['apiDB'].cursor()
    cursor.execute('select text from BillVersion where bid = "CA_201520160AB1";')  # sample SQL query
    row = cursor.fetchall()
    return row



