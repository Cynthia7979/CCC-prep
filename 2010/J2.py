a, b, c, d, s = [int(i) for i in (input(),input(),input(),input(),input())]

nikky_steps = (s // (a+b)) * (a-b)
if s % (a+b) <= a:
    nikky_steps += s % (a+b)
else:
    nikky_steps -= (s % (a+b)) - a

byron_steps = (s // (c+d)) * (c-d)
if s % (c+d) <= c:
    byron_steps += s % (c+d)
else:
    byron_steps -= (s % (c+d)) - c

if nikky_steps > byron_steps: print('Nikky')
elif nikky_steps < byron_steps: print('Byron')
else: print('Tied')