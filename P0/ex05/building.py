import sys


def main():
    """Takes a single string argument and displays the sums of its \
upper-case characters, lower-case\
characters, punctuation characters, digits and spaces."""
    try:
        assert len(sys.argv) < 3, "Wrong numbers of arguments"
        string = ''
        if len(sys.argv) == 1:
            print('What is the text to count?')
            string = input()
        else:
            string = sys.argv[1]
        print(f"The text contains {len(string)} characters:")
        print(f"{len(list(filter(isUpper, string)))} upper letters")
        print(f"{len(list(filter(isLower, string)))} lower letters")
        print(f"{len(list(filter(isPonctuation, string)))} ponctuation marks")
        print(f"{string.count(' ')} spaces")
        print(f"{len(list(filter(isDigit, string)))} digits")
    except (AssertionError, Exception, KeyboardInterrupt) as msg:
        print(msg)


def isUpper(char):
    """Return true if the param is uppercase"""
    if char >= 'A' and char <= 'Z':
        return True
    return False


def isLower(char):
    """Return true if the param is lowercase"""
    if char >= 'a' and char <= 'z':
        return True
    return False


def isDigit(char):
    """Return true if the param is a digit"""
    if char >= '0' and char <= '9':
        return True
    return False


def isPonctuation(char):
    """Return true if the param is a ponctuation mark"""
    if char in "!#$%&'()*+,-./:;<=>?@[\\]^_{|}~)" or char == '"':
        return True
    return False


if __name__ == "__main__":
    main()
