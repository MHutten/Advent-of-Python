dimensions = open('Day 2 I Was Told There Would Be No Math/input.txt', 'r')

feet_ribbon = 0

for box_dimensions in dimensions.readlines():
    (l, w, h) = box_dimensions.split('x')

    l = int(l)
    w = int(w)
    h = int(h)

    feet_ribbon += l*w*h + min(2*l+2*w, 2*w+2*h, 2*h+2*l)

print(feet_ribbon)