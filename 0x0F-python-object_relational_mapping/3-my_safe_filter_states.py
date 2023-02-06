#!/usr/bin/python3
"""
Displays all values in the states table of
hbtn_0e_0_usa where name matches the argument.
(Safe from SQL Injection)
"""

if __name__ == '__main__':
    from sys import argv
    import MySQLdb as mysql
    import re

    if (len(argv) != 5):
        print('Use: username, password, database name, state name')
        exit(1)

    searched = ' '.join(argv[4].split())

    if (re.search('^[a-zA-Z ]+$', searched) is None):
        print('Enter a valid name state (example: Arizona)')
        exit(1)

    try:
        db = mysql.connect(host='localhost', port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])
    except Exception:
        print('Failed to connect to the database')
        exit(0)

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states \
                    WHERE name = '{:s}' ORDER BY id ASC;".format(searched))

    result_query = cursor.fetchall()

    for row in result_query:
        print(row)

    cursor.close()
    db.close()
