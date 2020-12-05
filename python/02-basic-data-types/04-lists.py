if __name__ == '__main__':
    l = list()
    for _ in range(int(input())):
        command, *args = input().split()
        args = list(int(x) for x in args)

        if command == 'insert':
            l.insert(args[0], args[1])
        elif command == 'print':
            print(l)
        elif command == 'remove':
            l.remove(args[0])
        elif command == 'append':
            l.append(args[0])
        elif command == 'sort':
            l.sort()
        elif command == 'pop':
            l.pop()
        elif command == 'reverse':
            l.reverse()
