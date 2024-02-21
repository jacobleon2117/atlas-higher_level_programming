#!/usr/bin/python3

"""
Module - State SQLAlchemy definition
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State SQLAlchemy model
    Attributes:
        __tablename__: the name of the table
        id: an identifying integer
        name: the name of the state
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)

    cities = relationship("City", back_populates="state")
