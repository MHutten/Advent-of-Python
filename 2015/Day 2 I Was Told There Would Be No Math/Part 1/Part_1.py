dimensions = open('Day 2 I Was Told There Would Be No Math/input.txt', 'r')

square_feet_wrapping_paper = 0

for box_dimensions in dimensions.readlines():
    (l, w, h) = box_dimensions.split('x')

    l = int(l)
    w = int(w)
    h = int(h)

    square_feet_wrapping_paper += 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)

print(square_feet_wrapping_paper)