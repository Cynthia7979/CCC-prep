A3, A2, A1 = [int(i) for i in (input(), input(), input())]

B3, B2, B1 = [int(i) for i in (input(), input(), input())]

TA = 3*A3+2*A2+A1
TB = 3*B3+2*B2+B1
if TA>TB:
    print('A')
elif TA==TB:
    print('T')
else:
    print('B')
