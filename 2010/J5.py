import math

came = [[0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, ]
        ]


def move(current_x, current_y, target_x, target_y, steps):
    all_steps = []
    for delta_x, delta_y in ((1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)):
        new_x = current_x + delta_x
        new_y = current_y + delta_y
        if 1 <= new_x <= 8 and 1 <= new_y <= 8:
            if not came[new_x-1][new_y-1]:
                steps += 1
                if (new_x, new_y) == (target_x, target_y):
                    all_steps.append(steps)
                    return all_steps
                else:
                    all_steps += move(new_x, new_y, target_x, target_y, steps)
            else:
                all_steps.append(steps)
                return all_steps
    return all_steps


def main():
    x0, y0 = [int(i) for i in input().split()]
    x1, y1 = [int(i) for i in input().split()]

    if (x0, y0) == (x1, y1):
        print(0)
        return

    # Recursive approach
    print(min(move(x0, y0, x1, y1, 0)))

    # Try Greedy
    # x_now, y_now = x0, y0
    # steps = 0
    #
    # while (x_now, y_now) != (x1, y1):
    #     current_min = None
    #     current_min_distnce = None
    #     found = False
    #     for delta_x in (2, -2):
    #         if found: break
    #         for delta_y in (1, -1):
    #             x, y = x_now+delta_x, y_now+delta_y
    #             if 1 <= x <= 8 and 1 <= y <= 8:
    #                 distance = math.sqrt((x1 - x) ** 2 + (y1 - y) ** 2)
    #                 if current_min_distnce:
    #                     if distance < current_min_distnce:
    #                         current_min_distnce = distance
    #                         current_min = (x, y)
    #                 else:
    #                     current_min_distnce = distance
    #                     current_min = (x, y)
    #                 if distance == 0:
    #                     found = True
    #                     break
    #
    #     for delta_x in (1, -1):
    #         if found: break
    #         for delta_y in (2, -2):
    #             x, y = x_now+delta_x, y_now+delta_y
    #             if 1 <= x <= 8 and 1 <= y <= 8:
    #                 distance = math.sqrt((x1 - x) ** 2 + (y1 - y) ** 2)
    #                 if current_min_distnce:
    #                     if distance < current_min_distnce:
    #                         current_min_distnce = distance
    #                         current_min = (x, y)
    #                 else:
    #                     current_min_distnce = distance
    #                     current_min = (x, y)
    #                 if distance == 0:
    #                     found = True
    #                     break
    #
    #     x_now, y_now = current_min
    #     # print(x_now, y_now)
    #     steps += 1


if __name__ == '__main__':
    main()
