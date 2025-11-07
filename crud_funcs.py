"""
MATTEO GUERRA's CRUD function file
handles all the CRUD operation functions for database
"""

from models_db import Student
from init_db import Local_Session
from sqlalchemy import select
from test_helpers import out_print, err_print


# CRUD functions:
# displays and returns all current entries in the student table
def getAllStudents():
    query_get_all = select(Student).order_by(Student.student_id)
    with Local_Session() as session:
        students = session.scalars(query_get_all).all()
        if not students:
            out_print("No students found.")
            return None
        out_print(f"Found {len(students)} students in database: ")
        for s in students:
            out_print(f" {s}")
        return students

# adds a new entry to student table (if allowed)
def addStudent(first_name, last_name, email, enrollment_date):
    with Local_Session() as session:
        query_email_exists = select(Student).where(Student.email == email)
        if session.scalars(query_email_exists).first():
            err_print(f"Student with email {email} already exists.")
            return None
        new_student = Student(first_name, last_name, email, enrollment_date)
        session.add(new_student)
        session.commit()
        out_print(f"Successfully added new student {new_student}")
    return new_student

# Updates the email of a student with specified student_id
def updateStudentEmail(student_id, new_email):
    with Local_Session() as session:
        student = session.get(Student, student_id)
        if not student:
            err_print(f"No student found with ID {student_id}")
            return None
        student.email = new_email
        session.commit()
        out_print(f"Successfully updated student with ID {student_id} with new email {new_email}")
    return student

# Deletes the entry of a student with specified student_id
def deleteStudent(student_id):
    with Local_Session() as session:
        student = session.get(Student, student_id)
        if not student:
            err_print(f"No student found with ID {student_id}")
            return None
        session.delete(student)
        session.commit()
        out_print(f"Successfully deleted student with ID {student_id}")
    return student

