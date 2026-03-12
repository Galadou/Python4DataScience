import sys

try:
    assert len(sys.argv) <= 2, "more than one argument is provided"
    if (len(sys.argv) == 1):
        exit(1)
    try:
        number = int(sys.argv[1])
    except ValueError:
        raise AssertionError("argument is not an integer")

    if (number % 2 == 0):
        print("I'm Even.")
    else:
        print("I'm Odd.")
except KeyboardInterrupt as e:
    print(f"{type(e)}: {e}")
except Exception as error:
    print(f"{type(error)}: {error}")
