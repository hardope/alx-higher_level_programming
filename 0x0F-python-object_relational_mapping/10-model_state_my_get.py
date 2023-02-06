#!/usr/bin/python3
"""
Prints the State object with the name passed as argument
from the database hbtn_0e_6_usa
"""

if __name__ == "__main__":
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    from model_state import Base, State
    from sys import argv
    import re

    if (len(argv) != 5):
        print('Use: username, password, database_name, state')
        exit(1)

    searched = ' '.join(argv[4].split())

    if (re.search('^[a-zA-Z ]+$', searched) is None):
        print('Enter a valid name state (example: Arizona)')
        exit(1)

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).where(State.name == searched)

    if (states.count() == 0):
        print('Not found')
    else:
        for row in states:
            print(row.id)
    session.close()
