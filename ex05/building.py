import sys


def main():
    if len(sys.argv) > 2:
        print("AssertionError")
        return 1
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


def isUpper(char):
    if char >= 'A' and char <= 'Z':
        return True
    return False


def isLower(char):
    if char >= 'a' and char <= 'z':
        return True
    return False


def isDigit(char):
    if char >= '0' and char <= '9':
        return True
    return False


def isPonctuation(char):
    if char in "!#$%&'()*+,-./:;<=>?@[\\]^_{|}~)" or char == '"':
        return True
    return False


if __name__ == "__main__":
    main()
