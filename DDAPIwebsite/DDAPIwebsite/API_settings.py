"""
API settings for DDAPIwebsite project.

"""

HEARING_ID_STRING = 'select p.first, p.last, u.time, u.endTime, u.text from Hearing h, Video v, Utterance u' \
                    ' left join Person p on u.pid = p.pid where h.hid = v.hid and v.vid = u.vid' \
                    ' and h.hid = %s order by u.uid'