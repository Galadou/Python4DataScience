def ft_filter(function, iterable):
    for item in iterable:
        if (function(item)):
            yield (item)
