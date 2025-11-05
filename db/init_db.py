import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker, declarative_base
from models import Base, Student


def reset_db(engine, test_data=None):
    Session = sessionmaker(bind=engine)
    Base = declarative_base()

    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    #...

def add_test_data()

#conect to and insert data into db


