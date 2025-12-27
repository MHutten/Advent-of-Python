import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))

from file import read_lines
from Doesnt_He_Have_Inter_Elves_For_This import is_nice_now

def main() -> None:

    number_of_nice_strings = 0

    for string in read_lines(sys.argv[1]):

        if is_nice_now(string):
            number_of_nice_strings += 1

    print(number_of_nice_strings)

if __name__ == "__main__":
    main()