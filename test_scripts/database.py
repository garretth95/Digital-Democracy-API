import mysql.connector

# connect to database
db = mysql.connector.connect(host='dev.digitaldemocracy.org', user='pupil', password='slolife805',
                             database='DDDB2016Aug')
# prepare cursor object
cursor = db.cursor()

# this query is just an example SQL statement that only returns 2 tuples
query = 'select number, house, state, sessionYear from Bill where billState = "Amended Senate" and status = "passed" and type = "SJR"'

print '\n' + query + '\n'

try:
    # execute the select statement
    cursor.execute(query)

    # get the results from the query
    results = cursor.fetchall()

    # print nicely
    for row in results:
        num = row[0]
        house = row[1]
        state = row[2]
        year = row[3]

        print "numer: %s, house: %s, state: %s, year: %s" % (num, house, state, year)

except:
    print 'Error querying data'

# close connection to database
db.close()
