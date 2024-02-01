#!/usr/bin/python3

"""
 A that lists all City objects, and corresponding State objects,
 contained in the database hbtn_0e_101_usa
"""
if __name__ == "__main__":
    # Import necessary modules.
    from sqlalchemy import create_engine
    from relationship_state import Base, State
    from relationship_city import City
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
        cities = session.query(City)
        for city in cities:
            print(f"{city.id}: {city.name} -> {city.state.name}")
    except Exception as e:
        print(f"An error occureded {e}")
    finally:
        session.close()
