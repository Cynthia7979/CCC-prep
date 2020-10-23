xes = []
ys = []
for n in range(int(input())):
    line = input()
    x, y = [int(i) for i in line.split(',')]
    xes.append(x)
    ys.append(y)
print(','.join([str(num) for num in [
    min(xes)-1,
    min(ys)-1
]]))
print(','.join([str(num) for num in [
    max(xes)+1,
    max(ys)+1
]]))
