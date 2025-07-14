#!/usr/bin/python3
"""Script to list all City objects from hbtn_0e_14_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}')
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query cities joined with states to get state names, sorted by city id
    cities = session.query(City).join(State).order_by(City.id).all()

    for city in cities:
        print(f"{city.state.name}: ({city.id}) {city.name}")

    session.close()
