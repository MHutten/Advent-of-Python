directions = open('Day 1 Not Quite Lisp/input.txt', 'r')

floor = 0
instruction_count = 0

for char in directions.read():
    if char == '(':
        floor += 1
    else: # i.e. if char == ')'
        floor -= 1

    instruction_count += 1

    if floor == -1:
        break

print(instruction_count)