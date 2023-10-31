n = int(input())
invites = [set() for i in range(n+1)]  # [0] => [], [n] => [all]
rm_sets = {(ppl for ppl in range(1, n+1)), ()}
for i in range(1, n):
    i_invited_by = int(input())
    invites[i_invited_by].add(i)

max_rm = n-2
while max_rm > 0:
    i = 1
    to_rm = set()
    last_to_rm = None
    while i < n:
        to_rm.add(i)
        to_rm = to_rm.union(invites[i])
        if len(to_rm) <= max_rm:
            rm_sets.add(tuple(to_rm))
            print('Added', tuple(to_rm))
            i += 1
        else:
            if to_rm == last_to_rm:  # In infinite loop
                i += 1
                last_to_rm = None
            else:
                last_to_rm = to_rm.copy()
                to_rm = set()
    max_rm -= 1
print(len(rm_sets))
