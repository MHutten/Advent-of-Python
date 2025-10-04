import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))

from file import read_lines
from Probably_a_Fire_Hazard import LightsWithBrightnessControls, parse_operation_string

def main() -> None:

    lights = LightsWithBrightnessControls(0)
    brightness = 0

    for string in read_lines(sys.argv[1]):

        operation, start, end = parse_operation_string(string)

        if operation == "on":

            brightness += lights.turn_on_ancient_nordic_elvish(start, end)

        elif operation == "toggle":

            brightness += lights.toggle_ancient_nordig_elvish(start, end)

        else:

            brightness -= lights.turn_off_ancient_nordic_elvish(start, end)


    print(brightness)

if __name__ == "__main__":
    main()