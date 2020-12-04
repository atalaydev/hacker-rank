if __name__ == '__main__':
    n = int(input().strip())

    if n % 2 == 0:
        print('Not Weird' if n in range(2,6) or n > 20 else 'Weird' if n in range(6,21) else '')
    else:
        print('Weird')
