from itertools import permutations


if __name__ == '__main__':
    a, k = list(input().split())
    for p in permutations(sorted(a), int(k)):
        print(''.join(p))
