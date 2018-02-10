"""
API settings for DDAPIwebsite project.

"""

HEARING_ID_STRING = 'select p.first, p.last, u.time, u.endTime, u.text from Hearing h, Video v, Utterance u' \
                    ' left join Person p on u.pid = p.pid where h.hid = v.hid and v.vid = u.vid' \
                    ' and h.hid = %s order by u.uid'

HEARING_ID = 'select h.hid,h.date,h.session_year from Hearing h, Committee c ' \
             'where h.date = %s and h.session_year = c.session_year and h.state = %s c.name = %s' \
             'and h.state = c.state limit 1'