from itertools import combinations_with_replacement


if __name__ == '__main__':
    a, k = list(input().split())
    for p in combinations_with_replacement(sorted(a), int(k)):
        print(''.join(p))
