if __name__ == '__main__':
    _ = input()
    a = set(map(int, input().split()))
    _ = input()
    b = set(map(int, input().split()))
    
    print(len(a.intersection(b)))