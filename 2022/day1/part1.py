import sys
import numpy as np
import operator


def main():
    dataFile = sys.argv[1]
    data = open(dataFile)
    max_index = 0
    index = 0
    elves = dict()
    elves[0] = 0
    for line in data:
        if line != "\n":
            elves[index] += int(line)
        else:
            if elves[index] > elves[max_index]:
                max_index = index
            index += 1
            elves[index] = 0

    sorted_elves = sorted(elves.items(), key=operator.itemgetter(1))
    print(sorted_elves[-1][1] + sorted_elves[-2][1] + sorted_elves[-3][1])

if __name__ == '__main__':
    main()