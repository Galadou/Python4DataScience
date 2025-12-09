def count_in_list(lists, str):
    """Counts the number of occurrences of a string within a list.

    The function checks if the first argument is a list and raises an
    AssertionError if it is not.

    Args:
        lists (list): The list in which to search.
        str (str): The string element to count.

    Returns:
        int: The total number of times the string appears in the list.

    Raises:
        AssertionError: If the first argument (`lists`) is not a list.
    """
    if type(lists) is not list:
        raise AssertionError("the arguments are bad")
    return lists.count(str)
