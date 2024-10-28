import sys


def main():
    """The program take a string as an argument and encodes\
it into Morse Code"""

    NESTED_MORSE = {
        " ": "/ ",
        "A": ".- ",
        "B": "-... ",
        "C": "-.-. ",
        "D": "-.. ",
        "E": ". ",
        "F": "..-. ",
        "G": "--. ",
        "H": ".... ",
        "I": ".. ",
        "J": ".--- ",
        "K": "-.- ",
        "L": ".-.. ",
        "M": "-- ",
        "N": "-. ",
        "O": "--- ",
        "P": ".--. ",
        "Q": "--.- ",
        "R": ".-. ",
        "S": "... ",
        "T": "- ",
        "U": "..- ",
        "V": "...- ",
        "W": ".-- ",
        "X": "-..- ",
        "Y": "-.-- ",
        "Z": "--.. ",
        "0": "----- ",
        "1": ".---- ",
        "2": "..--- ",
        "3": "...-- ",
        "4": "....- ",
        "5": "..... ",
        "6": "-.... ",
        "7": "--... ",
        "8": "---.. ",
        "9": "----. "
        }
    try:
        assert len(sys.argv) == 2, "the arguments are bad"
        assert all(
            c.isalnum() or c.isspace() for c in sys.argv[1]
            ), "the arguments are bad"
        str = ''
        for char in sys.argv[1].upper():
            str += NESTED_MORSE[char]
        print(str)
    except (AssertionError, KeyboardInterrupt) as error:
        print(error)


if __name__ == "__main__":
    main()
