import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))

from file import read_lines
from I_Was_Told_There_Would_Be_No_Math import calculate_area_of_wrapping_paper

def main() -> None:

    boxes = read_lines(sys.argv[1])

    area_of_wrapping_paper = 0

    for box in boxes:
        length, width, height = map(int, box.split('x'))
        area_of_present = calculate_area_of_wrapping_paper(length, width, height)
        area_of_wrapping_paper += area_of_present
        print("dimensions: {} length: {} width: {} height: {} area_of_present: {} area_of_wrapping_paper: {}".format(box[:-1], length, width, height, area_of_present, area_of_wrapping_paper))

    print(area_of_wrapping_paper)

if __name__ == "__main__":
    main()