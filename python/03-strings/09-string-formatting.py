def print_formatted(number):
    max = len(str(bin(number)).replace('0b', ''))
    for i in range(1, n+1):
        print(str(i).rjust(max, ' '), str(oct(i)).replace('0o', '', 1).rjust(max, ' '), str(hex(i)).replace('0x', '', 1).upper().rjust(max, ' '), str(bin(i)).replace('0b', '', 1).rjust(max, ' '))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
