INDENT = '    '
rowMax, colMax = int(input()), int(input())
grid = []
catalog = {}
for i in range(rowMax):
    row = [int(s) for s in input().split()]
    grid.append(row)
    for j, room in enumerate(row):
        try:
            catalog[room].append((i,j))
        except KeyError:
            catalog[room] = [(i,j)]
# print(catalog)


# Find the path backwards
def go_through(value, call_no=0, last_coord=None):
    found = False
    # print(f'{call_no*INDENT}. Finding path for value =', value)
    try:
        for coord in catalog[value]:
            if coord == last_coord:
                # print(f'{call_no*INDENT}. Passing repeated coord:', coord)
                continue
            if found:
                return True

            # print(f'{call_no * INDENT}. Coord =', coord)
            if coord == (0,0):
                # print(f'{call_no*INDENT}. found.')
                return True
            elif not found:
                # print(f'{call_no*INDENT}. Passing {coord[0]+1}*{coord[1]+1}={(coord[0]+1)*(coord[1]+1)}')
                found = go_through((coord[0]+1)*(coord[1]+1), call_no=call_no+1)
    except KeyError:
        # print(f'{call_no*INDENT}. Path dead.')
        return False
    return found


print('yes' if go_through(rowMax*colMax) else 'no')
