#!/usr/bin/python3

"""A script that lists all states from the database hbtn_0e_0_usa"""


import MySQLdb
import sys


def db_mysql_states(username, password, database_name):
    """Takes a user credentials and queries database for states"""
    db = MySQLdb.connect(host='localhost', port=3306, user=username,
                    passwd=password, db=database_name)
    
    cur = db.cursor()
    cur.execute('SELECT * FROM states ORDER BY id ASC;')
    states = cur.fetchall()
    
    for state in states:
        print(state)


if __name__ == "__main__":
    if len(sys.argv) == 4:
        username = sys.argv[1]
        password = sys.argv[2]
        database_name = sys.argv[3]
    
    db_mysql_states(username, password, database_name)
