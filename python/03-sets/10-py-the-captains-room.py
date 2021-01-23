from collections import Counter

if __name__ == '__main__':
    k = int(input())
    a = list(map(int, input().split()))
    b = set(a)

    c = Counter(a)
    for i in c:
        if c.get(i) != k:
            print(i)
            break