if __name__ == '__main__':
    result = True
    a = set(map(int, input().split()))
    # '>' operator can be used also.
    for _ in range(int(input())):
        n = set(map(int, input().split()))
        if a.issuperset(n):
            if a != n:
                continue
        result = False
        break

    print(result)