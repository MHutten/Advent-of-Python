import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))

from file import read
from Perfectly_Spherical_Houses_in_a_Vacuum import calculate_number_of_visited_houses_with_robo_santa

def main() -> None:

    print(calculate_number_of_visited_houses_with_robo_santa(read(sys.argv[1])))

if __name__ == "__main__":
    main()