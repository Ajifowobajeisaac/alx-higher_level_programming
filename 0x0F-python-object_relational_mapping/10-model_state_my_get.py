#!/usr/bin/python3

"""Defines script that returns a given State"""

from sqlalchemy import create_engine
from model_state import Base, State
from sys import argv
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    if len(argv) == 5:
        username = argv[1]
        password = argv[2]
        db_base = argv[3]
        search = argv[4]
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(username, password, db_base), pool_pre_ping=True)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    state = State()

    state_unique = session.query(State).filter(State.name == search).one()

    if state_unique is None:
        print("Not found")
    else:
        print(state_unique.id)
