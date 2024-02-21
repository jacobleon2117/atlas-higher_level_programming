#!/usr/bin/python3

"""
Module - a SQL Alchemy query to update the name of an entry
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State, City
from sys import argv

if __name__ == '__main__':

    user = argv[1]
    pwd = argv[2]
    db = argv[3]
    host = 'localhost'
    dia = 'mysql+mysqldb'

    connect = '{0}://{1}:{2}@{3}:3306/{4}'.format(dia, user, pwd, host, db)

    engine = create_engine(connect)

    Session = sessionmaker(bind=engine)
    session = Session()

    my_state = session.query(State).filter_by(id=2).first()
    my_state.name = "New Mexico"
    session.commit()
    session.close()
