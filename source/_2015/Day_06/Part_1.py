import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))

from file import read_lines
from Probably_a_Fire_Hazard import Lights, parse_operation_string

def main() -> None:

    lights = Lights(False)

    for string in read_lines(sys.argv[1]):

        operation, start, end = parse_operation_string(string)

        if operation == "on":

            lights.turn_on(start, end)

        elif operation == "toggle":

            lights.toggle(start, end)

        else:

            lights.turn_off(start, end)


    print(lights.get_number_of_lit_lights())

if __name__ == "__main__":
    main()