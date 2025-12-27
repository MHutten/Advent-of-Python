import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))

from file import read_lines
from I_Was_Told_There_Would_Be_No_Math import calculate_ribbon_length

def main() -> None:

    boxes = read_lines(sys.argv[1])

    ribbon_length = 0

    for box in boxes:
        length, width, height = map(int, box.split('x'))
        ribbon_length += calculate_ribbon_length(length, width, height)

    print(ribbon_length)

if __name__ == "__main__":
    main()