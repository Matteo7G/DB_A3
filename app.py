import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker, declarative_base
from db.init_db import reset_db
import datetime
import random
#from models import ...





# CRUD functions go here


# Data to insert
first_names = ("John", "Lincoln", "Hubert", "Stuart", "Anna", "Chris")
last_names = ("Carney", "McBeth", "Farrel", "Shefroy", "Frank", "Door")
email_ends = ("cmail.carleton.ca", "gmail.com", "hotmail.com", "yahoo.com", )

def generate_test_data(entries=5):
    random.seed(101)

    data = []
    emails = set()
    for i in range(entries):
        rand_fn = random.choice(first_names)
        rand_ln = random.choice(last_names)
        rand_date = datetime.date.today() - datetime.timedelta(days=random.randrange(365 * 5))
        for j in range(9):
            rand_email = rand_fn.lower() + rand_ln.lower() + ("" if j==0 else str(j)) + "@" + random.choice(email_ends)
            if rand_email not in emails:
                emails.add(rand_email)
                break
            if j == 4: return None
        data.append((rand_fn, rand_ln, rand_date, rand_email))
    return data



def main():
    DATABASE_URL = "postgresql+psycopg2://a_user:a_password@localhost/db_a3"

    engine = sa.create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    Base = declarative_base()

    gen_data = generate_test_data()
    if not gen_data:
        print("No entries generated; generating default 4")
        gen_data = [(
            first_names[i],
            last_names[i],
            datetime.date.today() - datetime.timedelta(days=random.randrange(20*i)),
            first_names[i][0] + last_names[i][0] + "@" + email_ends[i]
        ) for i in range(4)]


    reset_db(engine)


if __name__ == "__main__":
    main()
