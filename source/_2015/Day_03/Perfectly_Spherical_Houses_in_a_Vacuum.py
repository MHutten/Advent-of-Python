def __update_location(char: str, current_location: list[int]) -> None:

    if char == '^':

        current_location[1] += 1

    elif char == 'v':

        current_location[1] -= 1

    elif char == '<':

        current_location[0] -= 1

    else: # i.e. if char == '>'

        current_location[0] += 1


def __update_visited_houses(current_location: list[int], visited_house_coordinates: dict[tuple[int, int], int]) -> None:

    current_location = tuple(current_location)

    if current_location in visited_house_coordinates.keys():

        visited_house_coordinates[current_location] += 1

    else:

        visited_house_coordinates[current_location] = 1


def calculate_number_of_visited_houses(instructions: str) -> int:

    current_location = [0, 0]
    visited_house_coordinates = {(0, 0): 1}

    for char in instructions:

        __update_location(char, current_location)
        __update_visited_houses(current_location, visited_house_coordinates)

    return len(visited_house_coordinates)

def calculate_number_of_visited_houses_with_robo_santa(instructions: str) -> int:

    current_location_santa = [0, 0]
    current_location_robo_santa = [0, 0]
    visited_house_coordinates = {(0, 0): 2}

    for id, char in enumerate(instructions):

        if id % 2 == 0:

            __update_location(char, current_location_santa)
            __update_visited_houses(current_location_santa, visited_house_coordinates)

        else: # i.e. id % 2 == 1:

            __update_location(char, current_location_robo_santa)
            __update_visited_houses(current_location_robo_santa, visited_house_coordinates)
            

    return len(visited_house_coordinates)