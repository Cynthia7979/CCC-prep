# from pprint import pprint
# This code SHOULD work pretty well, except that it's too slow...


def find_notx(l):
    for ind, ele in enumerate(l):
        if ele != 'X':
            return ind, ele


def get_comn_diff(l):
    # print('Get comn diff of', l)
    pair = []
    last_i = None
    for index, c in enumerate(l):
        if len(pair) == 2: break
        if c != 'X':
            pair.append(c)
            if last_i!=None:
                dist = index - last_i
            else:
                last_i = index
    # print('dist', dist, 'pair', pair)
    comn_diff = (pair[1]-pair[0])/dist
    # print('Comn_diff:', comn_diff)
    return comn_diff


grid = []
for i in range(3):
    grid.append([int(a) if a != 'X' else 'X' for a in input().split()])
all_ = [grid[x][y] for x in range(3) for y in range(3)]

while all_.count('X') > 0:
    for i, row in enumerate(grid):
        rowxs = row.count('X')
        # print('Row', row)
        if rowxs == 0:
            continue
        for cell_ind, cell in enumerate(row):
            # print('Cell', i, cell_ind, cell)
            if cell == 'X':
                if rowxs == 1:
                    cmn_diff = get_comn_diff(row)
                    num_ind, avl_num = find_notx(row)
                    grid[i][cell_ind] = int(avl_num + cmn_diff * (cell_ind-num_ind))
                elif rowxs >= 2:
                    column = [r[cell_ind] for r in grid]
                    # print('Column', column)
                    columnxs = column.count('X')
                    if columnxs == 1:
                        cmn_diff = get_comn_diff(column)
                        num_ind, avl_num = find_notx(column)
                        grid[i][cell_ind] = int(avl_num + cmn_diff * (i - num_ind))
                    elif columnxs == 2 and all_.count('X') >= 6:
                        avl_list = []
                        for m in range(3):
                            for n in range(3):
                                if grid[n][m] != 'X':
                                    avl_list.append(grid[n][m])
                        cmn_diff = get_comn_diff(avl_list)
                        num_ind, avl_num = find_notx(column)
                        grid[i][cell_ind] = int(avl_num + cmn_diff * (cell_ind - num_ind))
                    else:
                        pass
                # pprint(grid, width=30)
            all_ = [grid[x][y] for x in range(3) for y in range(3)]
for row_ in grid:
    print(' '.join([str(ele) for ele in row_]))
