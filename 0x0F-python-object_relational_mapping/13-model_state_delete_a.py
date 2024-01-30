#!/usr/bin/python3

"""
Deletes a State object
"""
if __name__ == "__main__":
    # Import necessary modules.
    from sqlalchemy import create_engine
    from model_state import Base, State
    from sys import argv
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy.exc import NoResultFound

    # Set vairables to input arguments
    if len(argv) == 4:
        username = argv[1]
        password = argv[2]
        db_base = argv[3]

    # Start engine
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(username, password, db_base), pool_pre_ping=True)

    # Create a session
    Session = sessionmaker(bind=engine)

    # Create a Session instance
    session = Session()

    # my_session work
    try:
        state_del = session.query(State).filter(
            State.name.like('%a%')).delete(synchronize_session=False)

        if state_del:
            print(f"Deleted {state_del} rows.")
        else:
            print("No states with 'a' in their name were found.")

        session.commit()
    except Exception as e:
        print(f"An error occureded {e}")
    finally:
        session.close()
