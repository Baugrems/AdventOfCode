import numpy as np

import re

def naughty_or_nice(word):
    between = False
    pair = False

    for x in range(len(word)):
        if re.search("(.).\\1", word):
            between = True
        if re.search("(..).*\\1", word):
            pair = True
    if not between or not pair:
        return 0
    # print(word)
    return 1


def main():
    data = open('data1')
    total = 0
    for line in data:
        total += naughty_or_nice(line.strip())
    print(total)


if __name__ == '__main__':
    main()