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
        assert sys.argv[2].isdigit(), "the argument are bad"
        S = sys.argv[1]
        N = int(sys.argv[2])
        print(
            list(ft_filter(lambda S: True if len(S) > N else False, S.split()))
            )
    except (AssertionError, KeyboardInterrupt) as error:
        print(error)


if __name__ == "__main__":
    main()
