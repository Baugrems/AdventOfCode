import numpy as np

import hashlib


data = 'iwrupvqb'
# data = 'abcdef'

def main():
    for x in range(1, 100000000):
        md5 = hashlib.md5((data + str(x)).encode()).hexdigest()
        if md5[:5] == '00000':
            print(x)
            return

if __name__ == '__main__':
    main()