from math import log, floor

P, N, R = int(input()), int(input()), int(input())

if R == 1:
    print(P//N)
else:
    print(floor(log(-((P*(1-R))/N) + 1)/log(R)))