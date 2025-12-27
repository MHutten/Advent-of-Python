import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))

from file import read_lines
from Matchsticks import calculate_encoded_length

def main() -> None:

    difference = 0

    for line in read_lines(sys.argv[1]):

        difference += calculate_encoded_length(line) - len(line)

    print(difference)

if __name__ == "__main__":
    main()