from ft_filter import ft_filter
import sys


def main():
    """The program output a list of words from S that have a length greater \
than N."""
    try:
        assert len(sys.argv) == 3, "the arguments are bad"
        assert all(
            c.isalnum() or c.isspace() for c in sys.argv[1]
            ), "the arguments are bad"
        assert sys.argv[2].isdigit(), "the arguments are bad"
        S = sys.argv[1]
        N = int(sys.argv[2])
        result = ft_filter(lambda S: True if len(S) > N else False, S.split())
        for i in result:
            print(i)
    except (AssertionError, KeyboardInterrupt) as error:
        print("Assertion Error:", error)


if __name__ == "__main__":
    main()
