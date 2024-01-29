#!/usr/bin/python3

"""A script that takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa"""

import MySQLdb
import sys


def print_cities_in_state(username, password, db_name, state_name):
    """Takes a state name and return a list of cities in given state"""

    db = MySQLdb.connect(
        host="localhost", port=3306, user=username, passwd=password,
        db=db_name)
    cur = db.cursor()

    cur.execute(
        "SELECT cities.name FROM cities\
        JOIN states ON cities.state_id = states.id\
        WHERE BINARY states.name = %s;", (state_name, )
    )

    cities = cur.fetchall()
    city_names = [city[0] for city in cities]
    print(", ".join(city_names))

    cur.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) == 5:
        username = sys.argv[1]
        password = sys.argv[2]
        db_name = sys.argv[3]
        state_name = sys.argv[4]
    print_cities_in_state(username, password, db_name, state_name)
