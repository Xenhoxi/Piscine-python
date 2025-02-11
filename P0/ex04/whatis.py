import sys

try:
    assert len(sys.argv) < 3, "more than one argument is provided"
    assert len(sys.argv) > 1, "less than one argument is provided"
    try:
        int(sys.argv[1])
    except ValueError:
        assert 0, "Value is not a integer !"
    if int(sys.argv[1]) % 2 == 0:
        print("I'm Odd.")
    else:
        print("I'm Even.")
except AssertionError as msg:
    print(msg)
