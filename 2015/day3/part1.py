import numpy as np

def main():
    data = open('data1')
    houses = dict()
    pos = [0, 0]
    houses[(pos[0], pos[1])] = 1
    for line in data:
        for c in line:
            if c == 'v':
                pos[0] += 1
            elif c == '^':
                pos[0] -= 1
            elif c == '<':
                pos[1] -= 1
            elif c == '>':
                pos[1] += 1
            if (pos[0], pos[1]) in houses:
                houses[(pos[0], pos[1])] += 1
            else:
                houses[(pos[0], pos[1])] = 1
    print(len(houses))

if __name__ == '__main__':
    main()