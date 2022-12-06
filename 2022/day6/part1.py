import sys
import numpy as np


def main():
    dataFile = sys.argv[1]
    data = open(dataFile)
    line = data.readline()
    # find four characters in a row in variable line that do not have a repeating character
    # if there are multiple, take the first one
    for c in range(len(line)):
        if line[c] != line[c+1] and line[c] != line[c+2] and line[c] != line[c+3] and line[c+1] != line[c+2] and line[c+1] != line[c+3] and line[c+2] != line[c+3]:
            # print(line[c], line[c+1], line[c+2], line[c+3])
            print(c+4)
            break



if __name__ == '__main__':
    main()