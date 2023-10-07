instructions = open('Day 3 Perfectly Spherical Houses in a Vacuum/input.txt', 'r')

current_location_santa: tuple[int, int] = (0, 0)
current_location_robo_santa: tuple[int, int] = (0, 0)
visited_house_coordinates: dict[(int, int), int] = {
    (0, 0): 2
}

def handle_instruction(char: str, current_location: tuple[int, int]) -> tuple[int, int]:
    if char == '^':
        current_location = (current_location[0], current_location[1] + 1)
    elif char == 'v':
        current_location = (current_location[0], current_location[1] - 1)
    elif char == '<':
        current_location = (current_location[0] - 1, current_location[1])
    else: # i.e. if char == '>'
        current_location = (current_location[0] + 1, current_location[1])

    if current_location in visited_house_coordinates.keys():
        visited_house_coordinates[current_location] += 1
    else:
        visited_house_coordinates[current_location] = 1

    return current_location

for id, char in enumerate(instructions.read()):
    if id % 2 == 0:
        current_location_santa = handle_instruction(char, current_location_santa)
    else: # i.e. id % 2 == 1:
        current_location_robo_santa = handle_instruction(char, current_location_robo_santa)

print(len(visited_house_coordinates))