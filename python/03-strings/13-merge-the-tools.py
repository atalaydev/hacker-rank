def merge_the_tools(string, k):
    t = int(len(string) / k)
    for i in range(0, len(string), int(len(string) / t)):
        sub = list()
        for c in string[i:i+int(len(string) / t)]:
            c not in sub and sub.append(c)
        print(''.join(sub))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
