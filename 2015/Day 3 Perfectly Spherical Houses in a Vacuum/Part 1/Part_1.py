instructions = open('Day 3 Perfectly Spherical Houses in a Vacuum/input.txt', 'r')

current_location: tuple[int, int] = (0, 0)
visited_house_coordinates: dict[(int, int), int] = {
    (0, 0): 1
}

for char in instructions.read():
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

print(len(visited_house_coordinates))