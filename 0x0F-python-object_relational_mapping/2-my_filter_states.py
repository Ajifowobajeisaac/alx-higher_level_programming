#!/usr/bin/python3

"""A script that takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument"""

import MySQLdb
import sys


def search_filter(username, password, db_name, search):
    """Takes string input and searches a database table to return result"""

    db = MySQLdb.connect(
        host='localhost', port=3306, user=username,
        passwd=password, db=db_name)
    cur = db.cursor()

    cur.execute(
        "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC;"
        .format(search))

    state = cur.fetchall()
    print(state)

    cur.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) == 5:
        username = sys.argv[1]
        password = sys.argv[2]
        db_name = sys.argv[3]
        search = sys.argv[4]
    search_filter(username, password, db_name, search)
