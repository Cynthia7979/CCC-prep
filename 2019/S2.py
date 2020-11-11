# Coding time used: 13min
# Can't be tested by tester.py: Multiple solutions.


def prime(num):
    for k in range(2, num):
        if num%k==0:
            return False
    return True


for i in range(int(input())):
# for i in range(10000000):
    avg = int(input())
    # avg = i
    a, b = avg, avg
    for n in range(avg):
        p, q = a+n, b-n
        if p%2==0 or q%2==0:
            continue
        else:
            if prime(p) and prime(q):
                print(p, q)
                break
        # print('no!', avg)
