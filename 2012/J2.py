depths = [int(i) for i in (input(), input(), input(), input())]
diffs = [depths[i] - depths[i+1] for i in range(3)]

if all([i>0 for i in diffs]):
    print('Fish Diving')
elif all([i<0 for i in diffs]):
    print('Fish Rising')
elif all([i==0 for i in diffs]):
    print('Fish At Constant Depth')
else:
    print('No Fish')
