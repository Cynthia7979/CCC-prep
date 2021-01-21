"""
Fewest numbers of days = ceil(N/K)
Maximum number of attractions per day = K,
Minimum number of attractions per day = N % K

N=5, K=3:
    ceil(5/3)=2
    2,3
    3,2

N=5, K=2:
    ceil(5/2)=3
    1,2,2
    2,2,1

N=7, K=3:
    ceil(7/3)=3
    3,3,1
    3,2,2
    3,1,3
    2,3,2
    2,2,3
    2,1,  x
    1,3,3
    1,2,  x
"""

from math import ceil

def get_additions(sum_, max_):
    comp_per = ceil(sum_/max_)
    pairs = []
    a, b = max_, sum_-max_
    while b < max_:
        pairs.append((a, b))
        a -= 1
        b += 1
        if (a, b) == pairs[-1] or (b, a) == pairs[-1]:
            to_add = []
            for A, B in pairs:
                to_add.append((B, A))
            pairs += to_add
            break
    return pairs


N, K = [int(i) for i in input().split()]
attrcs = [int(i) for i in input().split()]
current_sum = 0
for n, m in get_additions(N, K):


