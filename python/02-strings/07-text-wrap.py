import textwrap


def wrap(string, max_width):
    w = textwrap.TextWrapper(width=max_width)
    return "\n".join(w.wrap(string))


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
