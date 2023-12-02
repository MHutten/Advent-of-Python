def get_required_square_feet_of_wrapping_paper(list_of_dimensions: str) -> int:
    square_feet_of_wrapping_paper: int = 0

    for line in list_of_dimensions.split('\n'):
        square_feet_of_wrapping_paper += get_square_feet_of_wrapping_paper_for_present(parse_dimensions_string(line))

    return square_feet_of_wrapping_paper

def parse_dimensions_string(box_dimensions: str) -> list[int]:
    result: list[int] = []

    for dimension in box_dimensions.split('x'):
        #print(dimension)
        result.append(10)

    return result

def get_square_feet_of_wrapping_paper_for_present(box_dimensions: list[int]) -> int:
    (l, w, h) = box_dimensions

    return 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)

# public static int getRequiredFeetOfRibbon(String listOfDimensions) {
#     Scanner scanner = new Scanner(listOfDimensions);
#     int feetOfRibbon = 0;

#     while (scanner.hasNextLine()) {
#         feetOfRibbon += getFeetOfRibbonForPresent(parseDimensionsString(scanner.nextLine()));
#     }

#     scanner.close();
#     return feetOfRibbon;
# }

# private static int getFeetOfRibbonForPresent(ArrayList<Integer> boxDimensions) {
#     int l = boxDimensions.get(0);
#     int w = boxDimensions.get(1);
#     int h = boxDimensions.get(2);

#     return l*w*h + Math.min(Math.min(2*l+2*w, 2*w+2*h), 2*h+2*l);
# }