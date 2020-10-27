mp = {'': [[1,2],
           [3,4]],
      'H': [[3,4],
            [1,2]],
      'V': [[2,1],
            [4,3]],
      'HV':[[4,3],
            [2,1]]}
flips = input()
H, V = flips.count('H'), flips.count('V')
H %= 2
V %= 2
for r in mp['H'*H+'V'*V]:
    print(' '.join([str(i) for i in r]))
