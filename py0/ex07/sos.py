import sys


def main():
    try:
        if len(sys.argv) != 2:
            raise AssertionError("the arguments are bad")
        for c in sys.argv[1]:
            if c.isalpha() is False and c.isdigit() is False and c != ' ':
                raise AssertionError("the arguments are bad")
        NESTED_MORSE = {
            " ": "/",
            "A": ".-",
            "B": "-...",
            "C": "-.-.",
            "D": "-..",
            "E": ".",
            "F": "..-.",
            "G": "--.",
            "H": "....",
            "I": "..",
            "J": ".---",
            "K": "-.-",
            "L": ".-..",
            "M": "--",
            "N": "-.",
            "O": "---",
            "P": ".--.",
            "Q": "--.-",
            "R": ".-.",
            "S": "...",
            "T": "-",
            "U": "..-",
            "V": "...-",
            "W": ".--",
            "X": "-..-",
            "Y": "-.--",
            "Z": "--..",
            "0": "-----",
            "1": ".----",
            "2": "..---",
            "3": "...--",
            "4": "....-",
            "5": ".....",
            "6": "-....",
            "7": "--...",
            "8": "---..",
            "9": "----.",
            }
        str = sys.argv[1].upper()

        i = 0
        for c in str:
            if i > 0:
                print(' ', end='')
            print(NESTED_MORSE[c], end='')
            i = 1
        print()
    except Exception as error:
        print(f"{type(error)} : {error}")


if __name__ == "__main__":
    main()
