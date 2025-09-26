def __follow_direction(direction: str) -> int:
    if direction == '(':
        return 1
    if direction == ')':
        return -1

def calculate_santas_final_destination(directions: str) -> int:
    floor: int = 0

    for direction in directions:
        floor += __follow_direction(direction)

    return floor

def calculate_basement_entering_instruction_position(directions: str) -> int:
    floor: int = 0
    instruction_count: int = 0

    for direction in directions:
        floor += __follow_direction(direction)
        instruction_count += 1
        if floor == -1:
            return instruction_count

    return -1