def solve(n, m):
    # list.sort() does not returns a variable so use Python's built-in sorted() function instead.
    return sorted(list(n.difference(m)) + list(m.difference(n)))


if __name__ == '__main__':
    _ = input()
    n = set(map(int, input().split()))
    _ = input()
    m = set(map(int, input().split()))
    print('\n'.join(map(str, solve(n, m))))