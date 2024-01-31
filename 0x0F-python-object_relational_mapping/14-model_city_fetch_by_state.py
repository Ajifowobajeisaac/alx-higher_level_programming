#!/usr/bin/python3

"""
  Prints all City onjects from the databace
"""
if __name__ == "__main__":
    # Import necessary modules.
    from sqlalchemy import create_engine
    from model_state import Base, State
    from model_city import City
    from sys import argv
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy.exc import NoResultFound

    # Set vairables to input arguments
    if len(argv) != 4:
        print("Usage: script.py <username> <password> <database>")
        exit(1)

    username, password, db_base = argv[1:4]

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
        for cities, states in session.query(City, State)\
                .filter(City.state_id == State.id)\
                .order_by(City.id):
            print(f"{states.name}: {cities.id} {cities.name}")
        session.commit()
    except Exception as e:
        print(f"An error occureded {e}")
    finally:
        session.close()
