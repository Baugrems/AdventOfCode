import numpy as np

def main():
    data = open('data1')
    houses = dict()
    pos = [[0, 0], [0, 0]]

    houses[(pos[0][0], pos[0][1])] = 1
    i = 0
    for line in data:
        for c in line:
            if i == 0:
                i = 1
            else:
                i = 0
            if c == 'v':
                pos[i][0] += 1
            elif c == '^':
                pos[i][0] -= 1
            elif c == '<':
                pos[i][1] -= 1
            elif c == '>':
                pos[i][1] += 1
            if (pos[i][0], pos[i][1]) in houses:
                houses[(pos[i][0], pos[i][1])] += 1
            else:
                houses[(pos[i][0], pos[i][1])] = 1
    print(len(houses))

if __name__ == '__main__':
    main()