import sys


def main():
    """Takes a single string argument and displays the sums of its \
upper-case characters, lower-case\
characters, punctuation characters, digits and spaces."""
    try:
        assert len(sys.argv) < 3, "Wrong numbers of arguments"
        string = ''
        if len(sys.argv) == 1:
            print("What is the text to count?")
            string = sys.stdin.readline()
            if not string.endswith("\n"):
                print("")
        else:
            string = sys.argv[1]
        print(f"The text contains {len(string)} characters:")
        print(f"{sum(1 for c in string if c.isupper())} upper letters")
        print(f"{sum(1 for c in string if c.islower())} lower letters")
        print(f"{len(list(filter(isPonctuation, string)))} ponctuation marks")
        print(sum(1 for c in string if c.isspace()), "spaces")
        print(f"{sum(1 for c in string if c.isdigit())} digits")
    except (AssertionError, Exception, KeyboardInterrupt) as msg:
        print(msg)


def isPonctuation(char):
    """Return true if the param is a ponctuation mark"""
    if char in "!#$%&'()*+,-./:;<=>?@[\\]^_{|}~)" or char == '"':
        return True
    return False


if __name__ == "__main__":
    main()
