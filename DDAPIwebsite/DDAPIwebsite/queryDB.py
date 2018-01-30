from django.db import connections


def test_get_bill_text():
    cursor = connections['apiDB'].cursor()
    cursor.execute('select text from BillVersion where bid = "CA_201520160AB1";')  # sample SQL query
    row = cursor.fetchall()
    return row


def hearing_transcript(hid):
    cursor = connections['apiDB'].cursor()
    cursor.execute('select p.first, p.last, u.time, u.endTime, u.text '
                   'from Hearing h, Video v, Utterance u left join Person p on u.pid = p.pid '
                   'where h.hid = v.hid and v.vid = u.vid and h.hid = ' + hid + ' order by u.uid')
    return cursor.fetchall()
