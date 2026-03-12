from ft_filter import ft_filter
import sys


def filterString(string, number):
    """
    Check if the length of a string is greater than a given number.

    Parameters:
        string (str): The string to check.
        number (int): The length threshold.

    Returns:
        bool: True if len(string) > number, False otherwise.
    """
    return (len(string) > number)


def main():
    """
    Filters words from a command-line string based on length.

    - Expects exactly 2 arguments: a string and a number.
    - Validates that the string contains only letters, digits, or spaces.
    - Converts the string into a list of words.
    - Uses ft_filter with filterString to select words longer than the number.
    - Prints the resulting list of words in a Python-style list format.
    - Prints an error if any validation fails.
    """
    try:
        assert len(sys.argv) == 3, "the arguments are bad"
        try:
            number = int(sys.argv[2])
        except ValueError:
            raise AssertionError("the arguments are bad")
        for c in sys.argv[1]:
            if c.isalpha() is False and c.isdigit() is False and c != ' ':
                raise AssertionError("Strings cannot "
                                     "contain any special characters "
                                     "(punctuation or invisible).")
        w = sys.argv[1].split()
        result = [x for x in ft_filter(lambda s: filterString(s, number), w)]

        i = 0
        print("[", end='')
        for words in result:
            if i > 0:
                print(", ", end='')
            print("'" + words + "'", end='')
            i += 1
        print("]")
    except KeyboardInterrupt as e:
        print(f"{type(e)}: {e}")
    except Exception as error:
        print(f"{type(error)}: {error}")
        return


if __name__ == "__main__":
    main()
