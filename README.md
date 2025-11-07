# COMP 3005 | Assignment 3

A Python application for performing specific CRUD (
Create, Read, Update, Delete) operations on a PostgreSQL 
database using SQLAlchemy.

### CRUD functions:
- **getAllStudents()**: Retrieves and displays all records from the students table.
- **addStudent(first_name, last_name, email, enrollment_date)**: Inserts a new student record into the students table.
- **updateStudentEmail(student_id, new_email)**: Updates the email address for a student with the specified student_id.
- **deleteStudent(student_id)**: Deletes the record of the student with the specified student_id.

---

### Steps to Compile and Run
1. Ensure PostgreSQL, Python, and Git are installed
2. Clone Git repository
3. Install dependencies from requirements.txt
4. Create a new database on PostgreSQL through command line
   - login: `sudo -u postgres psql`
   - create user: `CREATE USER a_user WITH PASSWORD 'a_password';`
   - create database: `CREATE DATABASE db_a3 OWNER a_user;`
   - exit: `\q`
5. Modify line 26 of init_db for your database:
   - `DATABASE_URL = "postgresql+psycopg2://a_user:a_password@localhost/db_a3"`
   - change `a_user` to your username
   - change `a_password` to your password
   - change `db_a3` if you used another database name
6. And finally the program is ready to run
   - Through an IDE: should be able to directly execute app.py 
   - Through command line: enter `python app.py`

