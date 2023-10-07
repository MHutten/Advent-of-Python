directions = open('Day 1 Not Quite Lisp/input.txt', 'r')

floor = 0

for char in directions.read():
    if char == '(':
        floor += 1
    else: # i.e. if char == ')'
        floor -= 1

print(floor)