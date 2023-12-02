def follow_direction(direction: str) -> int:
    if direction == '(':
        return 1
    if direction == ')':
        return -1

def get_santas_destination(directions: str) -> int:
    floor: int = 0

    for direction in directions:
        floor += follow_direction(direction)

    return floor

def santa_enters_basement_at(directions: str) -> int:
    floor: int = 0
    instruction_count: int = 0

    for direction in directions:
        floor += follow_direction(direction)
        instruction_count += 1
        if floor == -1:
            return instruction_count

    return -1