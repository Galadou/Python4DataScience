def ft_filter(function, iterable):
    """
    Filters elements from an iterable using a provided function.

    - Yields only the items for which function(item) returns True.
    - Behaves like the built-in filter() function.
    """
    for item in iterable:
        if (function(item)):
            yield (item)
