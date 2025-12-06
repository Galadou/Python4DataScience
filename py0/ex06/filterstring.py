from ft_filter import ft_filter
import sys


def filterString(string, number):
    if (len(string) > number):
        return True
    else:
        return False


def main():
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

    except Exception as error:
        print(f"{type(error)}: {error}")
        return


if __name__ == "__main__":
    main()
