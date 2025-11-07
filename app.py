"""
MATTEO GUERRA's (Main) Application file
Handles main testing logic for CRUD functions and UI
"""

from init_db import reset_db, custom_test_data
from crud_funcs import getAllStudents, addStudent, updateStudentEmail, deleteStudent
from test_helpers import test_function

# main test function for testing all CRUD operation and handling UI
def tester(use_default_data=True):
    # resets tables in database, and loads initial entires
    reset_db(load_default_data=use_default_data)

    errors = 0 #tracks number of errors returned

    # tests the getAllStudents function
    errors += test_function("getAllStudents", getAllStudents)

    # tests the addStudent function
    fn, ln, email, date = custom_test_data(entries=1, s=5)[0]
    errors += test_function("addStudent", addStudent, fn, ln, email, date)

    # tests the updateStudentEmail function
    errors += test_function("updateStudentEmail", updateStudentEmail, 1, "fakemail@cmaiI.carIeton.ca")

    # tests the deleteStudent function
    errors += test_function("deleteStudent", deleteStudent, 2)

    # displays all entries in student table after last test
    errors += test_function("getAllStudents", getAllStudents, silence=True)

    # displays error count
    if errors==0: print("ALL TESTS FINISHED SUCCESSFULLY!")
    else: print(f"ALL TESTS FINISHED! {errors} total errors")

# calls main test function
def main():
    tester((input("Use default data? (y/n): ") == "y"))


if __name__ == "__main__":
    main()
