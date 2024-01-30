#!/usr/bin/python3

"""A script that lists all State objects from the database hbtn_0e_6_usa"""

from sqlalchemy import create_engine
from model_state import Base, State
from sys import argv
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    if len(argv) == 4:
        username = argv[1]
        password = argv[2]
        db_base = argv[3]
        port = 33
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:{}/{}'
        .format(username, password, port, db_base), pool_pre_ping=True)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    state = State()
    first_state = session.query(State).first()

    if first_state is None:
        print("Nothing")
    else:
        print(f"{first_state.id}: {first_state.name}")
