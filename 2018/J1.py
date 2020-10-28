nb = input()+input()+input()+input()
print('ignore' if nb[0] in ('8','9') and nb[-1] in ('8','9') and nb[1]==nb[2] else 'answer')
