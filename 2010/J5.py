import math


def main():
    x0, y0 = [int(i) for i in input().split()]
    x1, y1 = [int(i) for i in input().split()]

    if (x0, y0) == (x1, y1):
        print(0)
        return

    # Try Greedy
    x_now, y_now = x0, y0
    steps = 0

    while (x_now, y_now) != (x1, y1):
        current_min = None
        current_min_distnce = None
        found = False
        for delta_x in (2, -2):
            if found: break
            for delta_y in (1, -1):
                x, y = x_now+delta_x, y_now+delta_y
                if 1 <= x <= 8 and 1 <= y <= 8:
                    distance = math.sqrt((x1 - x) ** 2 + (y1 - y) ** 2)
                    if current_min_distnce:
                        if distance < current_min_distnce:
                            current_min_distnce = distance
                            current_min = (x, y)
                    else:
                        current_min_distnce = distance
                        current_min = (x, y)
                    if distance == 0:
                        found = True
                        break

        for delta_x in (1, -1):
            if found: break
            for delta_y in (2, -2):
                x, y = x_now+delta_x, y_now+delta_y
                if 1 <= x <= 8 and 1 <= y <= 8:
                    distance = math.sqrt((x1 - x) ** 2 + (y1 - y) ** 2)
                    if current_min_distnce:
                        if distance < current_min_distnce:
                            current_min_distnce = distance
                            current_min = (x, y)
                    else:
                        current_min_distnce = distance
                        current_min = (x, y)
                    if distance == 0:
                        found = True
                        break

        x_now, y_now = current_min
        # print(x_now, y_now)
        steps += 1

    print(steps)


if __name__ == '__main__':
    main()
