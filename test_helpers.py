"""
Test helper file
handles CRUD function testing and custom output/error message format
"""

#just prints errors in red
def err_print(msg):
    print(f"\033[31m{msg}\033[0m")

#just prints outputs in bright white
def out_print(msg):
    print(f"\033[1;97m{msg}\033[0m")

# tests a provided function and handles errors
def test_function(name, func, *args, silence=False):
    number_of_errors = 0
    if not silence: out_print(f"testing {name}")
    try:
        result = func(*args)
        if result:
            if not silence: out_print(f"function {name} returned success!")
        else:
            if not silence: err_print(f"function {name} returned failure..")
            number_of_errors = 1
    except Exception as e:
        if not silence: err_print(f"ERROR: Function {name} raised exception {e}")
        number_of_errors = 1
    finally:
        if not silence:
            input("Press Enter to continue...")
            print("\n")
        return number_of_errors