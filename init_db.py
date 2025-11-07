"""
MATTEO GUERRA's Database initialization file
Handles database connection/setup
Resets database and re-populates using default or custom test data
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from random import seed, choice, randrange
from datetime import timedelta, date
from models_db import Base, Student
from test_helpers import err_print

# Default student data from assignment specifications
DEFAULT_DATA = [
    ('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
    ('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
    ('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02')
]

#URL to database where:
# - a_user is your username
# - a_password is your password
# - localhost is the location of the database
# - db_a3 is the name of the database
DATABASE_URL = "postgresql+psycopg2://matteo:matteo_password@localhost/test_db"

engine = create_engine(DATABASE_URL) #connects to database
Local_Session = sessionmaker(engine) #initialies function to create sessions

# Resets the database by dropping and recreating all tables
# and then populating them either the default or custom data
def reset_db(load_default_data=True):
    Base.metadata.drop_all(engine) #drops existing tables
    Base.metadata.create_all(engine) #recreates tables

    test_data = DEFAULT_DATA if load_default_data else custom_test_data(10)
    if not test_data:
        return

    # re-populates tables with test data
    student_list = [Student(fn, ln, e, d) for fn, ln, e, d in test_data]
    with Local_Session() as session:
        session.add_all(student_list)
        session.commit()


#loads random custom data for testing
def custom_test_data(entries=10, s=101):
    if s: seed(s) #sets random seed value for consistent testing

    # Random data to insert
    first_names = ("John", "Lincoln", "Hubert", "Stuart", "Anna", "Chris")
    last_names = ("Carney", "McBeth", "Farrel", "Chefroy", "Frank", "Door")
    email_ends = ("cmail.carleton.ca", "gmail.com", "hotmail.com", "yahoo.com")

    data, emails = [], set()
    #each loop creates a new entry, entries parameter specifies number of loops
    for i in range(entries):
        rand_fn = choice(first_names)
        rand_ln = choice(last_names)
        rand_date = date.today() - timedelta(days=randrange(365 * 5))
        rand_email = ""
        #logic loop to ensure emails are unique
        for j in range(10):
            rand_email = f"{rand_fn.lower()}.{rand_ln.lower()}{('' if j==0 else str(j))}@{choice(email_ends)}"
            if rand_email not in emails:
                emails.add(rand_email)
                break
            if j==9:
                err_print("MAX ITERATIONS REACHED")
                rand_email = f"email{i}@email.com"
        data.append((rand_fn, rand_ln, rand_email, rand_date))

    return data