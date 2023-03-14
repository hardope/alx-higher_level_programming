#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa
"""

if __name__ == "__main__":
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    from model_state import Base, State
    from model_city import City
    from sys import argv

    if (len(argv) != 4):
        print('Use: username, password database_name')
        exit(1)

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State, City.id, City).filter(
        City.state_id == State.id).order_by(City.id).all()

    for row in result:
        print(f'{row.State.name}: ({row.id}) {row.City.name}')
    session.close()
