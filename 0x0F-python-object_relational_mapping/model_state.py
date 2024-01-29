#!/usr/bin/pyhton3

"""A file that contains the class definition of a State and an instance 
Base = declarative_base()"""

import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Defines a state object"""

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    def __repr__(self):
        return f"{self.id}, {self.name}"
