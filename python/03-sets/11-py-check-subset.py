if __name__ == '__main__':
    results = []
    for _ in range(int(input())):
        _ = input()
        a = set(map(int, input().split()))
        _ = input()
        b = set(map(int, input().split()))

        (
            results.append('True') if a.issubset(b) 
            else results.append('False')
        )

    print('\n'.join(results))