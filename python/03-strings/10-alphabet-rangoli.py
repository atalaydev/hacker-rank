import string


def print_rangoli(size):
    max = ((2 * (size - 1) + 1) * 2) - 1

    indis = size - 1
    while indis >= 0:
        chars = [s for s in string.ascii_lowercase[indis:size]]
        print("-".join(list(reversed(chars)) + chars[1:]).center(max, '-'))
        indis -= 1

    indis = 1
    while indis < size:
        chars = [s for s in string.ascii_lowercase[indis:size]]
        print("-".join(list(reversed(chars)) + chars[1:]).center(max, '-'))
        indis += 1


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
