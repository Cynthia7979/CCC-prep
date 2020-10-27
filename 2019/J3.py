for i in range(int(input())):
    output_str = ''
    last_l = None
    count = 0
    for l in input():
        if not last_l:
            count = 1
            last_l = l
        elif last_l == l:
            count += 1
        else:
            output_str += f'{count} {last_l} '
            count = 1
            last_l = l
    output_str += f'{count} {last_l} '
    print(output_str[:-1])
