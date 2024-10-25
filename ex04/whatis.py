import sys

if len(sys.argv) != 2:
    print("AssertionError:", "more than one argument is provided")
elif not sys.argv[1].isnumeric():
    print("AssertionError:", "argument is not an integer")
else:
    if int(sys.argv[1]) % 2 == 0:
        print("I'm Odd.")
    else:
        print("I'm Even.")
