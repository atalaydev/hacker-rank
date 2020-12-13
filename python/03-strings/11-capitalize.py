#!/bin/python3

import math
import os
import random
import re
import sys


def iterate(i):
    for value in i:
        try:
            if value[0].isalpha():
                yield value.capitalize()
            else:
                yield value
        except Exception:
            yield value


# Complete the solve function below.
def solve(s):
    return " ".join([word for word in iterate(s.split(" "))])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = solve(s)
    fptr.write(result + '\n')
    fptr.close()
