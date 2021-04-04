from itertools import combinations


if __name__ == '__main__':
    a, k = list(input().split())
    i = 1
    while int(k) >= i:
        for p in combinations(sorted(a), int(i)):
            print(''.join(p))
        i += 1
