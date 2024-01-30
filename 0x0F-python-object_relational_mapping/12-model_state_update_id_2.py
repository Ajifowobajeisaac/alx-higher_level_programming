#!/usr/bin/python3

"""Updates a State object"""

from sqlalchemy import create_engine
from model_state import Base, State
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import NoResultFound

if __name__ == "__main__":
    if len(argv) == 4:
        username = argv[1]
        password = argv[2]
        db_base = argv[3]
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(username, password, db_base), pool_pre_ping=True)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    try:
        state_change = session.query(State).filter(State.id == 2).first()
        if state_change:
            state_change.name = "New Mexico"
            session.commit()
            print(f"{state_change.id}: {state_change.name}")
        else:
            print("State not found")
    except NoResultFound:
        print("Not found")
