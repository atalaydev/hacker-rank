if __name__ == '__main__':
    n = int(input())
    print(len(set([input() for x in range(n)])))