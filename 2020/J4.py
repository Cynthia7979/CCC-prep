# Clearly non-efficient solution but still got a pretty good testing time:
def find_cyclic_shift(s):
    shifts = [s]
    l = len(s)
    for i in range(l-1):
        s = s[-1]+s[:-1]
        shifts.append(s)
    # print(shifts)
    return shifts


T = input()
S = input()
# print(T, S)
found = False
for shift in find_cyclic_shift(S):
    for i in range(len(T)-len(S)+1):
        # print(shift, T[i:i+len(S)])
        if T[i:i+len(S)] == shift:
            found = True
            break
    if found: print('yes');break
if not found: print('no')
