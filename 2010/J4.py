while True:
    length, *sequence = [int(i) for i in input().split()]
    if not sequence:
        break
    if length == 1:
        print(0)
        continue

    # Build change sequence
    changes = []
    found = False
    for i in range(1, length):
        changes.append(sequence[i] - sequence[i-1])
    for j in range(1, len(changes)):  # cycle length
        if found: break
        if changes[0] == changes[j] and changes[1] == changes[1+j]:
            print(j)
            found = True
    if found: continue
    if changes[0] == changes[-1]:
        print(len(changes)-1)
    else:
        print(len(changes))
