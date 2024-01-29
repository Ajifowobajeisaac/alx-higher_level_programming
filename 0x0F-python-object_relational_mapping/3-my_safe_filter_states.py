#!/usr/bin/python3

"""A script that takes in arguments and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument. Must be SQL injection safe"""

import MySQLdb
import sys


def search_filter_injection_safe(username, password, db_name, search):
    """Searches a table for a value and reaturns the return the row safe from
    sql injections"""

    db = MySQLdb.connect(
        host='localhost', port=3306, user=username, passwd=password,
        db=db_name)
    cur = db.cursor()

    cur.execute(
        "SELECT * FROM states WHERE BINARY name = %s ORDER BY id ASC;",
        (search,))

    states = cur.fetchall()
    for state in states:
        print(state)

    cur.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) == 5:
        username = sys.argv[1]
        password = sys.argv[2]
        db_name = sys.argv[3]
        search = sys.argv[4]
    search_filter_injection_safe(username, password, db_name, search)
