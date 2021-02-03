namespace = {
    'A': 0,
    'B': 0
}
while True:
    args = input().split()
    if args[0] == '1':
        namespace[args[1]] = int(args[2])
    elif args[0] == '2':
        print(namespace[args[1]])
    elif args[0] == '3':
        namespace[args[1]] = namespace[args[1]] + namespace[args[2]]
    elif args[0] == '4':
        namespace[args[1]] = namespace[args[1]] * namespace[args[2]]
    elif args[0] == '5':
        namespace[args[1]] = namespace[args[1]] - namespace[args[2]]
    elif args[0] == '6':
        namespace[args[1]] = int(namespace[args[1]] / namespace[args[2]])
    elif args[0] == '7':
        break
