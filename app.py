from init_db import reset_db, custom_test_data
from crud_funcs import getAllStudents, addStudent, updateStudentEmail, deleteStudent

err_print = lambda msg: print(f"\033[31m{msg}\033[0m") #just prints errors in red
out_print = lambda msg: print(f"\033[1;97m{msg}\033[0m") #just prints outputs in bright white


def test_function(name, func, *args):
    out_print(f"testing {name}")
    try:
        result = func(*args)
        if result:
            out_print(f"function {name} returned success!\n")
        else:
            err_print(f"function {name} returned failure..\n")
    except Exception as e:
        err_print(f"ERROR: Function {name} raised exception {e}\n")

def main(use_default_data=True):
    # resets tables in database, and loads initial entires
    reset_db(load_default_data=use_default_data)

    # tests CRUD functions here:
    test_function("getAllStudents", getAllStudents)

    fn, ln, email, date = custom_test_data(entries=1, s=5)
    test_function("addStudent", addStudent, fn, ln, email, date)

    test_function("updateStudentEmail", updateStudentEmail, 1, "fakemail@cmaiI.carIeton.ca")

    test_function("deleteStudent", deleteStudent, 2)


if __name__ == "__main__":
    main()
