from models import Student
from init_db import Local_Session
from sqlalchemy import select

err_print = lambda msg: print(f"\033[31m{msg}\033[0m") #just prints errors in red
out_print = lambda msg: print(f"\033[1;97m{msg}\033[0m") #just prints outputs in bright white


# CRUD functions:
def getAllStudents():
    query_get_all = select(Student).order_by(Student.student_id)
    with Local_Session() as session:
        students = session.scalars(query_get_all).all()
        if not students:
            err_print("No students found.")
            return None
        out_print(f"Found {len(students)} students in database: ")
        for s in students:
            out_print(f" {s}")
        return students

def addStudent(first_name, last_name, email, enrollment_date):
    with Local_Session() as session:
        query_email_exists = select(Student).where(Student.email == email)
        if session.scalars(query_email_exists).first():
            err_print(f"Student with email {email} already exists.")
            return 1
        new_student = Student(first_name, last_name, email, enrollment_date)
        session.add(new_student)
        session.commit()
        out_print(f"Successfully added new student {new_student}")
    return new_student


def updateStudentEmail(student_id, new_email):
    with Local_Session() as session:
        student = session.get(Student, student_id)
        if not student:
            err_print(f"No student found with ID {student_id}")
            return 1
        student.email = new_email
        session.commit()
        out_print(f"Successfully updated student with ID {student_id} with new email {new_email}")
    return 0


def deleteStudent(student_id):
    with Local_Session() as session:
        student = session.get(Student, student_id)
        if not student:
            err_print(f"No student found with ID {student_id}")
            return 1
        session.delete(student)
        session.commit()
        out_print(f"Successfully deleted student with ID {student_id}")
    return 0

