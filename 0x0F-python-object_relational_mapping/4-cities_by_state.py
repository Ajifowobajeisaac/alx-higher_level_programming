#!/usr/bin/python3

"""A script that lists all cities from the database hbtn_0e_4_usa"""

import MySQLdb
import sys


def print_cites(username, password, db_name):
    """Prints all cities in database"""

    db = MySQLdb.connect(
        host='localhost', port=3306, user=username, passwd=password,
        db=db_name)
    cur = db.cursor()

    cur.execute(
        "SELECT * FROM cities ORDER BY id ASC")

    cities = cur.fetchall()
    for city in cities:
        print(city)

    cur.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        username = sys.argv[1]
        password = sys.argv[2]
        db_name = sys.argv[3]
    print_cites(username, password, db_name)
