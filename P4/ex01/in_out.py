def square(x: int | float) -> int | float:
    """Return the square of x"""
    return (x ** 2)


def pow(x: int | float) -> int | float:
    """Return the pow of x"""
    return (x ** x)


def outer(x: int | float, function) -> object:
    """Returns the result of the arguments calculation"""
    count = 0

    def inner() -> float:
        nonlocal count
        if count == 0:
            count = x
        count = function(count)
        return count
    return inner
