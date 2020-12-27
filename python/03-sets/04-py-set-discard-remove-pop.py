if __name__ == '__main__':
    _ = input()
    s = set(map(int, input().split()))
    m = list([input() for x in range(int(input()))])

    for i in m:
        cmd, val, *_ = i.split() + [None]
        if cmd == 'pop':
            s.pop()
        elif cmd == 'remove':
            s.remove(int(val))
        elif cmd == 'discard':
            s.discard(int(val))

    print(sum(s))