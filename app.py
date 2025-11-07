from init_db import reset_db, custom_test_data
from crud_funcs import getAllStudents, addStudent, updateStudentEmail, deleteStudent

err_print = lambda msg: print(f"\033[31m{msg}\033[0m") #just prints errors in red
out_print = lambda msg: print(f"\033[1;97m{msg}\033[0m") #just prints outputs in bright white

number_of_errors = 0

def test_function(name, func, *args):
    global number_of_errors
    out_print(f"testing {name}")
    try:
        result = func(*args)
        if result:
            out_print(f"function {name} returned success!")
        else:
            err_print(f"function {name} returned failure..")
            number_of_errors+=1
    except Exception as e:
        err_print(f"ERROR: Function {name} raised exception {e}")
    finally:
        input("Press Enter to continue...")
        print("\n")

def main(use_default_data=True):
    # resets tables in database, and loads initial entires
    reset_db(load_default_data=use_default_data)
    global number_of_errors
    number_of_errors = 0

    # tests CRUD functions here:
    test_function("getAllStudents", getAllStudents)

    fn, ln, email, date = custom_test_data(entries=1, s=5)[0]
    test_function("addStudent", addStudent, fn, ln, email, date)

    test_function("updateStudentEmail", updateStudentEmail, 1, "fakemail@cmaiI.carIeton.ca")

    test_function("deleteStudent", deleteStudent, 2)

    getAllStudents()
    if number_of_errors==0: print("ALL TESTS FINISHED SUCCESSFULLY!")
    else: print("ALL TESTS FINISHED!")

if __name__ == "__main__":
    val = input("Use default data? (y/n): ")
    main((val == "y"))
