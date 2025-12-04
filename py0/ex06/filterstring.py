from ft_filter import ft_filter
import sys

number = 0

def filterString(string, number):
    if (len(string) > number):
        return True
    else:
        return False

def main():
    try:
        assert len(sys.argv) == 3, "This program accept only 2 arguments."
        try: 
            number = int(sys.argv[2])
        except ValueError:
            raise AssertionError("argument is not an integer")
        words = sys.argv[1].split()

        result = ft_filter(lambda w :filterString(w, number), words)
        print(result)
    except Exception as error:
        print(f"{type(error)}: {error}")
        return
    

if __name__ == "__main__":
    main()

    #FONCTIONNE PAS