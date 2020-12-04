if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr = list(dict.fromkeys(arr))
    arr.pop(arr.index(max(arr)))
    print(max(arr))
