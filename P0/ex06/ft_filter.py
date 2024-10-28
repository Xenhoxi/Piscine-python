def ft_filter(func, iterable):
    """Return an iterator yielding those items of iterable for which\
function(item) is true. If function is None, return the items that\
are true."""
    if not func:
        new_iterator = [item for item in iterable if item]
    else:
        new_iterator = [item for item in iterable if func(item)]
    yield new_iterator
