def solve(n, a, b):
    return sum([1 if i in a else -1 if i in b else 0 for i in n])


if __name__ == '__main__':
    _ = input().split()
    n = list(map(int, input().split()))
    a = set(map(int, input().split()))
    b = set(map(int, input().split()))

    print(solve(n, a, b))