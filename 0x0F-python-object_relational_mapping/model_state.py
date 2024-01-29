#!/usr/bin/pyhton3

"""A file that contains the class definition of a State and an instance 
Base = declarative_base()"""

import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                       .format("root", "root", "my_db"), pool_pre_ping=True)
Base.metadata.create_all(engine)


class State(Base):
    """Defines a state object"""

    __tablename__ = 'state'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
