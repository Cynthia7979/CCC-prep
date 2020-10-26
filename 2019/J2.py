import sys
for i in range(int(input())):
    sl = input().split()
    times, sym = int(sl[0]), sl[1]
    if sym == "\\":
        sys.stdout.write(chr(92))
    else:
        print(sym*times)
