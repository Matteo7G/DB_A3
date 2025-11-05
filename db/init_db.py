import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker, declarative_base
#from models import orm_classes


def wipe_db():
    DATABASE_URL = "postgresql+psycopg2://a_user:a_password@localhost/db_a3"

    engine = sa.create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    Base = declarative_base()

    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    #...


#conect to and insert data into db


