#!/usr/bin/python3

""" A script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa."""

import MySQLdb
import sys


def filter_states(username, password, db_name):
    """Takes user credentials, filters a database and returns state"""

    db = MySQLdb.connect(
        host='localhost', port=3306, user=username,
        passwd=password, db=db_name)
    cur = db.cursor()

    cur.execute('SELECT * FROM states WHERE BINARY (name) LIKE \'N%\'')

    states = cur.fetchall()

    for state in states:
        print(state)
    
    cur.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        username = sys.argv[1]
        password = sys.argv[2]
        db_name = sys.argv[3]
    filter_states(username, password, db_name)
