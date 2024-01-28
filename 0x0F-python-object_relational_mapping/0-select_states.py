#!/usr/bin/python3
import MySQLdb
import sys

# print("success")

def db_mysql(username, password, database_name):
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
    
    db_mysql(username, password, database_name)
