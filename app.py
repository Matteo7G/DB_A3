import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker, declarative_base
#from db.init_db import wipe_db
#from models import ...

DATABASE_URL = "postgresql+psycopg2://a_user:a_password@localhost/db_a3"

engine = sa.create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
Base = declarative_base()



# CRUD functions go here




def main():
    print("hello wrld")
    #

if __name__ == "__main__":
    main()
