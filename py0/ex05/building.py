import sys

def main():
    try:
        assert len(sys.argv) <= 2, "more than one argument is provided"
        if (len(sys.argv)) == 1:
            text = input()
        else:
            text = sys.argv[1]

        upper = 0
        lower = 0
        space = 0
        dot = 0
        digit = 0
        char = 0
        for character in text:
            char += 1
            if (character.isupper()):
                upper += 1
            elif (character.islower()):
                lower += 1
            if (character.isdecimal()):
                digit += 1
            if (character.isspace()):
                space += 1
            if (character == '.' or character == ','):
                dot += 1
        print(f"The text conatins {char} characters:")
        print(f"{upper} upper letters")
        print(f"{lower} lower letters")
        print(f"{dot} punctuation marks")
        print(f"{space} spaces")
        print(f"{digit} digits")
    except Exception as error:
        print(f"{type(error)}: {error}")
        return

if __name__ == "__main__":
    main()
