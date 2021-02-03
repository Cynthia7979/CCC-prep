import math

x0, y0 = [int(i) for i in input().split()]
x1, y1 = [int(i) for i in input().split()]


def next_positions(x, y):
    pos = []
    for delta_x in (2, -2):
        for delta_y in (1, -1):
            if 1 <= x+delta_x <= 8 and 1 <= y+delta_y <= 8:
                pos.append((x+delta_x, y+delta_y))
    for delta_x in (1, -1):
        for delta_y in (2, -2):
            if 1 <= x+delta_x <= 8 and 1 <= y+delta_y <= 8:
                pos.append((x+delta_x, y+delta_y))
    return pos


# Try Greedy
x_now, y_now = x0, y0
steps = 0

while (x_now, y_now) != (x1, y1):
    current_min = None
    current_min_distnce = None
    for x, y in next_positions(x_now, y_now):
        distance = math.sqrt((x1 - x) ** 2 + (y1 - y) ** 2)
        if current_min_distnce:
            if distance < current_min_distnce:
                current_min_distnce = distance
                current_min = (x, y)
        else:
            current_min_distnce = distance
            current_min = (x, y)
        if distance == 0:
            break
    x_now, y_now = current_min
    # print(x_now, y_now)
    steps += 1

print(steps)
