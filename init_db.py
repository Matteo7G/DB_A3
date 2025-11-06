from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from random import seed, choice, randrange
from datetime import timedelta, date
from models import Base, Student

err_print = lambda msg: print(f"\033[31m{msg}\033[0m") #just prints errors in red


DEFAULT_DATA = (
    ('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
    ('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
    ('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02')
)
DATABASE_URL = "postgresql+psycopg2://a_user:a_password@localhost/db_a3"

engine = create_engine(DATABASE_URL)
Local_Session = sessionmaker(engine)


def reset_db(load_default_data=True):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    test_data = DEFAULT_DATA if load_default_data else custom_test_data(10)
    if len(test_data) == 0: return

    student_list = [Student(fn, ln, e, d) for fn, ln, e, d in test_data]
    with Local_Session() as session:
        if len(student_list) == 1: session.add(student_list[0])
        else: session.add_all(student_list)
        session.commit()


#loads custom data for testing
def custom_test_data(entries=10, s=101):
    seed(s)

    # Random data to insert
    first_names = ("John", "Lincoln", "Hubert", "Stuart", "Anna", "Chris")
    last_names = ("Carney", "McBeth", "Farrel", "Chefroy", "Frank", "Door")
    email_ends = ("cmail.carleton.ca", "gmail.com", "hotmail.com", "yahoo.com")

    data = []
    emails = set()
    for i in range(entries):
        rand_fn = choice(first_names)
        rand_ln = choice(last_names)
        rand_date = date.today() - timedelta(days=randrange(365 * 5))
        rand_email = ""
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