import numpy as np

import re

bad = ['ab', 'cd', 'pq', 'xy']
vowels = ['a', 'e', 'i', 'o', 'u']

def naughty_or_nice(word):
    for b in bad:
            if b in word:
                print("Bad Word")
                return 0

    vowelCount = re.search("[aeiou].*[aeiou].*[aeiou]", word)

    doubled = re.search("(.)\\1+", word)
    if not doubled:
        print("Not Doubled")
        return 0
    if not vowelCount:
        print("Needs Vowels")
        return 0
    return 1

def main():
    data = open('data1')
    total = 0
    for line in data:
        total += naughty_or_nice(line)
    print(total)


if __name__ == '__main__':
    main()