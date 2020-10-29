values = []
diffs = []
for i in range(int(input())):
    values.append([int(a) for a in input().split()])
values.sort(key=lambda v: v[0])
# print(values)
for i in range(1, len(values)):
    t0, s0 = values[i-1]
    t1, s1 = values[i]
    # print(s0, s1, t0, t1,(s1-s0)/(t1-t0))
    diffs.append(abs((s1-s0)/(t1-t0)))
print(max(diffs))
