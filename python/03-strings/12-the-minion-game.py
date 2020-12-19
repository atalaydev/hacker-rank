def minion_game(string):
    kevin, stuart = 0, 0

    for i in range(len(string)):
        # b[a]nana, if you see 'a' at the indis 1 then you can
        # generate 5 words as ['a', 'an', 'ana', 'anan', 'ananan'] and
        # all of them will start with a vowel and each one adds 1 point.
        # So sum them together.

        if string[i] in 'AEIOU':
            kevin += len(string) - i
        else:
            stuart += len(string) - i

    if kevin > stuart:
        print(f'Kevin {kevin}')
    elif kevin < stuart:
        print(f'Stuart {stuart}')
    else:
        print('Draw')


if __name__ == '__main__':
    s = input()
    minion_game(s)
